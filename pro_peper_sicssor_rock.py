#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nilesh
#
# Created:     20/02/2024
# Copyright:   (c) Nilesh 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------
import random
l=["rock","scissor","paper"]
while True:
    ccount=0
    ucount=0
    ch=int(input('''game start
    1 yes
    2 no | exit'''
    ))
    if ch==1:
        for a in range(1,6):
            uI=int(input('''
            1 rock
            2 scissor
            3 paper'''))

            if uI==1:
             uCh="rock"
             print(" your choice is =rock")

            elif uI==2:
             uCh="scissor"
             print("your choice is  scisso")

            elif uI==3:
             uCh="paper"
             print(" your choice is  =paper")
            cCh=random.choice(l)
            print(cCh)
            if uCh==cCh:
                print("game taii")
                ccount=ccount+1
                ucount=ucount+1
            elif(uCh=="rock" and cCh=="scissor") or (uCh=="paper" and cCh=="rock") or (uCh=="scissor" and cCh=="paper"):
                print(" you wint")
                ucount=ucount+1
            else:
                print("computer win")
                ccount=ccount+1

    else:
        break
