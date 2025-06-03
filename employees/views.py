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
   
   # Aufgabe 4: Durchschnittsgehalt im Sales-Team
    sales_avg_salary = Employee.objects.filter(department__name='Sales').aggregate(avg_salary=Avg('salary'))['avg_salary']
    sales_avg_salary = round(sales_avg_salary, 2) if sales_avg_salary else 0.00


   # Aufgabe 5: Mitarbeiter vor 1. Jan 2022, nicht in HR
    early_non_hr_employees = Employee.objects.filter(
        hire_date__lt=date(2022, 1, 1)
    ).exclude(
        department__name='HR'
    ).values('name', 'department__name', 'hire_date')

   # Context für das Template
    context = {
        'employees': employees,
        'high_earners': high_earners,
        'high_salary_count': high_salary_count,
        'sales_avg_salary': sales_avg_salary,
        'early_non_hr_employees': early_non_hr_employees,
    }

    return render(request, 'employees/employee_list.html', context)
