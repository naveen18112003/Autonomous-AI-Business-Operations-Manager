import requests
import json
import sys

# Configuration
BASE_URL = "http://localhost:8000"
ANALYZE_ENDPOINT = f"{BASE_URL}/analyze/"

def test_analysis_flow():
    print(f"Testing Analysis Endpoint: {ANALYZE_ENDPOINT}")
    
    # Simulate a CSV file upload
    csv_content = """Date,Region,Product,Sales,Units,Customer_Satisfaction
2024-01-01,North,Widget A,1000,50,4.5
2024-01-02,South,Widget B,1500,60,4.2
2024-01-03,East,Widget A,800,40,3.9
2024-01-04,West,Widget C,2000,80,4.8
2024-01-05,North,Widget B,1200,45,4.1"""

    files = {
        'file': ('test_data.csv', csv_content, 'text/csv')
    }
    data = {
        'text_input': 'Analyze this sales data and look for trends.'
    }

    try:
        response = requests.post(ANALYZE_ENDPOINT, files=files, data=data)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("Response JSON received.")
            
            # Validate expected keys in the response
            expected_keys = ["metric_summary", "key_trends", "anomalies", "root_causes"]
            missing_keys = [key for key in expected_keys if key not in result]
            
            if not missing_keys:
                print("SUCCESS: Full Analysis Response structure verified.")
                print("Metric Summary:", json.dumps(result.get("metric_summary"), indent=2))
            else:
                print(f"FAILURE: Missing keys in response: {missing_keys}")
                sys.exit(1)
        else:
            print(f"FAILURE: Backend returned error: {response.text}")
            sys.exit(1)
            
    except Exception as e:
        print(f"ERROR: Connection failed. {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_analysis_flow()
