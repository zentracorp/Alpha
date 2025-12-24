import json
from agent.domain_scout import DomainScout

def run_test():
    # 1. Initialize the agent
    scout = DomainScout()
    
    # 2. Load your test data
    try:
        with open('test_abstracts.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: test_abstracts.json not found in the root directory.")
        return

    # 3. Analyze each abstract
    results = []
    print(f"Starting analysis of {len(data)} abstracts...\n")
    
    for item in data:
        print(f"Processing ID {item['id']}...")
        analysis = scout.analyze(item['text'])
        
        # Combine the original data with the AI's analysis
        results.append({
            "id": item['id'],
            "abstract": item['text'],
            "domain_analysis": analysis
        })

    # 4. Save results to a new file
    with open('analysis_results.json', 'w') as f:
        json.dump(results, f, indent=4)
    
    print("\nSuccess! Results saved to 'analysis_results.json'.")

if __name__ == "__main__":
    run_test()