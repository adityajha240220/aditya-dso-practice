from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import logout

# Create your views here.

# Write a function-based view in Django that returns “Hello, Django” as an HTTP response.

def hello_view(request):
    return HttpResponse("Hello, Django")

# Write a class-based view that returns a template called home.html.  

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')        


# Write the Django view code that sends {'name': 'Aadi'} to a template called profile.html.

def profile_view(request):
    return render(request, 'profile.html', {'name': 'Aadi'})


# Write the code to handle a GET request in a Django view.

def get_view(request):
    if request.method == "GET":  
        return HttpResponse("This is a GET request") 


# Write the code to handle a POST request in a Django view.

@csrf_exempt
def post_view(request):
    if request.method == "POST":
        return HttpResponse("This is a POST request")      


# Write the Django context dictionary in a view that passes {'course': 'Django'} to course.html.

def course_view(request):
    return render(request, 'course.html', {'course': 'Django'})




def about_view(request):
    return render(request, "about.html")


# Show the code to extend Django’s default User model using AbstractUser.    


         
# Write the view code for logging out a user using Django’s built-in logout() function. enke answers

def logout_view(request):
    logout(request)
    return redirect('login')         