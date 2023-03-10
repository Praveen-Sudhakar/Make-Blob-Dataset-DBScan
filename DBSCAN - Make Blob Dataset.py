#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Import necessary packages

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


#Generating the data

centers = ([1,1],[-1,-1],[1,-1],[-1,1])
x,labels_true = make_blobs(n_samples = 1000,centers=centers,cluster_std = 0.4,random_state=0)


# In[31]:


x[0:5]


# In[6]:


set(labels_true)


# In[8]:


#plotting the graph of clusters generated by us

plt.scatter(x[:,0],x[:,1])
plt.show()


# In[9]:


#Standard scaling the IV

x = StandardScaler().fit_transform(x)
x[0:5]


# In[10]:


#Plotting the standard scaled data

plt.scatter(x[:,0],x[:,1])
plt.show()


# In[11]:


#Modeling 

db = DBSCAN(eps = 0.3,min_samples=15)

db.fit(x)


# In[16]:


#Generating labels created by DBSCAN

labels = db.labels_

print(labels[0:5])
print("No. of classes of labels",set(labels))


# In[20]:


#Comparing original & generated labels
from sklearn import metrics

print(f"Homogeneity score = {metrics.homogeneity_score(labels_true,db.labels_)*100} %")


# In[23]:


#Plotting the graph using generated labels

colormap = np.array(['yellow','green','red','black'])
plt.scatter(x[:,0],x[:,1],color=colormap[db.labels_])
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()


# In[24]:


#Plotting the graph using original labels

colormap = np.array(['yellow','green','red','black'])
plt.scatter(x[:,0],x[:,1],color=colormap[labels_true])
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()


# In[32]:


#Creating dataframe

import pandas as pd

df = pd.DataFrame({'X-Axis':x[:,0],'Y-Axis':x[:,1],'Original Labels':labels_true,'DBSCAN Labels':db.labels_})

df


# In[33]:


x[0:5]


# In[ ]:




