import pyqrcode

text = input()
qr_code = pyqrcode.create(text)
qr_code.show()
