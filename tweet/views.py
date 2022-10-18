from django.shortcuts import render
from .models import Image


def img_list(request):
    if request.method == "GET":
        image = Image.objects.all()
        return render(request, "tweet/upload-file.html", {'image': image})
    if request.method == "POST":

        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        document = Image(
            title=fileTitle,
            image=uploadedFile,
        )
        document.save()
        documents = Image.objects.all()

        return render(request, "tweet/upload-file.html",context = {
        "files": documents
    })
