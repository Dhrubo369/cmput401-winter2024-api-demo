from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from .models import Employee
from .serializers import EmployeeSerializer
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(["GET", "POST"])
def list_employees(request):
    if request.method == 'GET':
        # Logic to list employees
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        # Logic to add a new employee
        data = json.loads(request.body)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
@require_GET
def retrieve_employee(request, id):
    try:
        employee = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)



@csrf_exempt
@require_POST
def add_employee(request):
    try:
        data = json.loads(request.body)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status': 200, 'message': 'New employee added', 'id': serializer.data['id']}, status=200)
        return JsonResponse(serializer.errors, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

@csrf_exempt
@require_http_methods(["PUT"])
def update_employee(request, id):
    try:
        employee = Employee.objects.get(pk=id)
        data = json.loads(request.body)
        serializer = EmployeeSerializer(employee, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status': 200, 'message': 'Employee updated'}, status=200)
        return JsonResponse(serializer.errors, status=400)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

@csrf_exempt
@require_http_methods(["PATCH"])
def modify_employee(request, id):
    try:
        employee = Employee.objects.get(pk=id)
        data = json.loads(request.body)
        serializer = EmployeeSerializer(employee, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status': 200, 'message': 'Employee modified'}, status=200)
        return JsonResponse(serializer.errors, status=400)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

def home(request):
    return HttpResponse("Welcome to my Django app!")

def accounts_home(request):
    return HttpResponse("Welcome to the Accounts Section!")
