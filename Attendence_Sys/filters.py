import django_filters

from .models import Attendence

class AttendenceFilter(django_filters.FilterSet):
    class Meta:
        model = Attendence
        fields = '__all__'
        exclude = ['Faculty_Name', 'status','time','branch']
        
        

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Attendence
        fields = '__all__'
        exclude = ['Faculty_Name', 'status','time','branch','Student_ID']
        
        
        
class ReportFilter(django_filters.FilterSet):
    class Meta:
        model = Attendence
        fields = '__all__'
        exclude = ['Faculty_Name', 'status','time','Student_ID','date','period']