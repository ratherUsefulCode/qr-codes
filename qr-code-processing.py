'''
## Two very simple functions for creating and reading QR-Codes

Note:
To make the module "qrcode" work, use the PIL fork Pillow instead.

How-to:
$ pip install qrcode
$ python -m pip install --upgrade Pillow
$ pip install pyzbar
'''


def create_qr(link, size=10, path='QR-Code.png'):
    """ Create a QR-Code that leads to the given url."""
    import qrcode
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=size, border=1)
    qr.add_data(link)
    qr.make(fit=True) # In line 17 we chose version=None, so best fit is automatically chosen.
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(path)
    img.show()


# Example 1: Create QR-Code that links to https://dev.to/ruphaa/14-tips-to-google-like-a-pro-14jo
create_qr(link='https://dev.to/ruphaa/14-tips-to-google-like-a-pro-14jo')


def read_qr(path):
    """ Reads a QR-Code image and shows to what url it is linking to. """
    from pyzbar.pyzbar import decode
    from PIL import Image
    qr_code_data = Image.open(path)
    qr_text = decode(qr_code_data)[0].data.decode('utf-8')
    return qr_text


# Example 2: Read url from QR-Code
print(read_qr('QR-Code.png'))
