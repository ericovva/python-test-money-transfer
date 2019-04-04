"""URL routes for payment app"""
from django.conf.urls import url, include
from rest_framework import routers
from payment.views import Payment

def urls():
    """Make urls of routers"""
    router = routers.DefaultRouter()
    router.register(r'', Payment)
    return router.urls

urlpatterns = [
    url(r'^', include(urls())),
]
