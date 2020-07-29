from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^home/$', views.home, name="home"),
    re_path(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name="market"),
    re_path(r'^cart/$', views.cart, name="cart"),
    re_path(r'^mine/$', views.mine, name="mine"),
    re_path(r'^login/$', views.login, name="login"),
    re_path(r'^register/$', views.register, name="register"),
    # 验证账号是否被注册
    re_path(r'^checkuserid/$', views.checkuserid, name="checkuserid"),
    re_path(r'^quit/$', views.quit, name="quit"),
    # 修改购物车
    re_path(r'^changecart/(\d+)/$', views.changecart, name="changecart"),
    # 下订单
    re_path(r'^saveorder/$', views.saveorder, name="saveorder"),
]
