from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from contact.forms import ContactForm

# User can contact for help
def contact(request):

    form = ContactForm(request.POST, request.FILES)
    user = request.user

    if request.POST:
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user=user

            if form.cleaned_data.get("email"):
                email = form.cleaned_data.get("email")
            else:
                email = user.email

            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")

            # Email the admin
            # EmailThead([settings.EMAIL_HOST_USER, "kevinalex846@gmail.com"], message, subject).start()

            messages.info(request, "Help message received")
            # return redirect("analytics") # Update to remain untill user chooses another action

    return render(request, "dashboard/contact.html",
                  {"title": "Help contact","vendor":request.user})