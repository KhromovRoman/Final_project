from django.shortcuts import render

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import FileLibrary
from .forms import FileUploadForm

class LibraryListView(ListView):
    model = FileLibrary
    context_object_name = 'files'
    paginate_by = 10
    template_name = 'app/library_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset.order_by('-uploaded_at')

class UploadFileView(CreateView):
    model = FileLibrary
    form_class = FileUploadForm
    template_name = 'app/upload_file.html'
    success_url = reverse_lazy('urllibrary_list')

