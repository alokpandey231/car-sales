from django import forms
from car_sales_app.models import Customer,Sales
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class SalesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['purchased_date'].widget.attrs['readonly'] = True

    def clean_purchased_date(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.purchased_date
        else:
            return self.cleaned_data['purchased_date']
    class Meta():
        model = Sales
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class LoginForm (forms.Form):
    username = forms.CharField(label='username', max_length=20,required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput,required=True)

    def clean(self):
        all_clean_data = super().clean()
        username = all_clean_data.get("username")
        password = all_clean_data.get("password")


class Sales_view_form(forms.Form):
    choicelist = REGION_CHOICE = (('North','North'),('South','South'),('East','East'),('West','West'))
    choicelist1 = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'))
    region =  forms.ChoiceField(choices=choicelist,label='Region')
    month = forms.ChoiceField(choices=choicelist1,label='Month')
    year = forms.CharField(label='Year', max_length=4,required=True)

    #Month_year = forms.DateField(required=False,widget=MonthYearWidget(years=xrange(2004,2010)))
