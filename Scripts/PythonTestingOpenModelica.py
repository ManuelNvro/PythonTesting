#!/usr/bin/env python
# coding: utf-8

# In[17]:


from OMPython import OMCSessionZMQ
omc = OMCSessionZMQ()
from modelicares import SimRes
import pandas as pd
import numpy as np


# In[ ]:


#This is intended to be used in the manuelnvro Dell using Dymola 2020.


# In[18]:


print(omc.sendExpression("getVersion()"))
print("OpenModelica Simulation Start...")


# In[19]:


#Set WorkigDir
omc.sendExpression("cd(\"/home/manuelnvro/dev/Gitted/PythonTesting/WorkingDir/OpenModelica/\")") 


# In[20]:


#Loading Package
omc.sendExpression("loadFile(\"/home/manuelnvro/dev/Gitted/OpenIPSL/OpenIPSL/package.mo\")")


# In[21]:


#Package Instantiation
omc.sendExpression("instantiateModel(OpenIPSL)")


# In[22]:


#OpenModelica Simulation
omc.sendExpression("simulate(OpenIPSL.Examples.Controls.PSSE.ES.EXAC1, stopTime=10.0, numberOfIntervals=5000)")


# In[23]:


print("Simulation OK")
sim = SimRes("/home/manuelnvro/dev/Gitted/PythonTesting/WorkingDir/OpenModelica/OpenIPSL.Examples.Controls.PSSE.ES.EXAC1_res.mat")
variables = ['Time', 'gENROE.delta','gENROE.PELEC', 'eXAC1_1.EFD','gENROE.SPEED', 'GEN1.V', 'LOAD.V', 'GEN2.V', 'FAULT.V' ]
df_variables = pd.DataFrame([], columns = variables)
for var in variables:
    df_variables.drop(var, axis = 1, inplace = True)
    df_variables[var] = np.array(sim[var].values())
print("Vars OK")
os.chdir("/home/manuelnvro/dev/Gitted/PythonTesting/ResultData/")  
df_variables.to_csv('dataOpenModelica.csv', index = False)
print("Write OK")

