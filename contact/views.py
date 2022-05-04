from django.shortcuts import render, redirect
from .models import GetInTouch
from .forms import ContactForm


def contact_view(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST , request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            form.save()
            return redirect('/')
    return render(request,'contact/contact.html',{'form':form})
