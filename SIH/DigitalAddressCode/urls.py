
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("addDac/",views.addDac,name="addDac"),
    path("afterReg",views.afterReg,name="afterReg"),
    path("deleteDac/",views.deleteDac,name="deleteDac"),
    path("register/",views.register,name="register"),
    path("updateDac/",views.updateDac,name="updateDac"),
]
