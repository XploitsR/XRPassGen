######################################################################
# Copyright (c). All rights reserved                                 #
# GNU GENERAL PUBLIC LICENSE                                         #
# Version 3, 29 June 2007                                            #
#                                                                    #
# Developed by Solomon Narh (::XploitsR Author::)                    #
# Github: https://github.com/XploitsR/XRPassGen                      #
# Facebook: https://facebook.com/RXploits                            #
# Twitter: https://twitter.com/RXploits                              #
# Telegram: https://t.me/RXploits                                    #
# Website: https://xploitsr.tk                                       #
# Personal: https://facebook.com/solomon.narh.311                    #
######################################################################

import sys,time
import random,string

#Check for python version
try:

  if sys.version_info[0] < 3:
     raise "REQUIRED PYTHON 3.x"
except Exception as err:
  print(""" 
=======================================
    PYTHON 3.x IS REQUIRED
    PYTHON 2.x WILL SOON BE DEPRECATED
                 (^_^)
======================================= 
""")
  sys.exit()

time.sleep(0.5) 

#Instructions
def Usage():
    print("""
Password: ./xrpassgen.py [ -l ] [ integer ]
Version: ./xrpassgen.py [ -v ]

Options:
    
    -l    ::  Length Of Password
    -v    ::  Prints the version

""")

def Version():
    print(" XRPassGen Version: 1.0 ")

#Generate the password and return it to screen
def Generate(num):
    ran = random.SystemRandom()
    lent = num
    opd = string.ascii_letters + string.digits + string.punctuation
    return str().join(ran.choice(opd) for _ in range(lent))

print("""
#########################
#  XRPasswordGenerator  #
#       XploitsR        #
#########################
"""  )

try:
  
  if str(sys.argv[1]) == "-v":
     Version()  

  elif str(sys.argv[1]) == "-l" and sys.argv[2] is not None:
     if len(sys.argv[2]) > 0:
        pw = Generate(int(sys.argv[2]))
        print("Password:",pw,"\n")
  else:
     Usage()   
except Exception:
  Usage()
finally:
  sys.exit()
