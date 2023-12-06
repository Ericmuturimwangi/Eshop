from django.contrib import admin
from django.urls import path
from store.views.home import Index
from .views.signup import Signup
from .views.login import Login
from django.contrib.auth import logout
from store.views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store/', Index.as_view(), name='store'),  
    path('signup/', Signup.as_view(), name='signup'),  
    path('login/', Login.as_view(), name='login'), 
    path('logout/', logout, name='logout'),  
    path('cart/', auth_middleware(Cart.as_view()), name='cart'),  
    path('checkout/', CheckOut.as_view(), name='checkout'), 
    path('orders/', auth_middleware(OrderView.as_view()), name='orders'), 
]
