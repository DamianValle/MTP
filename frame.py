from Tkinter import *
import socket
import time
import sys
import os
import struct
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

UDP_PORT = 8008
DATA_PATH = "data"
DAMIAN_IP = "192.168.192.231"
JOSE_IP = "192.168.192.9"
ackd = False

root = Tk()
root.title("MTP Grupo C")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def b2():
    print("Damian es el sender")
    global sender_ip
    sender_ip = "192.168.192.231"

def b3():
    print("Jose es el sender")
    global sender_ip
    sender_ip = "192.168.192.9"
    
def b4():
    print("Alvaro es el sender")
    global sender_ip
    sender_ip = "192.168.192.234"
    
def b6():
    print("Damian es el receiver")
    #sock.bind(("192.168.192.231", UDP_PORT))
    global receiver_ip
    receiver_ip = "192.168.192.231"

def b7():
    print("Jose es el receiver")
    #sock.bind(("192.168.192.9", UDP_PORT))
    global receiver_ip
    receiver_ip = "192.168.192.9"
    
def b8():
    print("Alvaro es el receiver")
    global receiver_ip
    receiver_ip = "192.168.192.234"
    
    
def b9():
    print("Iniciando transmision...")
    
    global button_tx
    button_tx.destroy()
    button_tx = Label(f14, image=img_yellow)
    button_tx.pack()

    dest = (receiver_ip, UDP_PORT)
    sock.bind((sender_ip, UDP_PORT))
    
    sock.settimeout(4)
    
    for file in os.listdir(DATA_PATH):

        print("Encontrado archivo: " + file)

        if file.endswith(".txt"):

            with open("data/" + file, "r") as text_file:
                for line in text_file:

                    sock.sendto(line, dest)

                    print("Enviada linea: " + line)
                    
                    ackd=False
                    while not ackd:
                        try:
                            print("Esperando ack")
                            ACK, address = sock.recvfrom(1024)
                            print("Recibido ack: " + ACK)
                            ackd = True
                        except:
                            print("No ha llegado el ack, enviadndo de nuevo")
                            sock.sendto(line, dest)
                            print("Enviado de nuevo")
                    
                sock.sendto("EOF", dest)
                
    print("Terminada transmision")
    
    
    button_tx.destroy()
    button_tx = Label(f14, image=img_green)
    button_tx.pack()

            

def b10():
    print("Iniciando recepcion...")
    
    global button_tx
    button_tx.destroy()
    button_tx = Label(f14, image=img_yellow)
    button_tx.pack()

    f = open('received_data/MTP-F20-SRI-C-RX.txt', 'w')

    dest = (sender_ip, UDP_PORT)

    sock.bind((receiver_ip, UDP_PORT))

    while True:

        line, addr = sock.recvfrom(1024)

        sock.sendto("ha llegao to perfect nen", dest)

        if(line == "EOF"):
            break

        print("Received line: " + line)

        f.write(line)

    print("Recepcion terminada")
    
    button_tx.destroy()
    button_tx = Label(f14, image=img_green)
    button_tx.pack()

def button_email(color):
    global button_em
    button_em.destroy()
    if(color=="yellow"):
        button_em = Label(f16, image=img_yellow)
    elif(color=="green"):
        button_em = Label(f16, image=img_green)
    button_em.pack()
    

def b11():
    
    button_email("yellow")

    ffrom = "MTPgrupoC@gmail.com"

    to = "damidoppler@gmail.com"

    data = MIMEMultipart()

    # storing the senders email address  

    data['From'] = ffrom

    # storing the receivers email address 

    data['To'] = to

    # storing the subject 

    data['Subject'] = "Archivo del SRI"

    # string to store the body of the mail

    body = "Aqui va el archivo de mtp profe espero que este bien :P"

    # attach the body with the msg instance

    data.attach(MIMEText(body, 'plain'))

    filename = "text.txt"
    attachment = open("received_data/MTP-F20-SRI-C-RX.txt", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    data.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(ffrom, "Mtpgrupoc")
    text = data.as_string()
    s.sendmail(ffrom, to, text)
    s.quit()
    
    print("Email enviado")
    
    button_email("green")
    
def b12():
    exit()
    


f1 = Frame(root, borderwidth=2, relief="ridge")
f2 = Frame(root, borderwidth=2, relief="ridge")
f3 = Frame(root, borderwidth=2, relief="ridge")
f4 = Frame(root, borderwidth=2, relief="ridge")
f5 = Frame(root, borderwidth=2, relief="ridge")
f6 = Frame(root, borderwidth=2, relief="ridge")
f7 = Frame(root, borderwidth=2, relief="ridge")
f8 = Frame(root, borderwidth=2, relief="ridge")
f9 = Frame(root, borderwidth=2, relief="ridge")
f10 = Frame(root, borderwidth=2, relief="ridge")
f11 = Frame(root, borderwidth=2, relief="ridge")
f12 = Frame(root, borderwidth=2, relief="ridge")
f13 = Frame(root, borderwidth=2, relief="ridge")
f14 = Frame(root, borderwidth=2, relief="ridge")
f15 = Frame(root, borderwidth=2, relief="ridge")
f16 = Frame(root, borderwidth=2, relief="ridge")

f1.grid(column=0, row=0, sticky="nsew")
f2.grid(column=1, row=0, sticky="nsew")
f3.grid(column=2, row=0, sticky="nsew")
f4.grid(column=3, row=0, sticky="nsew")
f5.grid(column=0, row=1, sticky="nsew")
f6.grid(column=1, row=1, sticky="nsew")
f7.grid(column=2, row=1, sticky="nsew")
f8.grid(column=3, row=1, sticky="nsew")
f9.grid(column=0, row=2, sticky="nsew", columnspan=2)
f10.grid(column=2, row=2, sticky="nsew", columnspan=2)
f11.grid(column=0, row=3, sticky="nsew", columnspan=2)
f12.grid(column=2, row=3, sticky="nsew", columnspan=2)
f13.grid(column=4, row=1, sticky="nsew", columnspan=1)
f14.grid(column=5, row=1, sticky="nsew", columnspan=2)
f15.grid(column=4, row=2, sticky="nsew", columnspan=1)
f16.grid(column=5, row=2, sticky="nsew", columnspan=2)

label1 = Label(f1, text="sender address")
button2 = Button(f2, text="Damian", command=b2)
button3 = Button(f3, text="Jose", command=b3)
button4 = Button(f4, text="Alvaro", command=b4)
label5 = Label(f5, text="receiver address")
button6 = Button(f6, text="Damian", command=b6)
button7 = Button(f7, text="Jose", command=b7)
button8 = Button(f8, text="Alvaro", command=b8)
button9 = Button(f9, text="Iniciar transmision", command=b9)
button10 = Button(f10, text="Iniciar recepcion", command=b10)
button11 = Button(f11, text="Enviar mail", command=b11)
button12 = Button(f12, text="Cerrar", command=b12)
img_green = PhotoImage(file = "green.gif")
img_yellow = PhotoImage(file = "yellow.gif")
img_red = PhotoImage(file = "red.gif")
frame13 = Label(f13, text="Estado transmision")
button_tx = Label(f14, image=img_red)
frame15 = Label(f15, text="Estado email")
button_em = Label(f16, image=img_red)

label1.pack()
button2.pack()
button3.pack()
button4.pack()
label5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()
button11.pack()
button12.pack()
frame13.pack()
button_tx.pack()
frame15.pack()
button_em.pack()

root.mainloop()
