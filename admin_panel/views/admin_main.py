from django.shortcuts import render

def admin_main(request):
    return render(request, 'admin_panel/admin_main.html', {'user': request.user})