import os
import time

login_pass = open('user/password.pass')
login_name = open('user/dataname.pass')
l_p = login_pass.read()
l_n = login_name.read()
print("""
██████╗░██╗░░██╗███████╗
██╔══██╗██║░░██║██╔════╝
██║░░██║███████║█████╗░░
██║░░██║██╔══██║██╔══╝░░
██████╔╝██║░░██║██║░░░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░░░░

██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
""")

while True:
	log = input("Enter Password To " + l_n + " To Login: ")

	if log == l_p:
		print("Opening Home Page...")
		time.sleep(0.5)
		os.startfile("home.py")
		break

	else:
		print("Wrong Passowrd To " + l_n)