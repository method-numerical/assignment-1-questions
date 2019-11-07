import numpy as np
import matplotlib.pyplot as ml
from scipy.constants import h,k,c

"""
plotting black body spectrum at T=2.725.

"""
def spectrum(x):
    T=2.725
    y=2*h*c**2*x**5/(np.exp(h*c*x/(k*T))-1)    #x is wave number i.e. 1/lambda.
    return y
x=np.linspace(200,2200,100)                    #x is in m^-1.
ml.plot(x,spectrum(x),label='blackbody spectrum at T=2.725')

"""
reading data from file and plotting.

"""
file="firas_monopole_spec_v1.txt"
frequency=np.loadtxt(file,usecols=[0])
cmb_flux=np.loadtxt(file,usecols=[1])

p=100*frequency                                 #100 nultiplied to convert unit from cm^-1 (given data) to m^-1.
q=10e-7*cmb_flux                                #10e-7 multiplied to convert MJy/sr into corresponding s.i. unit.

ml.plot(p,q,label='data obtained from firas')

ml.xlabel('wave number in m^-1')
ml.ylabel('cmb_flux in W/(m^2 Hz)')
ml.legend()
ml.show()

"""
to find where cmb_flux has peak.

"""
q=np.amax(cmb_flux)                            #it results in maximum value of cmb_flux.
e=np.where(cmb_flux==q)                          #it results in the index of list for which cmb_flux is maximum.
maximum=frequency[e]
lambda_maximum=1/maximum

print('flux is maximum at wavel length=',lambda_maximum,'c.m.')


# after the plot come then close it and see in terminal, for which wave number cmb_flux has a maximun.

#The corresponding wavelength comes out to be 0.18348624 c.m. which is in microwave region.
