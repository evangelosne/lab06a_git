import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_treshold=0  # change this value
sound_treshold=0 # change this value


while True: 
  time.sleep(0.5) 
  for i in range(5):
    GPIO.output(chan_list,1)
    time.sleep(0.5)
    GPIO.output(chan_list,0) 

  for i in range(50):
    time.sleep(0.1)
    lux_reading = mcp.read([Adafruit_MCP3008.CH0])
    print(mcp.read([Adafruit_MCP3008.CH0]))
    if lux_reading > lux_treshold:
      print("bright")
    else:
      print("dark")
    
    for i in range(4):
      GPIO.output(chan_list,1)
      time.sleep(0.2)
      GPIO.output(chan_list,0) 
    
    for i in range(50):
      time.sleep(0.1)
      sound_reading = mcp.read([Adafruit_MCP3008.CH1])
      print(mcp.read([Adafruit_MCP3008.CH1]))
      if sound_reading > sound_treshold:
        GPIO.output(chan_list,1)
        time.sleep(0.1)
        GPIO.output(chan_list,0)
        
    
  #Following commands control the state of the output
  #GPIO.output(pin, GPIO.HIGH)
  #GPIO.output(pin, GPIO.LOW)

  # get reading from adc 
  # mcp.read_adc(adc_channel)
