
folder="L = "
conc=["TM","LM"]
r=["0","10"]
k=["0","10"]
#corlen = 1.0
delta_x=["0","01"]
#freq = ("1e8","1e9","1e10","1e11","1e12","1e13")
lamda3=[3.6,3.7,3.8,3.9,4.0]
lamda2=[3.1,3.2,3.3,3.4]
lamda1=[2.1,2.2,2.3,2.4,2.6,2.7,2.8,2.9]
freq=('1','2.4','2.5','2.6','3','4.0')
#freq=('3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9','4.0')
#freq=('250','255','260','265','270','275','280','285','290','295','300')
#freq=('0.2','0.3','0.4')
#freq=('270','275','280')
#freq=('355','360','365','370','375','380','385','390','395','400')
#freq=('305','310','315','320','325','330','335','340','345','350')
#freq=('250','260','265','290','300','320','340','360','380','400')
Temp=('00','01')
#Temp=('240K','260K')
#Temp=('280K','293K','320K')
file_name="FittedAvg_BSTO(2D)_x_04_dx_01_l{}_T260K.csv"
#path =


for i in range(0,len(freq)):
    df=pd.read_csv(file_name.format(freq[i]))
    fig0=plt.figure(num=0,figsize=(8,5))
    ax0=fig0.add_axes([0, 0, 1, 1])
# Edit the major and minor ticks of the x and y axes
    ax0.xaxis.set_tick_params(which='major', size=12, width=2, direction='in')
    ax0.xaxis.set_tick_params(which='minor', size=8, width=2, direction='in')
    ax0.yaxis.set_tick_params(which='major', size=10, width=2, direction='in',right="on")
    ax0.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in',right="on")
    plt.xscale("log")
    #ax0.set_xlabel(r'$\omega $', labelpad=10)
    ax0.set_xlabel(r'$ \omega $', labelpad=10)
#ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator())
#ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator())
    #ax0.yaxis.set_major_locator(mpl.ticker.MultipleLocator(2))
    #ax0.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))
    #ax0.scatter(df["freq"],abs(df["chi_real"]),linewidth=1,label = folder + Temp[i])
    #ax.scatter(df_fit_para["freq"],df_fit_para["chi_imag"], linewidth = 3 ,label="imag")
    ax0.scatter(df["freq"],abs(df["avg_chiReal"]),linewidth=1,label = folder + freq[i]+'nm')
    ax0.set_ylabel(r'$\chi^{\prime} $', labelpad = 10)
    plt.title(" $\chi ^{'} \  vs \ \omega $ (2D)_BSTO at x = 0.4, dx=0.1 T=260K diff_L")
    plt.legend(loc='upper right', prop={'size': 18})
    ax0.grid(True,color='k',linestyle='--', linewidth=2)
    fig0.savefig('TEST/Chi(real)_vs_omega_2D_BSTO_SDfourier x = 0.4, dx=0.1,T260K diff_L.png', dpi=300, transparent=False, bbox_inches='tight')

    fig1=plt.figure( num=1,figsize=(8,5))
    ax=fig1.add_axes([0, 0, 1, 1])
# Edit the major and minor tis of the x and y axes
    ax.xaxis.set_tick_params(which='major', size=12, width=2, direction='in')
    ax.xaxis.set_tick_params(which='minor', size=8, width=2, direction='in')
    ax.yaxis.set_tick_params(which='major', size=10, width=2, direction='in',right="on")
    ax.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in',right="on")
    plt.xscale("log")
    ax.set_xlabel(r'$\omega $', labelpad=10)
#ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator())
#ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator())
    #ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1000))
    #ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(500))
    ax.scatter(df["freq"],abs(df["avg_chiImag"]),linewidth=1, label = folder + freq[i]+'nm')
    #ax.scatter(df_fit_para["freq"],df_fit_para["chi_imag"], linewidth = 3 ,label="imag")
    ax.set_ylabel(r'$\chi^{\prime\prime} $', labelpad = 10)
    plt.title(" $\chi ^{''} \  vs \  \omega$ (2D) BSTO at x = 0.4,dx=0.1 T=260K diff_L")
    ax.grid(True,color='k',linestyle='--', linewidth=2)
    plt.legend(loc='upper right', prop={'size': 18})
    fig1.savefig('TEST/Chi(imag)_vs_omega_seed1_2D_BSTO_SDfourier diff seed at x = 0.4, dx=0.1 T260K diff_L.png', dpi=300, transparent=False, bbox_inches='tight')

    fig2=plt.figure( num=2,figsize=(8,5))
    ax2=fig2.add_axes([0, 0, 1, 1])
# Edit the major and minor ticks of the x and y axes
    ax2.xaxis.set_tick_params(which='major', size=12, width=2, direction='in')
    ax2.xaxis.set_tick_params(which='minor', size=8, width=2, direction='in')
    ax2.yaxis.set_tick_params(which='major', size=10, width=2, direction='in',right="on")
    ax2.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in',right="on")
    #plt.xscale("log")
    ax2.set_xlabel(r'$\chi ^{\prime} $', labelpad=10)
#ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator())
#ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator())
    #ax2.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1000))
    #ax2.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(500))
    ax2.scatter(abs(df["avg_chiReal"]),abs(df["avg_chiImag"]),linewidth=1, label = folder + freq[i]+'nm')
    #ax.scatter(df_fit_para["freq"],df_fit_para["chi_imag"], linewidth = 3 ,label="imag")
    ax2.set_ylabel(r'$\chi^ {\prime\prime} $', labelpad = 10)
    plt.title("$\chi ^{''} \  vs \  \chi ^{'}$ (2D)  BSTO at x = 0.4,dx=0.1 T260K diff_L")
    ax2.grid(True,color='k',linestyle='--', linewidth=2)
    plt.legend(loc='right', prop={'size': 18})
    fig2.savefig('TEST/Chi(imag)_vs_Chi(real)_2D_BSTO_SDfourier diff seed at x = 04, dx=dx=0.1 T260K diff_L.png', dpi=300, transparent=False, bbox_inches='tight')
plt.show()
