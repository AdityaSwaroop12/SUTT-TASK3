from django.contrib import admin
from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name = "Home"),
    path("about", views.about, name = "about"),
    path("login", views.loginUser, name = "login"),
    path("index1", views.index1, name = "index1"),
    path("login1", views.loginUser1, name = "login1"),
    path("index2", views.index2, name = "index2"),
    path('download-template/', views.download_template, name='download_template'),
    path("upload_books/", views.upload_books, name = "upload_books"),
    path("form", views.form, name = "form"),
    path("books", views.display_books, name = "display_books"),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('create-profile1/', views.create_profile1, name='create_profile1'),
    path('profiles1/', views.profile_list1, name='profile_list1'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('borrowed_books/', views.borrowed_books, name='borrowed_books'),
    path('upload_books/upload_books/', views.upload_books_upload_books, name='upload_books_upload_books'),
    path('delete_all_profiles/', views.delete_all_profiles, name='delete_all_profiles'),
    path('delete_all_profiles1/', views.delete_all_profiles1, name='delete_all_profiles1'),
    path("exist_profile", views.exist_profile, name = "exist_profile")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
