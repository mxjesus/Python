from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import Font
import tkinter as tk
import sys
import os
import pandas as pd               # Para la manipulación y análisis de datos
import numpy as np                # Para crear vectores matrices de n dimensiones
import matplotlib.pyplot as plt   # Para generar gráficos
import seaborn as sns             # Para la visualización de los datos               
from PIL import ImageTk,Image
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# Para Regresión Logística

#Se importan las bibliotecas necesarias para generar el modelo de regresión logística
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

ventanaconfiguracion = tk.Tk()
ValidarExtension = -2
NombreArchivo = ''
extension = ''
varPrueba = 'Selecciona un porcentaje para la prueba'
pd.set_option('max_columns', 25)

# Configuración 

def buttonAceptarVC(): 
    global ventanaconfiguracion, ValidarExtension
    if ValidarExtension == -1: # Poner ventana nueva que no es válido el archivo
    	messagebox.showinfo(message="El archivo debe tener extensión .csv o .txt.", title="¡Error!")
    elif ValidarExtension == -2:
    	messagebox.showinfo(message="No se ha subido algún archivo.", title="¡Error!")
    else: 
    	ventanaconfiguracion.destroy()
    	FuncionVenDatos()

def buttonCerrarPrograma():
    global ventanaconfiguracion
    sys.exit(0)

def callback():
    global name, ventanaconfiguracion, NombreArchivo, extension, BusquedaArchivo, ValidarExtension
    BusquedaArchivo = filedialog.askopenfilename()
    root, extension = os.path.splitext(BusquedaArchivo)
    ExtensionesAceptadas = ['.csv', '.txt']
    try:
    	ValidarExtension = ExtensionesAceptadas.index(extension)
    except:
    	ValidarExtension = -1
    if ValidarExtension != -1:
    	NombreArchivo = ''
    	for i in root:
    		if i == '/':
    			NombreArchivo = ''
    		else:
    			NombreArchivo = NombreArchivo + i
    	NombreArchivo = NombreArchivo + extension

def FuncionVenConf():

	ventanaconfiguracion.title("GUI - Minería de Datos 2021-2")
	ventanaconfiguracion.geometry('400x300+500+50')
	ventanaconfiguracion.resizable(width=0, height=0)
	ventanaconfiguracion.configure(background = 'dark turquoise')

	nombres = tk.Label(ventanaconfiguracion,text = "Realizado por: Jiménez Juárez Jesús", bg = "light cyan", fg = "goldenrod")
	nombres.pack(padx = 5, pady = 5, ipadx=5,ipady=5,fill = tk.X )
	nombres.place(x=100,y=10)

	texto = "¡Bienvenido!" 
	etiqueta = tk.Label(ventanaconfiguracion, text=texto)
	etiqueta.place(x=160,y=50)

	texto3 = "GUI - Proyecto Final de Minería de Datos 2021-2" 
	etiqueta3 = tk.Label(ventanaconfiguracion, text=texto3)
	etiqueta3.place(x=65,y=80)

	texto2 = "Esta interfaz trata de lo siguiente: \n 1. Subir un archivo, ya sea de extensión csv o txt. \n 2. Dé click en Avanzar, en caso de querer salir del\nprograma, dé click en \'Salir del programa\'\n3. Seleccionar un algoritmo que se encuentra en la barra de menu. \n 4. Dentro de las interfaces de los algoritmos, seguir los pasos \nque se indican." 
	etiqueta2 = tk.Label(ventanaconfiguracion,text = texto2, bg = "blue", fg = "white")
	etiqueta2.pack(padx = 5, pady = 5, ipadx=5,ipady=5,fill = tk.X )
	etiqueta2.place(x=22.5,y=110)


	errmsg = 'Error!'
	SubirArchivo = Button(text='Abrir archivo', command=callback, bg = "#90EE90")
	SubirArchivo.pack(padx = 5, pady = 5, ipadx=5,ipady=5,fill = tk.X )
	SubirArchivo.place(x=157,y=240)

	Acepta=Button(ventanaconfiguracion,text='Avanzar',command=buttonAceptarVC, bg = "#90EE90")
	Salir=Button(ventanaconfiguracion,text='Salir del programa',command=buttonCerrarPrograma, bg = "#90EE90")
	Acepta.place(x=75,y=270)
	Salir.place(x=250,y=270)
	ventanaconfiguracion.mainloop()

# Ventana Datos y Elección de Algoritmos

def FuncionVenDatos():

	global BusquedaArchivo, DatosTabla, extension, NombreArchivo, ventanaDatos,BusquedaArchivo

	ventanaDatos = tk.Tk()
	ventanaDatos.geometry('800x300+300+50')
	ventanaDatos.configure(background = 'dark turquoise')
	ventanaDatos.title("GUI - Minería de Datos 2021-2")
	ventanaDatos.resizable(width=0, height=0)

	if extension == '.csv':
		FuncionCSV()
	else:
		FuncionTXT()
	# Menu 

	menubar = Menu(ventanaDatos)
	Algoritmosmenu = Menu(menubar) # Algoritmos
	Algoritmosmenu = Menu(menubar, tearoff=0)
	Algoritmosmenu.add_command(label="Análisis exploratorio de datos", command=FuncionVenAlgoritmo1) # 
	Algoritmosmenu.add_command(label="Componentes Principales", command=FuncionVenAlgoritmo2) # 
	Algoritmosmenu.add_command(label="Cluster Particional", command=FuncionVenAlgoritmo3) # 
	Algoritmosmenu.add_command(label="Regresión Logística", command=FuncionVenAlgoritmo4) # 
	menubar.add_cascade(label="Seleccionar Algoritmo", menu=Algoritmosmenu)
	ventanaDatos.config(menu=menubar)  # Lo asignamos a la base

	texto5 = "\n"
	etiqueta5 = tk.Label(ventanaDatos,text = texto5, bg = "dark turquoise").pack(anchor=CENTER)
	texto7 = "Datos"
	etiqueta7 = tk.Label(ventanaDatos,text = texto7, bg = "light cyan", font=("Verdana",15)).pack(anchor=CENTER)
	botonpaso1 = Button(ventanaDatos, text="Ver datos", command= FuncionVenDatosOficial, bg = "#90EE90")
	botonpaso1.place(x=130,y=170)
	texto6 = "\n"
	etiqueta6 = tk.Label(ventanaDatos,text = texto6, bg = "dark turquoise").pack(anchor=CENTER)
	texto8 = "Archivo a analizar: " + BusquedaArchivo
	etiqueta8 = tk.Label(ventanaDatos,text = texto8, bg = "light cyan", font=("Verdana",8)).pack(anchor=CENTER)
	Salir=Button(ventanaDatos,text='Salir del programa',command=buttonCerrarPrograma, bg = "#90EE90")
	Salir.place(x=570,y=170)
	texto9 = "Nota: Si se tienen problemas, debe tener en cuenta que puede no ser el archivo\ncorrespondiente para ciertos algoritmos"
	etiqueta9 = tk.Label(ventanaDatos,text = texto9, bg = "light cyan", font=("Verdana",10))
	etiqueta9.place(x=130,y=240)
	ventanaDatos.mainloop()

def FuncionVenDatosOficial():

	global BusquedaArchivo, DatosTabla, extension
	
	ventanaDatos = tk.Tk()
	ventanaDatos.title("GUI - Minería de Datos 2021-2")
	ventanaDatos.geometry('700x500+350+100')
	ventanaDatos.resizable(width=0, height=0)
	

	scrollbary = Scrollbar(ventanaDatos)
	scrollbary.pack(side= RIGHT,fill = Y)
	scrollbarx = Scrollbar(ventanaDatos, orient=HORIZONTAL)
	scrollbarx.pack(side= BOTTOM, fill = X)
	texto = Text(ventanaDatos, width = 400, height = 200, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	try: 
		if extension == '.csv':
			FuncionCSV()
		texto4 = DatosTabla
		texto.insert(INSERT,texto4)
		texto.configure(state='disabled')
	except:
		print("No se hizo nada")

	ventanaDatos.mainloop()

def FuncionCSV():

	global DatosTabla,BusquedaArchivo

	DatosTabla = pd.read_csv(BusquedaArchivo)

def FuncionTXT():

	global DatosTabla,BusquedaArchivo

	DatosTabla = pd.read_table(BusquedaArchivo)


# Algoritmo 1

def FuncionHistograma():

	global DatosTabla

	DatosTabla.hist(figsize=(20,20),xrot=45)
	plt.show()

def FuncionPaso1A1():

	global DatosTabla

	ventanaPaso1A1 = tk.Tk()
	ventanaPaso1A1.geometry('400x200+500+150')
	ventanaPaso1A1.configure(background = 'white')
	ventanaPaso1A1.title("Análisis exploratorio de datos")
	ventanaPaso1A1.resizable(width=0, height=0)
	scrollbary = Scrollbar(ventanaPaso1A1)
	scrollbary.pack(side="right",fill = Y)
	scrollbarx = Scrollbar(ventanaPaso1A1, orient=HORIZONTAL)
	scrollbarx.pack(side="bottom", fill = X)
	texto = Text(ventanaPaso1A1, width = 150, height = 15, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	texto8 = DatosTabla.dtypes
	texto.insert(INSERT,texto8)
	texto.configure(state='disabled')

	ventanaPaso1A1.mainloop()

def FuncionPaso2A1():

	global DatosTabla

	ventanaPaso2A1 = tk.Tk()
	ventanaPaso2A1.geometry('400x200+500+150')
	ventanaPaso2A1.configure(background = 'white')
	ventanaPaso2A1.title("Análisis exploratorio de datos")
	ventanaPaso2A1.resizable(width=0, height=0)
	scrollbary = Scrollbar(ventanaPaso2A1)
	scrollbary.pack(side="right",fill = Y)
	scrollbarx = Scrollbar(ventanaPaso2A1, orient=HORIZONTAL)
	scrollbarx.pack(side="bottom", fill = X)
	texto = Text(ventanaPaso2A1, width = 150, height = 15, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	texto8 = DatosTabla.isnull().sum() 
	texto.insert(INSERT,texto8)
	texto.configure(state='disabled')

	ventanaPaso2A1.mainloop()

def FuncionPaso3A1():

	global DatosTabla

	ventanaPaso3A1 = tk.Tk()
	ventanaPaso3A1.geometry('400x200+500+150')
	ventanaPaso3A1.configure(background = 'white')
	ventanaPaso3A1.title("Análisis exploratorio de datos")
	scrollbary = Scrollbar(ventanaPaso3A1)
	scrollbary.pack(side="right",fill = Y)
	scrollbarx = Scrollbar(ventanaPaso3A1, orient=HORIZONTAL)
	scrollbarx.pack(side="bottom", fill = X)
	texto = Text(ventanaPaso3A1, width = 400, height = 200, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	texto8 = DatosTabla.describe()
	texto.insert(INSERT,texto8)
	texto.configure(state='disabled')

	ventanaPaso3A1.mainloop()

def FuncionPaso3A1_2():

	global DatosTabla

	ventanaPaso3A1_2 = tk.Tk()
	ventanaPaso3A1_2.geometry('400x200+500+150')
	ventanaPaso3A1_2.configure(background = 'white')
	ventanaPaso3A1_2.title("Análisis exploratorio de datos")
	scrollbary = Scrollbar(ventanaPaso3A1_2)
	scrollbary.pack(side="right",fill = Y)
	scrollbarx = Scrollbar(ventanaPaso3A1_2, orient=HORIZONTAL)
	scrollbarx.pack(side="bottom", fill = X)
	texto = Text(ventanaPaso3A1_2, width = 400, height = 200, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	texto8 = DatosTabla.describe(include='object')
	texto.insert(INSERT,texto8)
	texto.configure(state='disabled')

	ventanaPaso3A1_2.mainloop()

def FuncionPaso4A1():

	global DatosTabla

	plt.figure(figsize=(14,14))
	sns.heatmap(DatosTabla.corr(), cmap='RdBu_r', annot= True)
	plt.show()

def FuncionVenAlgoritmo1():

	global DatosTabla

	ventanaAlgoritmo1 = tk.Tk()
	ventanaAlgoritmo1.geometry('700x500+350+100')
	ventanaAlgoritmo1.configure(background = 'goldenrod')
	ventanaAlgoritmo1.title("Análisis exploratorio de datos")
	ventanaAlgoritmo1.resizable(width=0, height=0)
	texto5 = "\n"
	etiqueta5 = tk.Label(ventanaAlgoritmo1,text = texto5, bg = "goldenrod").pack(anchor=CENTER)
	texto7 = "Análisis exploratorio de datos"
	etiqueta7 = tk.Label(ventanaAlgoritmo1,text = texto7, bg = "white", font=("Verdana",12)).pack(anchor=CENTER)

	# Paso 1

	texto9 = "Paso 1: Descripción de la estructura de los datos."
	etiqueta9 = tk.Label(ventanaAlgoritmo1,text = texto9, bg = "white", font=("Verdana",8))
	etiqueta9.place(x=50,y=80)
	texto8 = "Conteo de filas y columnas, respectivamente: " + str(DatosTabla.shape)
	etiqueta8 = tk.Label(ventanaAlgoritmo1,text = texto8, bg = "light cyan", font=("Verdana",7))
	etiqueta8.pack(padx = 5, pady = 5, ipadx=5,ipady=5,fill = tk.X )
	etiqueta8.place(x=50,y=110)
	botonpaso1 = Button(ventanaAlgoritmo1, text="Ver Tipo de variable de los datos", command= FuncionPaso1A1, bg = "#90EE90")
	botonpaso1.place(x=400,y=107.5)

	# Paso 2 

	texto10 = "Paso 2: Identificación de datos faltantes."
	etiqueta10 = tk.Label(ventanaAlgoritmo1,text = texto10, bg = "white", font=("Verdana",8))
	etiqueta10.place(x=50,y=140)
	botonpaso2 = Button(ventanaAlgoritmo1, text="Ver variables nulos (que están vacíos)", command= FuncionPaso2A1, bg = "#90EE90")
	botonpaso2.place(x=245,y=167.5)

	# Paso 3

	texto11 = "Paso 3: Detección de valores atípicos."
	etiqueta11 = tk.Label(ventanaAlgoritmo1,text = texto11, bg = "white", font=("Verdana",8))
	etiqueta11.place(x=50,y=200)
	texto12 = "1) Características numéricas"
	etiqueta12 = tk.Label(ventanaAlgoritmo1,text = texto12, bg = "white", font=("Verdana",8))
	etiqueta12.place(x=60,y=230)

	botonhistograma = Button(ventanaAlgoritmo1, text="Ver histograma", command= FuncionHistograma, bg = "#90EE90")
	botonhistograma.place(x=95,y=257.5)

	botonpaso3 = Button(ventanaAlgoritmo1, text="Ver información estadísticos", command= FuncionPaso3A1, bg = "#90EE90")
	botonpaso3.place(x=400,y=257.5)

	texto13 = "2) Características nominales"
	etiqueta13 = tk.Label(ventanaAlgoritmo1,text = texto13, bg = "white", font=("Verdana",8))
	etiqueta13.place(x=60,y=290)

	botonpaso3_2 = Button(ventanaAlgoritmo1, text="Ver conteo de los registros", command= FuncionPaso3A1_2, bg = "#90EE90")
	botonpaso3_2.place(x=275,y=317.5)

	texto14 = "Nota: Quedará a criterio del usuario cómo va a utilizar los datos"
	etiqueta14 = tk.Label(ventanaAlgoritmo1,text = texto14, bg = "white", font=("Verdana",8))
	etiqueta14.place(x=175,y=350)

	# Paso 4 

	texto15 = "Paso 4: Identificación de relaciones entre pares variables."
	etiqueta15 = tk.Label(ventanaAlgoritmo1,text = texto15, bg = "white", font=("Verdana",8))
	etiqueta15.place(x=50,y=380)

	botonpaso4 = Button(ventanaAlgoritmo1, text="Ver Gráfica de correlación", command= FuncionPaso4A1, bg = "#90EE90")
	botonpaso4.place(x=275,y=407.5)



	ventanaAlgoritmo1.mainloop()

# Algoritmo 2

def BotonAgregaVarA2():

	global CopiaDatosTablaA2, varAEliminar, ventanaAlgoritmo2, listaEliminar, textoVarEliminar, contador2A2
	
	eliminaVar = str(varAEliminar.get("1.0","end-1c"))
	varAEliminar.delete("1.0", "end")

	if eliminaVar in CopiaDatosTablaA2.columns.values and (eliminaVar not in listaEliminar):
		listaEliminar.append(eliminaVar)
		columnaVarA2 = 'Variables que se van a eliminar:\n'
		contador2A2 = 0
	# Imprimir lo que está en la lista
		contador = 0
		for i in listaEliminar:
			columnaVarA2 = columnaVarA2 + " - " + i  
			contador = contador + 1
			if contador % 5 == 0:
				columnaVarA2 = columnaVarA2 + "\n"
		textoVarEliminar = Text(ventanaAlgoritmo2, width = 75, height = 6, wrap = NONE)
		textoVarEliminar.place(x=60,y=280)
		textoVarEliminar.insert(INSERT,columnaVarA2)
		textoVarEliminar.configure(state='disabled')
	else:
		messagebox.showinfo(master= ventanaAlgoritmo2, message= "Ingrese una variable existente o que no haya sido agregada.", title="¡Error!")

def VerPaso1A2():

	global MNormalizada, varT

	ventanaMNormalizada = tk.Tk()
	ventanaMNormalizada.geometry('400x300+450+100')
	ventanaMNormalizada.configure(background = 'white')
	ventanaMNormalizada.title("MNormalizada")
	scrollbary = Scrollbar(ventanaMNormalizada)
	scrollbary.pack(side="right",fill = Y)
	scrollbarx = Scrollbar(ventanaMNormalizada, orient=HORIZONTAL)
	scrollbarx.pack(side="bottom", fill = X)
	texto = Text(ventanaMNormalizada, width = 250, height = 30, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	texto2 = pd.DataFrame(MNormalizada, columns=varT.columns)
	texto.insert(INSERT,texto2)
	texto.configure(state='disabled')

	ventanaMNormalizada.mainloop()

def VerPaso2A2():

	global MNormalizada, varT, pca, X_pca

	ventanaPaso2A2 = tk.Tk()
	ventanaPaso2A2.geometry('700x500+350+100')
	ventanaPaso2A2.configure(background = 'white')
	ventanaPaso2A2.title("Paso 2 y 3 - Componentes Principales")
	ventanaPaso2A2.resizable(width=0, height=0)
	scrollbary = Scrollbar(ventanaPaso2A2)
	scrollbary.pack(side="right",fill = Y)
	scrollbarx = Scrollbar(ventanaPaso2A2, orient=HORIZONTAL)
	scrollbarx.pack(side="bottom", fill = X)
	texto = Text(ventanaPaso2A2, width = 250, height = 30, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	texto2 = "\nAplicando pd.DataFrame(X_pca)\n" + str(pd.DataFrame(X_pca)) + "\n\nAplicando pca.components_\n" + str(pca.components_)
	texto.insert(INSERT,texto2)
	texto.configure(state='disabled')

	ventanaPaso2A2.mainloop()

def VerPaso4O1A2():

	global pca, Varianza, Eigenvalues

	textoVarianza = ''

	for i in range (1,len(Varianza)):
		textoVarianza = textoVarianza + " - " + str(i) + ": " + str(sum(Varianza[0:i])) + "\n"
	ventanaPaso4O1A2 = tk.Tk()
	ventanaPaso4O1A2.geometry('700x300+350+100')
	ventanaPaso4O1A2.configure(background = 'white')
	ventanaPaso4O1A2.title("Paso 4 - Componentes Principales")
	scrollbary = Scrollbar(ventanaPaso4O1A2)
	scrollbary.pack(side="right",fill = Y)
	scrollbarx = Scrollbar(ventanaPaso4O1A2, orient=HORIZONTAL)
	scrollbarx.pack(side="bottom", fill = X)
	texto = Text(ventanaPaso4O1A2, width = 250, height = 30, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	texto2 = "Eigenvalues: " + str(Varianza) + "\n\nVarianza acumulada para decir el número de componentes principales: \n\n" + textoVarianza
	texto.insert(INSERT,texto2)
	texto.configure(state='disabled')

	ventanaPaso4O1A2.mainloop()


def VerPaso4O2A2():

	global pca

	plt.plot(np.cumsum(pca.explained_variance_ratio_))
	plt.xlabel('Número de componentes')
	plt.ylabel('Varianza acumulada')
	plt.grid()
	plt.show()

def VerPaso4O3A2():

	global Eigenvalues

	ventanaPaso4O2A2 = tk.Tk()
	ventanaPaso4O2A2.geometry('400x300+450+100')
	ventanaPaso4O2A2.configure(background = 'white')
	ventanaPaso4O2A2.title("Paso 4 - Componentes Principales")
	scrollbary = Scrollbar(ventanaPaso4O2A2)
	scrollbary.pack(side="right",fill = Y)
	scrollbarx = Scrollbar(ventanaPaso4O2A2, orient=HORIZONTAL)
	scrollbarx.pack(side="bottom", fill = X)
	texto = Text(ventanaPaso4O2A2, width = 250, height = 30, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	texto2 = "*Se elige las dimensiones cuya varianza sea\nmayor a 1: \n" + str(pd.DataFrame(Eigenvalues))
	texto.insert(INSERT,texto2)
	texto.configure(state='disabled')

	ventanaPaso4O2A2.mainloop()

def VerPaso5A2():

	global MNormalizada, varT, pca, X_pca

	ventanaPaso5A2 = tk.Tk()
	ventanaPaso5A2.geometry('700x500+350+100')
	ventanaPaso5A2.configure(background = 'white')
	ventanaPaso5A2.title("Paso 5 - Componentes Principales")
	ventanaPaso5A2.resizable(width=0, height=0)
	scrollbary = Scrollbar(ventanaPaso5A2)
	scrollbary.pack(side="right",fill = Y)
	scrollbarx = Scrollbar(ventanaPaso5A2, orient=HORIZONTAL)
	scrollbarx.pack(side="bottom", fill = X)
	texto = Text(ventanaPaso5A2, width = 250, height = 30, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	texto2 = "\nSe revisan los valores absolutos de los componentes principales seleccionados.\nCuanto mayor sea el valor absoluto, más importante es esa variable en el\ncomponente principal.\n\n" + str(pd.DataFrame(abs(pca.components_), columns = varT.columns))
	texto.insert(INSERT,texto2)
	texto.configure(state='disabled')

	ventanaPaso5A2.mainloop()

def Pestaña2A2():

	global normalizar, MNormalizada, CopiaDatosTablaA2, varT, pca, Eigenvalues, Varianza, X_pca


	ventanaAlgoritmo2_2 = tk.Tk()
	ventanaAlgoritmo2_2.geometry('500x500+450+100')
	ventanaAlgoritmo2_2.configure(background = '#AFEEEE')
	ventanaAlgoritmo2_2.resizable(width=0, height=0)
	ventanaAlgoritmo2_2.title("Componentes Principales")
	textopasos = "Componentes Principales - Resultados"
	etiquetapasos = tk.Label(ventanaAlgoritmo2_2,text = textopasos, bg = "#FA8072", fg = "white", font=("Verdana",8)).pack()

	# Paso 1 Se hace una estandarización de los datos.

	textopaso1 = "Paso 1 - Se hace una estandarización de los datos: "
	etiquetapaso1 = tk.Label(ventanaAlgoritmo2_2,text = textopaso1, bg = "#FA8072", fg = "white", font=("Verdana",8))
	etiquetapaso1.place(x=25,y=37.5)
	Paso1A2=Button(ventanaAlgoritmo2_2,text='Ver Paso 1',command=VerPaso1A2, bg = "#90EE90")
	Paso1A2.place(x=375,y=35)

	# Paso 2 y 3 Se calcula la matriz de covarianzas o correlaciones y se calculan los componentes (eigen-vectores) y la varianza (eigen-valores)

	textopaso2 = "Paso 2 y 3 - Se calcula la matriz de covarianzas\no correlaciones y se calculan los componentes\n(eigen-vectores) y la varianza (eigen-valores)"
	etiquetapaso2 = tk.Label(ventanaAlgoritmo2_2,text = textopaso2, bg = "#FA8072", fg = "white", font=("Verdana",8))
	etiquetapaso2.place(x=25,y=92.5)
	Paso2A2=Button(ventanaAlgoritmo2_2,text='Ver paso 2',command=VerPaso2A2, bg = "#90EE90")
	Paso2A2.place(x=375,y=100)

	pca = PCA(n_components=None)              # Se instancia el objeto PCA
	pca.fit(MNormalizada)                     # Se obtiene los componentes
	X_pca = pca.transform(MNormalizada)       # Se convierte los datos con las nuevas dimensiones

	# Paso 4: Se decide el número de componentes principales.

	textopaso4 = "Paso 4: Se decide el número de componentes principales."
	etiquetapaso4 = tk.Label(ventanaAlgoritmo2_2,text = textopaso4, bg = "#FA8072", fg = "white", font=("Verdana",8))
	etiquetapaso4.place(x=25,y=157.5)
	textopaso4_1 = "Opción 1: Se calcula el porcentaje de relevancia,\nes decir, entre el 75 y 90% de varianza total."
	etiquetapaso4_1 = tk.Label(ventanaAlgoritmo2_2,text = textopaso4_1, bg = "#D2691E", fg = "white", font=("Verdana",8))
	etiquetapaso4_1.place(x=25,y=197.5)
	Paso4O1A2=Button(ventanaAlgoritmo2_2,text='Opción 1 Paso 4',command=VerPaso4O1A2, bg = "#90EE90")
	Paso4O1A2.place(x=375,y=202.5)
	textopaso4_2 = "Opción 2: Se identifica mediante una gráfica el\ngrupo de componentes con mayor varianza."
	etiquetapaso4_2 = tk.Label(ventanaAlgoritmo2_2,text = textopaso4_2, bg = "#D2691E", fg = "white", font=("Verdana",8))
	etiquetapaso4_2.place(x=25,y=247.5)
	Paso4O2A2=Button(ventanaAlgoritmo2_2,text='Opción 2 Paso 4',command=VerPaso4O2A2, bg = "#90EE90")
	Paso4O2A2.place(x=375,y=252.5)
	textopaso4_3 = "*Opción 3: Se elige las dimensiones cuya\nvarianza sea mayor a 1."
	etiquetapaso4_3 = tk.Label(ventanaAlgoritmo2_2,text = textopaso4_3, bg = "#D2691E", fg = "white", font=("Verdana",8))
	etiquetapaso4_3.place(x=25,y=297.5)
	Paso4O3A2=Button(ventanaAlgoritmo2_2,text='Opción 3 Paso 4',command=VerPaso4O3A2, bg = "#90EE90")
	Paso4O3A2.place(x=375,y=302.5)

	Varianza = pca.explained_variance_ratio_
	Eigenvalues = pca.explained_variance_

	# Paso 5: Se examina la proporción de relevancias -cargas-

	textopaso5 = "Paso 5: Se examina la proporción de relevancias\n-cargas-"
	etiquetapaso5 = tk.Label(ventanaAlgoritmo2_2,text = textopaso5, bg = "#FA8072", fg = "white", font=("Verdana",8))
	etiquetapaso5.place(x=25,y=347.5)
	Paso5A2=Button(ventanaAlgoritmo2_2,text='Ver Paso 5',command=VerPaso5A2, bg = "#90EE90")
	Paso5A2.place(x=375,y=352.5)

	textopaso1 = "Instrucciones: En esta ventana se presentan los resultados de los\ndatos que se han cargado, además de ya haber eliminado las variables\ndadas anteriormente. Para el paso 5, el usuario deberá descartar las variables\ndependiendo de lo que observó en el paso 4 con respecto al número de\ncomponentes principales (Mayor magnitud es sinónimo de mayor importancia)"
	etiquetapaso1 = tk.Label(ventanaAlgoritmo2_2,text = textopaso1, bg = "#FA8072", fg = "white", font=("Verdana",8))
	etiquetapaso1.place(x=20,y=400)


def Parte2A2():

	global varT, CopiaDatosTablaA2, ventanaAlgoritmo2, textoVarEliminar, normalizar, MNormalizada, contador2A2

	try: 
		# Paso 1 Se hace una estandarización de los datos.

		normalizar = StandardScaler()                     # Se instancia el objeto StandardScaler
		normalizar.fit(varT)                         # Se calcula la media y desviación para cada dimensión
		MNormalizada = normalizar.transform(varT)    # Se normalizan los datos
		ventanaAlgoritmo2.destroy()
		Pestaña2A2()
	except:
		messagebox.showinfo(master= ventanaAlgoritmo2, message= "No eliminó las variables correctas. Se ha limpiado la lista, inicie de nuevo.", title="¡Error!")
		if contador2A2 != -1:
			textoVarEliminar.configure(state='normal')
			textoVarEliminar.delete("1.0", "end")
			textoVarEliminar.configure(state='disabled')


def BotonEliminaVarA2():

	global CopiaDatosTablaA2, checkEliminar, varAEliminar, ventanaAlgoritmo2, listaEliminar, varT, verificaCheck
	if verificaCheck.get() == "Sí":
		if len(listaEliminar) > 0:
			varT = CopiaDatosTablaA2.drop(listaEliminar, axis=1)    # Se quita la variable dependiente "Y"
			listaEliminar.clear()
			Parte2A2()
		else: 
			messagebox.showinfo(master= ventanaAlgoritmo2, message= "Agregue al menos una variable a eliminar", title="¡Error!")
	elif verificaCheck.get() == "No":
		varT = CopiaDatosTablaA2
		Parte2A2()
	else: 
		messagebox.showinfo(master= ventanaAlgoritmo2, message= "Seleccione sí o no eliminar una o varias variables", title="¡Error!")

def FuncionVenAlgoritmo2():

	global DatosTabla, checkEliminar, varAEliminar, CopiaDatosTablaA2, ventanaAlgoritmo2, listaEliminar, verificaCheck, contador2A2

	ventanaAlgoritmo2 = tk.Tk()
	ventanaAlgoritmo2.geometry('700x400+350+100')
	ventanaAlgoritmo2.configure(background = '#AFEEEE')
	ventanaAlgoritmo2.resizable(width=0, height=0)
	ventanaAlgoritmo2.title("Componentes Principales")
	listaEliminar = []
	CopiaDatosTablaA2 = DatosTabla
	contador2A2 = -1
	texto = "\n"
	etiqueta = tk.Label(ventanaAlgoritmo2,text = texto, bg = "#AFEEEE").pack(anchor=CENTER)
	texto2 = "Componentes Principales"
	etiqueta2 = tk.Label(ventanaAlgoritmo2,text = texto2, bg = "#AFEEEE", fg = "black", font=("Verdana",12)).pack(anchor=CENTER)
	texto2 = "Instrucciones: Debe eliminar una o más variables que sean dependientes dentro de los datos cargados,\nen caso de que no, seleccione en el menú No. Debe escribir las variables una por una, dé click en\n Agregar. Cuando esté seguro de no eliminar más variables, dé click en Aceptar y\npasará a una siguiente ventana"
	etiqueta2 = tk.Label(ventanaAlgoritmo2,text = texto2, bg = "#AFEEEE", fg = "black", font=("Verdana",8)).pack(anchor=CENTER)
	contadorA2 = 0
	columnasA2 = 'Variables:\n'
	for i in DatosTabla.columns.values:
		columnasA2 = columnasA2 +" - " + i
		contadorA2 = contadorA2 + 1
		if contadorA2 % 6 == 0:
			columnasA2 = columnasA2 + "\n"
	etiqueta33 = tk.Label(ventanaAlgoritmo2,text = columnasA2, bg = "white", fg = "black", width = 75, height = 5, font=("Verdana",8)).pack(anchor=CENTER)
	texto3 = "Variable a eliminar: "
	etiqueta3 = tk.Label(ventanaAlgoritmo2,text = texto3, bg = "#FA8072", fg = "white", font=("Verdana",8))
	etiqueta3.place(x=100,y=240.5)

	verificaCheck = tk.StringVar(ventanaAlgoritmo2)
	verificaCheck.set('¿Desea eliminar variables?')
	opcionesCheck = ['Sí','No']
	opcionCheck= tk.OptionMenu(ventanaAlgoritmo2,verificaCheck,*opcionesCheck)
	opcionCheck.pack()
	opcionCheck.config(width = 30, font=("Verdana",7), bg = "goldenrod")

	AgregarVarA2=Button(ventanaAlgoritmo2,text='Agregar',command=BotonAgregaVarA2, bg = "#90EE90")
	AgregarVarA2.place(x=505,y=238.5)

	EliminaVarA2=Button(ventanaAlgoritmo2,text='Aceptar',command=BotonEliminaVarA2, bg = "#90EE90")
	EliminaVarA2.place(x=575,y=238.5)
		
	varAEliminar=Text(ventanaAlgoritmo2, height = 1, width = 32)
	varAEliminar.place(x=230,y=240)
	
	ventanaAlgoritmo2.mainloop()


# Algoritmo 3

def BotonGraficaGlusterA3():

	global MLista, MParticional

	plt.figure(figsize=(10,7))
	plt.scatter(MLista[:,0], MLista[:,1], c=MParticional.labels_, cmap = 'rainbow')
	plt.show()

def BotonClusterNumeroA3():

	global CopiaDatosTabla

	ventanaClusterA3 = tk.Tk()
	ventanaClusterA3.geometry('500x300+450+100')
	ventanaClusterA3.configure(background = 'white')
	ventanaClusterA3.title("Cluster")
	scrollbary = Scrollbar(ventanaClusterA3)
	scrollbary.pack(side="right",fill = Y)
	scrollbarx = Scrollbar(ventanaClusterA3, orient=HORIZONTAL)
	scrollbarx.pack(side="bottom", fill = X)
	texto = Text(ventanaClusterA3, width = 150, height = 15, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	texto2 = CopiaDatosTabla.groupby(['clusterP'])['clusterP'].count()
	texto.insert(INSERT,texto2)
	texto.configure(state='disabled')
		
	ventanaClusterA3.mainloop()

def BotonElbowA3():

	global SSE

	plt.figure(figsize=(10,7))
	plt.plot(range(2,14), SSE, marker='o')
	plt.xlabel('Cantidad de clusters *k*')
	plt.ylabel('SSE')
	plt.title('Elbow Method')
	plt.show()


def BotonClusterA3():

	global DatosTabla, numCluster, ventanaAlgoritmo3, colorA3, colorletraA3, MLista, varClusterOf, CopiaDatosTabla, MParticional

	try:
		CopiaDatosTabla = DatosTabla
		varClusterOf=int(numCluster.get("1.0","end-1c"))
		numCluster.delete("1.0", "end")
		texto = "Número de Cluster dado: " + str(varClusterOf)
		etiqueta = tk.Label(ventanaAlgoritmo3,text = texto, bg = colorA3, fg = colorletraA3, font=("Verdana",8))
		etiqueta.place(x=475,y=350)

		MParticional = KMeans(n_clusters=varClusterOf, random_state=0).fit(MLista)
		MParticional.predict(MLista)
		CopiaDatosTabla['clusterP'] = MParticional.labels_

		MostrarNumCluster=Button(ventanaAlgoritmo3,text='Ver clusters',command=BotonClusterNumeroA3, bg = "#90EE90")
		MostrarNumCluster.place(x=520,y=390)

		MostrarGraCluster=Button(ventanaAlgoritmo3,text='Ver gráfica',command=BotonGraficaGlusterA3, bg = "#90EE90")
		MostrarGraCluster.place(x=520.5,y=430)

	except:
		messagebox.showinfo(master= ventanaAlgoritmo3, message= "Ingrese un número entero", title="¡Error!")


def BotonAceptarA3():

	global listaVarAgrega, textoVarList, columnasAgregadas, ventanaAlgoritmo3, DatosTabla, SSE, colorletraA3, colorA3, numCluster, MLista


	# Condicional para aceptar
	try:

		if len(listaVarAgrega) >= 2: 

		# Empezar a poner los algoritmos y poner botones para los algoritmos

			MLista = np.array(DatosTabla[listaVarAgrega])
			pd.DataFrame(MLista)
			# Definición de k clusters para K-means
			# Se utiliza random_state para inicializar el generador interno de números aleatorios
			SSE = []
			for i in range(2,14):
			  km = KMeans(n_clusters = i, random_state=0)
			  km.fit(MLista)
			  SSE.append(km.inertia_)

			# Se grafica SSE en función de k, se va a tener un botón para ello. 

			MostrarElbow=Button(ventanaAlgoritmo3,text='Ver Elbow Method',command=BotonElbowA3, bg = "#90EE90")
			MostrarElbow.place(x=500,y=230)

			# Poner el número de clusters. 

			texto = "Número de Cluster:"
			etiqueta = tk.Label(ventanaAlgoritmo3,text = texto, bg = colorA3, fg = colorletraA3, font=("Verdana",8))
			etiqueta.place(x=475,y=270.5)
			
			numCluster=Text(ventanaAlgoritmo3, height = 1, width = 3)
			numCluster.place(x=610,y=270)

			MostrarCluster=Button(ventanaAlgoritmo3,text='Siguiente',command=BotonClusterA3, bg = "#90EE90")
			MostrarCluster.place(x=520,y=310)

		else:
			messagebox.showinfo(master= ventanaAlgoritmo3, message= "Deben ser dos o más variables que se escogen de la lista.", title="¡Error!")
	except: 
		messagebox.showinfo(master= ventanaAlgoritmo3, message= "Escoge otras variables, los que fueron agregados no pueden ser analizados.", title="¡Error!")

	# Listo :) 

def BotonReiniciaA3():

	global listaVarAgrega, textoVarList, columnasAgregadas, ventanaAlgoritmo3

	listaVarAgrega = []
	columnasAgregadas = ''
	textoVarList = Text(ventanaAlgoritmo3, width = 20, height = 20, wrap = NONE)
	textoVarList.place(x=275,y=170)
	textoVarList.insert(INSERT,columnasAgregadas)
	textoVarList.configure(state='disabled')

def BotonListaA3():

	global ventanaAlgoritmo3, ListaVar, DatosTabla, listaVarAgrega,textoVarList

	agregaVar = str(ListaVar.get("1.0","end-1c"))
	ListaVar.delete("1.0", "end")
	# Verificar que esté en la columna

	if agregaVar in DatosTabla.columns.values and (agregaVar not in listaVarAgrega):
		listaVarAgrega.append(agregaVar)
		columnasAgregadas = ''

	# Imprimir lo que está en la lista

		for i in listaVarAgrega:
			columnasAgregadas = columnasAgregadas  +" - " + i +  "\n"
		textoVarList = Text(ventanaAlgoritmo3, width = 20, height = 20, wrap = NONE)
		textoVarList.place(x=275,y=170)
		textoVarList.insert(INSERT,columnasAgregadas)
		textoVarList.configure(state='disabled')

	else:

		messagebox.showinfo(master= ventanaAlgoritmo3, message= "El nombre de la columna no es la correcta o ya se agregó a la lista.", title="¡Error!")


def FuncionVenAlgoritmo3():

	global DatosTabla, ventanaAlgoritmo3,ListaVar, listaVarAgrega, colorA3, colorletraA3

	listaVarAgrega = []
	colorA3 = "white"
	colorletraA3 = "black"
	ventanaAlgoritmo3 = tk.Tk()
	ventanaAlgoritmo3.geometry('700x500+350+100')
	ventanaAlgoritmo3.configure(background = "blue")
	ventanaAlgoritmo3.resizable(width=0, height=0)
	ventanaAlgoritmo3.title("Cluster Particional")
	texto = "\n"
	etiqueta = tk.Label(ventanaAlgoritmo3,text = texto, bg = "blue").pack(anchor=CENTER)
	texto2 = "Cluster Particional"
	etiqueta2 = tk.Label(ventanaAlgoritmo3,text = texto2, bg = colorA3, fg = colorletraA3, font=("Verdana",12)).pack(anchor=CENTER)

	texto10 = "Instrucciones: Seleccione una variable del\nlistado y dé click en Agregar, cuando haya\ningresado dos o más, clickeé Aceptar, puede\n visualizar Elbow Method. Después ingrese\nun número del cluster y se activarán\ndos botones para ver información."
	etiqueta10 = tk.Label(ventanaAlgoritmo3,text = texto10, bg = colorA3, fg = colorletraA3, font=("Verdana",7))
	etiqueta10.place(x=450,y=10)

	columnas = 'Variables:\n'
	for i in DatosTabla.columns.values:
		columnas = columnas +  "\n" +" - " + i 
	etiqueta3 = tk.Label(ventanaAlgoritmo3,text = columnas, bg = colorA3, fg = colorletraA3, font=("Verdana",10))
	etiqueta3.place(x=75,y=80)

	texto4 = "Selección de variables"
	etiqueta4 = tk.Label(ventanaAlgoritmo3,text = texto4, bg = colorA3, fg = colorletraA3, font=("Verdana",10))
	etiqueta4.place(x=275,y=80)

	texto12 = "Variable a seleccionar:"
	etiqueta12 = tk.Label(ventanaAlgoritmo3,text = texto12, bg = colorA3, fg = colorletraA3, font=("Verdana",8))
	etiqueta12.place(x=275,y=110.5)
	
	ListaVar=Text(ventanaAlgoritmo3, height = 1, width = 22)
	ListaVar.place(x=420,y=110)

	AgregarLista=Button(ventanaAlgoritmo3,text='Agregar',command=BotonListaA3, bg = "#90EE90")
	AgregarLista.place(x=610,y=108.5)

	texto5 = "Lista de variables seleccionadas:"
	etiqueta5 = tk.Label(ventanaAlgoritmo3,text = texto5, bg = colorA3, fg = colorletraA3, font=("Verdana",8))
	etiqueta5.place(x=275,y=140.5)

	ReiniciarLista=Button(ventanaAlgoritmo3,text='Borrar lista',command=BotonReiniciaA3, bg = "#90EE90")
	ReiniciarLista.place(x=610,y=140)
	AceptarLista=Button(ventanaAlgoritmo3,text='Aceptar',command=BotonAceptarA3, bg = "#90EE90")
	AceptarLista.place(x=610,y=170)

	ventanaAlgoritmo3.mainloop()

# Algoritmo 4

def FuncionVenAlgoritmo4():

	global DatosTabla, varPrueba, ventanaAlgoritmo4, seedUsuario

	ventanaAlgoritmo4 = tk.Tk()
	ventanaAlgoritmo4.geometry('500x300+450+100')
	ventanaAlgoritmo4.configure(background = '#DEB887')
	ventanaAlgoritmo4.resizable(width=0, height=0)
	ventanaAlgoritmo4.title("Regresión Logística")
	texto2 = "\nRegresión Logística"
	etiqueta2 = tk.Label(ventanaAlgoritmo4,text = texto2, bg = "#DEB887", font=("Verdana",12)).pack(anchor=CENTER)
	texto4 = "En esta ventana, lo que se va a realizar es el algoritmo de Regresión Logistica\ncon base en los datos que se cargaron con anterioridad. Lo primero que se tiene\nque hacer es darle el valor de la prueba y al seed (Si un valor menor o igual 0, \nel programa va a tomar por default el valor de 1234) y después aparecerá\nel botón Aceptar,dé click en el para ver la siguiente ventana."
	etiqueta4 = tk.Label(ventanaAlgoritmo4,text = texto4, bg = "blue", fg = "white", font=("Verdana",8)).pack(anchor=CENTER)


	
	#Se declara el modelo de tipo regresión logística

	varPrueba = tk.StringVar(ventanaAlgoritmo4)
	varPrueba.set('Selecciona un porcentaje para la prueba')
	opciones2 = ['0.20','0.25','0.30']
	opcion2 = tk.OptionMenu(ventanaAlgoritmo4,varPrueba,*opciones2)
	opcion2.config(width = 30, font=("Verdana",7), bg = "goldenrod")
	opcion2.place(x=70,y=125)
	texto3 = "Exactitud: "
	etiqueta3 = tk.Label(ventanaAlgoritmo4,text = texto3, bg = "white", fg = "black", font=("Verdana",8))
	etiqueta3.place(x=140,y=240.5)
	texto4 = "Seed: "
	etiqueta4 = tk.Label(ventanaAlgoritmo4,text = texto4, bg = "white", fg = "black", font=("Verdana",8))
	etiqueta4.place(x=80,y=171.5)

	seedUsuario = Text(ventanaAlgoritmo4, height = 1, width = 18)
	seedUsuario.place(x=140,y=170)
	BotonPrueba = Button(ventanaAlgoritmo4,text='Ver Exactitud', command=BotonExactitud, font=("Verdana",8), bg = "#90EE90")
	BotonPrueba.place(x=345,y=167.5)
	ventanaAlgoritmo4.mainloop()

def BotonInformacionA4():

	global DatosTabla, Y_validation, PrediccionesNuevas

	ventanaInfoA4 = tk.Tk()
	ventanaInfoA4.geometry('400x200+500+150')
	ventanaInfoA4.configure(background = 'white')
	ventanaInfoA4.title("Análisis exploratorio de datos")
	ventanaInfoA4.resizable(width=0, height=0)
	scrollbary = Scrollbar(ventanaInfoA4)
	scrollbary.pack(side="right",fill = Y)
	scrollbarx = Scrollbar(ventanaInfoA4, orient=HORIZONTAL)
	scrollbarx.pack(side="bottom", fill = X)
	texto = Text(ventanaInfoA4, width = 150, height = 15, wrap = NONE,yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set)
	texto.pack(side=TOP, fill=X)
	scrollbary.config(command=texto.yview)
	scrollbarx.config(command=texto.xview)
	texto2 = classification_report(Y_validation, PrediccionesNuevas)
	texto.insert(INSERT,texto2)
	texto.configure(state='disabled')

	ventanaInfoA4.mainloop()

def BotonExactitud():

	global varPrueba, DatosTabla, ventanaAlgoritmo4, Clasificacion, X_validation, Y_validation, PrediccionesNuevas, seedUsuario

	try:
		# Esto se realiza en la segunda interfaz. 
		DatosTabla = DatosTabla.replace({'M': 0, 'B': 1})
		#Variables predictoras
		X = np.array(DatosTabla[['Texture', 'Area', 'Smoothness', 'Compactness', 'Symmetry', 'FractalDimension']])
		#X = BCancer.iloc[:, [3, 5, 6, 7, 10, 11]].values  #iloc para seleccionar filas y columnas según su posición

		# Poner esto  --> pd.DataFrame(X)

		#Variable clase
		Y = np.array(DatosTabla[['Diagnosis']])

		# Poner esto  --> pd.DataFrame(Y)
		Clasificacion = linear_model.LogisticRegression()
		prueba = float(varPrueba.get())
		seed = int(seedUsuario.get("1.0","end-1c"))
		if seed <= 0:
			seed = 1234
		X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=prueba, random_state=seed, shuffle = True)
		#Se entrena el modelo a partir de los datos de entrada
		Clasificacion.fit(X_train, Y_train)
		#Predicciones probabilísticas
		Probabilidad = Clasificacion.predict_proba(X_train)
		#Predicciones con clasificación final 
		Predicciones = Clasificacion.predict(X_train)
		#Matriz de clasificación
		PrediccionesNuevas = Clasificacion.predict(X_validation)
		confusion_matrix = pd.crosstab(Y_validation.ravel(), PrediccionesNuevas, rownames=['Real'], colnames=['Clasificación'])
		#Reporte de la clasificación
		texto = Text(ventanaAlgoritmo4, height = 1, width = 18)
		texto.place(x=225,y=240)
		texto2 = Clasificacion.score(X_validation, Y_validation)
		texto.insert(INSERT,texto2)
		texto.configure(state='disabled')
		# Poner botón de aceptar

		BotonConfirmar = Button(ventanaAlgoritmo4,text='Confirmar', command= FuncionVenAlgoritmo4_2, font=("Verdana",8), bg = "#90EE90")
		BotonConfirmar.place(x=220,y=270)

		BotonVerInfo = Button(ventanaAlgoritmo4,text='Información', command= BotonInformacionA4, font=("Verdana",8), bg = "#90EE90")
		BotonVerInfo.place(x=215,y=200)
	
		# Poner botón de calcular
	except:

		messagebox.showinfo(master= ventanaAlgoritmo4, message= "No ha seleccionado un porcentaje para la prueba o ha dado un mal valor.", title="¡Error!")

# Segunda ventana Algoritmo1

def BotonResultadoA4():

	global DatosTabla, ventanaAlgoritmo4_2, Clasificacion, X_validation, Y_validation, EntradaID, EntradaTexture, EntradaArea, EntradaSmoothness, EntradaCompactness, EntradaSymmetry, EntradaFD

	# Resultado

	try: 
		Resultado =Text(ventanaAlgoritmo4_2, height = 1, width = 75)
		Resultado.place(x=150,y=270)
		varID = str(EntradaID.get("1.0","end-1c"))

	# Crear variables para obtener lo que pone el usuario
		varTexture = float(EntradaTexture.get("1.0","end-1c"))
		varArea = float(EntradaArea.get("1.0","end-1c"))
		varSmoothness = float(EntradaSmoothness.get("1.0","end-1c"))
		varCompactness = float(EntradaCompactness.get("1.0","end-1c"))
		varSymmetry = float(EntradaSymmetry.get("1.0","end-1c"))
		varFD = float(EntradaFD.get("1.0","end-1c"))
	# Poner la formula
		NuevoPaciente = pd.DataFrame({'Texture': [varTexture], 'Area': [varArea], 'Smoothness': [varSmoothness], 'Compactness': [varCompactness], 'Symmetry': [varSymmetry], 'FractalDimension': [varFD]})
		Cero0Uno = str(Clasificacion.predict(NuevoPaciente))
	# Benigno o Maligno
		BoM = ""
		if varID == '':
			BoM = "ID - Desconocido: "
		else: 
			BoM = BoM + "ID - " + varID + ": "
		if Cero0Uno == '[0]':
			BoM = BoM + "Maligno"
			Resultado.insert(INSERT,BoM)
			Resultado.configure(state='disabled')
		else: 
			BoM = BoM + "Benigno"
			Resultado.insert(INSERT,BoM)
			Resultado.configure(state='disabled')

	except:

		messagebox.showinfo(master= ventanaAlgoritmo4_2, message= "Debe ingresar solo números", title="¡Error!")
	# Poner la formula
	# Benigno o Maligno
	"""
	texto5 = Clasificacion.score(X_validation, Y_validation)
	Resultado.insert(INSERT,texto5)
	Resultado.configure(state='disabled')
	"""

def FuncionVenAlgoritmo4_2():

	global DatosTabla, ventanaAlgoritmo4, Clasificacion, X_validation, Y_validation, EntradaID, EntradaTexture, EntradaArea, EntradaSmoothness, EntradaCompactness, EntradaSymmetry, EntradaFD, ventanaAlgoritmo4_2

	ventanaAlgoritmo4.destroy()
	ventanaAlgoritmo4_2 = tk.Tk()
	ventanaAlgoritmo4_2.geometry('800x300+300+100')
	ventanaAlgoritmo4_2.configure(background = '#ADD8E6')
	ventanaAlgoritmo4_2.resizable(width=0, height=0)
	ventanaAlgoritmo4_2.title("Regresión Logística")
	texto = "\n"
	etiqueta = tk.Label(ventanaAlgoritmo4_2,text = texto, bg = "#ADD8E6").pack(anchor=CENTER)
	texto2 = "Regresión Logística"
	etiqueta2 = tk.Label(ventanaAlgoritmo4_2,text = texto2, bg = "#ADD8E6", font=("Verdana",12)).pack(anchor=CENTER)

	# Entradas 

	EntradaID = Text(ventanaAlgoritmo4_2, height = 1, width = 18)
	EntradaID.place(x=200,y=90)
	EntradaTexture = Text(ventanaAlgoritmo4_2, height = 1, width = 18)
	EntradaTexture.place(x=200,y=120)
	EntradaArea = Text(ventanaAlgoritmo4_2, height = 1, width = 18)
	EntradaArea.place(x=200,y=150)
	EntradaSmoothness =Text(ventanaAlgoritmo4_2, height = 1, width = 18)
	EntradaSmoothness.place(x=200,y=180)
	EntradaCompactness =Text(ventanaAlgoritmo4_2, height = 1, width = 18)
	EntradaCompactness.place(x=520,y=120)
	EntradaSymmetry = Text(ventanaAlgoritmo4_2, height = 1, width = 18)
	EntradaSymmetry.place(x=520,y=150)
	EntradaFD =Text(ventanaAlgoritmo4_2, height = 1, width = 18)
	EntradaFD.place(x=520,y=180)

	# Etiquetas

	texto3 = "Exactitud: "
	etiqueta3 = tk.Label(ventanaAlgoritmo4_2,text = texto3, bg = "white", fg = "black", font=("Verdana",8))
	etiqueta3.place(x=400,y=90.5)
	texto4 = Text(ventanaAlgoritmo4_2, height = 1, width = 18)
	texto4.place(x=520,y=90)
	texto5 = Clasificacion.score(X_validation, Y_validation)
	texto4.insert(INSERT,texto5)
	texto4.configure(state='disabled')

	texto6 = "ID: "
	etiqueta6 = tk.Label(ventanaAlgoritmo4_2,text = texto6, bg = "white", fg = "black", font=("Verdana",8))
	etiqueta6.place(x=80,y=90.5)

	texto7 = "Texture: "
	etiqueta7 = tk.Label(ventanaAlgoritmo4_2,text = texto7, bg = "white", fg = "black", font=("Verdana",8))
	etiqueta7.place(x=80,y=120.5)

	texto8 = "Area: "
	etiqueta8 = tk.Label(ventanaAlgoritmo4_2,text = texto8, bg = "white", fg = "black", font=("Verdana",8))
	etiqueta8.place(x=80,y=150.5)

	texto9 = "Smoothness: "
	etiqueta9 = tk.Label(ventanaAlgoritmo4_2,text = texto9, bg = "white", fg = "black", font=("Verdana",8))
	etiqueta9.place(x=80,y=180.5)

	texto10 = "Compactness: "
	etiqueta10 = tk.Label(ventanaAlgoritmo4_2,text = texto10, bg = "white", fg = "black", font=("Verdana",8))
	etiqueta10.place(x=400,y=120.5)

	texto11 = "Symmetry: "
	etiqueta11 = tk.Label(ventanaAlgoritmo4_2,text = texto11, bg = "white", fg = "black", font=("Verdana",8))
	etiqueta11.place(x=400,y=150.5)

	texto12 = "Fractal Dimension: "
	etiqueta12 = tk.Label(ventanaAlgoritmo4_2,text = texto12, bg = "white", fg = "black", font=("Verdana",8))
	etiqueta12.place(x=400,y=180.5)

	Acepta=Button(ventanaAlgoritmo4_2,text='Obtener resultado',command=BotonResultadoA4, bg = "#90EE90")
	Acepta.place(x=350,y=225.5)
	texto12 = "Diagnosis: "
	etiqueta12 = tk.Label(ventanaAlgoritmo4_2,text = texto12, bg = "white", fg = "black", font=("Verdana",8))
	etiqueta12.place(x=50,y=270.5)
	ventanaAlgoritmo4_2.mainloop()

FuncionVenConf()