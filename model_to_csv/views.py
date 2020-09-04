from django.shortcuts import render, redirect
from .models import *
from .forms import *
import io,csv
from django.http import HttpResponse
def Persons_View(request):
    persons=Person.objects.all()
    form=PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Person.objects.update_or_create(
                first_name=column[0],
                last_name=column[1]
            )
        if form.is_valid():
            form.save()
    context={'persons':persons,'form':form}
    return render(request,'persons.html',context)
