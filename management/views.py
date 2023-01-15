# import email
# from django.shortcuts import render, redirect
# from django.http import request, HttpResponse
# from django.contrib import admin
# from django.contrib.auth.models import User, auth
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from management.models import Book
# from management.forms import BookForm
# # to allow other domains easily access our methods
# from django.views.decorators.csrf import csrf_exempt
# #json parser to parse the in concomming data into the data model
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# # import local data
# from .serializer import BookSerializer

# # Create your views here. #Create a Django Template for the form #Render the ModelForm and Model objects
# def homepage(request):

#     book_form = BookForm()
#     books = Book.objects.all()

#     if request.method == "POST":
#         book_form = BookForm(request.POST, request.FILES)
#         # Adding an if condition for the form posting.
#         # Adding request.FILES as the sources of the file data or your image will not save to the form.
#         if book_form.is_valid():
#             book_form.save()
#             messages.success(request, ('Your book was successfully added!'))
#         else:
#             messages.error(request, 'Error saving form')
            
#         return redirect('/') #redirect("management:homepage")
        
#     return render(request=request, template_name="index.html", context={'book_form':book_form, 'books':books})

# # Because the form is a BookForm, saving the form will also add a new model object to the Book model making it easy to...
# # render the form and the model objects

# def signup(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']

#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, "Email Already Used")
#                 return redirect('signup')
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request, "Username Already Used")
#                 return redirect('signup')
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save();
#                 return redirect('login')

#         else:
#             messages.info(request, "Password is not the same")
#             return redirect('signup')
#     else:
#         return render(request, 'signup.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request, 'Credentials Invalid')
#             return redirect('login')

#     return render(request, 'login.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('/')

# @csrf_exempt
# # Normally when you make a request via a form you want the form being submitted to your view to 
# # originate from your website and not come from some other domain. To ensure that this happens, you 
# # can put a csrf token in your form for your view to recognize. If you add @csrf_exempt to the top 
# # of your view, then you are basically telling the view that it doesn't need the token. This is a 
# # security exemption that you should take seriously.

# def BookView(request):

#     if request.method == 'POST':
#         book_data=JSONParser().parse(request)
#         #use serializer to convert it into model type
#         book_serializer = BookSerializer(data = book_data)
#         #check if model is valid
#         if book_serializer.is_valid():
#             #if valid save and send success message if not return fail message
#             print(book_data)
#             book_serializer.save()
#             return JsonResponse("Added Successfully!!", safe=False)
#         return JsonResponse("Failed to Add.", safe=False)

#     if request.method == 'GET':
#         books = Book.objects.all()
#         #we are using serializer class to help it convert into json format
#         #serialize it with serializer class which we have defined
#         book_serializer = BookSerializer(books, many=True)
#         #and then return a json response
#         return JsonResponse(book_serializer.data, safe=False)

