from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
from app.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')




def Registration(request):
    ufo=UserForm()
    d={'ufo':ufo}
    if request.method=='POST':
        ufd=UserForm(request.POST)
        if ufd.is_valid():
            nuso=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            nuso.set_password(password)
            nuso.save()
            return HttpResponse('User Registration Successfully...!')
        else:
            return HttpResponse('Invalid data...!')

    return render(request,'Registration.html',d)



def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        lio=authenticate(username=username,password=password)
        if lio is not None:
            login(request,lio)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('invalid username or password...!')
    return render(request,'user_login.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def Questions_Form(request):
    qfo=QuestionsForm()
    d1={'qfo':qfo}
    if request.method=='POST':
        qfd=QuestionsForm(request.POST)
        if qfd.is_valid():
            username=request.session['username']
            UO=User.objects.get(username=username)
            unso=qfd.save(commit=False)
            unso.user=UO
            unso.save()
            return HttpResponseRedirect(reverse('display_questions'))

    return render(request,'Questions_Form.html',d1)

def display_questions(request):
    dqo=Questions.objects.all()
    d3={'dqo':dqo}
    return render(request,'display_questions.html',d3)


def Answers_Form(request):
    afo=AnswersForm()
    d2={'afo':afo}
    if request.method=='POST':
        afd=AnswersForm(request.POST)
        if afd.is_valid():
            username=request.session['username']
            Uo=User.objects.get(username=username)
            Asuo=afd.save(commit=False)
            Asuo.user=Uo
            Asuo.save()
            Ans=Asuo.dqo
            AO=Answers.objects.filter(dqo=Ans)
            d4={'AO':AO}

            return HttpResponseRedirect(reverse('display_questions'))
            
    return render(request,'Answers_Form.html',d2)