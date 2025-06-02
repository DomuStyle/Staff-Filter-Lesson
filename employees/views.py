from django.shortcuts import render
from .models import Employee, Department
from django.db.models import Avg, Count
from datetime import date

def employee_overview(request):

   # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben

   # Aufgabe 1
   # QuerySet für Mitarbeiter mit Name, Abteilung und Gehalt
    employees = Employee.objects.all().select_related('department').values('name', 'department__name', 'salary')
    
   # Aufgabe 2: Namen von Mitarbeitern mit Gehalt > 3000 €
    high_earners = Employee.objects.filter(salary__gt=3000).values('name')
   
   # Aufgabe 3: Anzahl der Mitarbeiter mit Gehalt ≥ 5000 €
    high_salary_count = Employee.objects.filter(salary__gte=5000).count()
   
   # Context für das Template
    context = {
        'employees': employees,
        'high_earners': high_earners,
        'high_salary_count': high_salary_count,
    }

    return render(request, 'employees/employee_list.html')
