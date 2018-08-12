#With this code, it's now much easier to update a firbease database from the arduino
import serial
import string
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Initialize credentials - where to find the .json file
cred = credentials.Certificate('C:/Users/BP/Downloads/hackathon - thacks/arthrowfighter.json')

#where to find the database
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://arthrowfighter.firebaseio.com/'
})

#initializing ref - Which object is being considered
ref = db.reference('room')
#Where to get the serial output from Arduino
ser = serial.Serial('COM15', baudrate = 9600, timeout=1)
#Always do this; turn serial output from Arduino into Serial input for Python
while 1:
		arduinoData = ser.readline().rstrip().decode('ascii')
		print(arduinoData)
	
	#Updating ref
		ref.update({
		'player1' : arduinoData
	})
