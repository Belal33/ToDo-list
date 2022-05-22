
from django.views.generic import ListView , DetailView ,CreateView ,UpdateView ,DeleteView
from django.urls import reverse_lazy # to redirect
from .models import Task

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login # redirect to login page 


#######################################################################
# will search for a template  with name todo/task_list.html by default
# and variable object_list contains all objectes
class Tasklist(LoginRequiredMixin, ListView): 
  # model = Task  is shorthand for saying queryset = Task.objects.all() 
  model = Task 
  def get_context_data(self, **kwargs):
    
    context = super().get_context_data(**kwargs)# return a dictionary
    # ----------------------------------------------------
  #     context	
  # {'is_paginated': False,
  #  'object_list': <QuerySet [<Task: sddsd>, <Task: kmkm;km>, <Task: sadsdcsd>]>,
  #  'page_obj': None,
  #  'paginator': None,
  #  'task_list': <QuerySet [<Task: sddsd>, <Task: kmkm;km>, <Task: sadsdcsd>]>,
  #  'view': <todo.views.Tasklist object at 0x0000024E5DE6D270>}
    # ----------------------------------------------------

    # to filter this QuerySet in object_list key 
    context['object_list'] = context['object_list'].filter(user=self.request.user)
    
    context['count'] = context['object_list'].filter(complete=False).count()
    search_area_data = self.request.GET.get('search-area') or ""
    if search_area_data :
      context['object_list'] = context['object_list'].filter(
        # title__icontains = search_area_data # --> which item contains
        title__icontains = search_area_data # --> which item begin with
        )
    context['search_area_data'] = search_area_data
    return context
  
  # context_object_name = 'tasks'  ---> to change the name (broject_list)
  # template_name = 'todo.filename.html' ---> to set template name
#######################################################################


#######################################################################
# will search for a template  with name todo/task_detail.html by default
# and variable object contains a object with id = pk
class TaskDetail(LoginRequiredMixin, DetailView): 
  model = Task 
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)# return a dictionary
  #   context['object'] = Task.objects.filter(user=self.request.user)
  #   #context {'object': <Task: sddsd>, 'task': <Task: sddsd>, 'view': <todo.views.TaskDetail object at 0x000001FE3026B2E0>}
  #   print(context['view'])
  #   print(self.request.user)
  #   return context
  
  def get_queryset(self):
    '''
    You can get the current user, who is requesting
    the view and filter their records only as by the following  
    '''
    queryset = Task.objects.filter(user=self.request.user)
    return queryset
  # context_object_name = 'tasks'  ---> to change the name (broject)
  # template_name = 'todo/filename.html'
#######################################################################



#######################################################################
# will search for a template  with name todo/task_form.html by default
# create a form in a variable called form 
class TaskCreate(LoginRequiredMixin, CreateView): 
  model = Task 
  
  # feilds --> what will be in that form
  fields = ['title','description','complete']  
  
  success_url = reverse_lazy('todo:tasks')

  
  def form_valid(self, form):

    # form_valid(form)
    # Saves the form instance, sets the current object for the view, and redirects to get_success_url().
    # form_invalid(form)
    # Renders a response, providing the invalid form as context.
    
    form.instance.user = self.request.user
    return super().form_valid(form)

  
  # template_name = 'todo/filename.html'
#######################################################################



#######################################################################
# will search for a template  with name todo/task_form.html by default
class TaskUpdate(LoginRequiredMixin, UpdateView): 
  model = Task 
  # feilds --> what will be in that form
  fields = ['title','description','complete'] 
  success_url = reverse_lazy('todo:tasks')
  def get_queryset(self):
    '''
    You can get the current user, who is requesting
    the view and filter their records only as by the following  
    '''
    queryset = Task.objects.filter(user=self.request.user)
    return queryset
  # template_name = 'todo.filename.html'
#######################################################################


#######################################################################
# will search for a template  with name todo/task_confirm_delete.html by default
# and variable object contains a object with id = pk
class TaskDelete(LoginRequiredMixin, DeleteView): 
  model = Task 
  # feilds --> what will be in that form
  fields = "__all__" # or put speciefic fields in a list --> ['title','user',...]
  success_url = reverse_lazy('todo:tasks')
  # context_object_name = 'tasks'  ---> to change the name (broject)
  # template_name = 'todo.filename.html'
#######################################################################