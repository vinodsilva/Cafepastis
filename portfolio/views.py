from django.shortcuts import render
from .models import Images
from django.core.mail import EmailMessage

def home(request):
    context = {}
    images = Images.objects.all()
    context["images"] = images

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        email_message = EmailMessage(
            subject = name + " : " +subject,
            body = message,
            to = ['beachpastissade@gmail.com'],
            headers = {"Reply-To": email}
        )
        email_message.send()
    return render(request, "index.html", context)
