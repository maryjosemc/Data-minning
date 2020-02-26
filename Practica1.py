#!/usr/bin/env python
# coding: utf-8

# # PRACTICA 1

# In[1]:


#Importamos lo que vamos a necesitar
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import numpy as np    
from numpy import dot
from numpy.linalg import norm


# # Limpieza de Datos.

# In[2]:


##leemos el archivo del que extraemos los tweets

archivo = open("Tweet.txt","r",encoding="utf-8")
text_01 = []
while(True):
    linea = archivo.readline()
    text_01.append(linea)
    if not linea:
        break


# In[3]:


#Funcion para remover saltos de linea y espacios del txt 
def removeSaltosLinea(vector):
    while( "\n" in vector ):
        vector.remove("\n")
    while( "" in vector ):
        vector.remove("")


# In[4]:


#Funcion para eliminar las stopwords
def deleteStopWords(tweet):
    tweetWoutSoptWords = []
    for palabra in tweet:
        
        if palabra not in stopwords.words('spanish'):
            tweetWoutSoptWords.append(palabra)
    return tweetWoutSoptWords


# In[5]:


#Funcion para homogeneizar los tweets
tokenizer = RegexpTokenizer(r'\w+')
def removeSignosPuntuacion(tweet):
    return tokenizer.tokenize(tweet.lower())


# In[6]:


#depuramos el arreglo que leimos 
removeSaltosLinea(text_01)
for i in range(len(text_01)):
    text_01[i]= removeSignosPuntuacion(text_01[i])
    text_01[i]=deleteStopWords(text_01[i])


# In[7]:


#impresion de los tweets en su forma vectorial y limpios
#print(len(text_01[0]))
#for elemento in text_01:
#    print(elemento)



# # Creación de BoW.

# In[8]:


#Creación de la BoW
dicc_texts = {}
texto = "text "

for i in range(0,len(text_01)):
    indice =  texto + str(i)
    dicc_texts[indice] = text_01[i]

#dicc_texts


# In[9]:


dicc_termns = {}

for text in dicc_texts:
    for word in dicc_texts[text]:
        
#        print("EVALUAR:", word, "EN", text)
        
        if(word in dicc_termns):#incrementar palabras al diccionario
            dicc_termns[word] = dicc_termns[word] + 1
            
#            print(word, "IN", "dicc_termns")
            
        elif(word not in dicc_termns):#agregar palabras al diccionario        
            dicc_termns[word] = 1
            
#            print(word, "NOT IN", "dicc_termns")            

#print(len(dicc_termns))
#dicc_termns


# # Creación de Matriz Término Documento (binaria)

# In[10]:


#Creación de Matriz Término Documento(binaria)
matrix = np.zeros((len(dicc_texts), len(dicc_termns))) # Pre-allocate matrix


# In[11]:


i = 0
j = 0

for word_termns in dicc_termns: #dicc_termns todos los términos
#    print()
    for word_texts in dicc_texts: #dicc_texts todos los textos
#        print("EVALUAR:", word_termns, "EN: ", word_texts)
        if(word_termns in dicc_texts[word_texts]): #si está
            print(word_termns, "IN", word_texts)
            
            matrix[j, i] = 1
            
        elif(word_termns not in dicc_texts[word_texts]): # si no está
            print(word_termns, "NOT IN", word_texts)
            
            matrix[j, i] = 0
            
            
        print("se agregó: ", matrix[j,i], "en: ", j, i)
            
        j = j + 1
        
    j = 0
    i = i + 1


# In[12]:


matrix


# In[13]:


len(matrix[0])


# In[14]:


matrix[0]


# # Distancia Coseno de Matriz Término Documento (binaria)

# In[15]:


for i in range(0, len(matrix)):
    for j in range(0,len(matrix)):
        bin_cos_ti_tj = dot(matrix[i],matrix[j])/(norm(matrix[i])*norm(matrix[j]))
        print("Similaridad entre el vector "+str(i)+" con el vector "+str(j)+" es "+ str(bin_cos_ti_tj))


# # Distancia Euclidiana de Matriz Término Documento (binaria)

# In[16]:


for i in range(0, len(matrix)):
    for j in range(0,len(matrix)):
        bin_euc_ti_tj = np.sqrt(dot(matrix[i],matrix[j]))
        print("Distancia entre el vector "+str(i)+" con el vector "+str(j)+" es "+ str(bin_euc_ti_tj))


# # Matriz Término Documento (frecuencia) 

# In[17]:


matrix = np.zeros((len(dicc_texts), len(dicc_termns))) # Pre-allocate matrix
#matrix


# In[18]:


i = 0
j = 0

for word_termns in dicc_termns: #dicc_termns todos los términos
#    print()
    for word_texts in dicc_texts: #dicc_texts todos los textos
#        print("EVALUAR:", word_termns, "EN: ", word_texts)
        if(word_termns in dicc_texts[word_texts]): #si está
            print(word_termns, "IN", word_texts)
            
            matrix[j, i] = dicc_termns[word_termns]
            
        elif(word_termns not in dicc_texts[word_texts]): # si no está
            print(word_termns, "NOT IN", word_texts)
            
            matrix[j, i] = 0
            
            
        print("se agregó: ", matrix[j,i], "en: ", j, i)
            
        j = j + 1
        
    j = 0
    i = i + 1


# In[19]:


matrix


# # Distancia Coseno de Matriz Término Documento (frecuencia)

# In[20]:


for i in range(0, len(matrix)):
    for j in range(0,len(matrix)):
        bin_cos_ti_tj = dot(matrix[i],matrix[j])/(norm(matrix[i])*norm(matrix[j]))
        print("Similaridad entre el vector "+str(i)+" con el vector "+str(j)+" es "+ str(bin_cos_ti_tj))


# # Distancia Euclidiana de Matriz Término Documento (frecuencia)

# In[21]:


for i in range(0, len(matrix)):
    for j in range(0,len(matrix)):
        bin_euc_ti_tj = np.sqrt(dot(matrix[i],matrix[j]))
        print("Distancia entre el vector "+str(i)+" con el vector "+str(j)+" es "+ str(bin_euc_ti_tj))

