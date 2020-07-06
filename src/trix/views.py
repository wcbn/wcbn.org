import os
from django.views import View
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin
from storages.backends.s3boto3 import S3Boto3Storage


class UploadMediaView(View, LoginRequiredMixin):
    def post(self, request, **kwargs):
        file_obj =  request.FILES.get('file', '')

        # TODO do your validation here e.g. file size/type check

        # locally, just save the file
        if 'dev' in settings.DJANGO_SETTINGS_MODULE:
            fs = FileSystemStorage()
            filename = fs.save(file_obj.name, file_obj)
            uploaded_file_url = fs.url(filename)

            return JsonResponse({
                'message': 'OK',
                'url': uploaded_file_url,
            })

        # PROD
        # organize a path for the file in bucket
        file_directory_within_bucket = 'trix_uploads'

        # synthesize a full file path; note that we included the filename
        file_path_within_bucket = os.path.join(
            file_directory_within_bucket,
            file_obj.name
        )

        media_storage = S3Boto3Storage()

        if not media_storage.exists(file_path_within_bucket):  # avoid overwriting existing file
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)

            return JsonResponse({
                'message': 'OK',
                'fileUrl': file_url,
            })
        else:
            return JsonResponse({
                'message': 'Error: file {filename} already exists at {file_directory} in bucket {bucket_name}'.format(
                    filename=file_obj.name,
                    file_directory=file_directory_within_bucket,
                    bucket_name=media_storage.bucket_name
                ),
            }, status=400)
