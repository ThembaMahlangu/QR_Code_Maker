import qrcode
from PIL import Image

data = input("Enter the data to be encoded: \n")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")

image.save("qr_code.png")
image.show()
