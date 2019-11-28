from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from car_sales_app.forms import SalesForm,UserForm,LoginForm,Sales_view_form
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class IndexView(LoginRequiredMixin,TemplateView):

    template_name = 'base.html'


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() :

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'index.html',
                          {'user_form':user_form,
                           'registered':registered})


class SalesListView(LoginRequiredMixin,ListView):
    context_object_name = 'sales_list'
    model = models.Sales
    template_name = 'sales_list.html'
    paginate_by = 8


class SalesDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'sales_details'
    model = models.Sales
    template_name = 'sales_detail.html'


class SalesCreateView(LoginRequiredMixin,CreateView):
    fields = ('sales_id','fuel','vehicle_segment','selling_price','purchased_date','customer','power_steering','airbags','sunroof','matt_finish','music_system')
    model = models.Sales
    template_name = 'sales_form.html'


class SalesUpdateView(LoginRequiredMixin,UpdateView):
    #fields = ('sales_id','fuel','vehicle_segment','selling_price','purchased_date','customer','power_steering','airbags','sunroof','matt_finish','music_system')
    model = models.Sales
    form_class = SalesForm
    template_name = 'sales_form.html'

class SalesDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Sales
    success_url = reverse_lazy("car_sales_app:sales_list")
    template_name = 'sales_confirm_delete.html'


class CustomerListView(LoginRequiredMixin,ListView):
    context_object_name = 'customer_list'
    model = models.Customer
    template_name = 'customer_list.html'
    paginate_by = 8


class CustomerDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'customer_details'
    model = models.Customer
    template_name = 'customer_detail.html'


class CustomerCreateView(LoginRequiredMixin,CreateView):
    fields = ('customer_id','customer_gender','customer_region','customer_marital_status','customer_income_group')
    model = models.Customer
    template_name = 'customer_form.html'


class CustomerUpdateView(LoginRequiredMixin,UpdateView):
    fields = ('customer_id','customer_gender','customer_region','customer_marital_status','customer_income_group')
    model = models.Customer
    template_name = 'customer_form.html'

class CustomerDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Customer
    success_url = reverse_lazy("car_sales_app:customer_list")
    template_name = 'customer_confirm_delete.html'

def ajax_search(request):
    print ("hello")
    if request.is_ajax():
        print (request.GET.get("search"))
        try :
            qs1 = models.Sales.objects.filter(sales_id__icontains = request.GET.get("search")).values('sales_id')[:5]
        except :
            qs1 = models.Sales.objects.filter(sales_id__icontains = request.GET.get("search")).values('sales_id')
        try:
            qs2 = models.Customer.objects.filter(customer_id__icontains = request.GET.get("search")).values('customer_id')[:5]
        except:
            qs2 = models.Customer.objects.filter(customer_id__icontains = request.GET.get("search")).values('customer_id')

        result = []
        for i in list(qs1):
            result.append("sal:"+str(i['sales_id']))
        for i in list(qs2):
            result.append("cus:"+str(i['customer_id']))
        print (result)
        data = json.dumps(result)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
@login_required
def get_search_result(request):
    text_search = request.GET.get('txt')
    print ("hello")
    if text_search.startswith("sal"):
        sales_details = models.Sales.objects.get(sales_id = text_search.split(":")[1])
        return HttpResponseRedirect(reverse('car_sales_app:sales_detail', args=[str(sales_details.id)]))
    elif text_search.startswith("cus"):
        customer_details = models.Customer.objects.get(customer_id = text_search.split(":")[1])
        return HttpResponseRedirect(reverse('car_sales_app:customer_detail', args=[str(customer_details.id)]))
    else:
        return render(request, 'data_not_found.html', context ={})





@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # First get the username and password supplied
            username = request.POST.get('username')
            password = request.POST.get('password')
            print (username,password)

            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            if  user:
                if user.is_active:

                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    messages.error(request, "User is not active")
                    return HttpResponseRedirect(reverse('car_sales_app:user_login'))
            else:
                messages.error(request, "Username or password is not valid")
                return HttpResponseRedirect(reverse('car_sales_app:user_login'))



        #Nothing has been provided for username or password.
    return render(request, 'login.html', context = {'form': form})

def sales_view(request):
    form = Sales_view_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # First get the username and password supplied
            reg = request.POST.get('region')
            month = request.POST.get('month')
            year = request.POST.get('year')
            print (reg,month,year)

            #print ([ i for i in range(1950,(datetime.now().year+1)])
            sales_list = models.Sales.objects.filter(customer__customer_region=reg,purchased_date__year = year,purchased_date__month = month)
            print (len(sales_list))
            return render(request, 'sales_list.html', context = {'sales_list': sales_list})
            # Django's built-in authentication function:




        #Nothing has been provided for username or password.
    return render(request, 'sales_view.html', context = {'form': form})
