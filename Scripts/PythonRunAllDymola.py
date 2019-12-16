#!/usr/bin/env python
# coding: utf-8

# In[12]:


import platform
from dymola.dymola_interface import DymolaInterface
from dymola.dymola_exception import DymolaException
from modelicares import SimRes
import pandas as pd
import numpy as np
import os
import shutil
from subprocess import Popen


# In[ ]:


#This is intended to be used in the manuelnvro Dell using Dymola 2020


# In[13]:


#Run Exciters
print('Exciters Testing ----------------------------------------')
try:
    os.chdir(f"/home/manuelnvro/dev/Gitted/PythonTesting/Scripts/")
    os.system('PythonExcitersDymola.py')
    print('Exciters Testing OK...')
except:
    print('Error in Exciters Testing')

