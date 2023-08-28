from django.urls import path
from . import views
urlpatterns=[

    path('',views.index,name="index"),
    path('settings/',views.settings,name="settings"),
    path('Upload/',views.Upload,name="Upload"),
    path('profile/<str:pk>',views.profile,name="profile"),
    path('follow/',views.follow,name="follow"),
    path('likePost/',views.likePost,name="likePost"),
    path('search/',views.search,name="search"),


    #authentication
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('logout/',views.logout,name="logout"),

]