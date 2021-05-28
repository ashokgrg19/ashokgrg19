df=pd.DataFrame(lis,columns =['freq','p_fit','theta_fit','chi_real', 'chi_imag'])
totReal=0
totImag=0
df["chi_realAvg"]=" "
df["chi_imagAvg"]=" "
df["num_seed"]=" "
for i in range(0,len(df)):
    totReal+=df["chi_real"].iloc[i]
    df["chi_realAvg"].iloc[i]=abs((totReal))/(i+1)
    totImag+=df["chi_imag"].iloc[i]
    df["chi_imagAvg"].iloc[i]=(totImag)/(i+1)
    df["num_seed"].iloc[i]=1+i
df1=df.reset_index(drop=True)
#print(df1)
df2=df1.iloc[[10,20,30,40,50,60,70,79]]
df2.to_csv("Diff_seed_averaging_x_04_dx_01_l3_T280K.csv")
df2
