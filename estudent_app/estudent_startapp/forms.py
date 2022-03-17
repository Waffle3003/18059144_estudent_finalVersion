from pyexpat import model
from socket import fromshare
from django.forms import ModelForm, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Budget, Need, Want, Saving, Goal
from datetime import datetime, timedelta

class AddNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = [
            'user',
            'budget',
            'needs',
            'wants',
            'savings'
        ]

    def clean(self):
        data = self.cleaned_data
        calculation = data['needs'] + data['wants'] + data['savings']
        if data['budget'] != calculation:
            raise forms.ValidationError('The value for budget must equal the sum of needs, wants and savings!')
        return self.cleaned_data

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(BudgetForm, self).__init__(*args, **kwargs)


class NeedsForm(forms.ModelForm):
    class Meta:
        model = Need
        fields = [
            'user',
            'needs_budget',
            'rent_accomodation',
            'food',
            'utility_bills',
            'mobile_phone',
            'compulsory_course_expenses',
            'compulsory_travel',
            'other_needs',
        ]

    def clean(self):
        data = self.cleaned_data
        calculation = data['rent_accomodation'] + data['food'] + data['utility_bills'] + data['mobile_phone'] + data['compulsory_course_expenses'] + data['compulsory_travel'] + data['other_needs']
        if data['needs_budget'] < calculation:
            raise forms.ValidationError('Budget exceeded! Cannot have a negative balance!')
        return self.cleaned_data

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(NeedsForm, self).__init__(*args, **kwargs)

class WantsForm(forms.ModelForm):
    class Meta:
        model = Want
        fields = [
            'user',
            'wants_budget',
            'going_out',
            'takeaway',
            'unnecessary_transport',
            'clothes_personal_care',
            'other_wants'
        ]

    def clean(self):
        data = self.cleaned_data
        calculation = data['going_out'] + data['takeaway'] + data['unnecessary_transport'] + data['clothes_personal_care'] + data['other_wants']
        if data['wants_budget'] < calculation:
            raise forms.ValidationError('Budget exceeded! Cannot have a negative balance!')
        return self.cleaned_data

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(WantsForm, self).__init__(*args, **kwargs)

class SavingsForm(forms.ModelForm):
    class Meta:
        model = Saving
        fields = [
            'user',
            'savings_budget',
            'savings_used'
        ]

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SavingsForm, self).__init__(*args, **kwargs)

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = [
            'user',
            'name',
            'amount',
            'id',
            'date_due',
        ]

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(GoalForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        goaldate = str(data['date_due'])
        today = datetime.today().strftime('%Y-%m-%d')
        if goaldate < today:
            raise forms.ValidationError('Only upcoming dates can be set!')
        return self.cleaned_data

    
