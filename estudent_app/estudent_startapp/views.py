from multiprocessing import context
from turtle import pd
from urllib import response
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db.models import Avg
from django.utils import timezone
import csv
import pandas as pd



# Create your views here.
# request => response (request handler)
from .models import *
from .forms import AddNewUser, BudgetForm, NeedsForm, WantsForm, SavingsForm, GoalForm

def landingprototype(request):
    #return HttpResponse('Hello Martyna')
    return render(request, 'landingprototype.html', { 'name': '' })

def landing(request):
    form = AddNewUser()
    if request.method =='POST' and request.POST.get("register_user"):
        form = AddNewUser(request.POST)
        if form.is_valid():
            form.save()
            userUsername = form.cleaned_data.get('username')
            messages.success(request, 'User' + ' ' + userUsername + ' ' + 'has been successfully added! Please log in using your new login credentials')
            #messages.error(request, 'User' + ' ' + userUsername + ' ' + 'was unable to be added to the database! Please see the errors below')
    else:
        if request.method =='POST' and request.POST.get("login_user"):
            username = request.POST.get('login_username')
            password = request.POST.get('login_password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'The Username or Password provided is incorrect! Please check your spelling')



    context = {'form':form}
    return render(request, 'landing.html', context)

def logoutUser(request):
    logout(request)
    return render(request, 'logout')

def homepage(request):
    #data = pd.read_csv("usersavings.csv")
    #print(data.head())
    avgNeedsFin = 0
    avgWantsFin = 0
    avgSavingsFin = 0
    avgNeeds = 0
    avgWants = 0
    avgSavings = 0

    try:
        avgNeeds = Need.objects.filter(user = request.user).values_list('total_left_needs').order_by('-edit_date_needs')[:5].aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
        if avgNeeds != None and avgNeedsFin != None:
            avgNeedsFin = avgNeeds / 5
        else:
            avgNeedsFin = 100
    except ObjectDoesNotExist:
            avgNeedsFin = 100

    try:
        avgWants = Want.objects.filter(user = request.user).values_list('total_left_wants').order_by('-edit_date_wants')[:5].aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
        if avgWants != None and avgWantsFin != None:
            avgWantsFin = avgWants / 5
        else:
            avgWantsFin = 100
    except ObjectDoesNotExist:
            avgWantsFin = 100

    try:
        avgSavings = Saving.objects.filter(user = request.user).values_list('total_left_savings').order_by('-edit_date_savings')[:5].aggregate(Sum('total_left_savings')).get('total_left_savings__sum')
        if avgSavings != None and avgSavingsFin != None:
            avgSavingsFin = avgSavings / 5
        else:
            avgSavingsFin = 100
    except ObjectDoesNotExist:
            avgSavingsFin = 100

    #Graph
    #get sum of all needs wants and savings per user ordered by month
    needsJan = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-01-01", "2022-01-31"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
    needsFeb = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-02-01", "2022-02-28"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
    needsMar = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-03-01", "2022-03-31"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
    needsApr = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-04-01", "2022-04-30"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
    needsMay = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-05-01", "2022-05-31"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
    needsJun = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-06-01", "2022-06-30"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
    needsJul = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-07-01", "2022-07-31"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
    needsAug = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-08-01", "2022-08-31"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
    needsSep = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-09-01", "2022-09-30"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
    needsOct = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-10-01", "2022-10-31"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
    needsNov = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-11-01", "2022-11-30"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')
    needsDec = Need.objects.filter(user = request.user).values_list('total_left_needs').filter(edit_date_needs__range=["2022-12-01", "2022-12-31"]).aggregate(Sum('total_left_needs')).get('total_left_needs__sum')

    wantsJan = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-01-01", "2022-01-31"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
    wantsFeb = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-02-01", "2022-02-28"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
    wantsMar = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-03-01", "2022-03-31"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
    wantsApr = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-04-01", "2022-04-30"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
    wantsMay = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-05-01", "2022-05-31"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
    wantsJun = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-06-01", "2022-06-30"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
    wantsJul = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-07-01", "2022-07-31"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
    wantsAug = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-08-01", "2022-08-31"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
    wantsSep = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-09-01", "2022-09-30"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
    wantsOct = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-10-01", "2022-10-31"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
    wantsNov = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-11-01", "2022-11-30"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')
    wantsDec = Want.objects.filter(user = request.user).values_list('total_left_wants').filter(edit_date_wants__range=["2022-12-01", "2022-12-31"]).aggregate(Sum('total_left_wants')).get('total_left_wants__sum')

    savingsJan = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-01-01", "2022-01-31"]).aggregate(Sum('savings_used')).get('savings_used__sum')
    savingsFeb = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-02-01", "2022-02-28"]).aggregate(Sum('savings_used')).get('savings_used__sum')
    savingsMar = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-03-01", "2022-03-31"]).aggregate(Sum('savings_used')).get('savings_used__sum')
    savingsApr = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-04-01", "2022-04-30"]).aggregate(Sum('savings_used')).get('savings_used__sum')
    savingsMay = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-05-01", "2022-05-31"]).aggregate(Sum('savings_used')).get('savings_used__sum')
    savingsJun = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-06-01", "2022-06-30"]).aggregate(Sum('savings_used')).get('savings_used__sum')
    savingsJul = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-07-01", "2022-07-31"]).aggregate(Sum('savings_used')).get('savings_used__sum')
    savingsAug = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-08-01", "2022-08-31"]).aggregate(Sum('savings_used')).get('savings_used__sum')
    savingsSep = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-09-01", "2022-09-30"]).aggregate(Sum('savings_used')).get('savings_used__sum')
    savingsOct = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-10-01", "2022-10-31"]).aggregate(Sum('savings_used')).get('savings_used__sum')
    savingsNov = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-11-01", "2022-11-30"]).aggregate(Sum('savings_used')).get('savings_used__sum')
    savingsDec = Saving.objects.filter(user = request.user).values_list('savings_used').filter(edit_date_savings__range=["2022-12-01", "2022-12-31"]).aggregate(Sum('savings_used')).get('savings_used__sum')

    needsByMonth = 0
    wantsByMonth = 0
    savingsByMonth = 0
    #add to graph data to show month and where money went for need want and saving

    goal = None
    try:
        goal = Goal.objects.filter(user=request.user).values().order_by('date_due')
    except ObjectDoesNotExist:
        goal = None
    user = request.user
    form = GoalForm(user)
    if not request.user.is_authenticated:
        return redirect('landing')


    #Forecasting
    #I wanna show an estimate of how much money will be spent next month based on what has already been spent
    #and then we done :)


    context = {
        'form':form,
        'user':user,
        'goals':goal,
        'avgNeeds':avgNeeds,
        'avgWants':avgWants,
        'avgSavings':avgSavings,
        'avgNeedsFin':avgNeedsFin,
        'avgWantsFin':avgWantsFin,
        'avgSavingsFin':avgSavingsFin,

        'needsByMonth':needsByMonth,
        'wantsByMonth':wantsByMonth,
        'savingsByMonth':savingsByMonth,

        'needsJan':needsJan,
        'wantsJan':wantsJan,
        'savingsJan':savingsJan,
        'needsFeb':needsFeb,
        'wantsFeb':wantsFeb,
        'savingsFeb':savingsFeb,
        'needsMar':needsMar,
        'wantsMar':wantsMar,
        'savingsMar':savingsMar,
        'needsApr':needsApr,
        'wantsApr':wantsApr,
        'savingsApr':savingsApr,
        'needsMay':needsMay,
        'wantsMay':wantsMay,
        'savingsMay':savingsMay,
        'needsJun':needsJun,
        'wantsJun':wantsJun,
        'savingsJun':savingsJun,
        'needsJul':needsJul,
        'wantsJul':wantsJul,
        'savingsJul':savingsJul,
        'needsAug':needsAug,
        'wantsAug':wantsAug,
        'savingsAug':savingsAug,
        'needsSep':needsSep,
        'wantsSep':wantsSep,
        'savingsSep':savingsSep,
        'needsOct':needsOct,
        'wantsOct':wantsOct,
        'savingsOct':savingsOct,
        'needsNov':needsNov,
        'wantsNov':wantsNov,
        'savingsNov':savingsNov,
        'needsDec':needsDec,
        'wantsDec':wantsDec,
        'savingsDec':savingsDec,

    }
    return render(request, 'homepage.html', context)

def export_to_csv(request):
    userSavings = Saving.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=usersavings.csv'
    writer = csv.writer(response)
    writer.writerow(['user', 'savings_budget', 'savings_used', 'edit_date_savings', 'total_left_savings', 'month_int'])
    fields = userSavings.values_list('user', 'savings_budget', 'savings_used', 'edit_date_savings', 'total_left_savings', 'month_int')
    for i in fields:
        writer.writerow(i)
    return response

def profile(request):
    user = request.user.id

    if not request.user.is_authenticated:
        return redirect('landing')
    context = {
        "userid" : user,
    }
    return render(request, 'profile.html', context)

def goals(request):
    goal = None
    deletion = None

    try:
        goal = Goal.objects.filter(user=request.user).values().order_by('date_due')
    except ObjectDoesNotExist:
        goal = None

    user = request.user
    form = GoalForm(user)
    if not request.user.is_authenticated:
        return redirect('landing')
    else:
        if request.user.is_authenticated:
            if request.method =='POST' and request.POST.get("submit_goal"):
                form = GoalForm(user, request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Goal has been successfully added!')
                else:
                    form = GoalForm(user)
                    messages.error(request, 'Due date chosen has already passed!')
            else:
                if request.method =='POST' and request.POST.get("delete_goal"):
                    try:
                        #deletion = Goal.objects.filter(id = 30)
                        deletion = Goal.objects.filter(user=request.user).first()
                        deletion.delete()
                        messages.success(request, 'Goal has been successfully deleted!')
                    except:
                        messages.success(request, 'Goal cannot be deleted')

    context = {
        'form':form,
        'user':user,
        'goals':goal,
        'deletion':deletion
    }
    return render(request, 'goals.html', context)

def information(request):
    budgetI = None
    needsI = None
    wantsI = None
    savingsI = None

    try:
        budgetI = Budget.objects.filter(user=request.user).values().order_by('-edit_date_budget').first()
    except ObjectDoesNotExist:
        budgetI = None

    try:
        needsI = Need.objects.filter(user=request.user).values().order_by('-edit_date_needs').first()
    except ObjectDoesNotExist:
        needsI = None

    try:
        wantsI = Want.objects.filter(user=request.user).values().order_by('-edit_date_wants').first()
    except ObjectDoesNotExist:
        wantsI = None

    try:
        savingsI = Saving.objects.filter(user=request.user).values().order_by('-edit_date_savings').first()
    except ObjectDoesNotExist:
        savingsI = None

    user = request.user
    form = BudgetForm(user)
    form2 = NeedsForm(user)
    form3 = WantsForm(user)
    form4 = SavingsForm(user)
    if not request.user.is_authenticated:
        return redirect('landing')
    else:
        if request.user.is_authenticated:
            if request.method == 'POST' and request.POST.get("submit_budget"):
                form = BudgetForm(user, request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Budget has been successfully added!')
                else:
                    form = BudgetForm(user)
                    messages.error(request, 'The value for budget must equal the sum of needs, wants and savings!\n \u2193')
            if request.method == 'POST' and request.POST.get("submit_needs"):
                form2 = NeedsForm(user, request.POST)
                if form2.is_valid():
                    form2.save()
                    messages.success(request, 'Needs information has been successfully added!')
                else:
                    form2 = NeedsForm(user)
                    messages.error(request, 'Budget for Needs exceeded! Cannot have a negative balance!')
            if request.method == 'POST' and request.POST.get("submit_wants"):
                form3 = WantsForm(user, request.POST)
                if form3.is_valid():
                    form3.save()
                    messages.success(request, 'Wants information has been successfully added!')
                else:
                    form3 = WantsForm(user)
                    messages.error(request, 'Budget for Wants exceeded! Cannot have a negative balance!')
            if request.method == 'POST' and request.POST.get("submit_savings"):
                form4 = SavingsForm(user, request.POST)
                if form4.is_valid():
                    form4.save()
                    messages.success(request, 'Savings information has been successfully added!')
                else:
                    form4 = SavingsForm(user)
                    messages.error(request, 'Budget for Savings exceeded! Cannot have a negative balance!')
    context = {
        'form':form,
        'form2':form2,
        'form3':form3,
        'form4':form4,
        'user':user,
        'budgetI':budgetI,
        'needsI':needsI,
        'wantsI':wantsI,
        'savingsI':savingsI
        }
    return render(request, 'info.html', context)

def about(request):
    return render(request, 'about.html')

def termsandconditions(request):
    return render(request, 'termsandconditions.html')

def newstyle(request):
    return render(request, 'newstyle.html')

def pagesstyle(request):
    return render(request,'pagesstyle.html')

def oldhomepage(request):
    return render(request, 'oldhomepage.html')

def style(request):
    return render(request, 'style.html')

def chart(request):
    return render(request, 'chart.html')

def getHomepageData(request, *args, **kwargs):
    context = {
            "people": 250,
            "sales": 550,
    }
    return JsonResponse(context, safe=False)

#def register(request):
    #form = UserCreationForm()
    #if request.method =='POST':
        #form = UserCreationForm(request.POST)
        #if form.is_valid():
            #form.save()

    #context = {'form':form}
    #return render(request,'testregister.html', context)

