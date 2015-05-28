from django.conf.urls import url, include
from rest_framework import routers
from jy_api.apps.api import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'links', views.LinkViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'interests', views.InterestViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^interactive/', include('rest_framework_swagger.urls')),
]
