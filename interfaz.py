import tkinter as tk
from PIL import Image, ImageTk  # Requiere instalar Pillow
import random
ventana = tk.Tk()
ventana.attributes('-fullscreen', True)
ventana.configure(bg="#0a0a0a")
#definicion de imagenes 
imagen_original = Image.open("boton.png")  
imagen_redimensionada = imagen_original.resize((100, 50)) 
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
#Imagen carta por detars
imagen_original = Image.open("carta.png")  
imagen_redimensionada = imagen_original.resize((200, 300))  
carta_detras = ImageTk.PhotoImage(imagen_redimensionada)
#cartas
class Cartas:
    def __init__(self, valor, apariencia):
        self.valor = valor
        self.apariencia = apariencia

Todas_cartas = [
    Cartas(1, "Carta1.png"),
    Cartas(2, "Carta2.png"),
    Cartas(3, "Carta3.png"),
    Cartas(4, "Carta4.png"),
    Cartas(5, "Carta5.png"),
    Cartas(6, "Carta6.png"),
    Cartas(7, "Carta7.png"),
    Cartas(8, "Carta8.png"),
    Cartas(9, "Carta9.png"),
    Cartas(10, "Carta10.png"),
    Cartas(11, "Carta11.png"),
    Cartas(12, "Carta12.png"),
    Cartas(13, "Carta13.png"),
]
def crear_cartas():
    seleccion = random.sample(Todas_cartas, 3)
    return seleccion 



#Funcionalidades:


import random
class mesa:
    def __init__(self,Usuario,rondas,cartas,apuesta,marcador,saldo):
        self.usuario=Usuario
        self.rondas=rondas
        self.cartas=list(cartas)
        self.apuesta=int(apuesta)
        self.marcador=int(marcador)
        self.saldo=int(saldo)
    
    def apostar(self, apuesta):
        global apostado
        apuesta=self.apuesta
        self.saldo=self.saldo-self.apuesta
        texto2.set(f"SALDO: {mesa1.saldo}")
        apostado=True
        if self.saldo==0:
            all_in()
        
    def bonus_c1(self,valor_boton):
        carta=self.cartas[0]    
        valor_carta=carta.valor
        condicion1=valor_carta+1
        condicion2=valor_carta-1
        if valor_boton == valor_carta:
            self.marcador=self.marcador+3
        elif valor_boton == condicion1 or valor_boton == condicion2:
            self.marcador = self.marcador+1
        elif valor_carta == 13 and valor_boton==1:
                self.marcador = self.marcador+1
        elif valor_carta == 1 and valor_boton == 13:
                self.marcador = self.marcador+1
                
    def bonus_c2(self,valor_boton):
        carta=self.cartas[1]    
        valor_carta=carta.valor
        condicion1=valor_carta+1
        condicion2=valor_carta-1
        if valor_boton == valor_carta:
            self.marcador=self.marcador+3
        elif valor_boton == condicion1 or valor_boton == condicion2:
            self.marcador = self.marcador+1
        elif valor_carta == 13 and valor_boton==1:
                self.marcador = self.marcador+1
        elif valor_carta == 1 and valor_boton == 13:
                self.marcador = self.marcador+1
                
    def bonus_c3(self,valor_boton):
        carta=self.cartas[2]    
        valor_carta=carta.valor
        condicion1=valor_carta+1
        condicion2=valor_carta-1
        if valor_boton == valor_carta:
            self.marcador=self.marcador+3
        elif valor_boton == condicion1 or valor_boton == condicion2:
            self.marcador = self.marcador+1
        elif valor_carta == 13 and valor_boton==1:
                self.marcador = self.marcador+1
        elif valor_carta == 1 and valor_boton == 13:
                self.marcador = self.marcador+1
                
               
    def comparar_valores_c1(self,valor_boton):
        carta=self.cartas[0]    
        valor_carta=carta.valor
        condicion1=valor_carta+1
        condicion2=valor_carta-1
        if valor_boton == valor_carta:
            self.marcador=self.marcador+2
        elif valor_boton == condicion1 or valor_boton == condicion2:
            self.marcador = self.marcador+1
        elif valor_carta == 13 and valor_boton==1:
                self.marcador = self.marcador+1
        elif valor_carta == 1 and valor_boton == 13:
                self.marcador = self.marcador+1
        else:
            return False
                
            
    def comparar_valores_c2(self,valor_boton):
        carta=self.cartas[1]
        valor_carta=carta.valor
        condicion1=valor_carta+1
        condicion2=valor_carta-1
        if valor_boton == valor_carta:
            self.marcador=self.marcador+2
        elif valor_boton == condicion1 or valor_boton == condicion2:
            self.marcador = self.marcador+1
        elif valor_carta == 13 and valor_boton==1:
                self.marcador = self.marcador+1
        elif valor_carta == 1 and valor_boton == 13:
                self.marcador = self.marcador+1
        else:
            return False
                
            
    def comparar_valores_c3(self,valor_boton):
        carta=self.cartas[2]
        valor_carta=carta.valor
        condicion1=valor_carta+1
        condicion2=valor_carta-1
        if valor_boton == valor_carta:
            self.marcador=self.marcador+2
        elif valor_boton == condicion1 or valor_boton == condicion2:
            self.marcador = self.marcador+1
        elif valor_carta == 13 and valor_boton==1:
                self.marcador = self.marcador+1
        elif valor_carta == 1 and valor_boton == 13:
                self.marcador = self.marcador+1
        else:
            return False
                
            
    def pagar(self):
        if bonus_valor == 1:
            if self.marcador==3:
                self.saldo=self.saldo+self.apuesta
                return True
            elif self.marcador==1:
                self.saldo=self.saldo+(self.apuesta*0.5)
            else:
                    self.saldo=self.saldo
                    return False   
        elif self.marcador>=3:
            self.saldo=self.saldo+(self.apuesta*2)+self.apuesta
            return True
        elif self.marcador==2:
            self.saldo=self.saldo+(self.apuesta*0.5)+self.apuesta
        elif self.marcador==1:
            self.saldo=self.saldo
        else:
            self.saldo=self.saldo
            return False
        
            
    def revelar_cartas(self):
        valores_cartas=[]
        for i in self.cartas:
            valores_cartas.append(i.valor)
        print("Los valores de las cartas eran:")
        print(f"Carta 1: {valores_cartas[0]}")
        print(f"Carta 2: {valores_cartas[1]}")
        print(f"Carta 3: {valores_cartas[2]}")
    
    
class Usuario:
    def __init__(self,nombre,saldo):
        self.nombre=nombre
        self.saldo=saldo
               
class Rondas:
    def __init__(self,cantidad, orden):
        self.cantidad=cantidad
        self.orden=orden
            
apostado=False
#mostrar botones
def mostrar_botones_c1(): #CADA BOTON MIDE 60*80
    boton_apostar.place_forget()
    global apostado
    if mesa1.apuesta == 100 and apostado==False:
        mesa1.apostar(100)
        apostado == True
    num1_c1.place(x=250, y=570)
    num2_c1.place(x=290, y=570)
    num3_c1.place(x=330, y=570)
    num4_c1.place(x=370, y=570)
    num5_c1.place(x=410, y=570)
    num6_c1.place(x=250, y=610)
    num7_c1.place(x=290, y=610)
    num8_c1.place(x=330, y=610)
    num9_c1.place(x=370, y=610)
    num10_c1.place(x=410, y=610)
    num11_c1.place(x=290, y=650)
    num12_c1.place(x=330, y=650)
    num13_c1.place(x=370, y=650)
    
    
def mostrar_botones_c2(): #CADA BOTON MIDE 60*#*Yano
    boton_apostar.place_forget()
    global apostado
    if mesa1.apuesta == 100 and apostado==False:
        mesa1.apostar(100)
        apostado == True
    num1_c2.place(x=650, y=570)
    num2_c2.place(x=690, y=570)
    num3_c2.place(x=730, y=570)
    num4_c2.place(x=770, y=570)
    num5_c2.place(x=810, y=570)
    num6_c2.place(x=650, y=610)
    num7_c2.place(x=690, y=610)
    num8_c2.place(x=730, y=610)
    num9_c2.place(x=770, y=610)
    num10_c2.place(x=810, y=610)
    num11_c2.place(x=690, y=650)
    num12_c2.place(x=730, y=650)
    num13_c2.place(x=770, y=650)
    
def mostrar_botones_c3(): #CADA BOTON MIDE 60*80 
    boton_apostar.place_forget()
    global apostado
    if mesa1.apuesta == 100 and apostado==False:
        mesa1.apostar(100)
        apostado == True
    num1_c3.place(x=1050, y=570)
    num2_c3.place(x=1090, y=570)
    num3_c3.place(x=1130, y=570)
    num4_c3.place(x=1170, y=570)
    num5_c3.place(x=1210, y=570)
    num6_c3.place(x=1050, y=610)
    num7_c3.place(x=1090, y=610)
    num8_c3.place(x=1130, y=610)
    num9_c3.place(x=1170, y=610)
    num10_c3.place(x=1210, y=610)
    num11_c3.place(x=1090, y=650)
    num12_c3.place(x=1130, y=650)
    num13_c3.place(x=1170, y=650)
    
#All-in
def all_in():
    label_allin = tk.Label(ventana, text="ALL-IN", borderwidth=0, bg="#0a0a0a", fg="#c4b454",font=("Verdana", 50, "bold"))
    label_allin.place(x=600, y=100) 
    ventana.after(5000, label_allin.destroy)
#MARCADOR PERFECTO:
def marcador_perfecto():
    label_marcador = tk.Label(ventana, text="MARCADOR PERFECTO", borderwidth=0, bg="#0a0a0a", fg="#c4b454",font=("Verdana", 50, "bold"))
    label_marcador.place(x=330, y=100) 
    ventana.after(5000, label_marcador.destroy)   
#Bonus:
bonus_valor = None 
def mostrar_bonus():
    global bonus_valor
    bonus_valor = 1  
    label = tk.Label(ventana, text="BONUS ACTIVADO", borderwidth=0, bg="#0a0a0a", fg="#c4b454",font=("Verdana", 50, "bold"))
    label.place(x=430, y=100)
    ventana.after(5000, label.destroy) #Delay

def mostrar_cartas(ruta_imagen, x, y):
    img = Image.open(ruta_imagen).resize((200, 300))
    img_tk = ImageTk.PhotoImage(img)
    label = tk.Label(ventana, image=img_tk, bg="#0a0a0a")
    label.image = img_tk 
    label.place(x=x, y=y)

#opciones selccionadas

valor_c1=0
def opcion_seleccionada_c1(valor):
    print(f"Seleccionaste: {valor}")
    global valor_c1
    valor_c1=valor
    num1_c1.place_forget()
    num2_c1.place_forget()
    num3_c1.place_forget()
    num4_c1.place_forget()
    num5_c1.place_forget()
    num6_c1.place_forget()
    num7_c1.place_forget()
    num8_c1.place_forget()
    num9_c1.place_forget()
    num10_c1.place_forget()
    num11_c1.place_forget()
    num12_c1.place_forget()
    num13_c1.place_forget()
    carta1.place_forget()
    mostrar_cartas(carta1.carta.apariencia,250,250)
    if bonus_valor==1:
        mesa1.bonus_c1(valor_c1)
        condicion=True
    else:
        condicion=mesa1.comparar_valores_c1(valor_c1)
        print(mesa1.marcador)
    if condicion == False:
        if mesa1.marcador ==0 and valor_c1!=0 and valor_c3!=0:
            mostrar_bonus()
        elif mesa1.marcador ==0 and valor_c1!=0 and valor_c2!=0:
            mostrar_bonus()
    texto.set(f"MARCADOR: {mesa1.marcador} |")
    if valor_c1!=0 and valor_c2!=0 and valor_c3!=0:
        Pagar.place(x=700, y=700)
    if mesa1.marcador == 6:
        marcador_perfecto()
       
    
    
valor_c2=0   
def opcion_seleccionada_c2(valor):
    print(f"Seleccionaste: {valor}")
    global valor_c2
    valor_c2=valor
    num1_c2.place_forget()
    num2_c2.place_forget()
    num3_c2.place_forget()
    num4_c2.place_forget()
    num5_c2.place_forget()
    num6_c2.place_forget()
    num7_c2.place_forget()
    num8_c2.place_forget()
    num9_c2.place_forget()
    num10_c2.place_forget()
    num11_c2.place_forget()
    num12_c2.place_forget()
    num13_c2.place_forget()
    carta2.place_forget()
    mostrar_cartas(carta2.carta.apariencia,650,250)
    if bonus_valor==1:
        mesa1.bonus_c2(valor_c2)
        condicion=True
    else:
        condicion=mesa1.comparar_valores_c2(valor_c2)
        print(mesa1.marcador)
    if condicion == False:
        if mesa1.marcador ==0 and valor_c2!=0 and valor_c1!=0:
            mostrar_bonus()
        elif mesa1.marcador ==0 and valor_c2!=0 and valor_c3!=0:
            mostrar_bonus()
    texto.set(f"MARCADOR: {mesa1.marcador} |")
    if valor_c1!=0 and valor_c2!=0 and valor_c3!=0:
        Pagar.place(x=700, y=700)
    if mesa1.marcador == 6:
        marcador_perfecto()
    
valor_c3=0       
def opcion_seleccionada_c3(valor):
    print(f"Seleccionaste: {valor}")
    global valor_c3
    valor_c3=valor
    num1_c3.place_forget()
    num2_c3.place_forget()
    num3_c3.place_forget()
    num4_c3.place_forget()
    num5_c3.place_forget()
    num6_c3.place_forget()
    num7_c3.place_forget()
    num8_c3.place_forget()
    num9_c3.place_forget()
    num10_c3.place_forget()
    num11_c3.place_forget()
    num12_c3.place_forget()
    num13_c3.place_forget()
    carta3.place_forget()
    mostrar_cartas(carta3.carta.apariencia,1050,250)
    if bonus_valor==1:
        mesa1.bonus_c3(valor_c3)
        condicion=True
    else:
        condicion=mesa1.comparar_valores_c3(valor_c3)
        print(mesa1.marcador)
    if condicion == False:
        if mesa1.marcador ==0 and valor_c3!=0 and valor_c1!=0:
            mostrar_bonus()
        elif mesa1.marcador ==0 and valor_c3!=0 and valor_c2!=0:
            mostrar_bonus()
    texto.set(f"MARCADOR: {mesa1.marcador} |")
    if valor_c1!=0 and valor_c2!=0 and valor_c3!=0:
        Pagar.place(x=700, y=700)
    if mesa1.marcador == 6:
        marcador_perfecto()
        
#pagar y actualizar:
def pagar_actualizar():
    mesa1.pagar()
    texto2.set(f"SALDO: {mesa1.saldo}")
    print(mesa1.saldo)
    Pagar.destroy()
    Continuar.place(x=500, y=700)
    boton2.place(x=800,y=700)
    
#Nombre del usuario:

    
#entrada de la apuesta:

def obtener_valor():
    global valor_apuesta,numero, mesa1
    valor_apuesta = entrada.get()
    if mesa1.saldo is None:
        valor_maximo = 2000
    else:
        valor_maximo = mesa1.saldo
    try:
        numero = int(valor_apuesta)
        if valor_minimo <= numero <= valor_maximo:
            mensaje_label.config(text=f"Apuesta aceptada por : {numero}", fg="#c4b454", bg="#0a0a0a")
            mesa1=mesa("Usuario",1,cartas_final,numero,0,valor_maximo)
            mesa1.apostar(mesa1.apuesta)
            ventana_pequena.after(2000, ventana_pequena.destroy)
            boton_apostar.place_forget()
        else:
            mensaje_label.config(text=f"La apuesta debe estar entre {valor_minimo} y {valor_maximo}.", fg="#800020", bg="#0a0a0a")
            mensaje_label.config(text=f"Recuerde que su saldo es de {valor_maximo}", fg="#800020", bg="#0a0a0a")
    except ValueError:
        mensaje_label.config(text="Por favor ingresa un número válido.", fg="#800020",bg="#0a0a0a")
        
    
#Ventana secundaria:
def abrir_ventana2():
    global mensaje_label, ventana_pequena, entrada
    ventana_pequena = tk.Toplevel(ventana)
    ventana_pequena.configure(bg="#0a0a0a")
    ventana_pequena.title("Ventana Pequeña")
    ventana_pequena.geometry("500x500+500+300")  # Tamaño y posición
    ventana_pequena.lift()       # Traer al frente
    ventana_pequena.focus_set()  # Poner foco
    ventana_pequena.grab_set()   # Bloquear interacción con la ventana principal hasta cerrar esta
    tk.Label(ventana_pequena, text="Al cerrar sin contestar se daran valores predetermindos",
             fg="#800020",bg="#0a0a0a",font=("Times New Roman", 13, "bold")).pack(pady=20)
    label = tk.Label(ventana_pequena, text=f"Ingrese el valor a apostar.",bg="#0a0a0a",  fg= "#c4b454",
                     font=("Times New Roman", 20, "bold"))
    label.pack(pady=5)
    entrada = tk.Entry(ventana_pequena,bg="#c4b454",insertbackground="#0a0a0a")
    entrada.pack(pady=5)
    boton = tk.Button(ventana_pequena, text="Aceptar",fg="#c4b454", command=obtener_valor,bg="#0a0a0a",
                      font=("Times New Roman", 14, "bold"))
    boton.pack(pady=10)
    mensaje_label = tk.Label(ventana_pequena, text="Ingrese el valor a apostar", fg="#800020",bg="#0a0a0a",
                             font=("Times New Roman", 17, "bold"))
    mensaje_label.pack(pady=5)
    tk.Button(ventana_pequena, text="Cerrar", fg="#800020",bg="#0a0a0a", font=("Times New Roman", 14, "bold"),
              command=ventana_pequena.destroy).pack()
    
def cerrar_ventanas():
    ventana.destroy()
    ventana_final.destroy()    
def abrir_ventanafinal():
    global mensaje_label, ventana_pequena, entrada,ventana_final
    ventana_final = tk.Toplevel(ventana)
    ventana_final.configure(bg="#0a0a0a")
    ventana_final.title("Ventana Pequeña")
    ventana_final.geometry("700x300+400+300")  # Tamaño y posición
    ventana_final.lift()       
    ventana_final.focus_set()  
    ventana_final.grab_set()
    tk.Label(ventana_final, text="No puedes jugar mas, te quedatse sin saldo",
             fg="#c4b454",bg="#0a0a0a",font=("Times New Roman", 20 , "bold")).pack(pady=20)
    label_3 = tk.Label(ventana_final, text="Gracias por jugar mas suerte para la proxima :)",bg="#0a0a0a",  fg= "#c4b454",
                     font=("Times New Roman", 20, "bold"))
    label_3.pack(pady=5)
    label_4 = tk.Label(ventana_final, text=f"Cerrando el juego en unos segundos",bg="#0a0a0a",  fg= "#c4b454",
                     font=("Times New Roman", 13 , "bold"))
    label_4.pack(pady=5)
    ventana_final.after(10000,ventana.destroy)

    



#active backgound es el color al darle click al boton:)
num1_c1 = tk.Button(ventana, text="A",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(1))
num2_c1 = tk.Button(ventana, text="2",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(2))
num3_c1 = tk.Button(ventana, text="3",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(3))
num4_c1 = tk.Button(ventana, text="4",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(4))
num5_c1 = tk.Button(ventana, text="5",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(5))
num6_c1 = tk.Button(ventana, text="6",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(6))
num7_c1 = tk.Button(ventana, text="7",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(7))
num8_c1 = tk.Button(ventana, text="8",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(8))
num9_c1 = tk.Button(ventana, text="9",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(9))
num10_c1 = tk.Button(ventana, text="10",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(10))
num11_c1 = tk.Button(ventana, text="J",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(11))
num12_c1 = tk.Button(ventana, text="Q",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(12))
num13_c1 = tk.Button(ventana, text="K",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c1(13))

num1_c2 = tk.Button(ventana, text="A",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(1))
num2_c2 = tk.Button(ventana, text="2",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(2))
num3_c2 = tk.Button(ventana, text="3",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(3))
num4_c2 = tk.Button(ventana, text="4",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(4))
num5_c2 = tk.Button(ventana, text="5",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(5))
num6_c2 = tk.Button(ventana, text="6",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(6))
num7_c2 = tk.Button(ventana, text="7",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(7))
num8_c2 = tk.Button(ventana, text="8",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(8))
num9_c2 = tk.Button(ventana, text="9",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(9))
num10_c2 = tk.Button(ventana, text="10",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(10))
num11_c2 = tk.Button(ventana, text="J",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(11))
num12_c2 = tk.Button(ventana, text="Q",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(12))
num13_c2 = tk.Button(ventana, text="K",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c2(13))


num1_c3 = tk.Button(ventana, text="A",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(1))
num2_c3 = tk.Button(ventana, text="2",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(2))
num3_c3 = tk.Button(ventana, text="3",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(3))
num4_c3 = tk.Button(ventana, text="4",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(4))
num5_c3 = tk.Button(ventana, text="5",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(5))
num6_c3 = tk.Button(ventana, text="6",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(6))
num7_c3 = tk.Button(ventana, text="7",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(7))
num8_c3 = tk.Button(ventana, text="8",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(8))
num9_c3 = tk.Button(ventana, text="9",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(9))
num10_c3 = tk.Button(ventana, text="10",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(10))
num11_c3 = tk.Button(ventana, text="J",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(11))
num12_c3 = tk.Button(ventana, text="Q",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(12))
num13_c3 = tk.Button(ventana, text="K",font=("Times New Roman",20),fg="#800020",bg="#0a0a0a",activebackground="#0a0a0a",
                    activeforeground="#c4b454",borderwidth=0,command=lambda: opcion_seleccionada_c3(13))


boton_apostar = tk.Button(ventana, text="APOSTAR",font=("Times New Roman",20),fg="#c4b454",bg="#0a0a0a",activebackground="#c4b454",
                                activeforeground="#0a0a0a", command=abrir_ventana2)
boton_apostar.place(x=680, y=100)
cartas_final = crear_cartas()
print([c.valor for c in cartas_final])
mesa1=mesa("Usuario",1,cartas_final,100,0,2000)
valor_minimo = 101 
boton2 = tk.Button(ventana,text="SALIR", bg="#0a0a0a",borderwidth=0, font=("Times New Roman", 20, "bold"),fg="#800020",
                   command=lambda: ventana.destroy())
boton2.place(x=15, y=30)
carta1 = tk.Button(ventana, image=carta_detras,bg="#0a0a0a",activebackground="#0a0a0a", borderwidth=0, 
                command=lambda:mostrar_botones_c1())
carta1.carta=cartas_final[0]
carta1.place(x=250, y=250)
carta2 = tk.Button(ventana, image=carta_detras,bg="#0a0a0a",activebackground="#0a0a0a",borderwidth=0, 
                command=lambda: mostrar_botones_c2())
carta2.carta=cartas_final[1]
carta2.place(x=650, y=250)
carta3 = tk.Button(ventana, image=carta_detras,bg="#0a0a0a", activebackground="#0a0a0a",borderwidth=0, 
                command=lambda: mostrar_botones_c3())
carta3.carta=cartas_final[2]
carta3.place(x=1050, y=250)

texto = tk.StringVar(value=f"MARCADOR: {mesa1.marcador} |")  # StringVar actualiza el valor
texto2 = tk.StringVar(value=f"SALDO: {mesa1.saldo}")

label = tk.Label(ventana, textvariable=texto, borderwidth=0, bg="#0a0a0a", fg="#c4b454",font=("Times New Roman", 20, "bold"))
label.place(x=1100, y=0)
label2 = tk.Label(ventana, textvariable=texto2, borderwidth=0, bg="#0a0a0a", fg="#c4b454",font=("Times New Roman", 20, "bold"))
label2.place(x=1310, y=0)
Pagar = tk.Button(ventana, text="PAGAR", borderwidth=0, bg="#0a0a0a", fg="#3b454f",font=("Verdana", 25, "bold")
                ,command=lambda: pagar_actualizar())
Continuar = tk.Button(ventana, text="CONTINUAR", borderwidth=0, bg="#0a0a0a", fg="#3b454f",font=("Times New Roman", 20, "bold")
                 ,command=lambda:juego_otra())
        
def juego_otra():
    
    global Pagar, Continuar,boton2, valor_c1,valor_c2,valor_c3, bonus_valor, cartas_final, carta1,carta2,carta3,mesa1,apostado
    if mesa1.saldo ==0:
        abrir_ventanafinal()
    apostado = False
    boton_apostar.place(x=680, y=100)
    Continuar.place_forget()
    boton2.place_forget()
    cartas_final=[]
    cartas_final = crear_cartas()
    mesa1.cartas=cartas_final
    mesa1.marcador=0
    mesa1.apuesta=100
    valor_c1=0
    valor_c2=0
    valor_c3=0
    bonus_valor=0
    print([c.valor for c in cartas_final])
    boton2.place(x=15, y=30)
    carta1 = tk.Button(ventana, image=carta_detras,bg="#0a0a0a",activebackground="#0a0a0a", borderwidth=0, 
                    command=lambda:mostrar_botones_c1())
    texto.set(f"MARCADOR: {mesa1.marcador} |")
    texto2.set(f"SALDO: {mesa1.saldo}")
    carta1.carta=cartas_final[0]
    carta1.place(x=250, y=250)
    carta2 = tk.Button(ventana, image=carta_detras,bg="#0a0a0a",activebackground="#0a0a0a",borderwidth=0, 
                    command=lambda: mostrar_botones_c2())
    carta2.carta=cartas_final[1]
    carta2.place(x=650, y=250)
    carta3 = tk.Button(ventana, image=carta_detras,bg="#0a0a0a", activebackground="#0a0a0a",borderwidth=0, 
                    command=lambda: mostrar_botones_c3())
    carta3.carta=cartas_final[2]
    carta3.place(x=1050, y=250)

    texto.set(f"MARCADOR: {mesa1.marcador} |")
    texto2.set(f"SALDO: {mesa1.saldo}")

    label = tk.Label(ventana, textvariable=texto, borderwidth=0, bg="#0a0a0a", fg="#c4b454",font=("Times New Roman", 20, "bold"))
    label.place(x=1100, y=0)
    label2 = tk.Label(ventana, textvariable=texto2, borderwidth=0, bg="#0a0a0a", fg="#c4b454",font=("Times New Roman", 20, "bold"))
    label2.place(x=1310, y=0)
    Pagar = tk.Button(ventana, text="PAGAR", borderwidth=0, bg="#0a0a0a", fg="#3b454f",font=("Verdana", 25, "bold")
                    ,command=lambda: pagar_actualizar())
    
ventana.mainloop()
