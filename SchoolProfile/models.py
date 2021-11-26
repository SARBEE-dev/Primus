from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse
from django.conf.urls.static import static
# Create your models here.
class Religion(models.Model):
    religion = models.CharField(max_length=100)
    def __str__(self):
        return self.religion
class Complexion(models.Model):
    complexion = models.CharField(max_length=200)
    def __str__(self):
        return self.complexion
class Genotype(models.Model):
    genotype = models.CharField(max_length=2)
    def __str__(self):
        return self.genotype
class State(models.Model):
    state = models.CharField(max_length=20)
    def __str__(self):
        return self.state
class BloodGroup(models.Model):
    blood_group = models.CharField(max_length=4)
    def __str__(self):
        return self.blood_group
class PreviousClass(models.Model):
    previous = models.CharField(max_length=10)
    def __str__(self):
        return self.previous
class NextClass(models.Model):
    next = models.CharField(max_length=10)
    def __str__(self):
        return self.next
class Sex(models.Model):
    sex = models.CharField(max_length=7)
    def __str__(self):
        return self.sex
class SchoolProfile(models.Model):
    SurName = models.CharField(max_length=150)
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150, blank=True)
    Sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    Birth_date = models.DateField()
    Religion = models.ForeignKey(Religion, on_delete=models.CASCADE, blank=True)
    Weight = models.FloatField(blank=True)
    Height = models.FloatField(blank=True)
    State_of_origin = models.ForeignKey(State, on_delete=models.CASCADE)
    Local_government_Area = models.CharField(max_length=200, blank=True)
    complexion = models.ForeignKey(Complexion, on_delete=models.CASCADE, blank=True)
    Name_of_parent_or_guardian = models.CharField(max_length=250)
    Address_of_parent_or_guardian = models.TextField()
    Phone_number = models.IntegerField()
    In_case_of_emergency_call = models.IntegerField()
    E_mail = models.EmailField(blank=True)
    Blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, blank=True)
    genotype = models.ForeignKey(Genotype, on_delete=models.CASCADE, blank=True)
    Admission_date = models.DateTimeField(default=timezone.now)
    Admission_number = models.CharField(max_length=30, blank=True)
    previous_class = models.ForeignKey(PreviousClass, on_delete=models.CASCADE)
    current_class = models.ForeignKey(NextClass, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_Pics')

    def get_absolute_url(self):
        return reverse('students_detail',
                    kwargs={'pk':self.pk})
'''
    def save(self, *args, **kwargs):
        # change profile image size
        super(SchoolProfile, self).save(*args, **kwargs)
        result = Image.open(self.profile_picture.path)
        if result.height > 300 or result.width > 300:
            output_size = (200, 200)
            result.thumbnail(output_size)
            result.save(self.profile_picture.path) '''

class Dates(models.Model):
    Year = models.DateField()

    def __str__(self):
        return self.year

class SchoolPrefect(models.Model):
    SurName = models.CharField(max_length=150)
    FirstName = models.CharField(max_length=150)
    OtherNames = models.CharField(blank=True, max_length=200)
    BirthDate = models.DateField()
    Religion = models.CharField(blank=True, max_length=50)
    Age = models.IntegerField(default=10)
    StateOfOrigin = models.CharField(max_length=30)
    LocalGovernmentArea = models.CharField(blank=True, max_length=200)
    Gender = models.CharField(max_length=10)
    Office = models.CharField(max_length=100)
    WiseQuote = models.TextField(blank=True)
    Picture = models.ImageField(upload_to='profile_pics')
    BestSubject = models.CharField(max_length=20)
    Class = models.CharField(max_length=10)
    Career = models.CharField(max_length=200)
    FavouriteTeacher = models.CharField(blank=True,max_length=200)
    RoleModel = models.TextField(blank=True)
    Skills = models.TextField(blank=True)
    FavouriteFood = models.CharField(max_length=200, blank=True)
    FavouriteMusic = models.TextField(blank=True)
    FavouriteTvShows = models.TextField(blank=True)
    Department = models.CharField(max_length=10)
    Dislikes = models.TextField(blank=True)
    YearInducted = models.DateField()

    def get_absolute_url(self):
        return reverse('prefects_detail',
                    kwargs={'pk':self.pk})

