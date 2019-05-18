from django.conf.urls import url


from .views import (EdukacijaListView, EdukacijaDetailSlugView )


urlpatterns = [
    url(r'^$' , EdukacijaListView.as_view(), name="list"),
    url(r'^(?P<slug>[\w-]+)/$' , EdukacijaDetailSlugView.as_view(), name="detail")
]
