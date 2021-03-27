from django import forms
from .models import Student
from .models import Data_source


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class DataSourceForm(forms.ModelForm):
    class Meta:
        model = Data_source
        fields = "__all__"
