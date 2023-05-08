# pillow
from PIL import Image
with Image.open("sample.jpg") as im:
    im.rotate(45).show()
