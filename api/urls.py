from django.urls import path, include
from .views import (list_employees, retrieve_employee, add_employee, 
                    update_employee, modify_employee, accounts_home)

urlpatterns = [
    path('', accounts_home, name='accounts_home'),  # Add this line
    path('employees/', list_employees, name='list_employees'),
    path('employees/<int:id>/', retrieve_employee, name='retrieve_employee'),
    path('employees/<int:id>/update/', update_employee, name='update_employee'),
    path('employees/<int:id>/modify/', modify_employee, name='modify_employee'),
]
