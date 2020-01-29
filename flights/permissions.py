from rest_framework.permissions import BasePermission
from datetime import date

class IsOwnerorStaff(BasePermission):
	message="you have to be Owner or with admin account "
	def has_object_permission(self,request,view,obj):
		if request.user.is_staff or request.user == obj.user:
			return True
		return False

class Is3DaysAway(BasePermission):
	message= "has to be more than 3 days away "
	def has_object_permission(self,request,view,obj):
		if (obj.date - date.today()).days > 3:
			return True
		return False


