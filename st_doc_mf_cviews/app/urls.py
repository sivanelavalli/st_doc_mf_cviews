from django.conf.urls import url
from . import views
import re
urlpatterns = [
    url(r'^$',views.Save,name="save"),
    url(r'^viewall/$',views.ViewAll.as_view(),name='viewall-students'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.ViewOne.as_view(),
        name="viewonestudent"),

]
