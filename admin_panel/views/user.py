from django.shortcuts import render

def account(request):
    return render(request, 'admin_panel/user.html', {'user': request.user})