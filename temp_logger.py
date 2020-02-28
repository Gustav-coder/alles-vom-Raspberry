#!/usr/bin/env 
import Adafruit_DHT
import MySQLdb

sensor = Adafruit_DHT.DHT11
pin = 4
db = MySQLdb.connect("localhost", "root", "867_45?355!35", "testhaus")
curs=db.cursor()

try:
   humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
   curs.execute ("INSERT INTO temperatur_tb (datum, uhrzeit, wert) VALUES (CURRENT_DATE(), CURRENT_TIME(), %.2f);" % temperature) 
   db.commit()
   print("Done")
except:
   print("Error. Rolling Back.")
   db.rollback()
