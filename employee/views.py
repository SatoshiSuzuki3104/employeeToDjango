from django.views import generic
from .forms import SearchFrom
from .models import Employee


# class IndexView(generic.TemplateView):
# 	template_name = 'employee/employee_list.html'

class IndexView(generic.ListView):
	model = Employee
	paginate_by = 1
	
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data()
		context['form'] = SearchFrom(self.request.GET)
		return context
	
	def get_queryset(self):
		form = SearchFrom(self.request.GET)
		form.is_valid()
		
		queryset = super().get_queryset()
		
		department = form.cleaned_data['department']
		if department:
			queryset = queryset.filter(department=department)
		
		club = form.cleaned_data['club']
		
		# フィールド名 = 絞り込む内容
		if club:
			queryset = queryset.filter(club=club)
		
		return queryset
