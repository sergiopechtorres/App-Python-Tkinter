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
    database="anuies" # nombre de la base de datos  
)

query = "SELECT * FROM data;" # consulta SQL 
df = pd.read_sql(query,mydb) # Convertir un query en dataframe de Pandas
mydb.close()
print(df.info())

muestra=df[:100].copy()

 ## Creamos Gráfica
resultado= muestra.ENTIDAD_FEDERATIVA.unique()
colors = {"AGUASCALIENTES":"crimson","BAJA CALIFORNIA":"blue","BAJA CALIFORNIA SUR":"black", "CAMPECHE":"pink","CHIAPAS":"green"}
entidad_color= muestra.ENTIDAD_FEDERATIVA.map(colors)

h1=muestra.groupby(['ENTIDAD_FEDERATIVA']).sum()
h1.plot(kind='scatter',x='Lugares_Ofertados' ,y='Lugares_Ofertados',title='DATOS POR ESTADO-ANUIES')
    
resultado= muestra.ENTIDAD_FEDERATIVA.unique()
print(resultado)
colors = {"AGUASCALIENTES":"crimson","BAJA CALIFORNIA":"blue","BAJA CALIFORNIA SUR":"black", "CAMPECHE":"pink","CHIAPAS":"green"}
entidad_color= muestra.ENTIDAD_FEDERATIVA.map(colors)
muestra.groupby(['ENTIDAD_FEDERATIVA']).sum()
fig,ax=plt.subplots()
for ENTIDAD_FEDERATIVA in set(muestra.ENTIDAD_FEDERATIVA):
    muestra.groupby(['ENTIDAD_FEDERATIVA']).sum()
    ax.scatter(
        muestra.Lugares_Ofertados[muestra.ENTIDAD_FEDERATIVA == ENTIDAD_FEDERATIVA],
        muestra.Lugares_Ofertados[muestra.ENTIDAD_FEDERATIVA == ENTIDAD_FEDERATIVA],
        s = 30,
        c = colors[ENTIDAD_FEDERATIVA],
        
        label=ENTIDAD_FEDERATIVA)
plt.legend()
plt.show()


















"""muestra.groupby(['ENTIDAD_FEDERATIVA']).sum().plot(kind='bar', y='Solicitudes de Primer Ingreso',title='SOLICITUDES PRIMER INGRESO-ANUIES')
N = 5
df2 = muestra.append({'ENTIDAD_FEDERATIVA': '', 'Solicitudes de Primer Ingreso': muestra['Solicitudes de Primer Ingreso'].iloc[N:].sum()}, ignore_index=True)
df2.set_index('ENTIDAD_FEDERATIVA').plot.pie(y='Solicitudes de Primer Ingreso', legend=False)
leg = plt.legend(labels=df2['Solicitudes de Primer Ingreso'])
muestra.groupby(['ENTIDAD_FEDERATIVA',]).sum().plot(kind='pie', y='Lugares Ofertados',title='LUGARES OFERTADOS-ANUIES',autopct='%1.1f%%')
"""




#df.plot(kind='cubic',x='nombre',y="edad",title='Ejemplo 2')

 
## Mostramos Gráfica

 



"""colores = ['red','green','blue','yellow','brown','purple','turquoise']


df.groupby(['nombre']).sum().plot(kind='pie', y='edad',title='Ejemplo de una BD',autopct='%1.1f%%')

df.plot(kind='cubic',x='nombre',y="edad",title='Ejemplo 2',color=colores)"""

#barh
#line
#bar
#scatter


