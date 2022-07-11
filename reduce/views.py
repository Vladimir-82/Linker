import uuid

from django.shortcuts import render
from django.core.files.base import ContentFile
from django.http import HttpResponse


from .forms import AddForm
from .models import Link



def reduce(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        all_links = Link.objects.all()
