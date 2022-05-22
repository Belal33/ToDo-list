from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse_lazy


from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm # it create a new user ferm
from django.contrib.auth import login # redirect to login page 
# Create your views here.

#######################################################################
# will search for a template  with name registration/login.html by default
# create a form in a variable called form 
class CustomLoginVeiw(LoginView): 
  template_name = 'users/login.html'
  fields = "__all__" # or put speciefic fields in a list --> ['title','user',...]
  
  def get(self , *args, **kwargs):
    if self.request.user.is_authenticated :#if user already authenticated redirect
      return redirect('todo:tasks')
    return super().get( *args, **kwargs)
  
  def get_success_url(slef): # to return a auser into task list after login
    return reverse_lazy('todo:tasks')
#######################################################################



#######################################################################
# create a form in a variable called form 
class CustomRegister(FormView): 
  template_name = 'users/register.html'
  form_class = UserCreationForm 



  def form_valid(self, form) :
    # to save a new user 
    user = form.save()
    
    if user != None :  
      login(self.request,user)
      return redirect('todo:tasks')
    return super().form_valid(form)
  
  def get(self , *args, **kwargs):
    if self.request.user.is_authenticated :#if user already authenticated redirect
      return redirect('todo:tasks')
    return super().get(*args, **kwargs)

  

  
  # def get_success_url(slef): # to return a auser into task list when form is valid
  #   return reverse_lazy('tasks')
  
  # Variable --->	Value
  # form     --->	<UserCreationForm bound=True, valid=True, fields=(username;password1;password2)>
  # self     --->	<todo.views.CustomRegister object at 0x000002BA5B2B4DF0
  #*******or*******#
  # success_url = reverse_lazy('tasks')
########################################################################

