import matplotlib.pyplot as plt
import pandas as pd


#%%

def Ensayo_Traccion(archivo):
    
    f = pd.read_excel(archivo)
    
    t = f[f.columns[0]].values
    d = f[f.columns[1]].values
    F = f[f.columns[2]].values
    
    
    if d[0] > 0:
        def_0 = abs(d[0])
    else:
        def_0 = d[0]
    
    for i in range(len(d)):
        d[i] = (d[i] - def_0)
        F[i] = F[i]/1000
    
    
    return t,d,F

def Graficar_1(T,D,F):
    
    for i in range(len(F)):
        if F[i] == max(F):
            d = D[i]
    
    plt.plot(D,F, color="#557087", label=("Max Strees = {} KN").format(round(max(F),2)))
    plt.bar(d,max(F), color = "#d6dee5ff", width=0.05, label=("Strain = {} mm").format(round(d,2)))
    
    plt.title("Steel Tube", fontsize=14)
    plt.xlabel("Strain [mm]", fontsize=12)
    plt.ylabel("Stress [KN]", fontsize=12)
    
    # plt.grid()
    plt.xlim(0)
    plt.ylim(0)
    
    plt.legend(fontsize=11)



def Graficar_3(T,D,F):
    
    for i in range(len(F)):
        if F[i] == max(F):
            d = D[i]
    
    fig = plt.figure(figsize=(7,8.5), constrained_layout=True)
    spec = fig.add_gridspec(2, 2)
    
    ax0 = fig.add_subplot(spec[0, 0])
    ax0.plot(T,D, color = "#0c273dff")
    
    ax0.set_xlabel("Time [sec]")
    ax0.set_ylabel("Strain [mm]")
    ax0.set_ylim(0)

    ax01 = fig.add_subplot(spec[0, 1])
    ax01.plot(T,F, color = "#0c273dff")
    
    ax01.set_xlabel("Time [sec]")
    ax01.set_ylabel("Stress [KN]")
    ax01.set_ylim(0)
    
    
    ax1 = fig.add_subplot(spec[1, :])
    ax1.plot(D,F, color="#557087", label=("Max Strees = {} KN").format(round(max(F),2)))
    
    ax1.bar(d,max(F), color = "#d6dee5ff", width=0.05)
    
    ax1.set_xlabel("Strain [mm]")
    ax1.set_ylabel("Stress [KN]")
    ax1.set_ylim(0)
    
    ax1.legend()
    
    ax0.grid()
    ax01.grid()
    ax1.grid()

    fig.suptitle('Steel tube')



def Graficar_2(T,D,F, name):
    
    for i in range(len(F)):
        if F[i] == max(F):
            d = D[i]
    
    fig = plt.figure(figsize=(7,8.5), constrained_layout=True)
    spec = fig.add_gridspec(2, 2)
    
    ax0 = fig.add_subplot(spec[0, 0])
    ax0.plot(T,D, color = "#0c273dff")
    
    ax0.set_xlabel("Time [sec]")
    ax0.set_ylabel("Strain [mm]")
    ax0.set_ylim(0)

    ax01 = fig.add_subplot(spec[0, 1])
    ax01.plot(T,F, color = "#0c273dff")
    
    ax01.set_xlabel("Time [sec]")
    ax01.set_ylabel("Stress [KN]")
    ax01.set_ylim(0)
    
    
    ax1 = fig.add_subplot(spec[1, :])
    ax1.plot(D,F, color="#557087", label=("Max Strees = {} KN").format(round(max(F),2)))
    
    ax1.bar(d,max(F), color = "#d6dee5ff", width=0.05)
    
    ax1.set_xlabel("Strain [mm]")
    ax1.set_ylabel("Stress [KN]")
    ax1.set_ylim(0)
    
    ax1.legend()
    
    ax0.grid()
    ax01.grid()
    ax1.grid()

    fig.suptitle(name)

def comparar(D,F):
    
    for i in range(len(D)):
        plt.plot(D[i],F[i], label="Permabond ES Tube {}".format(i+1))
    plt.grid()
    plt.ylim(0)
    
    plt.legend()
    # plt.title("Quick break")
    plt.xlabel("Strain [mm]")
    plt.ylabel("Strees [kN]")

#%%

archivo1 = "Ensayo 1.xlsx"
archivo2 = "Ensayo 2.xlsx"
archivo3 = "Ensayo 3.xlsx"
archivo4 = "Ensayo 4.xlsx"

ES0 = "PermabondES/Probeta0ES.xlsx"
ES1 = "PermabondES/Probeta1ES.xlsx"
ES1H = "PermabondES/Probeta1ES_H.xlsx"
ES2 = "PermabondES/Probeta2ES.xlsx"
ES2H = "PermabondES/Probeta2ES_H.xlsx"


ETL = "PermabondET/Carbono_liso.xlsx"
ETLH = "PermabondET/Carbono_liso_H.xlsx"

Liso_2 = "Liso/FC_liso_2.xlsx"
Pablo_1 = "Liso/FC_Pablo_1.xlsx"

T=[]
D=[]
F=[]

# T1,D1,F1 = Ensayo_Traccion(ETL)
# T2,D2,F2 = Ensayo_Traccion(ETLH)

# F.append(F1)
# F.append(F2)

# D.append(D1)
# D.append(D2)

# comparar(D, F)

T1,D1,F1 = Ensayo_Traccion(Pablo_1)

Graficar_2(T1,D1,F1,"Pablo_1")
