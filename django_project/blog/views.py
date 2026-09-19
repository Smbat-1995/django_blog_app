from django.shortcuts import render
# Create your views here.

posts = [
    {'title':'Post 1',
     'content':'Smbat post',
     'author':'Smbat',
     'date_posted':'7 January 1995'},
    {'title':'Post 2',
     'content':'Arman post',
        'author':'Arman',
        'date_posted':'7 July 1999'}

]

def home(request):
    context = {'posts':posts}
    return render(request, 'blog/home.html',context=context)