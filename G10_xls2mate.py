import pandas as pd

FILE = "FILE.xlsx"


f = open("text.txt","w")

df_ms = pd.read_excel(FILE,sheet_name="マルチスプリング要素",header=9)
df_li = pd.read_excel(FILE,sheet_name="線形平面要素",header=9)
df_jo = pd.read_excel(FILE,sheet_name="ジョイント要素",header=9)

#マルチスプリング要素
f.write("#マルチスプリング要素\n")
for i in df.index:
    col1 = df_ms.iloc[i][["MA","IEL","XHED"]].tolist()
    col2 = df_ms.iloc[i][["SIGM0","G0","PMG","RK0","PMK","POI","AA","BB"]].tolist()
    col3 = df_ms.iloc[i][["RHO","PN","WKF","WIDTH","L","JOINTS","LR","IAABB","FAABB","IUST","KILL"]].tolist()
    col4 = df_ms.iloc[i][["HMAX","IS12","ITAU","TAU1","DTAU","IRYL","ALPHAE","BETAE","NSPR4","IGKSW"]].tolist()
    col5 = df_ms.iloc[i][["COH","PHIF","PHIP","S1","W1","P1","P2","C1"]].tolist()
    col6 = df_ms.iloc[i][["ITMP3","ITERMD","STOL","SUS"]].tolist()

    text = "{:>5}{:>5} {}\n".format(*col1)
    text += "#----SIGM0--------G0-------PMG-------RK0-------PMK-------POI--------AA--------BB\n"
    text += "{:>10.1f}{:>10.3E}{:>10.3f}{:>10.3E}{:>10.3f}{:>10.1f}{:>10}{:>10}\n".format(*col2)
    text += "#------RHO--------PN-------WKF-----WIDTH----L-JOIN---LR--IAB-----FAABB-IUST-KILL\n"
    text += "{:>10.3f}{:>10.2f}{:>10.1E}{:>10}{:>5}{:>5}{:>5}{:>5}{:>10.1f}{:>5}{:>5}\n".format(*col3)
    text += "#-----HMAX-IS12-ITAU------TAU1------DTAU-NEXT-IRYL----ALPHAE-----BETAE-NSPR-IGKS\n"
    text += "{:>10.3f}{:>5}{:>5}{:>10.2f}{:>10.4f}{:>5}    1{:>10.3E}{:>10.3E}{:>5}{:>5}\n".format(*col4)
    text += "#------COH------PHIF------PHIP--------S1--------W1--------P1--------P2--------C1\n"
    text += "{:>10.3E}{:>10.1f}{:>10.1f}{:>10.3f}{:>10.2f}{:>10.1f}{:>10.1f}{:>10.2f}\n".format(*col5)
    text += "#TMP3-ITER------STOL-----PHIP2--------------------------------SUS---------------\n"
    text += "{:>5}{:>5}{:>10.1E}{:>45.1f}\n".format(*col6)
    text += "#-------------------------------------------------------------------------------\n"
    f.write(text)
    text = ""

f.write("#線形平面要素\n")
for i in df2.index:
    col1 = df_li.iloc[i][["MA","IEL","XHED"]].tolist()
    col2 = df_li.iloc[i][["E","POI","RHO","L","JOINTS","LR","WIDTH","IUST","IRYL","KILL"]].tolist()
    col3 = df_li.iloc[i][["ALPHAE","BETAE"]].tolist()
    text = "{:>5}{:>5} {}\n".format(*col1)
    text += "#--------E-------POI-------RHO----L-JOIN---LR-----WIDTH-IUST-IRYL-KILL------NEXT\n"
    text += "{:>10.3E}{:>10.3f}{:>10.3f}{:>5}{:>5}{:>5}{:>10}{:>5}{:>5}{:>5}         1\n".format(*col2)
    text += "#---ALPHAE-----BETAE------------------------------------------------------------\n"
    text += "{:>10.3E}{:>10.3E}\n".format(*col3)
    text += "#-------------------------------------------------------------------------------\n"
    f.write(text)
    text = ""

f.write("#ジョイント要素\n")    
for i in df4.index:
    col1 = df_jo.iloc[i][["MA","IEL","XHED"]].tolist()
    col2 = df_jo.iloc[i][["TKN","TKS","CJ","PHIJ","ITYP","ISNTYP","AA","BB"]].tolist()
    col3 = df_jo.iloc[i][["WIDTH","IAABB","FAABB","IRYL","ALPHAE","BETAE","IUSS","IUSN","KILL"]].tolist()
    text = "{:>5}{:>5} {}\n".format(*col1)
    text += "#------TKN-------TKS---------C-------PHI-ITYPISNTP------NEXT--------AA--------BB\n"
    text += "{:>10.1E}{:>10.1E}{:>10.3E}{:>10.1f}{:>5}{:>5}         1{:>10.3f}{:>10.1f}\n".format(*col2)
    text += "#----WIDTHIAABB-----FAABB-IRYL----ALPHAE-----BETAE-IUSS-IUSN-KILL\n"
    text += "{:>10.3f}{:>5}{:>10.1f}{:>5}{:>10.3E}{:>10.3E}{:>5}{:>5}{:>5}\n".format(*col3)
    text += "#-------------------------------------------------------------------------------\n"
    f.write(text)
    text = ""

f.close()

