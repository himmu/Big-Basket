from django.shortcuts import render
from django.views.generic import View
import jwt
from .models import *
# Create your views here.


def role_based_permission(token):
	token_payload = jwt.decode(token, 'settings.SECRET_KEY', algorithms=['HS256'])
	return token_payload['role']



class Login(View):
	
	def post(self,request):

		# Getting post parameters
		username = request.POST['username']
		password = request.POST['password']
		try:
			user_obj = User.objects.get(email=username)
			if user_obj and user_obj.check_password(password)==True:
				payload_obj = {
                    'email': user_obj.email,
                    'role': user_obj.user_role.id,
                }
                token = jwt.encode(payload_obj, settings.SECRET_KEY, algorithm="HS256")
                return JsonResponse({'message':"Successfully logged in","token":token},status=200)
            else:
            	return JsonResponse({"message":"Username or password does'nt matched"},status=400)
        except:
        	return JsonResponse({"message":"Account with this email id does'nt exist! Please signup"},status=400)


class Category(View):

	def post(self,request):
		if role_based_permission(request.token)
		try:
			category_name = request.POST['category_name']
			Category.objects.create(name=category_name)
			return JsonResponse({"message":"Category added successfully"},status=200)
		except:
			return JsonResponse({"message":"Something went wrong please try again"},status=400)


class Sub_Category(View):

	def post(self,request):
		try:
			category_id = request.POST['category_name']
			category_obj = Category.objects.get(id=category_id)
			sub_category_name = request.POST['sub_category_name']
			Subcategory.objects.create(name=sub_category_name,fk_category=category_obj)
			return JsonResponse({"message":"Sub-category added successfully"},status=200)
		except:
			return JsonResponse({"message":"Something went wrong please try again"},status=400)

class Item(View):
	def post(self,request):
		try:
			sub_category_id = request.POST['sub_category_id']
			item_name = request.POST['item_name']
			try:
				featureimage = request.FILES['feature_image']
			except:
				featureimage = None

			price = request.POST['price']
			description = request.POST['description']
			sub_category_obj = Subcategory.objects.get(id=sub_category_id)

			Item.objects.create(name=item_name,price=price,description=description,fk_subcategory=sub_category_obj,
				featureimage=featureimage)

	# def get(self,request)

