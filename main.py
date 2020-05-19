import json
import requests
#insert your info here
API_KEY = None
PROJECT_TOKEN = None
RUN_TOKEN = None

class Data():
    '''
    responsible for getting data regarding COVID-19 such as:
    1) number of cases
    2) number of deaths 
    3) number of recovery 
    4) information for a specifc countrty regarding its covid-19 status
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

    def getTotalCases(self): #retrun the total cases
        data = self.data['total']
        for value in data:
            return value['values'] if value['name'] == "Coronavirus Cases:" else None
    
    def getTotalDeaths(self): #return the total deaths
        data = self.data['total']
        for value in data:
            if value['name'] == 'Deaths:':
                return value['values']
    
    def getTotalRecovery(self): #return total recovery
        data = self.data['total']
        for value in data:
            if value['name'] == 'Recovered:':
                return value['values']
    
    def getCountryData(self, country): #return information countriesS
        data = self.data['country']
        for value in data:
            if value['name'].lower() == country.lower():
                return value

