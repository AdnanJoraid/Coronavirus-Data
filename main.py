import json
import requests
API_KEY = None
PROJECT_TOKEN = None
RUN_TOKEN = None

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',params={"api_key":API_KEY})
data = json.loads(response.text)
print(data)