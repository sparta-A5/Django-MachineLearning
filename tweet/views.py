from django.shortcuts import render, redirect
from .models import Image

def img_list(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:#로그인이 되어 있다면
            return render(request,'tweet/upload-file.html')
        else:#로그인이 안되어 있다면
            return redirect('/signin')
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