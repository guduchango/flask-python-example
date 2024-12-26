import firebase_admin
from firebase_admin import credentials,firestore

credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(credentials)

db = firestore.client()

def get_users():
    return db.collection('users').get()

