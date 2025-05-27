"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
    path('',include('blog.urls')),
]
# This line includes Django's built-in authentication URLs under the 'accounts/' path prefix
# It provides the following authentication endpoints:
# - /accounts/login/ - User login page
# - /accounts/logout/ - User logout functionality
# - /accounts/password_change/ - Password change form
# - /accounts/password_reset/ - Password reset request
# - /accounts/password_reset/done/ - Password reset confirmation
# - /accounts/reset/<uidb64>/<token>/ - Password reset token validation
# - /accounts/reset/done/ - Final password reset confirmation
"""
URL configuration for blog_project project.

This file defines the main URL patterns for the blog project. It includes:
1. Admin interface URLs
2. Blog application URLs

The urlpatterns list contains:
- admin/: Routes to the Django admin interface
- '': Includes all URLs from the blog app, making it the root URL pattern
"""
