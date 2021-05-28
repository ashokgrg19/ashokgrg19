file_name = 'csvfile/out_perturbBSTO_SDfourier_T300K_seed{}_x_04_dx_{}_l03_freq{}.csv'
#fit_para = []
seed_num=[1,18,50,133,250,363,370,406]
#seed_=[]
#temp=[250,255,260,265,270,275,280,285,290,295,300]
temp=[0.2,0.3,0.4]
#temp=[355,360,365,370,375,380,385,390,395,400]
#temp=[305,310,315,320,325,330,335,340,345,350]
#lamda=[3.6,3.7,3.8,3.9,4.0]
Eamp= 0.00012499999999940637
for T in range(0, len(temp)):
    seed=np.linspace(1,25,25,endpoint=True).astype(int)
    for s in range(1,26):
        fit_para = []
        for f in range(0, len(lis)):
            df=pd.read_csv(file_name.format(s,temp[T],f))
            df_1=df.iloc[50:]
            t=np.array(df_1["time"])
            p_y=np.array(df_1["avePy"])
            def model(x,a,b,c):
                return a*np.sin(lis[f]*x+b)+c
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

            fit_para.append([lis[f],p_fit,theta_fit,chi_real,chi_imag])
            #seed_num.append(i)
            #plt.plot(t,data_fit,"b--",label="Fitted Polarization Curve")
            #plt.plot(t,p_y,"ok",label="Actual Polarization Curve")
            #plt.legend(["Fitted Polarization Curve","Actual Polarization Curve"])
            #plt.savefig('out_perturbDomain_seed1_293K_x_0.4_dx_0.025_l_1.0_f{}_amp_0.02.png'.format(f))
            #fine_t=np.arrange(0,max(t),0.1)
            #data_fit=est_amp*np.sin(1e11*fine_t+est_phase)
            #seed_num.append(i)
        #df_fit_para = pd.DataFrame(data=fit_para, columns=["freq","seed num","p_fit","theta_fit","chi_real","chi_imag"])
        #df_fit_para
        df_fit_para = pd.DataFrame(data=fit_para, columns=["freq", "p_fit","theta_fit","chi_real","chi_imag"])
        df_fit_para.to_csv("Fitted_params/dx{}/Fitted_params_BSTO_SDfourier_seed{}_2D_300K_x_04_dx_{}_l03_amp_1e-3.csv".format(temp[T],s,temp[T]))
