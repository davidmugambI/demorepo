from django.urls import path
from inventoryapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create_desktop/',views.desktopCreateView,
         name='create_desktop'),
    path('create_laptop/',views.laptopCreateView,
         name='create_laptop'),
    path('create_mobile/',views.mobileCreateView,
         name='create_mobile'),


    path('retrieve_desktop/', views.retrieveDesktopView,
         name='retrieve_desktop'),
    path('retrieve_laptop/', views.retrieveLaptopView,
         name='retrieve_laptop'),
    path('retrieve_mobile/', views.retrieveMobileView,
         name='retrieve_mobile'),

    path('edit_desktop/<int:pk>/', views.edit_desktop,
         name='edit_desktop'),
    path('edit_laptop/<int:pk>/', views.edit_laptop,
         name='edit_laptop'),
    path('edit_mobile/<int:pk>/', views.edit_mobile,
         name='edit_mobile'),

    path('delete_laptop/<int:pk>/', views.delete_laptop,
         name='delete_laptop'),
    path('delete_desktop/<int:pk>/', views.delete_desktop,
         name='delete_desktop'),
    path('delete_laptop/<int:pk>/', views.delete_mobile,
         name='delete_mobile'),
]