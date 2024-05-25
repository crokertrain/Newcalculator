#!/usr/bin/python3
##############################################################################
#                                                                            #
# Script Name     : calc.py                                                  #
# Description     : This is the python calculator program                    #
# Author          : Neville Croker                                           #
# Date            : 21 April 2022                                            #
# Version         : 1.0.1                                                    #
#----------------------------------------------------------------------------#
#                                                                            #
#                  PROPRIETARY AND CONFIDENTIAL INFORMATION                  #
#                    AND INTELLECTUAL PROPERTY OF CROKER.                    #
#                              (C) 2022 CROKER.                              #
#                            ALL RIGHTS RESERVED.                            #
#                                                                            #
# NOTE        : DO NOT MAKE ANY CHANGES TO THIS PROGRAM.........             #
#             : Please feel free to copy this program.                       #
#                                                                            #
#--------------------------- Amendment History ------------------------------#
# Date        | Author             | Description                             #
#----------------------------------------------------------------------------#
# dd/mm/yyyy  |                    |                                         #
##############################################################################

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
first_num = form.getvalue('first_number')
last_num = form.getvalue('second_number')
oper = form.getvalue('operator')

if oper == "+":
   answer = int(first_num) + int(last_num)
elif oper == "-":
   answer = int(first_num) - int(last_num)
elif oper == "/":
   answer = int(first_num) / int(last_num)
elif oper == "*":
   answer = int(first_num) * int(last_num)
else:
   answer = "Something is wrong"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")

print("<title>Calculator</title>")
print("</head>")
print("<body>")

print("<h2>The result of the calculation %s %s %s</h2>" % (first_num, oper, last_num))

print("<h2>Is %s</h2>" % answer)

print("</body>")
print("</html>")

