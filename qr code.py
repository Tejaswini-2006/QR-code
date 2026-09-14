import qrcode
from PIL import Image

# Function to create a customized QR code
def create_qr(data, fill_color="black", back_color="white", box_size=10, border=4, filename="my_qr.png"):
    # Create qr code instance
    qr = qrcode.QRCode(
        version=1,  # controls size of the QR Code (1 to 40), 1 is 21x21
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=box_size,  # size of each box in pixels
        border=border,  # thickness of border (minimum is 4)
    )
    
    qr.add_data(data)  # Add text or link
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image
    img.save(filename)
    print(f"✅ QR code saved as {filename}")

# Example usage
text_or_url = input("Enter text or website URL: ")
create_qr(
    data=text_or_url,
    fill_color="blue",       # You can change to red, green, etc.
    back_color="white",      # Background color
    box_size=10,             # Size of QR code
    border=5,                # Border thickness
    filename="custom_qr.png" # Output file name
)

