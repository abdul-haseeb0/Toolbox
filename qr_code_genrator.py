import qrcode

# Configure the QR code properties
qr = qrcode.QRCode(
    version=1,  # Controls the size (1 is 21x21 grid, up to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # About 30% error correction
    box_size=10,  # Number of pixels for each box in the grid
    border=4,  # Thickness of the border (minimum is 4)
)

# Add your text or URL
data = input("Enter URL (www.example.com)")
qr.add_data(data)
qr.make(fit=True)

# Create the image with custom foreground and background colors
img = qr.make_image(fill_color="darkblue", back_color="white")

# Save the custom image
img.save("custom_qr.png")
print("Custom QR Code generated successfully!")
