from django.conf.urls import url
from blog.views import myview

urlpatterns = [
    url(r'^$', myview)
]
