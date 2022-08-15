from msilib.schema import CheckBox, Font
import tkinter as tk
from tkinter import ttk
from tkinter import *
from turtle import left
from numpy import place, size, tile

from ttkwidgets import CheckboxTreeview


ventana = tk.Tk()

# -----IMAGEN DE FONDO---------------------------------------------------
bgprincipal = PhotoImage(file="Imagenes/fondo.png")
label1 = Label(ventana, image=bgprincipal)
label1.place(x=0, y=0)


# -----AJUSTAR LA VENTANA SEGUN LA RESOLUCIÓN DE LA COMPUTADORA----------

width = ventana.winfo_screenwidth()
height = ventana.winfo_screenheight()
tama = '%dx%d' % (width, height)
ventana.geometry(tama)
ventana.title("Pantalla principal")
# ......IMAGEN DE LOGO DEL TECNOLÓGICO...................................
img = PhotoImage(file="Imagenes/descarga.png")
logo = Label(ventana, image=img)
logo.place(x=745, y=12)
# .......TEXTO..........................................................
label = tk.Label(ventana, text="Sistema de Evaluación Estadística de Educación Superior Computacional",
                 bg="#02cab1", fg="white", font=('Arial Black', 13))
label.place(x=335, y=105)

ventana.iconbitmap('Imagenes/casa.ico')
# ----------------- CONSULTA DEF ------------------------------------------------------------------------------------
# .....VENTANA DE TIPO DE INSTITUCIÓN.....................................


def tipodeinsti():
    ventana.deiconify()
    global bg
    global img2
    # CREACION DE LA VENTANA CON TOPLEVEL
    ventana_tipo = Toplevel()
    
    # Creación de la Resolución de la ventana
    width = ventana_tipo.winfo_screenwidth()
    height = ventana_tipo.winfo_screenheight()
    ventana_tipo.geometry("%dx%d" % (width, height))
    
    # Titulo de la Ventana
    ventana_tipo.title("Tipo de Institución")
    
    # -----Fondo de la Ventana ---------------------
    bg = PhotoImage(file="Imagenes/fondo.png")
    label = tk.Label(ventana_tipo, image=bg)
    label.pack()
    
    # ------ICON de la Ventana--------------------
    ventana_tipo.iconbitmap('Imagenes/banco.ico')
    
   
    
    # ......IMAGEN DE LOGO DEL TECNOLÓGICO...................................
    img2 = PhotoImage(file="Imagenes/descarga.png")
    logo = Label(ventana_tipo, image=img2)
    logo.place(x=745, y=12)
    #.......TEXTO.......................
    label = tk.Label(ventana_tipo, text="Sistema de Evaluación Estadística de Educación Superior Computacional",
                 bg="#02cab1", fg="white", font=('Arial Black', 11))
    label.place(x=335, y=105)
    
# .....VENTANA DE AREA DE CONOCIMIENTO..................................
    style=ttk.Style()
    style.theme_use('xpnative')
    style.configure('Treeview.Heading',rowheight=50,font=("Arial Black", 10))
    style.configure('Treeview',rowheight=30,rowwidth=30)


    tv = ttk.Treeview(ventana_tipo,show='headings')
    tv['columns']=('Tipo','Selección','Indicador','Seleccion2','Periodos','Seleccion3')
    tv.tag_configure('fuente', font=("Arial Black", 10))
    tv.column('#0', width=0, stretch=NO)
    tv.column('Tipo', anchor=W,width=250)
    tv.column('Selección',anchor=CENTER,width=120)
    tv.column('Indicador',anchor=W,width=250)
    tv.column('Seleccion2',anchor=CENTER,width=120)
    tv.column('Periodos',anchor=W,width=250)
    tv.column('Seleccion3',anchor=CENTER,width=120)

    
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Tipo', text='TIPO DE INSTITUCIÓN', anchor=CENTER)
    tv.heading('Selección',text='SELECCIÓN',anchor=CENTER)
    tv.heading('Indicador',text='INDICADOR',anchor=CENTER)
    tv.heading('Seleccion2',text='SELECCIÓN',anchor=CENTER)
    tv.heading("Periodos", text="PERIODOS")
    tv.heading("Seleccion3", text="SELECCIÓN")
    tv.insert(parent='', index=0, iid=0, text='', values=('TecNM','','Oferta','','Actual'),tags='fondoblanco')
    tv.insert(parent='', index=1, iid=1, text='', values=('Universidad en General','','Solicitudes de Ingreso','','Todos'),tags='fondo')
    tv.insert(parent='', index=2, iid=2, text='', values=('Universidad Tecnológica','','Nuevo Ingreso','',''),tags='fondoblanco')
    tv.insert(parent='', index=3, iid=3, text='', values=('Universidad Politécnica','','Matrícula Actual','',''),tags='fondo')
    tv.insert(parent='', index=4, iid=4, text='', values=('Otros','','Egresados','',''),tags='fondoblanco')
    tv.place(x=125, y=150)
    
    #-----TAGS ESTILOS--------------------------------------------------------------------------
    tv.tag_configure('fondoblanco',foreground="#00b4d8",font=('Arial Black', 10))

    tv.tag_configure('fondo',background="#e5fcff",foreground="#00b4d8",font=('Arial Black', 10))
    
    tv.tag_configure('fondo',background="#e5fcff",foreground="#00b4d8",font=('Arial Black', 10))


    #-------------Lista Checkbutton-------------------------------------
    
    seleccion1=tk.IntVar()
    c1=Checkbutton(ventana_tipo,text="Opción 1",variable=seleccion1)
    c1.place(x=400,y=175)
    
    seleccion2=tk.IntVar()
    c2=Checkbutton(ventana_tipo,text="Opción 2",variable=seleccion2)
    c2.place(x=400,y=208)
    
    seleccion3=tk.IntVar()
    c3=Checkbutton(ventana_tipo,text="Opción 3",variable=seleccion3)
    c3.place(x=400,y=237)
    
    seleccion4=tk.IntVar()
    c4=Checkbutton(ventana_tipo,text="Opción 4",variable=seleccion4)
    c4.place(x=400,y=267)
    
    seleccion5=tk.IntVar()
    c5=Checkbutton(ventana_tipo,text="Opción 5",variable=seleccion5)
    c5.place(x=400,y=300)
    
    def verificar():   
         cant=0
         if seleccion1.get()==1:
            cant+=1
         if seleccion2.get()==1:
            cant+=1
         if seleccion3.get()==1:
            cant+=1
         if seleccion4.get()==1:
             cant+=1
         if seleccion5.get()==1:
             cant+=1
         label1.configure(text="cantidad:"+str(cant))
    boton1=tk.Button(ventana_tipo, text="Verificar", command=verificar)
    boton1.place(x=415,y=610)
    label1=tk.Label(ventana_tipo,text="cantidad:")
    label1.place(x=410,y=580)
    
    #------RadioButton Lista  Indicadores----------------------------------
    
    
    
    def selectIndicadores():
        monitor3.config(text = "Opción {}".format(opcion.get() ) )
    
    opcion = IntVar() # Como StrinVar pero en entero
    
    r1=Radiobutton(ventana_tipo, text="Opción 1",variable=opcion, 
            value=1,command=selectIndicadores )
    r1.place(x=770,y=175)
    
    r2=Radiobutton(ventana_tipo, text="Opción 2",variable=opcion, 
            value=2,command=selectIndicadores )
    r2.place(x=770,y=208)
    
    r3=Radiobutton(ventana_tipo, text="Opción 3",variable=opcion, 
            value=3,command=selectIndicadores )
    r3.place(x=770,y=237)
    
    r4=Radiobutton(ventana_tipo, text="Opción 4",variable=opcion, 
            value=4,command=selectIndicadores )
    r4.place(x=770,y=267)
    
    r5=Radiobutton(ventana_tipo, text="Opción 5",variable=opcion, 
            value=5,command=selectIndicadores )
    r5.place(x=770,y=300)
    
    monitor3 = Label(ventana_tipo)
    monitor3.place(x=780,y=590)
    #---------Select Periodos--------------------------
    def selectPeriodos():
        monitor1.config(text = "Opción {}".format(opcion2.get() ) )
    
    opcion2 = IntVar() # Como StrinVar pero en entero
    

    r1=Radiobutton(ventana_tipo, text="Opción 1",variable=opcion2, 
            value=1,command=selectPeriodos )
    r1.place(x=1135,y=175)
    
    r2=Radiobutton(ventana_tipo, text="Opción 2",variable=opcion2, 
            value=2,command=selectPeriodos )
    r2.place(x=1135,y=208)
    
    monitor1 = Label(ventana_tipo)
    monitor1.place(x=880,y=590)
    """
    #-------Selección de Graficos--------------------------------
    def selectGraficos():
        monitor2.config(text = " Opción {}".format(opcion3.get()) )
        
    opcion3 = IntVar()
    
    r1=Radiobutton(ventana_tipo,text="Opción 1", variable=opcion3,value=1,command=selectGraficos)
    r1.place(x=1135,y=305)
    
    r2=Radiobutton(ventana_tipo,text="Opción 2", variable=opcion3,value=2,command=selectGraficos)
    r2.place(x=1135,y=345)
    
    
    monitor2 = Label(ventana_tipo)
    monitor2.place(x=1000,y=590)
    
    #-------Selección de Dispersión--------------------------------
    def selectDispersion():
        monitor3.config(text = "Opción {}".format(opcion4.get() ) )
    
    opcion4 = IntVar() # Como StrinVar pero en entero
    
    r1=Radiobutton(ventana_tipo, text="Opción 1",variable=opcion4, 
            value=1,command=selectDispersion )
    r1.place(x=1135,y=420)
    
    r2=Radiobutton(ventana_tipo, text="Opción 2",variable=opcion4, 
            value=2,command=selectDispersion )
    r2.place(x=1135,y=465)
    
    r3=Radiobutton(ventana_tipo, text="Opción 3",variable=opcion4, 
            value=3,command=selectDispersion )
    r3.place(x=1135,y=505)
    
    monitor3 = Label(ventana_tipo)
    monitor3.place(x=1090,y=590)"""
    
    boton = Button(ventana_tipo,text="Aceptar",bg='#61a9ec',width=13,height=2,command=crearnuevaventana)
    boton.place(x=990, y=500)
    
    boton2 = Button(ventana_tipo,text="Regresar",bg='#e9ec61',width=13,height=2)
    boton2.place(x=1110, y=500)
    
def crearnuevaventana():
    ventana.deiconify()
    global bg3
    global img3
    nuevaventana = tk.Toplevel()
    nuevaventana.title("Gráficos") 
    nuevaventana.geometry("1200x650") 
    nuevaventana.resizable(0,0)
    # -----Fondo de la Ventana ---------------------
    bg3 = PhotoImage(file="Imagenes/fondo.png")
    label = tk.Label(nuevaventana, image=bg3)
    label.pack()
    
    # ......IMAGEN DE LOGO DEL TECNOLÓGICO...................................
    img3 = PhotoImage(file="Imagenes/descarga.png")
    logo = Label(nuevaventana, image=img3)
    logo.place(x=590, y=12)
    #---------------------------------------------------------------------------------
    label = tk.Label(nuevaventana, text="Sistema de Evaluación Estadística de Educación Superior Computacional",
                 bg="#02cab1", fg="white", font=('Arial Black', 11))
    label.place(x=335, y=105)
    # ------ICON de la Ventana--------------------
    nuevaventana.iconbitmap('Imagenes/graficos.ico')
    
    #-------------------------------------------------------------------------------------
    style=ttk.Style()
    style.theme_use('xpnative')
    style.configure('Treeview.Heading',rowheight=50,font=("Arial Black", 10))
    style.configure('Treeview',rowheight=40,rowwidth=30)
    
    treeview = ttk.Treeview(nuevaventana,columns=("tipo", "seleccion"))
    
    treeview.column('#0', width=0, stretch=NO)
    treeview.column('tipo', anchor=W,width=250)
    treeview.column('seleccion',anchor=CENTER,width=250)
    
    treeview.heading("#0", text="",anchor=CENTER)
    treeview.heading("tipo", text="TIPO DE GRÁFICO",anchor=CENTER)
    treeview.heading("seleccion", text="SELECCIÓN")
    
    treeview.insert(parent='', index=0, iid=0, text='', values=('Diagramas de barras',''),tags='fondoblanco')
    treeview.insert(parent='', index=1, iid=1, text='', values=('Diagramas de sectores',''),tags='fondoblanco')
    treeview.insert(parent='', index=2, iid=2, text='', values=('Diagramas de dispersión o puntos',''),tags='fondoblanco')
    treeview.insert(parent='', index=3, iid=3, text='', values=('Diagramas de lineas',''),tags='fondoblanco')
    treeview.insert(parent='', index=4, iid=4, text='', values=('Diagramas de areas',''),tags='fondoblanco')

    treeview.place(x=350, y=150)
    treeview.tag_configure('fondoblanco',foreground="Black",font=('Arial', 13))
    
    
    
    def mostrarseleccionado():
        if seleccion.get()==1 :
            label1.configure(text="opcion seleccionada= Diagrama de Barras")
             
            from matplotlib import colors
            import mysql.connector
            import pandas as pd
            import matplotlib.pyplot as plt
            import seaborn as sns 
            
            mydb=mysql.connector.connect(
            host="localhost", # servidor de base de datos
            user="root", # usuario
            password="", # contraseña
            database="anuarios" # nombre de la base de datos  
            )

            query = "SELECT * FROM `data` WHERE `Clasificacion`='TECNM' AND `Lugares_Ofertados` and `Fecha`=2012;" # consulta SQL 
            df = pd.read_sql(query,mydb) # Convertir un query en dataframe de Pandas
            mydb.close()
            print(df.info())
            muestra=df[:4000].copy()
            muestra.groupby(['Clasificacion','ENTIDAD_FEDERATIVA']).sum().plot(kind='bar',y=['Lugares_Ofertados'],title='LUGARES OFERTADOS POR ESTADO-ANUIES')
            muestra.groupby(['Clasificacion','ENTIDAD_FEDERATIVA']).sum().plot(kind='bar',y=['Solicitudes_de_Primer_Ingreso'],title='SOLICITADOS DE 1° INGRESO POR ESTADO-ANUIES')
            muestra.groupby(['Clasificacion','ENTIDAD_FEDERATIVA']).sum().plot(kind='bar',y=['Primer_Ingreso_Total'],title='1° INGRESO TOTAL POR ESTADO-ANUIES')
            muestra.groupby(['Clasificacion','ENTIDAD_FEDERATIVA']).sum().plot(kind='bar',y=['Matrícula_Total'],title='MATRICULA TOTAL POR ESTADO-ANUIES')
            muestra.groupby(['Clasificacion','ENTIDAD_FEDERATIVA']).sum().plot(kind='bar',y=['Egresados_Total'],title='EGRESADOS TOTAL POR ESTADO-ANUIES')


         
 
            ## Legenda en el eje y
            plt.ylabel('Cantidad')
 
            ## Legenda en el eje x
            plt.xlabel('Tipo De institución')
 
            ## Título de Gráfica
            #plt.title('LUGARES OFERTADOS POR ESTADO-ANUIES')
 
            ## Mostramos Gráfica
            plt.show()
        if seleccion.get()==2:
            from matplotlib import colors
            import mysql.connector
            import pandas as pd
            import matplotlib.pyplot as plt
            import seaborn as sns 
            
            mydb=mysql.connector.connect(
            host="localhost", # servidor de base de datos
            user="root", # usuario
            password="", # contraseña
            database="anuarios" # nombre de la base de datos  
            )

            query = "SELECT * FROM `data` WHERE `Clasificacion`='TECNM' AND `Lugares_Ofertados` and `Fecha`=2012;" # consulta SQL 
            df = pd.read_sql(query,mydb) # Convertir un query en dataframe de Pandas
            mydb.close()
            print(df.info())
            muestra=df[:4000].copy()
            muestra.groupby(['Clasificacion','ENTIDAD_FEDERATIVA',]).sum().plot(kind='pie', y='Lugares_Ofertados',title='LUGARES OFERTADOS-ANUIES',autopct='%1.1f%%')
            muestra.groupby(['Clasificacion','ENTIDAD_FEDERATIVA',]).sum().plot(kind='pie', y='Solicitudes_de_Primer_Ingreso',title='SOLICITUDES DE INGRESO-ANUIES',autopct='%1.1f%%')
            muestra.groupby(['Clasificacion','ENTIDAD_FEDERATIVA',]).sum().plot(kind='pie', y='Primer_Ingreso_Total',title='NUEVO INGRESO -ANUIES',autopct='%1.1f%%')
            muestra.groupby(['Clasificacion','ENTIDAD_FEDERATIVA',]).sum().plot(kind='pie', y='Matrícula_Total',title='MATRICULAS ACTUALES -ANUIES',autopct='%1.1f%%')
            muestra.groupby(['Clasificacion','ENTIDAD_FEDERATIVA',]).sum().plot(kind='pie', y='Egresados_Total',title='EGRESADOS -ANUIES',autopct='%1.1f%%')
            
            plt.show()
            
        if seleccion.get()==3:
            from cProfile import label
            from turtle import color
            from unicodedata import name
            from matplotlib import colors
            import mysql.connector
            import pandas as pd
            import matplotlib.pyplot as plt
            import seaborn as sns 

            mydb=mysql.connector.connect(
                host="localhost", # servidor de base de datos
                user="root", # usuario
                password="", # contraseña
                database="anuarios" # nombre de la base de datos  
            )

            query = "SELECT * FROM `data` WHERE `Clasificacion`='TECNM' AND `Lugares_Ofertados` and `Fecha`=2012;" # consulta SQL 
            df = pd.read_sql(query,mydb) # Convertir un query en dataframe de Pandas
            mydb.close()
            print(df.info())
            
            muestra=df[:519].copy()

            """ ## Creamos Gráfica 1 
            colors = {"AGUASCALIENTES":"crimson","BAJA CALIFORNIA":"blue","BAJA CALIFORNIA SUR":"black", "CAMPECHE":"pink","CHIAPAS":"green","CHIHUAHUA":"Yellow","COAHUILA":"Pink","COLIMA":"Purple","DISTRITO FEDERAL":"Gold","DURANGO":"Brown"}
            entidad_color= muestra.ENTIDAD_FEDERATIVA.map(colors)
            h1=muestra.groupby(['ENTIDAD_FEDERATIVA']).sum()
            h1.plot(kind='scatter',x='Lugares_Ofertados' ,y='Lugares_Ofertados',title='Lugares Ofertados POR ESTADO-ANUIES')
            """
            #..................................................................................................
            #muestra.ENTIDAD_FEDERATIVA.sum()
            #resultado= muestra.ENTIDAD_FEDERATIVA.unique()
            print(muestra)
            colors = {"AGUASCALIENTES":"crimson","BAJA CALIFORNIA":"blue","BAJA CALIFORNIA SUR":"black", "CAMPECHE":"pink","CHIAPAS":"green","CHIHUAHUA":"Yellow","COAHUILA":"Pink","COLIMA":"Purple","DISTRITO FEDERAL":"Gold","DURANGO":"Brown"}

            entidad_color= muestra.ENTIDAD_FEDERATIVA.map(colors)
            muestra.groupby(['Clasificacion','ENTIDAD_FEDERATIVA']).sum()
            fig,ax=plt.subplots()
            for ENTIDAD_FEDERATIVA in set(muestra.ENTIDAD_FEDERATIVA):
               #muestra.groupby(['ENTIDAD_FEDERATIVA']).sum()
               ax.scatter(
               muestra.Lugares_Ofertados[muestra.ENTIDAD_FEDERATIVA== ENTIDAD_FEDERATIVA],
               muestra.Lugares_Ofertados[muestra.ENTIDAD_FEDERATIVA== ENTIDAD_FEDERATIVA],
               s = 30,
               c = colors[ENTIDAD_FEDERATIVA],
               label=ENTIDAD_FEDERATIVA)
        plt.title('Lugares Ofertados')
        plt.legend()
        plt.show()
        
        if seleccion.get()==4:
            label1.configure(text="Opción selecccionada = Diagramas de Líneas ") 
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3, 4], [1, 2, 0, 0.5])
            plt.show()  
        if seleccion.get()==5:
            label1.configure(text="Opción seleccioanada = Diagrama de Areas") 
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            ax.fill_between([1, 2, 3, 4], [1, 2, 0, 0.5])
            plt.show()
        
            
            
    seleccion=tk.IntVar()
    seleccion.set(2)
    radio1=tk.Radiobutton(nuevaventana,text="Opción 1", variable=seleccion, value=1)
    radio1.place(x=680,y=182)
    radio2=tk.Radiobutton(nuevaventana,text="Opción 2", variable=seleccion, value=2)
    radio2.place(x=680,y=220)
    radio3=tk.Radiobutton(nuevaventana,text="Opción 3",variable=seleccion,value=3)
    radio3.place(x=680,y=260)
    radio4=tk.Radiobutton(nuevaventana,text="Opción 4", variable=seleccion,value=4)
    radio4.place(x=680,y=302)
    radio5=tk.Radiobutton(nuevaventana,text="Opción 5",variable=seleccion,value=5)
    radio5.place(x=680,y=342)
   
    
    boton1=tk.Button(nuevaventana, text="Mostrar seleccionado",width=17,height=2,command=mostrarseleccionado )
    boton1.place(x=700,y=580)
    label1=tk.Label(nuevaventana,text="opcion seleccionada")
    label1.place(x=950,y=470)
        

    
crearnuevaventana()    
    

    
    
    
    
    
    

    

def areaconocimiento():
    global bg
    global img2
    
    ventana.deiconify()
    ventana_cono = Toplevel()
    width = ventana_cono.winfo_screenwidth()
    height = ventana_cono.winfo_screenheight()
    tama = '%dx%d' % (width, height)
    ventana_cono.geometry(tama)
    ventana_cono.title("Área de conocimiento")
    ventana_cono.iconbitmap('Imagenes/pensamiento.ico')
    
    # -----Fondo de la Ventana ---------------------
    
    bg = PhotoImage(file="Imagenes/fondo.png")
    label = tk.Label(ventana_cono, image=bg)
    label.pack()
    
    # ......IMAGEN DE LOGO DEL TECNOLÓGICO...................................
    
    img2 = PhotoImage(file="Imagenes/descarga.png")
    logo = Label(ventana_cono, image=img2)
    logo.place(x=745, y=12)
    
    #.......TEXTO.......................
    
    label = tk.Label(ventana_cono, text="Sistema de Evaluación Estadística de Educación Superior Computacional",
                 bg="#02cab1", fg="white", font=('Arial Black', 11))
    label.place(x=335, y=105)
    
    #--STYLE----------------------------------------------
    
    style=ttk.Style()
    style.theme_use('xpnative')
    style.configure('Treeview.Heading', rowheight=40,font=("Arial Black", 10))
    style.configure('Treeview', rowheight=40)

    #---------TREEVIEW ---------------------------------------- 
     
    tv = ttk.Treeview(ventana_cono,show='headings')
    tv['columns']=('Area','Selección','Indicador','Seleccion2','Periodos','Seleccion3')
    tv.tag_configure('fuente', font=("Arial Black", 10))
    tv.column('#0', width=0, stretch=NO)
    tv.column('Area', anchor=W,width=250)
    tv.column('Selección',anchor=CENTER,width=120)
    tv.column('Indicador',anchor=W,width=250)
    tv.column('Seleccion2',anchor=CENTER,width=120)
    tv.column('Periodos',anchor=W,width=250)
    tv.column('Seleccion3',anchor=CENTER,width=120)

    
    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Area', text='ÁREA DE CONOCIMIENTO', anchor=CENTER)
    tv.heading('Selección',text='SELECCIÓN',anchor=CENTER)
    tv.heading('Indicador',text='INDICADOR',anchor=CENTER)
    tv.heading('Seleccion2',text='SELECCIÓN',anchor=CENTER)
    tv.heading("Periodos", text="PERIODOS")
    tv.heading("Seleccion3", text="SELECCIÓN")
    tv.insert(parent='', index=0, iid=0, text='', values=('Ciencias Computacionales','','Oferta','','Actual'),tags='fondo')
    tv.insert(parent='', index=1, iid=1, text='', values=('Desarrollo de Software','','Solicitudes de Ingreso','','Todos'),tags='fondoverde')
    tv.insert(parent='', index=2, iid=2, text='', values=('Informática','','Nuevo Ingreso','','GRÁFICOS'),tags='fondo')
    tv.insert(parent='', index=3, iid=3, text='', values=('Inteligencia Artificial','','Matrícula Actual','','Barras'),tags='fondoverde')
    tv.insert(parent='', index=4, iid=4, text='', values=('Sistemas Computacionales','','Egresados','','Puntos'),tags='fondo')
    tv.insert(parent='', index=5, iid=5, text='', values=('Sistemas de Información','','','','GRÁFICOS DE DISPERSIÓN'),tags='fondoverde')
    tv.insert(parent='', index=6, iid=6, text='', values=('Tecnologías de la Información','','','','R²'),tags='fondo')
    tv.insert(parent='', index=7, iid=7, text='', values=('Telemática','','','','Ecuación'),tags='fondoverde')
    tv.insert(parent='', index=8, iid=8, text='', values=('Otros','','','','Proyectar'),tags='fondo')
    tv.place(x=125, y=150)
    
    #-----TAGS ESTILOS--------------------------------------------------------------------------
    
    tv.tag_configure('fondo',background="#fffbcf",foreground="#46544a",font=('Arial Black', 10))
    
    tv.tag_configure('fondoverde',background="#e7f0f0",foreground="#46544a",font=('Arial Black', 10))
    
    #-------------Lista Checkbutton-------------------------------------
    
    seleccion1=tk.IntVar()
    c1=Checkbutton(ventana_cono,text="Opción 1",variable=seleccion1)
    c1.place(x=400,y=185)
    
    seleccion2=tk.IntVar()
    c2=Checkbutton(ventana_cono,text="Opción 2",variable=seleccion2)
    c2.place(x=400,y=225)
    
    seleccion3=tk.IntVar()
    c3=Checkbutton(ventana_cono,text="Opción 3",variable=seleccion3)
    c3.place(x=400,y=265)
    
    seleccion4=tk.IntVar()
    c4=Checkbutton(ventana_cono,text="Opción 4",variable=seleccion4)
    c4.place(x=400,y=305)
    
    seleccion5=tk.IntVar()
    c5=Checkbutton(ventana_cono,text="Opción 5",variable=seleccion5)
    c5.place(x=400,y=345)
    
    seleccion6=tk.IntVar()
    c6=Checkbutton(ventana_cono,text="Opción 6",variable=seleccion6)
    c6.place(x=400,y=385)
    
    seleccion7=tk.IntVar()
    c7=Checkbutton(ventana_cono,text="Opción 7",variable=seleccion7)
    c7.place(x=400,y=420)
    
    seleccion8=tk.IntVar()
    c8=Checkbutton(ventana_cono,text="Opción 8",variable=seleccion8)
    c8.place(x=400,y=460)
    
    seleccion9=tk.IntVar()
    c9=Checkbutton(ventana_cono,text="Opción 9",variable=seleccion9)
    c9.place(x=400,y=505)
    
    
    
    
    def verificar():   
         cant=0
         if seleccion1.get()==1:
            cant+=1
         if seleccion2.get()==1:
            cant+=1
         if seleccion3.get()==1:
            cant+=1
         if seleccion4.get()==1:
             cant+=1
         if seleccion5.get()==1:
             cant+=1
         if seleccion6.get()==1:
             cant+=1
         if seleccion7.get()==1:
             cant+=1
         if seleccion8.get()==1:
             cant+=1
         if seleccion9.get()==1:
             cant+=1
         label1.configure(text="cantidad:"+str(cant))
    boton1=tk.Button(ventana_cono, text="Verificar", command=verificar)
    boton1.place(x=415,y=610)
    label1=tk.Label(ventana_cono,text="cantidad:")
    label1.place(x=410,y=580)
    #----Indicadores Ventana de Conocimientos--------------------
    def selectIndicadoresCo():
        monitor.config(text = "Opción {}".format(opcion.get() ) )
    
    opcion = IntVar() # Como StrinVar pero en entero
    
    r1=Radiobutton(ventana_cono, text="Opción 1",variable=opcion, 
            value=1,command=selectIndicadoresCo)
    r1.place(x=770,y=185)
    
    r2=Radiobutton(ventana_cono, text="Opción 2",variable=opcion, 
            value=2,command=selectIndicadoresCo )
    r2.place(x=770,y=225)
    
    r3=Radiobutton(ventana_cono, text="Opción 3",variable=opcion, 
            value=3,command=selectIndicadoresCo )
    r3.place(x=770,y=260)
    
    r4=Radiobutton(ventana_cono, text="Opción 4",variable=opcion, 
            value=4,command=selectIndicadoresCo )
    r4.place(x=770,y=305)
    
    r5=Radiobutton(ventana_cono, text="Opción 5",variable=opcion, 
            value=5,command=selectIndicadoresCo )
    r5.place(x=770,y=345)
    
    monitor = Label(ventana_cono)
    monitor.place(x=780,y=590)
    
    #-- Seleccionar los Periodos de la ventana de conocimientos
    def selectPeriodosCo():
        monitor1.config(text = "Opción {}".format(opcion2.get() ) )
    
    opcion2 = IntVar() # Como StrinVar pero en entero
    

    r1=Radiobutton(ventana_cono, text="Opción 1",variable=opcion2, 
            value=1,command=selectPeriodosCo )
    r1.place(x=1135,y=185)
    
    r2=Radiobutton(ventana_cono, text="Opción 2",variable=opcion2, 
            value=2,command=selectPeriodosCo )
    r2.place(x=1135,y=225)
    
    monitor1 = Label(ventana_cono)
    monitor1.place(x=880,y=590)
    
    def selectGraficos():
        monitor2.config(text = " Opción {}".format(opcion3.get()) )
        
    opcion3 = IntVar()
    
    r1=Radiobutton(ventana_cono,text="Opción 1", variable=opcion3,value=1,command=selectGraficos)
    r1.place(x=1135,y=305)
    
    r2=Radiobutton(ventana_cono,text="Opción 2", variable=opcion3,value=2,command=selectGraficos)
    r2.place(x=1135,y=345)
    
    
    monitor2 = Label(ventana_cono)
    monitor2.place(x=1000,y=590)
    
    #-------Selección de Dispersión--------------------------------
    def selectDispersion():
        monitor3.config(text = "Opción {}".format(opcion4.get() ) )
    
    opcion4 = IntVar() # Como StrinVar pero en entero
    
    r1=Radiobutton(ventana_cono, text="Opción 1",variable=opcion4, 
            value=1,command=selectDispersion )
    r1.place(x=1135,y=420)
    
    r2=Radiobutton(ventana_cono, text="Opción 2",variable=opcion4, 
            value=2,command=selectDispersion )
    r2.place(x=1135,y=465)
    
    r3=Radiobutton(ventana_cono, text="Opción 3",variable=opcion4, 
            value=3,command=selectDispersion )
    r3.place(x=1135,y=505)
    
    monitor3 = Label(ventana_cono)
    monitor3.place(x=1090,y=590)
    
    
    
    
    
    
    
    
        
    
        
    
    
    
    
    
    

# ---------------------- BASE DE DATOS DEF --------------------------------------------------------------------------------
    
# .........Pestaña 1...............


def pestaña1():
    global bgp1
    ventana.deiconify()
    ventana_pesuno = Toplevel()
    width = ventana_pesuno.winfo_screenwidth()
    height = ventana_pesuno.winfo_screenheight()
    tam = '%dx%d' % (width, height)
    ventana_pesuno.geometry(tam)
    ventana_pesuno.title("Pestaña 1 Base de Datos")
    
    # -----Fondo de la Ventana ---------------------
    bgp1 = PhotoImage(file="Imagenes/fondo.png")
    label = tk.Label(ventana_pesuno, image=bgp1)
    label.pack()
    
    
    ventana_pesuno.iconbitmap('Imagenes/dato.ico')

# ........Pestaña 2................


def pestaña2():
    global bgp2
    ventana.deiconify()
    ventana_pesdos = Toplevel()
    width = ventana_pesdos.winfo_screenwidth()
    height = ventana_pesdos.winfo_screenheight()
    tam = '%dx%d' % (width, height)
    ventana_pesdos.geometry(tam)
    ventana_pesdos.title("Pestaña 2 Base de Datos")
    # -----Fondo de la Ventana ---------------------
    bgp2 = PhotoImage(file="Imagenes/fondo.png")
    label = tk.Label(ventana_pesdos, image=bgp2)
    label.pack()
    
    
    ventana_pesdos.iconbitmap('Imagenes/BD.ico')

# ..................... HERRAMIENTAS DEF .............................
# ------Agregar periodo Escolar------------------


def periodoescolar():
    ventana.deiconify()
    ventana_periodo = Toplevel()
    width = ventana_periodo.winfo_screenwidth()
    height = ventana_periodo.winfo_screenheight()
    tam = '%dx%d' % (width, height)
    ventana_periodo.geometry(tam)
    ventana_periodo.title("Agregar Perido Escolar")
    ventana_periodo.iconbitmap('Imagenes/calendario.ico')
# ...................... AYUDA DEF ..................................
# ---------Ayuda-------------------------------


def Ayuda():
    global bgayuda
    global imgayuda
    ventana.deiconify()
    ventana_ayuda = Toplevel()
    width = ventana_ayuda.winfo_screenwidth()
    height = ventana_ayuda.winfo_screenheight()
    tam = '%dx%d' % (width, height)
    ventana_ayuda.geometry(tam)
    ventana_ayuda.title("Ayuda")
    # -----Fondo de la Ventana ---------------------
    bgayuda = PhotoImage(file="Imagenes/ayuda.png")
    label = tk.Label(ventana_ayuda, image=bgayuda)
    label.pack()
    
    ventana_ayuda.iconbitmap('Imagenes/pregunta.ico')
    
    # ......IMAGEN DE LOGO DEL TECNOLÓGICO...................................
    imgayuda = PhotoImage(file="Imagenes/descarga.png")
    logoayuda = Label(ventana_ayuda, image=imgayuda)
    logoayuda.place(x=745, y=12)
    # .......TEXTO..........................................................
    label = tk.Label(ventana_ayuda, text="Sistema de Evaluación Estadística de Educación Superior Computacional",
                 bg="#02cab1", fg="white", font=('Arial Black', 10))
    label.place(x=370, y=105)
    
    # .......TEXTO..........................................................
    label = tk.Label(ventana_ayuda, height=19 , width=95,
                 bg="#E5F1FF", fg="white", font=('Arial Black', 13))
    label.place(x=100, y=150)


def AcercaDe():
    ventana.deiconify()
    ventana_acerca = Toplevel()
    width = ventana_acerca.winfo_screenwidth()
    height = ventana_acerca.winfo_screenheight()
    tam = '%dx%d' % (width, height)
    ventana_acerca.geometry(tam)
    ventana_acerca.title("Acerca de ....")
    ventana_acerca.iconbitmap('Imagenes/acercade.ico')
    
    


# .....Menu Bar.........................................................
my_menu = Menu(ventana, background="red")
ventana.config(menu=my_menu, background="red")

# ..... CONSULTA.......................................................
file_menu = Menu(my_menu, background="#033f8a", fg="white", tearoff=0)
my_menu.add_cascade(label="Consulta", menu=file_menu)
file_menu.add_command(label="Tipo de Institución", command=tipodeinsti)
file_menu.add_command(label="Área de conocimiento", command=areaconocimiento)


# ...BASE DE DATOS.....................................................
menubd = tk.Menu(my_menu, background="#0196c6", fg="white", tearoff=0)
my_menu.add_cascade(label="Base de Datos", menu=menubd)
menubd.add_command(label="Pestaña 1", command=pestaña1)
menubd.add_command(label="Pestaña 2", command=pestaña2)


# ...HERRAMIENTAS.................................................
menuherra = tk.Menu(my_menu, background="#01b4d9", fg="white", tearoff=0)
my_menu.add_cascade(label="Herramientas", menu=menuherra)
menuherra.add_command(label="Agregar periodo escolar", command=periodoescolar)
menuherra.add_command(label="Copiar")

# ....SALIR.......................................................
menusalir = tk.Menu(my_menu, background="red", fg="white", tearoff=0)
my_menu.add_cascade(label="Salir", menu=menusalir)
menusalir.add_command(label="Salir", command=ventana.quit)
# ....AYUDA......................................................
helpmenu = tk.Menu(my_menu, tearoff=0, background="#8db0d6", fg="black")
my_menu.add_cascade(label="Ayuda", menu=helpmenu)
helpmenu.add_command(label="Ayuda", command=Ayuda)
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...", command=AcercaDe)


ventana.mainloop()
