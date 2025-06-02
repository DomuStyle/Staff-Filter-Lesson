from django.shortcuts import render
from .models import Employee, Department
from django.db.models import Avg, Count
from datetime import date

def employee_overview(request):

   # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben

   # Aufgabe 1
   # QuerySet für Mitarbeiter mit Name, Abteilung und Gehalt
    employees = Employee.objects.all().select_related('department').values('name', 'department__name', 'salary')
    
   # Context für das Template
    context = {
        'employees': employees,
    }

    return render(request, 'employees/employee_list.html')
