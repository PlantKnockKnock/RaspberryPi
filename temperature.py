import time
import api
import Adafruit_DHT as DHT
sensor = DHT.DHT11
pin = 4

try :
   while True :
      h, t = DHT.read_retry(sensor, pin)
      if h is not None and t is not None :
           api.send_pusher_temperature(t,h)
           #result = api.send_tempAndhumidity_data(t,h)
           #print(result)
           print("Temperature = {0:0.1f}*C Humm idity = {1:0.1f}%".format(t,h))
      else :
           print("Read Error")
      time.sleep(1)
except KeyboardInterrupt :
   print("Terminated by Keyboard") 
finally :
   print("End of Program")
         