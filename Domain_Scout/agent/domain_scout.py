import ollama
import json
from prompt.domain_prompt import SYSTEM_PROMPT

class DomainScout:
    def __init__(self, model_name="llama3.2:latest"):
            self.model_name = model_name

    def analyze(self, abstract_text):
        # We add "Output in JSON format" to the user message to help the model
        user_input = f"Analyze this abstract and return ONLY JSON:\n\n{abstract_text}"
        
        response = ollama.chat(
            model=self.model_name,
            format='json', # <--- This is the key part!
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': user_input},
            ],
            options={'temperature': 0} # 0 makes it very consistent
        )
        
        # Parse the string into a Python Dictionary
        return json.loads(response['message']['content'])

# --- Testing the JSON File ---
if __name__ == "__main__":
    scout = DomainScout()
    
    # Load your manual test file
    with open('test_abstracts.json', 'r') as f:
        data = json.load(f)

    results = []
    for item in data:
        print(f"Processing ID {item['id']}...")
        analysis = scout.analyze(item['text'])
        results.append({
            "id": item['id'],
            "analysis": analysis
        })

    # Save the output to a new results file
    with open('analysis_results.json', 'w') as f:
        json.dump(results, f, indent=4)
    
    print("Done! Results saved to analysis_results.json")