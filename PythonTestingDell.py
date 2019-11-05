import platform
from dymola.dymola_interface import DymolaInterface
from dymola.dymola_exception import DymolaException
from modelicares import SimRes
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
dymola = DymolaInterface("/opt/dymola-2020-x86_64/bin64/dymola.sh")
dymola.openModel("/home/manuelnvro/dev/Gitted/PythonTesting/OpenIPSL-master/OpenIPSL/package.mo") #OpenIPSL library
#This is to use with Dell Lab computer with Modelica 2020
try:
    dymola.cd("/home/manuelnvro/dev/Gitted/PythonTesting/WorkingDir")
    resultPath = "/home/manuelnvro/dev/Gitted/PythonTesting/WorkingDir/EXAC1"
    # Call a function in Dymola and check its return value
    result = dymola.simulateModel("OpenIPSL.Examples.Controls.PSSE.ES.EXAC1", 
                                  numberOfIntervals = 5000,
                                 resultFile = resultPath)

    if not result:
        print("Simulation failed. Below is the translation log.")
        log = dymola.getLastErrorLog()
        print(log)
        exit(1)
        
    print("Simulation OK")
    sim = SimRes("/home/manuelnvro/dev/Gitted/PythonTesting/WorkingDir/EXAC1.mat")
    #n = dymola.readTrajectorySize("/home/manuelnvro/dev/Gitted/PythonTesting/WorkingDir/EXAC1.mat")
    #print(n)
    #print("Read OK")
    
    variables = ['Time', 'gENROE.delta','gENROE.PELEC', 'eXAC1_1.EFD','gENROE.SPEED', 'GEN1.V', 'LOAD.V', 'GEN2.V', 'FAULT.V' ]
    
    df_variables = pd.DataFrame([], columns = variables)
    print(df_variables.shape)
    
    for var in variables:
        df_variables.drop(var, axis = 1, inplace = True)
        df_variables[var] = np.array(sim[var].values())
        

    #varnames = {"Time","gENROE.delta","gENROE.PELEC"}
    #print(varnames)
    print("Vars OK")
    
    df_variables.to_csv('data.csv', index = False)
    #trajectories = dymola.readTrajectory("/home/dorads/Documents/Manuel/PythonTesting-master/WorkingDir/EXAC1.mat",  {"Time","gENROE.delta","gENROE.PELEC"}, n)
    #print("Trajectories OK")
    #dymola.DataFiles.writeCSVmatrix("EXAC1.csv",varnames,transpose(trajectories))
    print("Write OK")

    
except DymolaException as ex:
    print(("Error: " + str(ex)))
finally:
    pass
    #if dymola is not None:
        #dymola.close()
        #dymola = None