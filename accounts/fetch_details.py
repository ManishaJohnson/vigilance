class GetDetails:

	def signin_info(self,request):
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']

		return first_name,last_name,username,email,password1,password2

	def login_info(self,request):
		username=request.POST.get('username')
		password=request.POST.get('password')
		return username,password

	def user_info(self,request):
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		return first_name,last_name,username,email

