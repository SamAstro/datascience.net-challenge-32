
# coding: utf-8

# # Energies
# **TODO add description**

# In[1]:

# !pip install version_information
get_ipython().magic('load_ext version_information')
get_ipython().magic('reload_ext version_information')
get_ipython().magic('version_information numpy, scipy, matplotlib, pandas')


# In[2]:

get_ipython().magic('matplotlib inline')
get_ipython().magic("config InlineBackend.figure_format='retina'")


# In[3]:

from IPython.display import IFrame, HTML, YouTubeVideo
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.pyplot import GridSpec
import seaborn as sns
import numpy as np


# In[4]:

import pandas as pd
import os, sys
import warnings

sns.set();
plt.rcParams['figure.figsize'] = (12, 8)
sns.set_style("darkgrid")
sns.set_context("poster", font_scale=1.3)

warnings.filterwarnings('ignore')


# In[5]:

pd.set_option('display.max_rows', 99)
pd.set_option('display.max_columns', 999)


# In[6]:

#!conda install qgrid -y

#import qgrid # Put imports at the top
#qgrid.nbinstall(overwrite=True)


# ## Energie annuelle

# In[6]:

df = pd.read_csv('../data/eCO2mix_RTE_energie_A.xls', sep='\t', encoding = "ISO-8859-1")


# In[7]:

df.drop('Unnamed: 40', axis=1, inplace=True)


# In[8]:

df[df.Territoire == 'France'].head()


# In[9]:

df.info()


# ## Energie Mensuelle

# In[10]:

dfM = pd.read_csv('../data/eCO2mix_RTE_energie_M.xls', sep='\t', encoding = "ISO-8859-1")


# In[11]:

dfM.drop('Unnamed: 22', axis=1, inplace=True)


# In[12]:

dfM[dfM.Territoire == 'France'].head()


# In[13]:

dfM.info()


# In[ ]:



