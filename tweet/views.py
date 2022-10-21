from django.shortcuts import render, redirect
from .models import Image
import run_cat as rc


def img_list(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:#로그인이 되어 있다면
            # 메인에서는 저장된 이미지가 보이지 않는 문제 발견, 이미지 역순으로 출력
            documents = Image.objects.order_by("-id")
            return render(request,'tweet/upload-file.html',context = {"files": documents})
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
        # 새로고침하면 같은 사진이 계속 저장되는 문제 해결
        return redirect('/')

def pumjong(request):
    rc.ML()
    return render(request,'tweet/pumjong.html')