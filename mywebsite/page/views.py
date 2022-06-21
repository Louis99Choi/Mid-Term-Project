from django.shortcuts import render


def index(req):
    context = {


    }

    return render(req, "myIntro.html", context=context)  # myIntro.html을 반환
