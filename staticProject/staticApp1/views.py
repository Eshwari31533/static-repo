from django.shortcuts import render

# Create your views here.
def view1(request):
    myName="Eshwari"
    favPlayer="Dhoni"
    favAnimal="Lion"
    favSubject="python"
    d={'name':myName,'player':favPlayer,'subject':favSubject,'animal':favAnimal}
    return render(request,'staticApp1/1.html',d)
