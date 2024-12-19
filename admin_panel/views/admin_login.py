from django.shortcuts import render

def admin_login(request):
    return render(request, 'admin_panel/admin_auth.html', {'user': request.user})