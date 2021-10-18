from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

# for authentication and messaging output to user
from django.contrib import messages
from django.contrib.auth.models import User, auth

# for regular expression
import re

# decorator for restict other pages without loging in
from django.contrib.auth.decorators import login_required


# calling the product model here
from .models import Product


# signup backend
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # password validation
        if password == confirm_password:  # confirm password process

            if len(password) >= 8:  # logic for at least 8 digit long password

                # logic for at least 1 uppercase and 1 lower case
                if re.findall('[A-Z]', password) and re.findall('[a-z]', password):

                    # Logic for at least 1 special charecter.
                    if re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):

                        # logic for first digit cannot be a number
                        if not ((list(password))[0].isdigit()):

                            # existing username will not allowed
                            if User.objects.filter(username=username).exists():
                                messages.error(
                                    request, "take another username")
                                return render(request, 'shop/signup.html')

                            # existing email will not allowed
                            elif User.objects.filter(email=email).exists():
                                messages.error(request, "email already exists")
                                return render(request, 'shop/signup.html')

                            else:
                                user = User.objects.create_user(
                                    username=username, email=email, password=password)
                                user.save()

                        else:
                            messages.error(
                                request, "First digit can't be number.")
                            return render(request, 'shop/signup.html')

                    else:
                        messages.error(
                            request, "must contain at least 1 special charecter.")
                        return render(request, 'shop/signup.html')

                else:
                    messages.error(
                        request, "Must have at least 1 uppercase,\n 1 lowecase,\nand 1 special charecter.")
                    return render(request, 'shop/signup.html')

            else:
                messages.error(
                    request, "Password should be at least 8 digit long")
                return render(request, 'shop/signup.html')

        else:
            messages.error(request, "password Not macthed")
            return render(request, 'shop/signup.html')

        messages.success(request, "Registration completed Successfully")
        return render(request, "shop/login.html")

    else:
        return render(request, 'shop/signup.html')

    return render(request, 'shop/signup.html')


# login backend
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'successfully loged in')
            return redirect('/')
        else:
            messages.error(request, 'invalid credential')
            return render(request, "shop/login.html")

    else:
        messages.error(request, "invalid Credential !!")
        return render(request, "shop/login.html")

    return render(request, 'shop/login.html')


# Logout backend
def logout(request):
    auth.logout(request)
    messages.info(request, "Loged out from the site")
    return render(request, "shop/login.html")


# decorator- you will not have access untill you login
@login_required(login_url="/login")
# home backend
def home(request):
    product_database = Product.objects.all()
    return render(request, "shop/home.html", {"product_database": product_database})



# decorator- you will not have access untill you login
@login_required(login_url="/login")
# product preview backend
def product_preview(request, product_id):
    product_details = Product.objects.filter(id=product_id)

    #view counter for product preview
    """If any one previews the details of any product, the product view will increase """
    
    product_view = Product.objects.filter(id=product_id).first()
    product_view.view = product_view.view+1
    product_view.save()

    return render(request, "shop/productView.html", {"product_details": product_details[0]})
