from pirc522 import RFID
from time import sleep
import RPi.GPIO as GPIO
import sqlite3
rdr = RFID()
f = open("tgs.txt","w")
f.close()
c=0
#
print(GPIO.getmode())
LED_PIN = 11
GPIO.setup(LED_PIN, GPIO.OUT)
print(GPIO.getmode())

#
connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()
print("321")
while True:
  sleep(2)
  rdr.wait_for_tag()
  (error, tag_type) = rdr.request()
  if not error:
    print("Tag detected")
    (error, uid) = rdr.anticoll()
    if not error:
      print("UID: " + str(uid))
      temp = str(uid).replace("[","").replace("]","").replace(",","")
      checking = cursor.execute("SELECT * FROM card WHERE card=?",(temp,))
      if checking.fetchone() is None:
        #return 0
        print("CARD NOT FOUND")
      else:
        print("CARD FOUND")
        GPIO.output(LED_PIN, GPIO.HIGH)
        sleep(2)
        GPIO.output(LED_PIN, GPIO.LOW)
      f = open("tgs.txt","a")
      f.write(temp+"\n")
      f.flush()
      f.close()
      c+=1

  if c >= 1000:
    f = open("tgs.txt","w")
    f.write("")
    f.close()
    c=0

rdr.cleanup()