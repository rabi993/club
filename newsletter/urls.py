from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('', views.NewsletterViewset)
urlpatterns = [
    path('', include(router.urls)),
]

# router.register('subscriptions', views.NewsletterViewset, basename='newsletter')


