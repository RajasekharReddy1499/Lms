from django.db import models

# Create your models here.

class Course(models.Model):
    Course_Name = models.CharField(max_length=50)
    def __str__(self):
        return  f'{self.Course_Name}'


class Books(models.Model):
    Book_Name = models.CharField(max_length=50)
    Author_Name = models.CharField(max_length=50)
    Course_ID = models.ForeignKey(Course,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return  f'{self.Book_Name}'

class Student(models.Model):
    Stud_Name = models.CharField(max_length=50)
    Stud_Email = models.CharField(max_length=50)
    Stud_Phno = models.BigIntegerField()
    Stud_Password = models.CharField(max_length=50)
    Stud_Semester = models.IntegerField()
    Stud_Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return  f'{self.Stud_Name}'

class Issue_Book(models.Model):
    Stud_Name =  models.ForeignKey(Student, on_delete=models.CASCADE)
    Book_Name = models.ForeignKey(Books,on_delete=models.CASCADE)
    Issued_Date = models.DateField(default=None)
    Valid_Till = models.DateField(default=None)