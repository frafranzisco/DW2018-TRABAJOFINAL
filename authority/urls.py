from django.urls import path
from authority import views
urlpatterns = [
	path('register/',views.signup_user,name="signup_user"),
    path('',views.login_user,name="login_user"),
    path('logout/',views.logout_user,name="logout_user"),
    # path('create_admin/',views.signup_admin,name="create_admin")

]
