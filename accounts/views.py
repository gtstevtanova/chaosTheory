from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log the user in
            login(request,user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) #validating the data from the login
        if form.is_valid():
            #log in the user
            user = form.get_user() #retrieve the user
            login(request, user) #and log the this user in
            if'next' in request.POST: #get the 'next' input and redirect it
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')