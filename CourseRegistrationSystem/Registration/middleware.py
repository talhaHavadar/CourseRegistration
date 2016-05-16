from django.core.urlresolvers import *
from django.shortcuts import redirect

class ValidUserMiddleware:
    def process_request(self, request):
        if "admin" in request.path_info or "api" in request.path_info:
            return None
        if request.path_info != reverse("Registration:login"):
            if not request.session.get("user", False):
                return redirect("Registration:login")
            else:
                print(request.session.get("user", False))
        return None
