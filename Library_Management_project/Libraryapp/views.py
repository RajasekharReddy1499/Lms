from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template.context_processors import request

from Libraryapp.models import Student, Course, Books, Issue_Book


# Create your views here.
def login_fun(request):
    return render(request, 'login.html',{'data':''})



def Admin_Reg_page(request):
    return render(request,'admin.html')
def logdata_fun(request):
    username = request.POST['txtUserName']
    password = request.POST['txtUserPassword']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_superuser:
            auth.login(request, user)
            request.session["Student_name"] = user.username
            return redirect("Ahome")
        else:
            return render(request, "login.html", {'data': 'Invalid user name and password'})
    else:
        s1 = Student.objects.filter(Q(Stud_Name=username) & Q(Stud_Password=password)).exists()
        if s1:
            n1=request.session['Name'] = username
            print(n1)
            return render(request, "studenthome.html",{'dict':n1})
        else:
            return render(request, 'login.html', {'data': 'Invalid user name and password'})



def Areg_data_fun(request):
    return render(request, 'admin.html')


def Student_Register_fun(request):
    c1 = Course.objects.all()
    s1 = Student()
    if request.method=="POST":
        s1.Stud_Name = request.POST['txtUserName']
        s1.Stud_Email = request.POST['txtUserEmail']
        s1.Stud_Phno = request.POST['txtUserPhno']
        s1.Stud_Password = request.POST['txtUserPassword']
        s1.Stud_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s1.Stud_Semester = request.POST['txtUserSemister']
        if Student.objects.filter(Q(Stud_Name=s1.Stud_Name) | Q(Stud_Password=s1.Stud_Password)).exists():  # true or false function
            return render(request, 'login.html', {'data': 'Username and Email is already exists'})
        s1.save()
        return redirect('log')
    return render(request,'student.html',{'data':c1})




def Regdata_fun(request):
    user_name = request.POST['txtUserName']
    user_password = request.POST['txtUserPassword']
    user_email = request.POST['txtUserEmail']
                                                                                     #exists
    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():    # true or false function
        return render(request,'login.html',{'data':'Username and Email is already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name,email=user_email,password=user_password)
        u1.save()
        return redirect('')


def Adminhome_fun(request):
    return render(request,'adminhome.html')


def Studenthome_fun(request):
    return render(request,'studenthome.html')



def Addbook_fun(request):
    c1 = Course.objects.all()
    return render(request, 'AddBook.html', {'data': c1})

def readBookData(request):
    b1 = Books()
    course=Course.objects.all()
    b1.Book_Name = request.POST.get('txtBookName','ABCD')
    b1.Author_Name = request.POST.get('txtAuthorName','auth1')
    b1.Course_ID = Course.objects.get(Course_Name=request.POST['ddlCourse'])
    b1.save()
    return render(request,'Addbook.html',{"data":course})

def display_fun(request):
    b1 = Books.objects.all()
    return render(request,'display.html',{'data': b1})

def update_fun(request,id):
    b1 = Books.objects.get(id=id)
    c1 = Course.objects.all()

    if request.method == 'POST':
        b1.Book_Name = request.POST['txtBookName']
        b1.Author_Name = request.POST['txtAuthorName']
        b1.Course_ID = Course.objects.get(Course_Name=request.POST['ddlCourse'])
        b1.save()
        return redirect('display')

    return render(request,'update.html',{'data':b1,'Course_data':Course})

def delete_fun(request,id):
    b1 = Books.objects.get(id=id)
    b1.delete()
    return redirect('display')



def student_reg_fun(request):
    course = Course.objects.all()
    s1=Student()
    if request.method=="POST":
        s1.Stud_Name = request.POST['txtname']
        s1.Stud_Phone = request.POST['txtphone']
        s1.Stud_Semester = request.POST['txtsem']
        s1.Stud_Password = request.POST['txtpswd']
        s1.Stud_Course=Course.objects.get(Course_Name=request.POST['ddlcourse'])
        if Student.objects.filter(Q(Stud_Name=s1.Stud_Name) & Q(Stud_Password=s1.Stud_Password)).exists():
            return render(request, "student_signup.html", {'data': 'Student name and student password is already exists'})
        s1.save()
        return redirect('login')
    return render(request,"student.html",{'Course_Data':course})


def update_stud(request,id):
    s1=Student.objects.get(id=id)
    course=Course.objects.all()
    if request.method=="POST":
        s1.Stud_Name=request.POST["txtname"]
        s1.Stud_Phone=request.POST["txtphone"]
        s1.Stud_Semester=request.POST["txtsem"]
        s1.Stud_Course=Course.objects.get(Course_Name = request.POST["ddlcourse"])
        s1.save()
        return redirect('display_student')
    return render(request,"update_students.html",{'data': s1, 'Course_Data': course})

def delete_student(request,id):
    s1=Student.objects.get(id=id)
    s1.delete()
    return redirect("display_student")


def assign_books(request):
    c1=Course.objects.all()
    return render(request,'assignbook.html',{'data':c1})

def readsemester(request):
    student_semester=request.POST['txtsem']
    student_course=Course.objects.get(Course_Name=request.POST['ddlcourse'])
    student=Student.objects.filter(Q(Stud_Semester=student_semester) & Q(Stud_Course=student_course))

    book=Books.objects.filter(Q(Course_ID=Course.objects.get(Course_Name=student_course)))
    return render(request,'assignbook.html',{'Students':student,'Books':book})

def readassignbook(request):
    ib=Issue_Book()
    ib.Stud_Name=Student.objects.get(Stud_Name=request.POST['ddlSname'])
    ib.Book_Name=Books.objects.get(Book_Name=request.POST['ddlSbook'])
    ib.Issued_Date=request.POST['startDate']
    ib.Valid_Till=request.POST['endDate']
    ib.save()
    return render(request,'assignbook.html')


def issued_book(request):
    ib=Issue_Book.objects.all()
    return render(request,"issued_book.html",{'data':ib})

def issuebookupdate(request,id):
    ib=Issue_Book.objects.get(id=id)
    if request.method=='POST':
        ib.Stud_Name = Student.objects.get(Stud_Name=request.POST['txtStudentName'])
        ib.Book_Name = Books.objects.get(Book_Name=request.POST['txtBookName'])
        ib.Issued_Date = request.POST['txtissuedDate']
        ib.Valid_Till = request.POST['txtvalidtill']
        ib.save()
        return redirect('issued_book')
    return render(request,'issuebookupdate.html',{'data':ib})

def issubookdelete(request,id):
    ib = Issue_Book.objects.get(id=id)
    ib.delete()
    return redirect('issued_book')

def studentissuedbook(request):
    ib=Issue_Book.objects.filter(Student_Name=Student.objects.get(Stud_Name=request.session['Name']))
    return render(request,'student_issued_book.html',{'data':ib})


def logout_fun(request):
    return redirect('log')


