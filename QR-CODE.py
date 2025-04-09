import qrcode

# Replace this with your GitHub profile URL
data = "https://github.com/ashutosh0019"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code (1 = 21x21)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border (4 is default)
)

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("github_qr.png")
