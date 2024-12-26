import firebase_admin
from firebase_admin import credentials,firestore

project_id = "platzi-flask-445912"
credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(credentials,{
    'projectId': project_id
})

db = firestore.client()

def get_users():
    users = db.collection('users').get()
    print(f"{users}")
    return users

def get_todos(user_id):
    return 
    db.collection('users')\
    .document(user_id)\
    .collection('todos').get()