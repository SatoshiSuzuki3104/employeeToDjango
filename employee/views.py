from django.views import generic
from .models import Employee


# class IndexView(generic.TemplateView):
# 	template_name = 'employee/employee_list.html'

class IndexView(generic.ListView):
	model = Employee
