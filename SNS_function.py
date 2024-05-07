import numpy as np

class SNS_data:
    def __init__(self, f, label):
        # note that the measured value is 2**.5 times larger!!! the labview porgram should be modified at some point
        self.PSD = f[label][:]
        self.factor = get_factor(f, label)
        self.field = f[label].attrs['field(Gs)']

        self.wl = f[label].attrs['wavelength(nm)']
        self.T = f[label].attrs['Temperature (K)']
        self.sig_V0 = f[label].attrs['V0/2 in scope (mV)'] # mind the diffence (possible?) with MOKE program
        self.sr = f[label].attrs['sample rate(MHz)']*1e6
        self.label = label

class P_data:
    def __init__(self, f, label):
        self.P = f[label][:]
        self.T = f[label].attrs['T (K)']
        self.label = label

def get_property(SNS_data, prop_name):
    try:
        prop_list = []
        for datum in SNS_data:
            prop_list.append(datum.__dict__[prop_name])
        return np.array(prop_list)

    except:
        return datum.__dict__[prop_name]

def get_factor(f, name):
    '''
    Pick out the actual strength of laser(/V)--MTY
    '''
    # 200 Newport 1807 (80MHz)\
    if f[name].attrs['mode'] == '200':
        correction = (2)*2

    # 100 = Thorlabs PD210A (1MHz) monitor + no real-time DC (I noise, no 2)
    # 102 Thorlabs PD210A (1MHz) monitor + no real-time DC +  Dual\
    elif f[name].attrs['mode'] == '100':
        correction = (1/10*1.5)
    elif f[name].attrs['mode'] == '102':
        correction = (1/10*1.5)*2
    
    # 101 Thorlabs PD210A (1MHz) RF output + no real-time DC\
    # 103 Thorlabs PD210A (1MHz) RF(monitor- blocked) + no real-time DC\
    elif f[name].attrs['mode'] == '101':
        correction = (30*(1/300*100))*2
    elif f[name].attrs['mode'] == '103':
        correction = 30*(1/300*100)

    else:
        # print(f"{f[name].attrs['mode']} not considered in get_factor(f, name) yet")
        if f[name].attrs['mode'] == '111':
            correction = (30*(1/300*100))*2
            return correction
        else:
            print(f"{f[name].attrs['mode']} not considered in get_factor(f, name) yet")

    return f[name].attrs['V0/2 in scope (mV)']/1e3*correction

### note: if the value in oscilloscope is divided directly in Labview, then only "correction" need to be considered!


### fitting
def lorentzian_0(x, a, FWHM):
    return a*FWHM**2 / (FWHM**2 + 4*(x)**2 )
    # return a*FWHM**2 / (FWHM**2 + 4*(x)**2 )

def power_law(f, m, f0, a):
    return a*(f + f0)**m

def inverse_power_law(f, m, f0, a):
    return a/(f + f0)**m

def inverse_power_law_P(m, f0, a):
    return a/f0**(m-1)/(m-1)