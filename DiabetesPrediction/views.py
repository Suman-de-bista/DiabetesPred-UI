from itertools import count
from multiprocessing import context
from django.shortcuts import render
import pandas as pd
import numpy as np
from .models import Datalist
from .forms import DatalistForm
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from django.utils.datastructures import MultiValueDictKeyError


def home(request):
    return render(request, 'home.html')

def predict(request):
    form = DatalistForm()
    context = {'form':form}
    return render(request, 'predict.html', context)


def about(request):
    return render(request, 'about.html')

def result(request):
    df = pd.read_csv('diabetes.csv')
    # knn = joblib.load('Models/knn.joblib')
    #train_test_splitting of the dataset

    x = df.drop(columns = 'Outcome')

    # Getting Predicting Value
    y = df['Outcome']
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=10)
    #NAIVE BAYES
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb.fit(x_train,y_train)
    #KNN
    knn=KNeighborsClassifier(n_neighbors=7)
    knn.fit(x_train,y_train)

    #RANDOM FOREST
    from sklearn.ensemble import RandomForestClassifier
    rfc=RandomForestClassifier()
    rfc.fit(x_train,y_train)

    if request.method == 'POST':
        FName = request.POST['FName']
        LName = request.POST['LName']
        try:
            Gender = request.POST['Gender']
        except MultiValueDictKeyError:
            Gender = False
        Pregnancies = request.POST['Pregnancies']
        Glucose = request.POST['Glucose']
        BloodPressure = request.POST['BloodPressure']
        SkinThickness = request.POST['SkinThickness']
        Insulin = request.POST['Insulin']
        BMI = request.POST['BMI']
        DiabetesPedigreeFunction = request.POST['DiabetesPedigreeFunction']
        Age = request.POST['Age']


        InputData = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]

        pred_gnb = gnb.predict(InputData)
        pred_knn = knn.predict(InputData)
        pred_rfc = rfc.predict(InputData)
        # print(gnb.predict_proba(InputData))
        # print(knn.predict_proba(InputData))
        # print(rfc.predict_proba(InputData))

        result_gnb = ''
        count = 0
        if pred_gnb ==[1]:
            result_gnb = "Positive"
            count+=1
            findcolor1 = "red"
        else:
            result_gnb = "Negative"
            findcolor1 = "green"

        result_knn = ''
        if pred_knn ==[1]:
            result_knn = "Positive"
            count+=1
            findcolor2 = "red"
        else:
            result_knn = "Negative"
            findcolor2 = "green"

        result_rfc = ''
        if pred_rfc ==[1]:
            result_rfc = "Positive"
            count+=1
            findcolor3 = "red"
        else:
            result_rfc = "Negative"
            findcolor3 = "green"


        if count >= 2:
            Outcome = 1
            result = "Positive"
            findcolor = "red"
        else:
            Outcome = 0
            result = "Negative"
            findcolor = "green"


        ins = Datalist(FName=FName,LName=LName,Gender=Gender,Pregnancies=Pregnancies,Glucose=Glucose,BloodPressure=BloodPressure,SkinThickness=SkinThickness,Insulin=Insulin,BMI=BMI,DiabetesPedigreeFunction=DiabetesPedigreeFunction,Age=Age,Outcome=Outcome)
        ins.save()
        print("The data has been written to database")
        
    

    return render(request, 'result.html', {"result_overall":result,'result_gnb':result_gnb,'result_knn':result_knn,'result_rfc':result_rfc,'findcolor':findcolor,'findcolor1':findcolor1,'findcolor2':findcolor2,'findcolor3':findcolor3})

def stats(request):
    negative = Datalist.objects.filter(Outcome=0).count()
    positive = Datalist.objects.filter(Outcome=1).count()
    male = Datalist.objects.filter(Gender='M').count()
    male = int(male)
    female = Datalist.objects.filter(Gender='F').count()
    female = int(female)
    male_list = ['Male','Female']
    male_data = [male,female]
    outcome_list = ['Positive','Negative']
    outcome_data = [positive,negative]
    totaltest = Datalist.objects.count()
    totalpositive = Datalist.objects.filter(Outcome=1).count()
    totalnegative = Datalist.objects.filter(Outcome=0).count()
    if request.method =='POST':
        chart = request.POST['chart']
        if chart =='Gender':
            context = {
                'totaltest':totaltest,
                'totalpositive':totalpositive,
                'totalnegative':totalnegative,
                'chart':chart,
                'outcome_list':male_list,
                'outcome_data':male_data,
            }
        else:
            context = {
                'totaltest':totaltest,
                'totalpositive':totalpositive,
                'totalnegative':totalnegative,
                'chart':chart,
                'outcome_list':outcome_list,
                'outcome_data':outcome_data,
            }
    else:
        context = {
                'totaltest':totaltest,
                'totalpositive':totalpositive,
                'totalnegative':totalnegative,
                'chart':'Outcome',
                'outcome_list':outcome_list,
                'outcome_data':outcome_data,
            }
    
    return render(request, 'stats.html', context)