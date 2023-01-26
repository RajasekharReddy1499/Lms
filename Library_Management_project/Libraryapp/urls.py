from django.urls import path

from Libraryapp import views

urlpatterns = [
    path('',views.login_fun,name='log'),
    path('logdata',views.logdata_fun),
    path('Admin_reg',views.Admin_Reg_page),
    path('readdata',views.Regdata_fun),

    path('adminhome',views.Adminhome_fun,name='Ahome'),
    path('Studenthome',views.Studenthome_fun,name='Shome'),

    path('Aregdata',views.Areg_data_fun,name='Admin_reg'),
    path('Sregdata',views.Student_Register_fun,name='Student_reg'),

    path('add_books',views.Addbook_fun,name='add_books'),
    path('readAddBookData',views.readBookData,name='add'),

    path('display',views.display_fun,name='display'),
    path('Updata/<int:id>',views.update_fun,name='update'),
    path('delete/<int:id>',views.delete_fun,name='delete'),


    path("updatestudent/<int:id>",views.update_stud, name="update_student"),
    path("deletestud/<int:id>",views.delete_student,name="delete_student"),

    path("assignbook", views.assign_books,name="assign_book"),
    path('readassignbook',views.readassignbook,name='readassignbook'),
    path('readsemester',views.readsemester,name='readsemester'),

    path("issuedbook", views.issued_book, name="issued_book"),
    path('issuebookupdate/<int:id>',views.issuebookupdate,name='issuebookupdate'),
    path('issuebookdelete/<int:id>',views.issubookdelete,name='issuebookdelete'),
    path('student_issued_book',views.studentissuedbook,name='student_issued_book'),
    path("logout", views.logout_fun , name='logout'),

]