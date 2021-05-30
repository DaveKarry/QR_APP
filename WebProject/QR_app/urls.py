from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path(r'QR_app/register', Register.as_view(), name='register'),
    path(r'QR_app/out', Out.as_view(), name='out'),
    path(r'QR_app/createPerson', RegisterPerson.as_view(), name='createPerson'),
    path(r'QR_app/admin/admin', AdminPanel.as_view(), name='adminPanel'),
    path(r'QR_app/admin/Plist', PeopleList.as_view(), name='PList'),
    path(r'QR_app/admin/addnews', AddNews.as_view(), name='addnews'),
    path(r'QR_app/admin/delete/<slug>', DeleteNews.as_view(), name='deleteNews'),
    path(r'person/<slug>',  PersonDetailView.as_view(), name='person'),
    path(r'person/setStatus/<slug>', PersonSetStatus.as_view(), name='setStatus'),
    path(r'person/delete/<slug>', PersonSetStatus.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
