from django.shortcuts import render
from pymongo import MongoClient

client = pymongo.MongoClient(
    'mongodb+srv://test:test@cluster0.incky.mongodb.net/sih?retryWrites=true&w=majority')
db = client['db_name']

firebaseConfig = {
    'apiKey': "AIzaSyAQP0-gvtbP_rtwYyA_GjwDAdu01uT57FQ",
    'authDomain': "sih-lorem-ipsum.firebaseapp.com",
    'projectId': "sih-lorem-ipsum",
    'storageBucket': "sih-lorem-ipsum.appspot.com",
    'messagingSenderId': "972073866636",
    'appId': "1:972073866636:web:64f1002e34987ca32df2a9",
    'measurementId': "G-HVDJPTQP5B"
}

# need to install pyrebase
# firebase_app = pyrebase.initializeApp(firebaseConfig)


def home(request):
    print(db)
    return render(request, "index.html")
