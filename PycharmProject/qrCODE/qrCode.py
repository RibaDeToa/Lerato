import qrcode
from qrcode.image.pil import PilImage

data = "Don\'t forget to subscribe"

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")
img.save("/home/lerato/workspace/myqrcode1.png")
