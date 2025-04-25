import json
from degrees_of_kb import KevinBacon6Degrees  # ✅ Explicit import from local file

def lambda_handler(event, context):
    #AWS Lambda entry point
    k_b = KevinBacon6Degrees("/wiki/Six_Degrees_of_Kevin_Bacon")
    k_b.generate_6_degrees()
    
    return {
        'statusCode': 200,
        'body': json.dumps(k_b.get_urls())
    }

# Optional local run for testing (non-AWS context)
if __name__ == "__main__":
    print(lambda_handler({}, {}))




