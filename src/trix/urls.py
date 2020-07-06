from django.conf.urls import url
from .views import UploadMediaView


urlpatterns = [
    url('upload_media/', UploadMediaView.as_view()),
]
