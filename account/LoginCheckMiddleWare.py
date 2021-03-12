from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse


class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        # print(modulename)
        user = request.user

        #Check whether the user is logged in or not
        if user.is_authenticated:
            if user.is_admin and user.is_superuser ==True:
                if modulename == "administration.views" or  modulename == "account.views" or modulename == "performances.views" or modulename == "employee.views" or modulename == "management.views"  :
                    pass
                else:
                    return redirect("/administration/index")  
            elif user.is_employee ==True:
                if modulename == "employee.views"  or   modulename == "account.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("/employee/employee_dashboard")
            

            else:
                return redirect("signin")

        else:
            if request.path == reverse("signin") or request.path == reverse("signin"):
                pass
            else:
                return redirect("signin")
