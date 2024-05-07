# workflow
## PSD measurement (2cd order correlation)
SNS\labview
- SNS--monitor Barkhausen.vi

subVI
- InitializeScope.vi
- ScopeSettings.vi
- GetData.vi

- electromagnet_ramp.vi (old version: electromagnet.vi)\
    4 modes available:
    - ignore: visa of electromagnet power supply would not be seen
    - True: field alternate between 2 fields
    - False: 
    - Ramp: for Barkhausen measurement

- mode.vi\
    Calculate the correcting factor "DC multiplier" for the real time plots. 
    Note that the saved spectrum is not yet corrected by this factor. This correction is left for python script, in order to keep the raw data "raw".\
    if no real-time DC is measured:
        save raw data\
    elif oscilloscope/Aux measures real-time DC:
        save (raw data)/(raw oscilloscope reading)
    - Oscilloscope Average.vi
    - Oscilloscope DS1000 Average.vi (if the old DS1000 RIGOR scope is used <-- slightly different syntax is used)

- metadata generater.vi\
    Record all experimental conditions one would possibly need in the future and generate a metadata file along with the raw data.



sweeping the field requires:
- C:\Users\C102\Documents\SNS\labview\SNS---sweep B.vi
subVI
- SNS--monitor Barkhausen.vi

some of those subVIs depend on subsubVIs in this file:\
C:\Program Files (x86)\National Instruments\LabVIEW 2019\user.lib\Gage\CsTool.llb\

### input: BNC signal, (oscilloscope DC feedback)
### output: XXX_PSD, XXX_metadata

## h5writter.py
### input: [XXX_PSD, XXX_metadata]
### output: XXX.h5, containing a set of XXX_PSD as dataset, XXX_metadata as attribute

## h5reader.py
### input: XXX.h5
### output: XXX.fig


# measurement type index
## (detetor code) X (real-time DC or not) X (port configuration)
### detetor code
0. Nirvana (125kHz)\
port configuration:\
0 = AutoBAL.\
1 = 10X

1. Thorlabs PD210A (1MHz)\
port configuration:\
0 = mon,\
1 = RF,\
2 = Dual mon

2. Newport (80MHz)\
0 = diff

## examples
200 Newport 1807 (80MHz)\

101 Thorlabs PD210A (1MHz) RF output + no real-time DC\
111 Thorlabs PD210A (1MHz) RF output + monitor DC\
100 Thorlabs PD210A (1MHz) monitor + no real-time DC (I noise, no 2)\
110 Thorlabs PD210A (1MHz) monitor + monitor DC (I noise, no 2)\
102 Thorlabs PD210A (1MHz) monitor + no real-time DC +  Dual\

103 Thorlabs PD210A (1MHz) RF(monitor- blocked) + no real-time DC\

001 Nirvana (125KHz) 10X + no real-time DC\
011 Nirvana (125KHz) 10X + signal monitor DC\

## caution
1. make sure that the factor by which PSD is to be divided must be squared (dimension V^2)!!
2. 


## questions and problems
1. should signals be discrete, with steps ~ MOKE rotation size 100urad?
even if it does, $ \Delta V \approx 2V_0 \Delta\theta = 2\cdot1\cdot100 \mu rad = 0.2 mV$. That is to say, step an hardly be seen.
slope of hysteresis curves gets smaller because the \
Q: it seems that ellipticity signal be much larger!?
ellipticity ~ 2mrad ==> $ \Delta V \approx 2V_0 \Delta\theta = 4 mV$ !!!!
TRY ellipticity noise!!!!

2. well below SRT / well above SRT --> compare with shot noise
imbalance?
record typical size of signal in time domain, does it agree with 
 (1) rotation noise ~ 100urad, (2) ellipticity noise ~ 2mrad??

