from django.contrib import admin
from .models import SchoolProfile, Complexion, NextClass, PreviousClass, Genotype, Religion, \
    State,Sex, BloodGroup, SchoolPrefect, Dates

class SchoolProfileAdmin(admin.ModelAdmin):
    list_display = ('SurName','FirstName','LastName','Sex','Birth_date','Religion','Weight',
                    'Height','State_of_origin','Local_government_Area', 'complexion',
                    'Name_of_parent_or_guardian', 'Address_of_parent_or_guardian','Phone_number',
                    'In_case_of_emergency_call','E_mail', 'Blood_group','genotype','Admission_date',
                    'Admission_number','previous_class','current_class','profile_picture',)

class SchoolPrefectAdmin(admin.ModelAdmin):
    list_display = ('SurName', 'FirstName', 'OtherNames','BirthDate', 'Religion','Age',
                    'StateOfOrigin','LocalGovernmentArea', 'Gender','Office','WiseQuote','Picture',
                    'BestSubject','Class','Career','FavouriteTeacher','RoleModel','Skills',
                    'FavouriteFood','FavouriteMusic','FavouriteTvShows','Department',
                    'Dislikes','YearInducted')

admin.site.register(SchoolPrefect, SchoolPrefectAdmin)
admin.site.register(SchoolProfile, SchoolProfileAdmin)
admin.site.register(Complexion)
admin.site.register(NextClass)
admin.site.register(PreviousClass)
admin.site.register(Genotype)
admin.site.register(Religion)
admin.site.register(State)
admin.site.register(Sex)
admin.site.register(BloodGroup)
#admin.site.register(SchoolPrefect, SchoolPrefectAdmin)
admin.site.register(Dates)
