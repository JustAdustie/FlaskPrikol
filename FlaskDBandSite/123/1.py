from pirc522 import RFID
from time import sleep
rdr = RFID()
f = open("tgs.txt","w")
f.close()
c=0
while True:
  sleep(2)
  rdr.wait_for_tag()
  (error, tag_type) = rdr.request()
  if not error:
    print("Tag detected")
    (error, uid) = rdr.anticoll()
    if not error:
      print("UID: " + str(uid))
      f = open("tgs.txt","a")
      f.write(str(uid).replace("[","").replace("]","").replace(",","")+"\n")
      f.flush()
      f.close()
      c+=1

  if c >= 1000:
    f = open("tgs.txt","w")
    f.write("")
    f.close()
    c=0

rdr.cleanup()