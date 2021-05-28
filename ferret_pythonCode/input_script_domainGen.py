import numpy as np
import random
#creating domain_structure
input_directory = '/home/ashokgrg19/projects/ferret_output/BSTO/3D/trial/'
#out_directory='/home/ashokgrg19/projects/ferret_output/BSTO/3D/Frequency_response/213K/delta_func/x_06_dx_02/r4_k2'
out_directory='/mnt/hpc_uconn/projects/ferret_output/BSTO/2D/gen_domain/Temp/SDfourier_func/x_04_dx_01-04_l03/seed_vari/290K/input_file/'
#list of random seed
#seed=[406, 370, 133, 363, 746, 36]
#Temp=np.linspace(250,400,31,endpoint=True).astype(int)
dx=[0.2,0.3,0.4]
#lamda=['3.6','3.7','3.8','3.9','4.0']
#lamda=['2.1','2.2','2.3','2.4','2.6', '2.7','2.8','2.9','3.0','3.1','3.2','3.3','3.4','3.5']
lamda=0.3
#dx=0.1
x=0.4
Temp=290
def_TempFold='290K'
def_concFold='x_04_dx_01-04_l03'
#seed=np.linspace(1,25,25,endpoint=True).astype(int)
seed=np.linspace(1,25,25,endpoint=True).astype(int)
#lis=np.linspace(20,400,20,endpoint=True).astype(int
for t in range(0,len(dx)):
    for k in range(0,len(seed)):
        with open(input_directory+'gen_domain_SDfourier_2D_x_04_dx_02_l3_dim8_seedVari.i', 'r') as file :
            filedata = file.read()
        # Replace the target string
        filedata = filedata.replace('def_seed','{}'.format(seed[k]))
        filedata = filedata.replace('def_temp','{}'.format(Temp))
        filedata = filedata.replace('def_l','{}'.format(lamda))
        filedata = filedata.replace('def_dx','{}'.format(dx[t]))
        filedata = filedata.replace('def_x','{}'.format(x))
        filedata = filedata.replace('def_concFold','{}'.format(def_concFold))
        filedata = filedata.replace('def_TempFold','{}'.format(def_TempFold))
        filedata = filedata.replace('def_out','out_genDomain_SDfourier_seed{}_2D_T_{}K_x_04_dx_{}_l{}_dim8'.format(seed[k],Temp,dx[t],lamda))

        # Write the file out again
        with open(out_directory+'gen_domain_SDfourier_seed{}_2D_T{}K_x_04_dx_{}_l{}_dim8.i'.format(seed[k],Temp,dx[t],lamda), 'w') as file:
            file.write(filedata)

    
