import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10, border=4)
link=input("Paste your link here: ")
img=qr.add_data(link)
img=qr.make_image(fill_color='black',back_color='white')
img.save("QRcode.png")
