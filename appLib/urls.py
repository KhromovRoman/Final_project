from django.contrib import admin
from django.urls import path
from .views import LibraryListView, UploadFileView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('lib/', LibraryListView.as_view(), name='urllibrary_list'),
    path('upload/', UploadFileView.as_view(), name='urlupload_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
