import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Initialize credentials - where to find the .json file
cred = credentials.Certificate('C:/Users/BP/Hack The Barriers/hackthebarriers.json')

#where to find the database
try:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://hackthebarriers-fdb6a.firebaseio.com/'
    })
except:
    print "already initialized"

event_list = []
ref3 = db.reference('events')

#Sets up the current events in real time (Since every time the program was ran event_list got set to [])
snap = ref3.order_by_key().get()
if snap is None:
    event_list = []
else:
    for ki,valy in snap.items():
        event_list.append(ki.encode('utf-8'))

username = raw_input("username:")
name = raw_input("name:")
dob = raw_input("birthday:")
lang = raw_input("language:")
event_name = raw_input("event name: ")

ref1 = db.reference('events')
events_ref = ref1.child(event_name)

if not(event_name in event_list):
    location = raw_input("location: ")
    events_ref.set({
        'location' : location,
    })

ref = db.reference('Users')
users_ref = ref.child(username)

users_ref.set({
    'full_name' : name,
    'date_of_birth': dob,
    'language' : lang,
    'events' : event_name,
})

#Grab User data for a specific person (change to js for html)
desired_user = raw_input("whose information: ")

snapshot = ref.order_by_child('username').get()
for key, val in snapshot.items():
    if key == desired_user:
        print val[u'full_name']
        print val[u'date_of_birth']
        print val[u'language']
        print val[u'events']
