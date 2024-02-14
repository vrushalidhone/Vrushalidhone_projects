#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Vrushali Dhone
#
# Created:     09/02/2024
# Copyright:   (c) Nilesh 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import qrcode                  #import qrcode
from PIL import Image



qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr.add_data("https://www.naukri.com/mnjuser/homepage")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="black")   #chan basic propertis
img.save("nokari.png")                                    #save png image


