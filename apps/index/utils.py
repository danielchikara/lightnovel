from light_novel import storage

def upload_image_file(file, path):
    if not file:
        return None

    public_url = storage.upload_file(
        file.read(),
        file.name,
        path,
        file.content_type
    )

    return public_url


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None 