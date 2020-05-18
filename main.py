import json
import requests
API_KEY = None
PROJECT_TOKEN = None
RUN_TOKEN = None
class Data():
    '''
    responsible for getting data regarding COVID-19 such as:
    1) number of cases
    2) number of deaths 
    3) number of recovery 
    4) number of population for each country
    '''
    def __init__(self, apiKey, projectToken):
        self.apiKey = apiKey
        self.params = {'api_key' : self.apiKey}
        self.projectToken = projectToken
        self.data = self.getData()
        
        
    
    def getData(self): #gets all the data that was scrapped from the website. 
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.projectToken}/last_ready_run/data',params=self.params)
        data = json.loads(response.text)
        return data

    def getTotalCases(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Coronavirus Cases:":
                return content['values']


data = Data(API_KEY, PROJECT_TOKEN)
allData = data.getData()
totalCases = data.getTotalCases()
print(totalCases)