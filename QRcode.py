import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

def generate_qr_code(data, filename="qrcode.png", fill_color="black", back_color="white"):
    

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H, 
        box_size=12,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)

    print(f"QR code generated and saved as {filename}")
    print(f"Data encoded in QR code: {data}")
    print(f"Image size: {img.size}")

    return img


input_data = input("QR code me kya encode karna hai (URL/Text): ")


user_filename = input("Filename kya rakhna hai? (Default: my_qrcode.png): ").strip() or "my_qrcode.png"
user_fill = input("QR code ka color kya chahiye? (Default: black): ").strip() or "black"
user_back = input("Background color kya chahiye? (Default: white): ").strip() or "white"

generate_qr_code(input_data, filename=user_filename, fill_color=user_fill, back_color=user_back)