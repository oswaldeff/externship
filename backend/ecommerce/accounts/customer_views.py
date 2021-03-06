from venv import create
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.http import request, HttpResponseRedirect
from django.shortcuts import resolve_url
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView
from django.views import View
from django.db import transaction
from django.shortcuts import redirect, render
from .forms import SignupForm
from .models import User, Customer, Seller
from .socials import SocialLoginProfile
from .tokens import jwt_publish, jwt_authorization
import os
import jwt
# from products.views import MerchandiseALL


# Create your views here.


class CustomerSignup(RedirectView):
    
    def get(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                password = str(request.POST['password1'])
                password = make_password(password=password, salt=None, hasher='default')
                with transaction.atomic():
                    signed_user = User.objects.create(
                        username=str(request.POST['username']),
                        password=password,
                        email=str(request.POST['email'])
                    )
                    Customer.objects.create(
                        user=signed_user,
                        phone_number=str(request.POST['phone_number']),
                        is_local=True
                    )
                access_jwt = jwt_publish(str(signed_user)) # bcrypt ImportError: mac m1 issue
                response = HttpResponseRedirect('/')
                response.set_cookie(
                    key='_utk',
                    value=access_jwt
                )
                return response
        else:
            form = SignupForm()
        
        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)


class CustomerSignin(LoginView):
    
    next_page = 'home'
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def dispatch(self, request, *args, **kwargs):
        access_jwt = request.COOKIES.get('_utk', None)
        if access_jwt:
            try:
                payload = jwt.decode(access_jwt, key=os.environ.get('DJANGO_SECRET_KEY'), algorithms=os.environ.get('ALGORITHM'))
                request.user = User.objects.get(id=payload['user_id'])
            except:
                pass
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page)
    
    def get_success_url(self):
        return self.get_default_redirect_url()
    
    def form_valid(self, form):
        access_jwt = jwt_publish(str(form.get_user())) # bcrypt ImportError: mac m1 issue
        response = HttpResponseRedirect(self.get_success_url())
        response.set_cookie(
            key='_utk',
            value=access_jwt
        )
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        current_site = os.environ.get('HOST')
        context.update({
            self.redirect_field_name: self.get_redirect_url(),
            'site': current_site,
            'kakao_client_id': os.environ.get('KAKAO_CLIENT_ID'),
            **(self.extra_context or {})
        })
        return context


class CustomerSocialLogin(View):
    
    def get(self, request, *args, **kwargs):
        try:
            data = SocialLoginProfile.kakao(request, request.GET['code'])
            phone_number = data['phone_number']
            social_type = 'kakao'
            social_id = make_password(password=data['social_id'], salt=None, hasher='default') # bcrypt ImportError: mac m1 issue
        except:
            messages.error(request, 'KAKAO LOGIN FAIL')
            return redirect('login')
        
        if Customer.objects.filter(phone_number=phone_number):
            Customer.objects.filter(phone_number=phone_number).update(
                connect_social=True,
                social_type=social_type,
                social_id=social_id
            )
            user = Customer.objects.get(phone_number=phone_number).user
        elif Customer.objects.filter(social_id=social_id):
            user = Customer.objects.filter(social_id=social_id).user
        else:
            with transaction.atomic():
                signed_user = User.objects.create(
                    username=social_id,
                    password=None
                )
                Customer.objects.create(
                    user=signed_user,
                    phone_number=phone_number,
                    connect_social=True,
                    social_type=social_type,
                    social_id=social_id
                )
                user = signed_user
        access_jwt = jwt_publish(str(user)) # bcrypt ImportError: mac m1 issue
        response = HttpResponseRedirect('/')
        response.set_cookie(
            key='_utk',
            value=access_jwt
        )
        return response


class CustomerSignout(View):
    
    @jwt_authorization
    def get(self, request, *args, **kwargs):
        response = HttpResponseRedirect('/accounts/login')
        response.set_cookie(
            key='_utk',
            value=None
        )
        return response