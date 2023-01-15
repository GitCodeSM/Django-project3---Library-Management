import email
from django.shortcuts import render, redirect
from django.http import request
from django.contrib import admin
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from management.models import Book, Member
from management.forms import BookForm
# to allow other domains easily access our methods
from django.views.decorators.csrf import csrf_exempt
# import local data
from management.api.serializers import BookSerializer, MemberSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here. #Create a Django Template for the form #Render the ModelForm and Model objects
def homepage(request):

    book_form = BookForm()
    books = Book.objects.all()

    if request.method == "POST":
        book_form = BookForm(request.POST, request.FILES)
        # Adding an if condition for the form posting.
        # Adding request.FILES as the sources of the file data or your image will not save to the form.
        if book_form.is_valid():
            book_form.save()
            messages.success(request, ('Your book was successfully added!'))
        else:
            messages.error(request, 'Error saving form')
            
        return redirect('/') #redirect("management:homepage")
        
    return render(request=request, template_name="index.html", context={'book_form':book_form, 'books':books})

# Because the form is a BookForm, saving the form will also add a new model object to the Book model making it easy to...
# render the form and the model objects

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "Password is not the same")
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# @csrf_exempt was interfering with class BookAV

class BookAV(APIView):

    def get(self, request):

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailAV(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error':'Not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = Book(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk): #request is important
        book = Book.objects.get(pk=pk)
        book.delete()
        # return Response({'message':'this data is deleted'})
        return Response(status=status.HTTP_204_NO_CONTENT)


class MemberAV(APIView):

    def get(self, request):
        member = Member.objects.all()
        serializer = MemberSerializer(member, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

