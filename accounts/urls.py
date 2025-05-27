from django.urls import path, include

from .views import SignUpview

urlpatterns = [
    path('signup/',SignUpview.as_view(),name='signup'),
]
