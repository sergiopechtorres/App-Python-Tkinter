from cProfile import label
from turtle import color
from unicodedata import name
from matplotlib import colors
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model 
import statsmodels.formula.api as smf



mydb=mysql.connector.connect(
    host="localhost", # servidor de base de datos
    user="root", # usuario
    password="", # contraseña
    database="anuarios" # nombre de la base de datos  
)

query = "SELECT * FROM data;" # consulta SQL 
df = pd.read_sql(query,mydb) # Convertir un query en dataframe de Pandas
mydb.close()
print(df.info())

muestra=df[:100].copy()
#print(muestra)

linear_model= smf.ols(formula='Titulados_Total ~ Lugares_Ofertados', data= muestra).fit()
linear_model.params
print(linear_model.params)

#Titulados_Total= 9.1499 + Lugares_Ofertados*0.090178

print(linear_model.pvalues)
print(linear_model.rsquared)

print(linear_model.summary())

Titulados_predi=linear_model.predict(pd.DataFrame(muestra['Lugares_Ofertados']))
print(Titulados_predi)

muestra.plot(kind='scatter',x='Lugares_Ofertados',y='Titulados_Total')
plt.plot(pd.DataFrame(muestra['Lugares_Ofertados']),Titulados_predi,c='red',linewidth=3)
plt.show()
#sales= Titulados
#tv = lugares