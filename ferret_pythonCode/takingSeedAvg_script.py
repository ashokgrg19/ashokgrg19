df1_j=pd.read_csv("csvfile/frequencies.csv",usecols=[0],names=["freq"],header=None)
lis=df1_j["freq"]
file_name = 'out_perturbBSTO_SDfourier_2D_T293K_seed{}_x_04_dx_01_l3_freq3.csv'
fit_para = []
#seed_num=[1,18,36,50,133,250,363,370,406,746,25,411,555,890,3333,4950,8990]
#seed_=[]
lis=[1e8,1e9,1e10,1e11,1e12,1e13]

seed_num=np.linspace(2,61,60,endpoint=True).astype(int)
#1099 80 5050
Eamp= 0.00012499999999940637
for f in range(0, len(seed_num)):
    df=pd.read_csv(file_name.format(seed_num[f]))
    df_1=df.iloc[50:]
    t=np.array(df_1["time"])
    p_y=np.array(df_1["avePy"])
    def model(x,a,b,c):
        return a*np.sin(lis[3]*x+b)+c
    pcons,pcov=curve_fit(model,t,p_y)
    p_fit=pcons[0]
    theta_fit=pcons[1]
    cons=pcons[2]
    #p_fit_1=p_fit+cons
    data_fit=[]
    for i in t:
        data_fit.append(model(i,p_fit,theta_fit,cons))
    #print(leastsq(optimize_func,[guess_amp,guess_phase])[0])
    chi_real= p_fit/(Eamp*eps_0) *np.cos(theta_fit)
    chi_imag= p_fit/(Eamp*eps_0) *np.sin(theta_fit)

    fit_para.append([lis[3],seed_num[f],p_fit,theta_fit,chi_real,chi_imag])
    #seed_num.append(i)
    #plt.plot(t,data_fit,"b--",label="Fitted Polarization Curve")
    #plt.plot(t,p_y,"ok",label="Actual Polarization Curve")
    #plt.legend(["Fitted Polarization Curve","Actual Polarization Curve"])
    #plt.savefig('out_perturbDomain_seed1_293K_x_0.4_dx_0.025_l_1.0_f{}_amp_0.02.png'.format(f))
    #fine_t=np.arrange(0,max(t),0.1)
    #data_fit=est_amp*np.sin(1e11*fine_t+est_phase)
    #seed_num.append(i)
df_fit_para = pd.DataFrame(data=fit_para, columns=["freq","seed num","p_fit","theta_fit","chi_real","chi_imag"])
df_fit_para['chi_real']=-df_fit_para['chi_real']
totReal=0
totImag=0
df_fit_para["chi_realAvg"]=" "
df_fit_para["chi_imagAvg"]=" "
df_fit_para["num_seed"]=" "
for i in range(0,len(df_fit_para)):
    totReal+=df_fit_para["chi_real"].iloc[i]
    df_fit_para["chi_realAvg"].iloc[i]=abs((totReal))/(i+1)
    totImag+=df_fit_para["chi_imag"].iloc[i]
    df_fit_para["chi_imagAvg"].iloc[i]=(totImag)/(i+1)
    df_fit_para["num_seed"].iloc[i]=1+i
df_fit_para    
