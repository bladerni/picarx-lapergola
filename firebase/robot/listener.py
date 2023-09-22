from firebase_admin import credentials, initialize_app, db

cred = credentials.Certificate("./serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL' : 'https://erni-hackathon-default-rtdb.europe-west1.firebasedatabase.app'
})

def accelerationListener(event):
    print(event.data)

def carDirectionListener(event):
    print(event.data)

def carDiscoModeListener(event):
    print(event.data)

def carAutomaticModeListener(event):
    print(event.data)

def cameraDirectionListener(event):
    print(event.data)

ref = db.reference('/car/acceleration').listen(accelerationListener)
ref = db.reference('/car/direction').listen(carDirectionListener)
ref = db.reference('/car/disco_mode').listen(carDiscoModeListener)
ref = db.reference('/car/automatic_mode').listen(carAutomaticModeListener)
ref = db.reference('/camera/direction').listen(cameraDirectionListener)
