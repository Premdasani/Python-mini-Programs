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

generate_qr_code("https://github.com/Premdasani", filename="example_qrcode.png", fill_color="blue", back_color="white")  


