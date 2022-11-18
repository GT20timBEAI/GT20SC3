import os
from google.cloud import storage



storageconst = storage.Client()
bucket = storageconst.bucket("fashion-campuss")
blob = bucket.blob("Logo DCode whitemode.png")
with blob.open("rb") as file:
    images = file.read()


bucket = storageconst.bucket("fashion-campuss")
blob2 = bucket.blob("logo.txt")
# blob2.content_type = "image/png"
with blob2.open("w") as file2:
    file2.write("hmm")
# blob2.upload_from_string(images, content_type="image/png")


# import sys
# from PIL import Image
# from io import BytesIO

# PY3 = sys.version_info[0] > 2

# if PY3:
#     stream = BytesIO(images.encode())
# else:
#     stream = BytesIO(images)

# image = Image.open(stream).convert("RGBA")
# stream.close()
# image.show()

