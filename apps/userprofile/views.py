from django.http import HttpResponse


# Create your views here.
def login(request):
    return HttpResponse("登陆成功")


def index(request):
    return None