from django.conf.urls import url
from basic_app import views

# TEMPLATE tagging
app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$',views.registration,name="register"),
    url(r'^other/$',views.other,name="other"),
    url(r'^relative/$',views.relative,name="relative"),
    url(r'^user_login/$',views.user_login,name="user_login"),
]
