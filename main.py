import time
import threading
import api
import Adafruit_DHT as DHT
import RPi.GPIO as GPIO
import spidev

sensor = DHT.DHT11
pin = 4

GPIO.setmode(GPIO.BCM)
DIGIT=23
GPIO.setup(DIGIT,GPIO.IN)
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=50000

def read_temperature () :
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

def read_spi_adc(adcChannel):
       adcValue=0
       buff = spi.xfer2([1,(8+adcChannel)<<4,0])
       adcValue = ((buff[1]&3)<<8)+buff[2]
       return adcValue
       
def read_moisture() :
    try :
       while True :
           adcValue=read_spi_adc(0)
           api.send_pusher_moisture(adcValue)
           print("water : %d "%(adcValue))
           digit_val=GPIO.input(DIGIT)
           #print("Digit Value : %d"%(digit_val))
           time.sleep(0.5)
    finally :
           GPIO.cleanup()
           spi.close()
    

# 쓰레드 생성
thd = threading.Thread(target=read_temperature)
thd2 = threading.Thread(target=read_moisture)
# 쓰레드를 데몬으로 설정
thd.daemon = True
thd2.daemon = True
# 쓰레드 시작
thd.start()
thd2.start()
  