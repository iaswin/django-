from django.urls import path,include
from .import views
urlpatterns = [
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("forms",views.html,name='forms'),
    path("insertt",views.insertdata,name='insertt'),
    path("show",views.showpage,name='show'),
    path("edit/<int:pk>",views.editpage,name='edit'),
    path("update/<int:pk>",views.updatepage,name='up'),
    path("delete/<int:pk>",views.deletedata,name='delete'),
    path("register",views.registerpage,name='register'),
    path("regi",views.User,name='regi'),
    path("login",views.Login,name='login'),
    path("loginn",views.loguser,name='loginn'),
    path("image",views.image,name='image'),
    path("imageup",views.upload,name='upp'),
    
    
]
