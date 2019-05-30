from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages',LanguageView)

urlpatterns = [
    path('',include(router.urls)),
]
