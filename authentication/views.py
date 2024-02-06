from django.shortcuts import render

# Create your views here.
def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
    return render(request, template_name='registration/signin.html')