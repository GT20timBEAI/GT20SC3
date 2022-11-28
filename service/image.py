
 
 #TODO: get extension
def extensionImage(image):
    allow = ['jpg', 'png']
    extension = image.split('.')[1]
    if extension not in allow or '.' not in image:return False
    return extension


def getStorageImage(image):
    # get images from storages
    from google.cloud import storage

    storageconst = storage.Client()
    bucket = storageconst.bucket("fashion-campuss-gt20")
    blob = bucket.blob(image)
    with blob.open("rb") as file:
        images = file.read()
    return images