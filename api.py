import requests
import json

# Heroku Api Server URL
api_url = "http://api-plantsmartfarm.herokuapp.com/"
headers = {"Content-Type" : "application/json"}

def send_tempAndhumidity_data(temperature, humidity) :
    read_temperature_url = api_url + "temperature"
    data_value = {"temperature" : temperature , "humidity" : humidity}
    data_value = json.dumps(data_value)
    res = requests.post(read_temperature_url,headers= headers,data=data_value)
    
    return res.text
