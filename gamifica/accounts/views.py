from django.shortcuts import render, redirect
from accounts.forms import RegisterUsuarioForm

def register(request):

    form = RegisterUsuarioForm

    if request.method == 'POST': 

        form = RegisterUsuarioForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.profile_pic = request.FILES.get("profile_pic")
            user.save()
            return redirect("/accounts/login")

    context = {
        'form': form
    }

    return render(request, 'registration/registrar.html',context=context)