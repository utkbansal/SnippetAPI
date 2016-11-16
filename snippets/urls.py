from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
]
