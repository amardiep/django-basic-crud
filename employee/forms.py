from django import forms
from .models import Emp_data

class FeedbackForm(forms.Form):
    email= forms.EmailField(label="Enter Your Email Address",max_length=100)
    name = forms.CharField(label="Enter your name", max_length=30, required=False)
    feedback = forms.CharField(label="Give your feedback here", max_length=500, widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(FeedbackForm,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp_data
        fields = ['fname','lname','contact','department']