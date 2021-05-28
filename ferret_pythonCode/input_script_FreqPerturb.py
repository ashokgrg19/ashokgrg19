import numpy as np

input_directory = '/home/ashokgrg19/projects/ferret_output/BSTO/3D/trial/'
#out_directory='/home/ashokgrg19/projects/ferret_output/BSTO/3D/Frequency_response/213K/delta_func/x_06_dx_02/r4_k2'
out_directory='/mnt/hpc_uconn/projects/ferret_output/BSTO/2D/Frequency_response/290K/SDfourier_func/x_04_dx_01-04_l03/seed_vari1/'
#seed=np.linspace(1,25,25,endpoint=True).astype(int)
#Temp=293
N=60                                         # number of points in frequency space to sample

#def_temp=[355, 360, 365, 370, 375, 380, 385, 390, 395, 400]
#def_temp=[270,275,280]
dx=[0.2,0.3,0.4]
seed=np.linspace(1,25,25,endpoint=True).astype(int)
#lamda=['2.1','2.2','2.3','2.4','2.6','2.7','2.8','2.9']
#lamda=['3.6','3.7','3.8','3.9','4.0']
lamda=0.3
#dx=0.1
x=0.4
def_temp=290
def_concFold='x_04_dx_01-04_l03'
def_TempFold='290K'
freq_vec = np.logspace(8.00,14.00,N)          # frequencies to sample. Ondrejkovic studies 2.5 GHz to 20 THz (gamma dependent!!).
                                             # We may be able to push this in Ferret but maybe not wise.
#freq_vec = np.logspace(9.25,13.5,N)
step_vec = np.logspace(-6.50,-12.50,N)                                         # Sub-GHZ frequencies are tricky and perhaps not worth it.


#step_vec = np.logspace(-6.25,-11,N)          # modifier to find time step.
                                             # In general, higher frequencies require smaller time steps.
                                             # However, lower frequencies also require a large number of steps
                                             # in the cycle than higher frequencies on a log scale.

                          # electrostatic potential amplitude (volts)

num_cycles = 12                             # number of cycles to fit (seems OK)

cycle_period = np.zeros((N,1))
dtstep = np.zeros((N,1))
numsteps = np.zeros((N,1))

for l in range(0,N):
    cycle_period[l][0] = (2.0*np.pi)/freq_vec[l]
    grid = freq_vec[l]*step_vec[l]          # number of FEM grid points in time per one cycle of
                                            # induced polarization. This implies that each simulation
                                            # must have different size of time steps!
                                            # Not sure what the "optimum" number of points for a good
                                            # fit is. Can be reduced to speed up simulation
    dtstep[l][0] = (cycle_period[l][0]/grid)

    numsteps[l] = grid*num_cycles# numberof time steps in MOOSE/Ferret
for t in range(0,len(dx)):
    for i in range(0,len(seed)):
        for k in range(0,len(freq_vec)):
            with open(input_directory+'pert_domainSDfourier_hpc_2D_seedVari.i', 'r') as file :
                filedata = file.read()
            nst = np.rint(numsteps[k][0])
            # Replace the target string
            filedata = filedata.replace('freq = def_freq','freq = %s' % freq_vec[k])
            filedata = filedata.replace('diffSeed','seed{}'.format(seed[i]))
            filedata = filedata.replace('defL','l{}'.format(lamda))
            filedata = filedata.replace('seed = def_seed','seed = %s' % seed[i])
            filedata = filedata.replace('def_temp','{}'.format(def_temp))
            filedata = filedata.replace('def_l','{}'.format(lamda))
            filedata = filedata.replace('def_dx','{}'.format(dx[t]))
            filedata = filedata.replace('def_x','{}'.format(x))
            filedata = filedata.replace('dt = def_time','dt = %s' % dtstep[k][0])
            filedata = filedata.replace('num_steps = def_steps','num_steps = %s' % nst)
            filedata = filedata.replace('def_concFold','{}'.format(def_concFold))
            filedata = filedata.replace('def_TempFold','{}'.format(def_TempFold))
            filedata = filedata.replace('def_out','out_perturbBSTO_SDfourier_T{}K_seed{}_x_04_dx_{}_l{}_freq{}'.format(def_temp,seed[i],dx[t],lamda,k))

            # Write the file out again
            with open(out_directory+'input_file/perturbBSTODomain_SDfourier_T{}K_seed{}_x_04_dx_{}_l{}_freq{}.i'.format(def_temp,seed[i],dx[t],lamda,k), 'w') as file:
                file.write(filedata)

np.savetxt(out_directory+"out_file/csvfile/frequencies.csv", freq_vec, delimiter=",")
