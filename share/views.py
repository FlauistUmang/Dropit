from django.shortcuts import render, redirect
from .models import * 
from .forms import *
#from django.contrib import auth


def upload(request):
    if request.user.is_authenticated():
        form = UploadForm()
        files = File.objects.all()
        file = []
        for f in files:
            file.append(f.file)
        if request.method == 'POST':
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('upload')
            return render(request, 'upload.html', {'form':form, 'file':file})
        return render(request, 'upload.html', {'form':form, 'file':file})
    else:
        return redirect('login')


