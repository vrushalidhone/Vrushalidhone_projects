#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vushali Dhone
#
# Created:     09/02/2024
# Copyright:   (c) Nilesh 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import qrcode             #import qrcode
import qrcode as qr
img=qr.make("https://www.linkedin.com/in/vrushali-dhone-3410362b2")
img.save("linkled.png")     #save image in png