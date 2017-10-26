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

#initializing ref
ref = db.reference('room')

ser = serial.Serial('COM15', baudrate = 9600, timeout=1)

while 1:
		arduinoData = ser.readline().rstrip().decode('ascii')
		print(arduinoData)
	
	#Updating ref
		ref.update({
		'player1' : arduinoData
	})