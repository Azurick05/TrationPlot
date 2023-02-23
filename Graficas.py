import matplotlib.pyplot as plt
import pandas as pd

def Ensayo_Traccion(archivo):
    
    f = pd.read_excel(archivo)
    
    F = f[f.columns[0]].values
    d = f[f.columns[1]].values
    
    
    if d[0] > 0:
        def_0 = abs(d[0])
    else:
        def_0 = d[0]
    
    for i in range(len(d)):
        d[i] = (d[i] - def_0)
        F[i] = F[i]/1000
    
    return F,d




def Graf(F,d,name):
    
    for i in range(len(F)):
        if F[i] == max(F):
            m = d[i]
    
    plt.plot(d,F,color="#557087", label=("Max Strees = {} KN").format(round(max(F),2)))
    plt.bar(m,max(F), color = "#d6dee5ff", width=0.5, label=("Strain = {} mm").format(round(m,2)))
    plt.grid()
    
    plt.legend(fontsize=11)
    plt.title(name, fontsize=14)
    plt.xlabel("Strain [mm]", fontsize=12)
    plt.ylabel("Stress [KN]", fontsize=12)
    plt.xlim(0)
    plt.ylim(0)
    

Feb1 = "ARUS-23-02-23-1.xlsx"
Feb2 = "ARUS-23-02-23-2.xlsx"
Feb3 = "ARUS-23-02-23-3.xlsx"


F,d = Ensayo_Traccion(Feb3)
Graf(F, d, "23/02/2023 - 3")
