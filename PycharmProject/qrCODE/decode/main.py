from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("/home/lerato/workspace/myqrcode1.png")

result = decode(img)

print(result)