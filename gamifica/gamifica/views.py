from django.shortcuts import redirect, render

def home(request):
    if not request.user.is_authenticated: 
        return render(request, 'home.html')
    return redirect("/question/list/")