from glob import glob
import pandas as pd
#lamda=[2.1,2.2,2.3,2.4,2.6,2.7,2.8,2.9]
#lamda=[3.1,3.2,3.3,3.4]
#lamda=[3.6,3.7,3.8,3.9,4.0]
temp1=[250,255,260,265,285,290,295,300]
temp3=[355,360,365,370,375,380,385,390,395,400]
temp2=[305,310,315,320,325,330,335,340,345,350]
filenames = 'FittedAvg_BSTO(2D)_x_04_dx_01_l3_T{}K.csv'
temp=temp1+temp2+temp3
li=[]
for T in range(0,len(temp)):
    df = pd.read_csv(filenames.format(temp[T]), index_col=None, header=0)
    li.append(df.iloc[50])

df=pd.DataFrame(li,columns =['freq', 'avg_chiReal',
                         'avg_chiImag'])
df['temp']=temp
df.to_csv('TEST/FittedAvg_BSTO(2D)_x_04_dx_01_l3_TempVari_Freq1.22e13.csv')
