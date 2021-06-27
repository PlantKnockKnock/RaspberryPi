import requests
import json
import pusher

# Heroku Api Server URL
api_url = "http://api-plantsmartfarm.herokuapp.com/"
headers = {"Content-Type" : "application/json"}



def send_tempAndhumidity_data(temperature, humidity) :
    read_temperature_url = api_url + "temperature"
    data_value = {"temperature" : temperature , "humidity" : humidity}
    data_value = json.dumps(data_value)
    res = requests.post(read_temperature_url,headers= headers,data=data_value)
    
    return res.text

def send_pusher_temperature(temperature, humidity) :
        pusher_client = pusher.Pusher(app_id="1225626",key="da9af6249c692cb02284",secret="480ffb7393011d5f12ce",cluster="ap3")
        pusher_client.trigger("my-channel","my-event",{
            "temperature" : temperature,
            "humidity" : humidity
        })    