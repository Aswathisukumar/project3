import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from pro_7.models import teacherr
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
# Create your views here.
def fun(request):
    if request.method=='POST':
        a=request.POST['firstname']
        b=request.POST['lastname']
        c= request.POST['department']
        d=request.POST['age']
        e= request.POST['place']
        f=request.POST['phone']
        g=request.POST['email']
        h= request.FILES['photo']
        i=request.POST['username']
        j=request.POST['password']
        q=teacherr(firstname=a,lastname=b,department=c,age=d,place=e,phone=f,email=g,photo=h,username=i,password=j)
        q.save()
        z = User(first_name=a,last_name=b,username=i,email=g)
        z.set_password(j)
        z.save()
        return HttpResponse('data successfully saved')
    return render(request,'main_page.html')


def fun_1(request):
    return render(request,'home_page.html')


def teacherr_views(request):
    q=teacherr.objects.all()
    return render(request,'views.html',{'p':q})

def teacherr_edit(request,id1):
    p_id=id1
    q=teacherr.objects.get(id=p_id)
    if request.method=='POST':
        q.firstname = request.POST['firstname']
        q.lastname = request.POST['lastname']
        q.department = request.POST['department']
        q.age = request.POST['age']
        q.place = request.POST['place']
        q.phone = request.POST['phone']
        q.email = request.POST['email']
        if len(request.FILES)!=0:
            if len(q.photo)>0:
                os.remove(q.photo.path)
        q.photo = request.FILES['photo']
        q.username = request.POST['username']
        q.save()
        return HttpResponse('data successfully updated')
    return render(request,'views.html',{'r':q})


def teacherr_delete(request,id1):
    p_id=id1
    q=teacherr.objects.get(id=p_id)
    q.delete()
    return HttpResponse('data successfully removed')


def search(request):
    if request.method=='POST':
        a=request.POST['firstname']
        q=teacherr.objects.filter(firstname=a)
        return render(request,'search.html',{'s':q})
    return render(request,'search.html')

def teacherr_login(request):
    if request.method=='POST':
        a=request.POST['username']
        b= request.POST['password']
        q=authenticate(username=a,password=b)
        request.session['user_id']=a
        if q is not None and q.is_superuser == 1:
            return redirect(admin_home)
        else:
            m=teacherr.objects.get(username=a)
            print(m)
            if m.password == b:
                if q is not None and q.is_superuser == 0:
                    return redirect(user_home)
    return render(request,'login.html')



def user_home(request):
    return render(request,'user_home.html')
def admin_home(request):
    return render(request,'admin_home.html')

def logt(request):
    logout(request)
    return HttpResponse("logout")


def profile_edit(request):
    u_id = request.session['user_id']
    q = teacherr.objects.get(username=u_id)
    q1 = User.objects.get(username=u_id)
    if request.method == 'POST':
        q.firstname = request.POST['firstname']
        q.lastname = request.POST['lastname']
        q.department = request.POST['department']
        q.age = request.POST['age']
        q.place = request.POST['place']
        q.phone = request.POST['phone']
        q.email = request.POST['email']
        if len(request.FILES) != 0:
            if len(q.photo) > 0:
                os.remove(q.photo.path)
        q.photo = request.FILES['photo']
        q.username = request.POST['username']
        q.password= request.POST['password']
        q.save()
        q1.firstname = request.POST['firstname']
        q1.lastname = request.POST['lastname']
        q1.department = request.POST['department']
        q1.age = request.POST['age']
        q1.place = request.POST['place']
        q1.phone = request.POST['phone']
        q1.email = request.POST['email']
        q1.username = request.POST['username']
        q1.password = request.POST['password']
        return HttpResponse('data successfully updated')
    return render(request,'profile_edit.html',{'p':q})


def fun_2(request):
    if request.method=='POST':
        a=request.POST['firstname']
        b=request.POST['lastname']
        c= request.POST['gender']
        d=request.POST['age']
        e= request.POST['place']
        f=request.POST['phone']
        g=request.POST['email']
        h= request.FILES['photo']
        i=request.POST['username']
        j=request.POST['password']
        q=teacherr(firstname=a, lastname=b, gender=c, age=d, place=e, phone=f, email=g, photo=h, username=i, password=j)
        q.save()
        # z = User(first_name=a,last_name=b,username=i,email=g)
        # z.set_password(j)
        # z.save()
        return HttpResponse('data successfully saved')
    return render(request,'main.html')

def fun_3(request):
    return render(request,'home_page.html')

# def view(request):
#     q=teacherr.objects.all()
#     return render(request,'view.html',{'p':q})
#
# def edits(request,id1):
#     p_id=id1
#     q=teacherr.objects.get(id=p_id)
#     if request.method=='POST':
#         q.firstname = request.POST['firstname']
#         q.lastname = request.POST['lastname']
#         q.gender = request.POST['gender']
#         q.age = request.POST['age']
#         q.place = request.POST['place']
#         q.phone = request.POST['phone']
#         q.email = request.POST['email']
#         if len(request.FILES)!=0:
#             if len(q.photo)>0:
#                 os.remove(q.photo.path)
#         q.photo = request.FILES['photo']
#         q.username = request.POST['username']
#         q.save()
#         return HttpResponse('data successfully updated')
#     return render(request,'view.html',{'r':q})
#
#
# def delete(request,id1):
#     p_id=id1
#     q=teacherr.objects.get(id=p_id)
#     q.delete()
#     return HttpResponse('data successfully removed')
#
# def search_page(request):
#     if request.method=='POST':
#         a=request.POST['firstname']
#         q=teacherr.objects.filter(firstname=a)
#         return render(request,'search.html',{'s':q})
#     return render(request,'search.html')
#
#
def loginn(request):
    if request.method=='POST':
        a=request.POST['username']
        b= request.POST['password']
        q=authenticate(username=a,password=b)
        request.session['user_id']=a
        if q is not None and q.is_superuser == 1:
            return redirect(admin_home)
        else:
            m=teacherr.objects.get(username=a)
            print(m)
            if m.password == b:
                if q is not None and q.is_superuser == 0:
                    return redirect(user_home)
    return render(request,'loginn.html')