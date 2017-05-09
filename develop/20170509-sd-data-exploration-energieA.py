
# coding: utf-8

# # 

# In[1]:

get_ipython().magic('matplotlib inline')
get_ipython().magic("config InlineBackend.figure_format='retina'")


# In[2]:

from IPython.display import IFrame, HTML, YouTubeVideo
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.pyplot import GridSpec
import seaborn as sns
import numpy as np


# In[3]:

import pandas as pd
import os, sys
import warnings

sns.set();
plt.rcParams['figure.figsize'] = (12, 8)
sns.set_style("darkgrid")
sns.set_context("poster", font_scale=1.3)

warnings.filterwarnings('ignore')


# In[11]:

pd.set_option('display.max_rows', 99)
pd.set_option('display.max_columns', 999)


# In[6]:

#!conda install qgrid -y

#import qgrid # Put imports at the top
#qgrid.nbinstall(overwrite=True)


# In[32]:

df = pd.read_csv('../data/eCO2mix_RTE_energie_A.xls', sep='\t', encoding = "ISO-8859-1")


# In[33]:

df.drop('Unnamed: 40', axis=1, inplace=True)


# In[34]:

df[df.Territoire == 'France'].head()


# In[64]:

df.info()


# ___

# In[41]:

dfM = pd.read_csv('../data/eCO2mix_RTE_energie_M.xls', sep='\t', encoding = "ISO-8859-1")


# In[42]:

dfM.drop('Unnamed: 22', axis=1, inplace=True)


# In[43]:

dfM[dfM.Territoire == 'France'].head()


# In[63]:

dfM.info()


# ___

# In[49]:

df_Fr2012 = pd.read_csv('../data/france/eCO2mix_RTE_Annuel-Definitif_2012.xls', sep='\t', encoding = "ISO-8859-1")


# In[50]:

df_Fr2012.head()


# In[56]:

df_Fr2012.info()


# In[ ]:



