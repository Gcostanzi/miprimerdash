#!/usr/bin/env python
# coding: utf-8

#  <img src="https://eant.tech/imagenes/logo.png" width=25% height=80%  >

# In[1]:


#Instalación



# In[2]:


import pandas as pd
import numpy as np

# import dash
# from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input,Output,State
from dash import dash_table

import plotly.express as px


# In[3]:


# Ports disponibles localmente: 8124,8125,8126, 8050
#app._terminate_server_for_port("localhost", 8124)


# In[14]:


app = dash.Dash()


# In[5]:


df = px.data.gapminder()
df_filt = df.loc[df.year == 2007, ['country','continent','lifeExp', 'gdpPercap', 'pop']].reset_index(drop= True)
df_filt.head()


# In[6]:


figura_1 = px.scatter(data_frame= df_filt, x= "lifeExp", y = "gdpPercap", color = "pop", 
                      size= "pop", size_max= 80, hover_name="country",  labels={"lifeExp": "Esperanza de vida", "gdpPercap": "PIB per cápita", "pop": "Población"})  # Modificar etiquetas de los ejes)

figura_1.show()


# In[15]:


app.layout = html.Div( children = [
             html.Div(html.H1("Mi primer Dash en python")),
             html.Div(html.P("Este Dash lo realizamos con plotly")),
             dcc.Graph(id = "Grafico_1", figure= figura_1)])
    

if __name__ == "__main__":
      app.run_server(debug=True)


# In[ ]:




