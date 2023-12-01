from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.http import JsonResponse

def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            stud = User.objects.values()
            student_data = list(stud)
            return JsonResponse({'status': 'Save', 'student_data': student_data})
        else:
            return JsonResponse({'status': 'Failed'})
    else:
        form = UserForm()
        stud = User.objects.all()
        return render(request, "home.html", {'form': form, 'stud': stud})