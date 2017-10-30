import os
import numpy as np

def get_planets(catalog='tepcat',getMR=True):
    if catalog == 'tepcat':
        print '\t > Getting transiting planets from TOPCAT:'
        if not os.path.exists('allplanets-ascii.txt'):
            os.system('wget http://www.astro.keele.ac.uk/jkt/tepcat/allplanets-ascii.txt')
        Teff,TeffErrU,TeffErrD,FeH,FeHErrU,FeHErrD,M1,M1ErrU,M1ErrD,R1,R1ErrU,R1Errd,logg1,logg1ErrU,logg1ErrD,\
        rho1,rho1ErrU,rho1ErrD,Porb,ecc,eccErrU,eccErrD,sep,sepErrU,sepErrD,M2,M2ErrU,M2ErrD,\
        R2,R2ErrU,R2ErrD,g2 = np.loadtxt('allplanets-ascii.txt',unpack=True,usecols=range(1,33))#(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,\
        #21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38))
        if getMR:
            Merr = (M2ErrU+M2ErrD)/2.
            Rerr = (R2ErrU+R2ErrD)/2.
            return M2,Merr,R2,Rerr,Teff,R1,sep
        else:
            return Teff,FeH,M1,R1,logg1,rho1,Porb,ecc,sep,M2,R2,g2,rho2,Teq
