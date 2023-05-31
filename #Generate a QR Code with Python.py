#SCRIPT POUR FAIRE DES QR CODE
import qrcode
import os
#Fonctionne avec :
# The qrcode library: This library lets us perform all of our QR code related operations.
#The pillow library: This library helps us process and save images.
lien_du_site_web = 'https://noctinium.com/'
#Version: c'est la quantitét d'infos que peut contenir le QR code (1=21x21 cases et 40 le max = 177x177 cases)

#box size: Taille en pixel de chaque case du QR

#Border: La taille en case de la bordure (ici, 5 cases)
qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(lien_du_site_web)
qr.make()

img = qr.make_image(fill_color='black', back_color='white')
desktop_path = os.path.join('C:\\Users\\julc2\\Desktop')
img.save(os.path.join(desktop_path, 'QR_code_nom_image.png'))

