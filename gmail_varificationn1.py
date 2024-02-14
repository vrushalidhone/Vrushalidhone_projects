#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vrushali Dhone
#
# Created:     09/02/2024
# Copyright:   (c) Nilesh 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

email=input("ente your email:-")                  #take input email
k,j,d=0,0,0;
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^(email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@": #if else condition
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("wrong eamil5")
            else:
                print("wrong email4")
        else:
            print("wrong email3")
    else:
        print("wrong email2")
else:
    print("wrong email")