from django.shortcuts import render
from .models import SchoolProfile, SchoolPrefect, Dates
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
# Create your views here.
'''def Primus(request):
    context = {
        'schools': SchoolProfile.objects.all()
    }

    return render(request, 'primus.html', context)'''
class SchoolListView(ListView):
    model = SchoolProfile
    template_name = 'Primus.html'
    context_object_name = 'schools'
    ordering = ['-Admission_date']

class SchoolDetailView(DetailView):
    model = SchoolProfile
    template_name = 'students_detail.html'

class StudentCreateView(CreateView):
    model = SchoolProfile
    template_name = 'students_form.html'
    fields = ['SurName', 'FirstName', 'LastName','Sex','Birth_date', 'Religion','Weight',
              'Height','State_of_origin', 'Local_government_Area', 'complexion', 'Name_of_parent_or_guardian',
              'Address_of_parent_or_guardian','Phone_number','In_case_of_emergency_call','E_mail',
              'Blood_group','genotype', 'Admission_date', 'Admission_number', 'previous_class',
              'current_class', 'profile_picture']
class StudentUpdateView(UpdateView):
    model = SchoolProfile
    template_name = 'students_update.html'
    fields = ['SurName', 'FirstName', 'LastName','Sex','Birth_date', 'Religion','Weight',
              'Height','State_of_origin', 'Local_government_Area', 'complexion', 'Name_of_parent_or_guardian',
              'Address_of_parent_or_guardian','Phone_number','In_case_of_emergency_call','E_mail',
              'Blood_group','genotype', 'Admission_date', 'Admission_number', 'previous_class',
              'current_class', 'profile_picture']

    
class StudentDeleteView(DeleteView):
    model = SchoolProfile
    template_name = 'students_delete.html'
    success_url = '/'

class PrefectListView(ListView):
    model = SchoolPrefect
    template_name = 'prefect.html'
    context_object_name = 'prefects'
    ordering = ['YearInducted']

class PrefectDetailView(DetailView):
    model = SchoolPrefect
    template_name = 'prefects_detail.html'

class PrefectCreateView(CreateView):
    model = SchoolPrefect
    template_name = 'prefects_form.html'
    fields = ['SurName','FirstName', 'OtherNames','BirthDate', 'Religion','Age',
                    'StateOfOrigin','LocalGovernmentArea', 'Gender','Office','WiseQuote','Picture',
                    'BestSubject','Class','Career','FavouriteTeacher','RoleModel','Skills',
                    'FavouriteFood','FavouriteMusic','FavouriteTvShows','Department',
                    'Dislikes','YearInducted']

class PrefectUpdateView(UpdateView):
    model = SchoolPrefect
    template_name = 'prefects_update.html'
    fields = ['SurName','FirstName', 'OtherNames','BirthDate', 'Religion','Age',
                    'StateOfOrigin','LocalGovernmentArea', 'Gender','Office','WiseQuote','Picture',
                    'BestSubject','Class','Career','FavouriteTeacher','RoleModel','Skills',
                    'FavouriteFood','FavouriteMusic','FavouriteTvShows','Department',
                    'Dislikes','YearInducted']
class PrefectDeleteView(DeleteView):
    model = SchoolPrefect
    template_name = 'prefects_delete.html'
    success_url = '/'

