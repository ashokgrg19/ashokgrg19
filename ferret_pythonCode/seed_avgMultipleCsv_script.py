from glob import glob
import pandas as pd
#lamda=[2.1,2.2,2.3,2.4,2.6,2.7,2.8,2.9]
#lamda=[3.1,3.2,3.3,3.4]
#lamda=[3.6,3.7,3.8,3.9,4.0]
temp=[0.2,0.3,0.4]
#temp=[355,360,365,370,375,380,385,390,395,400]
#temp=[305,310,315,320,325,330,335,340,345,350]
for T in range(0, len(temp)):

    # getting a list of all the csv files' path
    filenames = glob('dx{}/*csv'.format(temp[T]))

    #new_colName=["chi_real1","chi_imag1","chi_real2","chi_imag2","chi_real3","chi_imag3"]
    new_colName=[]
    for lis in range(len(filenames)):
        real_val="chi_real{}".format(lis)
        img_val="chi_imag{}".format(lis)
        new_colName.append(real_val)
        new_colName.append(img_val)
    new_colVal=[]
    new_colDict={}
    #df_freq=pd.read_csv("new_freq/frequencies.csv")
    df_freq=pd.read_csv("../csvfile/frequencies.csv",usecols=[0],names=["freq"],header=None)
    #print((df_freq["freq"]))

    for file in filenames:
        df=pd.read_csv(file)
        new_colVal.append(df["chi_real"])
        new_colVal.append(df["chi_imag"])
    for i in range(len(new_colName)):
        new_colDict[new_colName[i]]=new_colVal[i]
    df1 = pd.DataFrame(new_colDict, columns = new_colName)
    df1["avg_chiReal"]= " "
    df1["avg_chiImag"]= " "
    df1["total_chiReal"]=0
    df1["total_chiImag"]=0
    for i in range(len(filenames)):
        df1["total_chiReal"]+=abs(df1["chi_real{}".format(i)])
        df1["total_chiImag"]+=abs(df1["chi_imag{}".format(i)])
        df1["avg_chiReal"]=df1["total_chiReal"]/len(filenames)
        df1["avg_chiImag"]=df1["total_chiImag"]/len(filenames)
        #print(abs(df1["chi_real{}".format(i)]))
    df1["freq"]=df_freq["freq"]
    #df1.head
    #plt.scatter(df1["avg_chiReal"],df1["avg_chiImag"])
    #plt.xscale("log")
    cols_to_keep=['freq','avg_chiReal','avg_chiImag']
    df1.loc[:, cols_to_keep].to_csv('FittedAvg_BSTO(2D)_x_04_dx_{}_l3_T300K.csv'.format(temp[T]))
