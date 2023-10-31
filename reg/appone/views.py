from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import pyrebase
""" Libraries of LR model """
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.metrics.pairwise import euclidean_distances





"""For Google Auth """
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


""" For Sign-Up page """
def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        passone = request.POST.get('passwordone')
        passtwo = request.POST.get('passwordtwo')

        """ confrim password Constraints """
        if passone!=passtwo:
            return HttpResponse("Your Password and Confirm password is not same")
        else:

            my_user = User.objects.create_user(uname,email,passone)
            my_user.save()
            return redirect('login')
        

    return render (request,'signup.html')
""" For Loginpage """
def LoginPage(request):
    if request.method == 'POST':
        loguser = request.POST.get('loginusername')
        logpass = request.POST.get('loginpass')
        userauth = authenticate(request,username=loguser,password=logpass)

        if userauth is not None:
            login(request,userauth)
            return redirect('home')
        else:
            return HttpResponse("terminated")

    return render (request,'login.html')
def LogoutPage(request):
    logout(request)
    return redirect('login')


def result(request):
    data_dia = pd.read_csv(r'E:\ML Project\diabetes.csv')
    A = data_dia.drop('Outcome', axis = 1)
    B = data_dia['Outcome']
    A_train, A_test, B_train, B_test = train_test_split(A,B,test_size = 0.2)
    A_train
    model = LogisticRegression()
    model.fit(A_train,B_train)

    input1 = float(request.GET['in1'])
    input2 = float(request.GET['in2'])
    input3 = float(request.GET['in3'])
    input4 = float(request.GET['in4'])
    input5 = float(request.GET['in5'])
    input6 = float(request.GET['in6'])
    input7 = float(request.GET['in7'])
    input8 = float(request.GET['in8'])

    predictionval = model.predict([[input1,input2,input3,input4,input5,input6,input7,input8]])

    resultvalmap = ''
    if predictionval ==[1]:
        resultvalmap ="Oops! You have DIABETES 😔"
    else:
        resultvalmap="Great! You DON'T have daibetes 🤗"

    return render(request,'home.html',{"resultval":resultvalmap})