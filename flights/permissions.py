from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):



    def has_object_permission(self, request, view, obj):
       if request.user.is_staff or (obj.user == request.user):
           return True
       else:
           return False

class Validity(BasePermission):
   def has_object_permission(self, request, view, obj):
       Third_Date = datetime.today() + timedelta(days=3)
       if datetime.now() > Third_Date :
           return True
       else:
           return False
