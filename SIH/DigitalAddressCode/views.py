from django.shortcuts import render
import pymongo
from pymongo import MongoClient
import pyrebase

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
    'measurementId': "G-HVDJPTQP5B",
    'databaseURL': 'https://sih-lorem-ipsum-default-rtdb.firebaseio.com/'
}

# need to install pyrebase
firebase_app = pyrebase.initialize_app(firebaseConfig)

def home(request):
    print(db)
    return render(request, "index.html")

def addDac(request):
    return render(request, "addDac.html")

def afterReg(request):
    return render(request, "afterRegistration.html")

def deleteDac(request):
    return render(request, "deleteDac.html")

def register(request):
    return render(request, "registration.html")

def updateDac(request):
    return render(request, "updateDac.html")
