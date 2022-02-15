from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.forms.models import model_to_dict
from .forms import SignupForm
from .models import User, Customer, Seller
from .seller_views import check_username_duplication, check_phone_duplication, check_email_duplication, check_password_validation, check_username_password_correct


# Create your tests here.


class CustomerSignUpTestCase(TestCase):
    
    def setUp(self):
        self.username = 'testCustomer'
        self.password = 'testPassword'
        self.email = 'testCustomer@gmail.com'
        self.phone_number = '01012345678'
        self.url = reverse('signup')
    
    def tearDown(self):
        User.objects.all().delete()
        Customer.objects.all().delete()
    
    def test_signup_form(self):
        form_data = {
            'username': self.username,
            'email': self.email,
            'phone_number': self.phone_number,
            'password1': self.password,
            'password2': self.password
        }
        form = SignupForm(form_data)
        
        self.assertTrue(form.is_valid())
    
    def test_return_signup_html(self):
        response = self.client.get(self.url)
        self.assertTrue(response.context['form'], SignupForm())
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')
        self.assertContains(response, 'MBLY')
    
    def test_create_user_customer(self):
        form_data = {
            'username': self.username,
            'email': self.email,
            'phone_number': self.phone_number,
            'password1': self.password,
            'password2': self.password
        }
        self.client.post(self.url, form_data)
        user = User.objects.first()
        customer = Customer.objects.first()
        
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(check_password(self.password, user.password))
        self.assertEqual(user, customer.user)
        self.assertEqual(customer.phone_number, self.phone_number)


class SellerSignUpTestCase(TestCase):
    
    def setUp(self):
        self.username = 'testSeller'
        self.password = 'testPassword12@'
        self.email = 'testSeller@gmail.com'
        self.phone_number = '01012345678'
        self.brand = 'ptry'
        self.url = reverse('seller_signup')
    
    def tearDown(self):
        User.objects.all().delete()
        Seller.objects.all().delete()
    
    def test_check_request_data(self):
        
        username_response = check_username_duplication(username=self.username)
        phone_response = check_phone_duplication(phone_number=self.phone_number)
        email_response = check_email_duplication(email=self.email)
        password_response = check_password_validation(password=self.password)
        
        self.assertIsNone(username_response)
        self.assertIsNone(phone_response)
        self.assertIsNone(email_response)
        self.assertIsNone(password_response)
    
    def test_create_user_seller(self):
        data = {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'phone_number': self.phone_number,
            'brand': self.brand
        }
        response = self.client.post(self.url, data, content_type='application/json')
        user = User.objects.first()
        seller = Seller.objects.first()
        
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertTrue(check_password(self.password, user.password))
        self.assertEqual(user, seller.user)
        self.assertEqual(seller.phone_number, self.phone_number)
        self.assertEqual(seller.brand, self.brand)
        self.assertTrue(response.status_code, 201)


class SellerSignInTestCase(TestCase):
    
    def setUp(self):
        self.username = 'testSeller'
        self.password = 'testPassword12@'
        self.email = 'testSeller@gmail.com'
        self.phone_number = '01012345678'
        self.brand = 'ptry'
        self.url = reverse('seller_signin')
        
        user_object = User.objects.create(username=self.username, password=self.password, email=self.email)
        Seller.objects.create(user=user_object, phone_number=self.phone_number, brand=self.brand)
    
    def test_check_request_data(self):
        
        username_password_correct_response = check_username_password_correct(username=self.username, password=self.password)
        
        self.assertIsNone(username_password_correct_response)
    
    def test_seller_correct(self):
        data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post(self.url, data, content_type='application/json')
        seller = Seller.objects.first()
        
        self.assertEqual(response['account'], model_to_dict(seller))