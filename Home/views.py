from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import Sum
import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
import pandas as pd
from django.contrib import messages
from Home.models import Book
from .models import UploadedFile
from django.db.models import Q
from .forms import UserProfileForm
from .models import UserProfile
from .models import UserProfile1
from .forms import UserProfile1Form
from django.shortcuts import get_object_or_404

#username - aditya
#password - sutt#*back

generated_id = None
a = None

BRANCH_CODES = {
    "Chemical": "A1",
    "Civil": "A2",
    "EEE": "A3",
    "Mechanical": "A4",
    "BPharma": "A5",
    "CSE": "A7",
    "ENI": "A8",
    "Biotech": "A9",
    "Bio": "B1",
    "Chem": "B2",
    "Eco": "B3",
    "Math": "B4",
    "Physics": "B5",
    "ECE": "AA",
    "Manufacturing": "AB"
}

def user_has_profile(user):
    return UserProfile.objects.filter(user=user).exists()

def create_profile(request):
    if request.user.is_anonymous:
        return redirect("/login1")
    # Check if the logged-in user already has a profile
    existing_profile = UserProfile.objects.filter(user=request.user).first()
    
    if existing_profile:
        # Redirect to the profile list or an appropriate page
        return redirect('profile_list')  

    if request.method == 'POST':
        global a
        a = 1
        global form
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Associate the profile with the logged-in user
            profile.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()

    return render(request, 'create_profile.html', {'form': form})

def create_profile1(request):
    if request.user.is_anonymous:
        return redirect("/login")
    # Check if the logged-in user already has a profile
    existing_profile = UserProfile1.objects.filter(user=request.user).first()
    
    if existing_profile:
        # Redirect to the profile list or an appropriate page
        return redirect('profile_list1')  

    if request.method == 'POST':
        branch_name = request.POST.get('branch')  # Input from user
        branch_code = BRANCH_CODES[branch_name]  # Get branch code from mapping

        global generated_id 
        generated_id = f"{year}{branch_code}PS{roll_number}P"

        global form1
        form1 = UserProfile1Form(request.POST, request.FILES)
        if form1.is_valid():
            profile = form1.save(commit=False)
            profile.user = request.user  # Associate the profile with the logged-in user
            profile.save()
            return redirect('profile_list1')
    else:
        form1 = UserProfile1Form()

    return render(request, 'create_profile1.html', {'form': form1})

def delete_all_profiles(request):
    if request.user.is_anonymous:
        return redirect("/login1")
    # Delete all profiles
    UserProfile.objects.all().delete()
    # Log out the user
    logout(request)
    # Redirect to the login page or any other page
    return redirect("/login1")

def delete_all_profiles1(request):
    if request.user.is_anonymous:
        return redirect("/login")
    # Delete all profiles
    UserProfile1.objects.all().delete()
    # Log out the user
    logout(request)
    # Redirect to the login page or any other page
    return redirect("/login")


def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Check if there are available copies to borrow
    if book.total_copies > 0:
        # Decrease total copies and increase borrowed count
        book.total_copies -= 1
        book.borrowed_count += 1
        book.save()

        return redirect('borrowed_books')  # Redirect to borrowed books page
    else:
        # Handle case where no copies are available to borrow
        return render(request, 'error_page.html', {'error': 'No copies left to borrow.'})

def borrowed_books(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if generated_id == None : 
        return redirect("/exist_profile")
    # Get all books that have been borrowed at least once
    books = Book.objects.filter(borrowed_count__gte=1)

    # Calculate the total number of books borrowed
    total_borrowed_count = sum(book.borrowed_count for book in books)

    # Pass the books and total borrowed count to the template
    return render(request, 'borrow_books.html', {
        'books': books,
        'borrowed_count': total_borrowed_count,
    })

def profile_list(request):
    if request.user.is_anonymous:
        return redirect("/login1")
    profiles = UserProfile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})

def profile_list1(request):
    if request.user.is_anonymous:
        return redirect("/login")
    profiles1 = UserProfile1.objects.all()
    return render(request, 'profile_list1.html', {'profiles': profiles1})

def index(request):
    return render(request, 'index.html')

def exist_profile(request):
    return render(request, 'exist_profile.html')

def form(request):
    if request.user.is_anonymous:
        return redirect("/login1")

    if a == None :
        return redirect("/exist_profile")

    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        isbn = request.POST.get('isbn')
        total_copies = request.POST.get('total_copies')
        image = request.FILES.get('image')

        if Book.objects.filter(isbn=isbn).exists():
            messages.error(request, "A book with this ISBN already exists.")
            return render(request, 'form.html')

        # Save book information in the database
        new_book = Book(title=title, author=author, publisher=publisher,
                        isbn=isbn, total_copies=total_copies, image=image)
        new_book.save()

        return redirect('/books')  # Redirect to the list or search page

    return render(request, 'form.html')

def index1(request):
    if request.user.is_anonymous:
        return redirect("/login")
    try:
        profile = UserProfile1.objects.get(user=request.user)
    except UserProfile1.DoesNotExist:
        profile = None
    borrowed_count = Book.objects.aggregate(total_borrowed=Sum('borrowed_count'))['total_borrowed'] or 0
    if generated_id is not None :
        return render(request, 'index1.html', {'borrowed_count': borrowed_count, 'profile': profile, 'generated_id' : generated_id})
    else : 
        return render(request, 'index1.html', {'borrowed_count': borrowed_count, 'profile': profile})

def index2(request):
    if request.user.is_anonymous:
        return redirect("/login1")
    # Fetch the user's profile
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'index2.html', {'profile': profile})


def about(request):
    return render(request, 'about.html')

def upload_books_upload_books(request):
    return render(request, 'message.html')

def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        global year
        global roll_number
        year = email[1:5]  # Extract year from email
        roll_number = email[5:9]  # Extract roll number from email
        
        username = User.objects.get(email = email.lower()).username
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            return render(request, 'index1.html')
        else:
            return redirect("/login")
    return render(request, 'login.html')

def loginUser1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect("/index2")
        else:
            return redirect("/login1")
    return render(request, 'login1.html')

def download_template(request):
    # Define the template file path
    file_path = os.path.join(settings.BASE_DIR, 'templates', 'book_template.xlsx')

    # Serve the file for download
    with open(file_path, 'rb') as template:
        response = HttpResponse(template.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=book_template.xlsx'
        return response

def upload_books(request):
    if request.user.is_anonymous:
        return redirect("/login1")
    
    if a == None : 
        return redirect("/exist_profile")

    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        # Save file to the database
        uploaded_file = UploadedFile.objects.create(file=excel_file)

        try:
            # Process the file using pandas
            df = pd.read_excel(uploaded_file.file.path)

            for _, row in df.iterrows():
                Book.objects.create(
                    title=row['Title'],
                    author=row['Author'],
                    publisher=row['Publisher'],
                    isbn=row['ISBN'],
                    total_copies=row['Total_Copies'],
                )
            messages.success(request, 'Books successfully uploaded!')

        except Exception as e:
            messages.error(request, f"Error processing file: {e}")

    return render(request, 'upload_books.html')

def display_books(request):
    if request.user.is_anonymous:
        return redirect("/login1")

    if generated_id == None : 
        return redirect("/exist_profile")

    previous_path = request.META.get('HTTP_REFERER', '')  # Get the previous URL
    if previous_path.endswith('/index2'):  # Check if it ends with '/index2'
        request.session['from_index2'] = True
    else:
        request.session['from_index2'] = False
    query = request.GET.get('query', '')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'display_books.html', {'books': books})