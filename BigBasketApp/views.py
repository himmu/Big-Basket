from django.shortcuts import render
from django.views.generic import View
import jwt
from models import *
from django.http import JsonResponse
from django.conf import settings
import json
# Create your views here.


def role_based_permission(token):
	token_payload = jwt.decode(token, 'settings.SECRET_KEY', algorithms=['HS256'])
	return token_payload['role']



class Login(View):
	
	def post(self,request):

		# Getting post parameters
		username = request.POST['email']
		password = request.POST['password']
		context = request.POST['context']
		try:
			user_obj = User.objects.get(email=username)
			if user_obj and user_obj.check_password(password)==True:
				payload_obj={}
				if user_obj.user_role.title=='User' and context=='User':
					payload_obj['email'] = user_obj.email
					payload_obj['role'] = "User"
					token = jwt.encode(payload_obj, settings.SECRET_KEY, algorithm="HS256")
					return JsonResponse({'message':"Successfully logged in","token":token},status=200)

				elif user_obj.user_role.title=='Admin' and context=='Admin':
					payload_obj['email'] = user_obj.email
					payload_obj['role'] = "Admin"
					token = jwt.encode(payload_obj, settings.SECRET_KEY, algorithm="HS256")
					return JsonResponse({'message':"Successfully logged in","token":token},status=200)
				else:
					return JsonResponse({'message':"You are not authorized for login"},status=400)

				
			else:
				return JsonResponse({"message":"Username or password does'nt matched"},status=400)
		except:
			return JsonResponse({"message":"Account with this email id does'nt exist! Please signup"},status=400)


class Category_View(View):

	def post(self,request):

		try:
			category_name = request.POST['category_name']
			Category.objects.create(name=category_name)
			return JsonResponse({"message":"Category added successfully"},status=200)
		except:
			return JsonResponse({"message":"Something went wrong please try again"},status=400)
	
	def get(self,request):
		category_obj = Category.objects.filter(is_active=1)
		category_list = []
		for cat in category_obj:
			category = {}
			category['id'] = cat.id
			category['category_name'] = cat.name
			category_list.append(category)
		return JsonResponse({"message":"Success","category_list":category_list},status=200)



class Sub_Category(View):

	def post(self,request):

		try:
			category_id = request.POST['category_id']
			category_obj = Category.objects.get(id=category_id)
			sub_category_name = request.POST['sub_category_name']
			Subcategory.objects.create(name=sub_category_name,fk_category=category_obj)
			return JsonResponse({"message":"Sub-category added successfully"},status=200)
		except:
			return JsonResponse({"message":"Something went wrong please try again"},status=400)

	def get(self,request):
		sub_category_obj = Subcategory.objects.filter(is_active=1)
		subcategory_list = []
		for subcat in sub_category_obj:
			subcat_dict = {}
			subcat_dict['id'] = subcat.id
			subcat_dict['subcategoty_name'] = subcat.name
			subcat_dict['categoty_id'] = subcat.fk_category.id
			subcategory_list.append(subcat_dict)
		return JsonResponse({"message":"Success","subcategory_list":subcategory_list},status=200)




class Items(View):
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

			return JsonResponse({"message":"Item added successfully"},status=200)
		except:
			return JsonResponse({"message":"Something went wrong"},status=400)

	def get(self,request):
		item_obj = Item.objects.filter(is_active=1)
		item_list = []
		for item in item_obj:
			item_dict = {}
			item_dict['id'] = item.id
			item_dict['name'] = item.name
			item_dict['description'] = item.description
			item_dict['image'] = str(item.featureimage)
			item_dict['price'] = item.price
			item_list.append(item_dict)
		return JsonResponse({"message":"Success","item_list":item_list},status=200)

	def delete(self,request):
		# import pdb;pdb.set_trace()
		try:
			item = json.loads(request.body)

			item_obj = Item.objects.get(id=item['id'])
			item_obj.is_active=False
			item_obj.save()
			return JsonResponse({"message":"Item removed successfully",},status=200)
		except:
			return JsonResponse({"message":"Something went wrong"},status=400)


class Update_Item(View):
	def post(self,request):
		try:

			item_name= request.POST['item_name']
			# category_id = request.POST['category_id']
			# subcategory_id = request.POST['subcategory_id']
			price = request.POST['price']
			description = request.POST['description']
			item_id = request.POST['item_id']
			
			item_obj = Item.objects.get(id=item_id)
			item_obj.name = item_name
			item_obj.price = price
			# item_obj.fk_subcategory = sub_category_obj

			try:
				if request.FILES['featureimage']:
					item_obj.featureimage = request.FILES['featureimage']
				else:
					featureimage = ""
			except:
				featureimage = ""
			
			item_obj.description = description
			
			item_obj.save()
			return JsonResponse({"message":"Item updated successfully"},status=200)
		except:
			return JsonResponse({"message":"Something went wrong"},status=400)


class Get_Subcategory_By_Id(View):
	def post(self,request):
		
		try:
			cat_id = request.POST['category_id']
			cat_obj = Category.objects.get(id=cat_id)
			sub_cat_obj = Subcategory.objects.filter(fk_category=cat_obj)
			subcategory_list = []
			for  subcat in sub_cat_obj:
				subcategory_dict = {}
				subcategory_dict['id'] = subcat.id
				subcategory_dict['subcategory_name'] = subcat.name
				subcategory_dict['category_id'] = subcat.fk_category.id
				subcategory_list.append(subcategory_dict)
			return JsonResponse({"message":"Success","subcategory_list":subcategory_list},status=200)
		except:
			return JsonResponse({"message":"Failure"},status=400)

class Get_Item_By_Id(View):
	def post(self,request):
		try:
			item_id = request.POST['item_id']
			item_obj = Item.objects.filter(id=item_id)

# Getting all category for rendering
			category_obj = Category.objects.filter(is_active=1)
			category_list = []
			for cat in category_obj:
				category = {}
				category['id'] = cat.id
				category['category_name'] = cat.name
				category_list.append(category)
# ====================================================================

# Getting all sub category for rendering
			sub_category_obj = Subcategory.objects.filter(is_active=1)
			subcategory_list = []
			for subcat in sub_category_obj:
				subcat_dict = {}
				subcat_dict['id'] = subcat.id
				subcat_dict['subcategory_name'] = subcat.name
				subcat_dict['categoty_id'] = subcat.fk_category.id
				subcategory_list.append(subcat_dict)
# ======================================================================

			item_list = []
			for item in item_obj:
				item_dict = {}
				item_dict['id'] = item.id
				item_dict['name'] = item.name
				item_dict['description'] = item.description
				item_dict['image'] = str(item.featureimage)
				item_dict['price'] = item.price
				item_dict['category_obj'] = int(item.fk_subcategory.fk_category.id)
				item_dict['sub_category_obj'] = int(item.fk_subcategory.id)
				item_list.append(item_dict)
			return JsonResponse({"message":"Success","item_detail":item_list,"category_list":category_list,"subcategory_list":subcategory_list},status=200)
		except:
			return JsonResponse({"message":"Something went wrong"},status=400)




