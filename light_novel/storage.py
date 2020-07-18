from .settings import FIREBASE_SERVICE_ACCOUNT_KEY, STORAGE_BUCKET_NAME, PROJECT_NAME
from google.oauth2 import service_account
from google.cloud import storage
import datetime
import uuid
import six
import os


def _get_storage_client():
    credentials = service_account.Credentials.from_service_account_file(
        FIREBASE_SERVICE_ACCOUNT_KEY)
    return storage.Client(credentials=credentials, project=PROJECT_NAME)


def _safe_filename(filename):
    filename = str(uuid.uuid4())
    date = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M%S")
    basename, extension = os.path.splitext(filename)
    return "{0}-{1}.{2}".format(basename, date, extension)


def upload_file(file_stream, filename, path, content_type):
    filename = _safe_filename(filename)

    client = _get_storage_client()
    bucket = client.bucket(STORAGE_BUCKET_NAME)
    blob = bucket.blob(path + filename)

    blob.upload_from_string(
        file_stream,
        content_type=content_type)
    blob.make_public()
    url = blob.public_url

    if isinstance(url, six.binary_type):
        url = url.decode('utf-8')

    return url 