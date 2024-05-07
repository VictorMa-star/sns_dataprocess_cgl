# # data taken at 20211113 is not subtracted by electronic noise before divided by the correction factor which is done in Labview, making it hard for later processing
# # bad habit to be kicked!
# I_noise_raw = [
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 50 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 100 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 202 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 303 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 400 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 500 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 600 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 800 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 900 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 1000 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     # r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 1200 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
    
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 1200 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19200 each field 30 PSD',\
# ]

# I_noise_relevent = [
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 100 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 202 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 303 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 400 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 500 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 600 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 800 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 900 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 1000 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19050 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs mon-mon sr 50M (65565) 700nm halfV0 1200 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19200 each field 30 PSD',\

#     # r'20211113\1112 thorlabs RF-no sr 50M (65565) 700nm halfV0 8550 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19200 each field 30 PSD',\
# ]
# shot_noise = [
#     r'..\20211113\1112 thorlabs RF-no sr 50M (65565) 700nm halfV0 8550 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19200 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs RF-no sr 50M (65565) 700nm halfV0 5600 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19200 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs RF-no sr 50M (65565) no lowpass2.5 700nm halfV0 8550 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19200 each field 30 PSD',\
#     r'..\20211113\1112 thorlabs RF-no sr 50M (65565) no lowpass2.5 700nm halfV0 5600 mV 0.0 G(low) 0.0 G(high) 296.0 K avg 19200 each field 30 PSD',\
# ]


BG_20211118 = [
    r'..\20211118\electronic noise (RF) sr=50M(65536)_filter=None_PSD',\
    r'..\20211118\shot noise sr=50M(65536)_filter=None_PSD',\
    r'..\20211118\intensity noise sr=50M(65536)_filter=None_PSD',\
    r'..\20211118\electronic noise (mon) sr=50M(65536)_filter=None_PSD',\

    r'..\20211118\electronic noise mode=102_filter=None_PSD',\
    r'..\20211118\shot noise mode=102_filter=None_PSD',\
]

BG_20211119 = [
    r'..\20211119\intensity noise 2 mode=100_filter=None_PSD',\
    r'..\20211119\shot noise (weird at 0.8) mode=102_filter=None_PSD',\
    r'..\20211119\shot noise 2 mode=102_filter=None_PSD',\
    r'..\20211119\electronic noise 2 mode=102_filter=None_PSD',\
    r'..\20211119\electronic noise (weird at 20) mode=100_filter=None_0PSD',\
    r'..\20211119\electronic noise 2 mode=100_filter=None_0PSD',\

    r'..\20211119\shot noise mode=102_halfV0(mV)=1000.0_0PSD',\
    r'..\20211119\intensity noise mode=100_halfV0(mV)=1000.0_0PSD',\
    r'..\20211119\shot noise mode=101_halfV0(mV)=1000.0_0PSD',\
    r'..\20211119\intensity noise mode=103_halfV0(mV)=30.0_0PSD',\
    r'..\20211119\electronic noise mode=101_0PSD',\

    r'..\20211119\shot noise (no PBS) mode=101_0PSD',\
    r'..\20211119\intensity noise (no PBS) mode=100_0PSD',\
    r'..\20211119\shot noise (no PBS) mode=102_0PSD',\
]

# intensity_noise = [
#     r'..\20211119\intensity noise 2 mode=100_filter=None_PSD',\ 
#     r'..\20211119\intensity noise mode=100_halfV0(mV)=1000.0_0PSD',\
#     r'..\20211119\intensity noise mode=103_halfV0(mV)=30.0_0PSD',\
#     r'..\20211119\intensity noise (no PBS) mode=100_0PSD',\
# ]

electronic_noise = [
    # r'..\20211118\electronic noise mode=102_filter=None_PSD',\
    # r'..\20211119\electronic noise 2 mode=102_filter=None_PSD',\
    # r'..\20211119\electronic noise (weird at 20) mode=100_filter=None_0PSD',\
    r'..\20211119\electronic noise 2 mode=100_filter=None_0PSD',\
    r'..\20211119\electronic noise mode=101_0PSD',\
]

intensity_noise = [
r'..\20211120\intensity noise mode=100_halfV0(mV)=20.0_0PSD',\
r'..\20211120\intensity noise mode=100_halfV0(mV)=50.0_0PSD',\
r'..\20211120\intensity noise mode=100_halfV0(mV)=100.0_0PSD',\
r'..\20211120\intensity noise mode=100_halfV0(mV)=200.0_0PSD',\
r'..\20211120\intensity noise mode=100_halfV0(mV)=300.0_0PSD',\
r'..\20211120\intensity noise mode=100_halfV0(mV)=500.0_0PSD',\
r'..\20211120\intensity noise mode=100_halfV0(mV)=700.0_0PSD',\
r'..\20211120\intensity noise mode=100_halfV0(mV)=1010.0_0PSD',\
]

shot_noise = [
r'..\20211120\shot noise mode=101_halfV0(mV)=20.0_0PSD',\
r'..\20211120\shot noise mode=101_halfV0(mV)=50.0_0PSD',\
r'..\20211120\shot noise mode=101_halfV0(mV)=100.0_0PSD',\
r'..\20211120\shot noise mode=101_halfV0(mV)=200.0_0PSD',\
r'..\20211120\shot noise mode=101_halfV0(mV)=300.0_0PSD',\
r'..\20211120\shot noise mode=101_halfV0(mV)=500.0_0PSD',\
r'..\20211120\shot noise mode=101_halfV0(mV)=700.0_0PSD',\
r'..\20211120\shot noise mode=101_halfV0(mV)=1010.0_0PSD',\
]

# directory = r'..\20211114'
# files = os.listdir('.')
# files.sort(key=lambda x: os.path.getmtime(x))
# for name in files:
#     if name.find('scale')==-1:
#         print("r'" + directory + f"\{name}'", end=',\ \n')


MLL785 = [
    r'..\20211128\shot nosie MLL mode=102_halfV0(mV)=100.0_0PSD',\
    r'..\20211128\shot nosie MLL mode=102_avg=100_each=64000_halfV0(mV)=100.0_0PSD',\
    r'..\20211128\intensity nosie MLL mode=100_avg=30_each=19200_halfV0(mV)=100.0_0PSD',\
    r'..\20211128\intensity nosie MLL mode=100_avg=100_each=64000_halfV0(mV)=100.0_0PSD',\
]


imbalance_335K = [
    r'..\20211129\sam1-1 site6 imbalance field=[-1000.0, 1000.0]_0PSD',\
    r'..\20211129\sam1-1 site6 imbalance field=[1000.0, -1000.0]_0PSD',\
    r'..\20211129\sam1-1 site6 imbalance 2 field=[-1000.0, 1000.0]_0PSD',\
    r'..\20211129\sam1-1 site6 imbalance 2 field=[1000.0, -1000.0]_0PSD',\
]

SN_rotation_335K = [
    r'..\20211201\sam1-1 site6 field=[-16.0, 30.0]_T=335.0_0PSD',\
    r'..\20211201\sam1-1 site6 field=[-5.0, 15.0]_T=335.0_0PSD',\
    r'..\20211201\sam1-1 site6 field=[-4.0, 15.0]_T=335.0_0PSD',\
    r'..\20211201\sam1-1 site6 field=[-3.0, 15.0]_T=335.0_0PSD',\
    r'..\20211201\sam1-1 site6 field=[-2.0, 15.0]_T=335.0_0PSD',\
    r'..\20211201\sam1-1 site6 field=[-1.0, 15.0]_T=335.0_0PSD',\
    r'..\20211201\sam1-1 site6 field=[0.0, 15.0]_T=335.0_0PSD',\
    r'..\20211201\sam1-1 site6 field=[1.0, 15.0]_T=335.0_0PSD',\
    r'..\20211201\sam1-1 site6 field=[2.0, 15.0]_T=335.0_0PSD',\
    r'..\20211201\sam1-1 site6 field=[3.0, 15.0]_T=335.0_0PSD',\
]

SN_rotation_340K = [
    r'..\20211202\sam1-1 site6 field=[-4.0, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[-3.5, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[-3.0, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[-2.5, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[-2.0, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[-1.5, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[-1.0, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[-0.5, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[0.0, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[0.5, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[1.0, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[1.5, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[2.0, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[2.5, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[3.0, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[3.5, 6.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 field=[4.0, 6.0]_T=340.0_0PSD',\
]

SN_ellipticity_340K = [
    r'..\20211202\sam1-1 site6 E field=[-7.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-6.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-6.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-5.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-5.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-4.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-4.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-0.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[5.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[5.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[6.0, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[6.5, 7.0]_T=340.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[7.0, 7.0]_T=340.0_0PSD',\
]

SN_ellipticity_335K = [
    r'..\20211202\sam1-1 site6 E field=[-4.0, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.9, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.8, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.7, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.6, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.5, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.4, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.3, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.2, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.1, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-3.0, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.9, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.8, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.7, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.6, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.5, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.4, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.3, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.2, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.1, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-2.0, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.9, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.8, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.7, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.6, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.5, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.4, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.3, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.2, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.1, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-1.0, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-0.9, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-0.8, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-0.7, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-0.6, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-0.5, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-0.4, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-0.3, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-0.2, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[-0.1, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.0, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.1, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.2, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.3, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.4, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.5, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.6, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.7, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.8, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[0.9, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.0, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.1, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.2, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.3, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.4, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.5, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.6, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.7, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.8, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[1.9, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.0, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.1, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.2, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.3, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.4, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.5, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.6, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.7, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.8, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[2.9, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.0, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.1, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.2, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.3, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.4, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.5, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.6, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.7, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.8, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[3.9, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.0, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.1, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.2, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.3, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.4, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.5, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.6, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.7, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.8, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[4.9, 5.0]_T=335.0_0PSD',\
    r'..\20211202\sam1-1 site6 E field=[5.0, 5.0]_T=335.0_0PSD',\
]

SN_ellipticity_330K = [
    r'..\20211203\sam1-1 site6 E field=[-2.0, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.9, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.8, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.7, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.6, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.5, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.4, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.3, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.2, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.1, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.0, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.9, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.8, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.7, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.6, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.5, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.4, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.3, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.2, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.1, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.0, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.1, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.2, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.3, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.4, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.5, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.6, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.7, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.8, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.9, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.0, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.1, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.2, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.3, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.4, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.5, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.6, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.7, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.8, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.9, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.0, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.1, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.2, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.3, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.4, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.5, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.6, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.7, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.8, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.9, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.0, 3.0]_T=330.0_0PSD',\
    
    r'..\20211203\sam1-1 site6 E 2 field=[1.1, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E 2 field=[1.2, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E 2 field=[1.3, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E 2 field=[1.4, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E 2 field=[1.5, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E 2 field=[1.6, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E 2 field=[1.7, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E 2 field=[1.9, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E 2 field=[2.0, 3.0]_T=330.0_0PSD',\
    r'..\20211203\sam1-1 site6 E 2 field=[2.1, 3.0]_T=330.0_0PSD',\
]


SN_ellipticity_325K = [
    r'..\20211203\sam1-1 site6 E field=[-2.0, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.9, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.8, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.7, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.6, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.5, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.4, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.3, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.2, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.1, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.0, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.9, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.8, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.7, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.6, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.5, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.4, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.3, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.2, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.1, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.0, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.1, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.2, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.3, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.4, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.5, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.6, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.7, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.8, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.9, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.0, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.1, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.2, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.3, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.4, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.5, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.6, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.7, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.8, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.9, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.0, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.1, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.2, 3.0]_T=325.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.3, 3.0]_T=325.0_0PSD',\
]

SN_ellipticity_345K = [
    # r'..\20211203\sam1-1 site6 E field=[-13.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-12.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-12.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-12.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-12.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-12.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-12.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-12.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-12.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-12.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-12.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-11.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-11.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-11.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-11.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-11.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-11.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-11.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-11.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-11.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-11.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-10.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-10.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-10.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-10.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-10.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-10.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-10.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-10.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-10.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-10.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-9.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-9.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-9.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-9.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-9.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-9.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-9.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-9.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-9.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-9.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-8.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-8.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-8.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-8.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-8.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-8.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-8.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-8.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-8.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-8.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-7.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-7.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-7.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-7.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-7.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-7.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-7.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-7.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-7.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-7.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-6.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-6.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-6.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-6.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-6.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-6.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-6.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-6.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-6.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-6.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-5.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-5.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-5.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-5.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-5.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-5.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-5.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-5.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-5.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-5.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-4.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-4.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-4.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-4.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-4.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-4.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-4.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-4.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-4.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-4.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-3.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-3.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-3.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-3.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-3.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-3.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-3.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-3.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-3.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-3.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-2.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-2.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-2.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-2.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-2.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-2.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-2.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-2.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-2.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-2.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-1.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-1.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-1.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-1.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-1.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-1.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-1.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-1.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-1.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-1.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-0.9, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-0.8, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-0.7, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-0.6, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-0.5, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-0.4, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-0.3, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-0.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[-0.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[0.0, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[0.1, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[0.2, 15.0]_T=345.0_0PSD',\
    # r'..\20211203\sam1-1 site6 E field=[0.3, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.4, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.5, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.6, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.7, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.8, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.9, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.2, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.5, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.8, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.1, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.4, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.7, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.0, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.3, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.6, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.9, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[4.2, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[4.5, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[4.8, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[5.1, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[5.4, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[5.7, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[6.0, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[6.3, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[6.6, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[6.9, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[7.2, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[7.5, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[7.8, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[8.1, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[8.4, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[8.7, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[9.0, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[9.3, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[9.6, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[9.9, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[10.2, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[10.5, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[10.8, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[11.1, 15.0]_T=345.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[11.4, 15.0]_T=345.0_0PSD',\
]


SN_ellipticity_333K = [
    r'..\20211203\sam1-1 site6 E field=[-3.0, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.9, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.8, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.7, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.6, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.5, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.4, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.3, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.2, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.1, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.0, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.9, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.8, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.7, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.6, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.5, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.4, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.3, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.2, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.1, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.0, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.9, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.8, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.7, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.6, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.5, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.4, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.3, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.2, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.1, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.0, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.1, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.2, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.3, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.4, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.5, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.6, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.7, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.8, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.9, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.0, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.1, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.2, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.3, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.4, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.5, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.6, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.7, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.8, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.9, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.0, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.1, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.2, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.3, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.4, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.5, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.6, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.7, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.8, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.9, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.0, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.1, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.2, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.3, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.4, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.5, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.6, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.7, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.8, 4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[3.9, 4.0]_T=333.0_0PSD',\
]


SN_ellipticity_333K_b = [
    r'..\20211203\sam1-1 site6 E field=[2.4, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.2, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[2.0, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.8, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.6, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.4, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.2, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[1.0, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.8, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.6, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.4, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.2, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[0.0, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.2, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.4, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.6, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.8, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.0, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.2, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.4, -4.0]_T=333.0_0PSD',\
]

SN_ellipticity_333K_b2= [
    r'..\20211203\sam1-1 site6 E field=[0.0, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.2, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.4, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.6, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-0.8, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.0, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.2, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.4, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.6, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-1.8, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.0, -4.0]_T=333.0_0PSD',\
    r'..\20211203\sam1-1 site6 E field=[-2.2, -4.0]_T=333.0_0PSD',\
]

SN_ellipticity_315K_site7= [
    r'..\20211206\sam1-1 site7 E field=[-2.0, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-1.9, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-1.8, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-1.7, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-1.6, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-1.5, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-1.4, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-1.3, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-1.2, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-1.1, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-1.0, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-0.9, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-0.8, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-0.7, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-0.6, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-0.5, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-0.4, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-0.3, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-0.2, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[-0.1, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[0.0, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[0.1, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[0.2, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[0.3, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[0.4, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[0.5, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[0.6, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[0.7, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[0.8, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[0.9, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[1.0, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[1.1, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[1.2, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[1.3, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[1.4, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[1.5, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[1.6, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[1.7, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[1.8, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[1.9, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[2.0, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[2.1, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[2.2, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[2.3, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[2.4, 5.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site7 E field=[2.5, 5.0]_T=315.0_0PSD',\
]

SN_ellipticity_315K_site8= [
    r'..\20211206\sam1-1 site8 E field=[-2.0, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.9, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.8, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.7, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.6, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.5, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.4, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.3, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.2, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.1, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.0, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.9, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.8, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.7, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.6, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.5, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.4, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.3, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.2, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.1, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[0.0, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[0.1, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[0.2, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[0.3, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[0.4, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[0.5, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[0.6, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[0.7, 4.0]_T=315.0_0PSD',\

    r'..\20211206\sam1-1 site8 E back field=[0.0, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.3, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.6, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.9, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.2, 4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.5, 4.0]_T=315.0_0PSD',\
]

SN_ellipticity_315K_site8_b = [
    r'..\20211206\sam1-1 site8 E back field=[0.0, -4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.3, -4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.6, -4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.9, -4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.2, -4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.6, -4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.3, -4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.2, -4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.5, -4.0]_T=315.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.9, -4.0]_T=315.0_0PSD',\
]

SN_ellipticity_330K_site8 = [
    r'..\20211206\sam1-1 site8 E field=[-2.8, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-2.6, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-2.4, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-2.2, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-2.0, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.8, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.6, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.4, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.2, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-1.0, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.8, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.6, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.4, 5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E field=[-0.2, 5.0]_T=330.0_0PSD',\
]

SN_ellipticity_330K_site8_b = [
    r'..\20211206\sam1-1 site8 E back field=[3.5, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[3.4, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[3.3, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[3.2, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[3.1, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[3.0, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[2.9, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[2.8, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[2.7, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[2.6, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[2.5, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[2.4, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[2.3, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[2.2, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[2.1, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[2.0, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.9, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.8, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.7, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.6, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.5, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.4, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.3, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.2, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.1, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[1.0, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.9, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.8, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.7, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.6, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.5, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.4, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.3, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.2, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[0.1, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.0, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.1, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.2, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.3, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.4, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.5, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.6, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.7, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.8, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-0.9, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.0, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.1, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.2, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.3, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.4, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.5, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.6, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.7, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.8, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-1.9, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-2.0, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-2.1, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-2.2, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-2.3, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-2.4, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-2.5, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-2.6, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-2.7, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-2.8, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-2.9, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-3.0, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-3.1, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-3.2, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-3.3, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-3.4, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-3.5, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-3.6, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-3.7, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-3.8, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-3.9, -5.0]_T=330.0_0PSD',\
    r'..\20211206\sam1-1 site8 E back field=[-4.0, -5.0]_T=330.0_0PSD',\
]

SN_ellipticity_335K_site8 = [
    # r'..\20211206\sam1-1 site8 E field=[1.0, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[1.1, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[1.2, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[1.3, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[1.4, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[1.5, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[1.6, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[1.7, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[1.8, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[1.9, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[2.0, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[2.1, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[2.2, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[2.3, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[2.4, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[2.5, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[2.6, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[2.7, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[2.8, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[2.9, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[3.0, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[3.1, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[3.2, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[3.3, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[3.4, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[3.5, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[3.6, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[3.7, 7.0]_T=335.0_0PSD',\
    # r'..\20211206\sam1-1 site8 E field=[3.8, 7.0]_T=335.0_0PSD',\

r'..\20211206\sam1-1 site8 E field=[3.9, 7.0]_T=335.0_0PSD',\
r'..\20211206\sam1-1 site8 E field=[4.0, 7.0]_T=335.0_0PSD',\
r'..\20211206\sam1-1 site8 E field=[4.1, 7.0]_T=335.0_0PSD',\
r'..\20211206\sam1-1 site8 E field=[4.2, 7.0]_T=335.0_0PSD',\
r'..\20211206\sam1-1 site8 E field=[4.3, 7.0]_T=335.0_0PSD',\
r'..\20211206\sam1-1 site8 E field=[4.4, 7.0]_T=335.0_0PSD',\
r'..\20211206\sam1-1 site8 E field=[4.5, 7.0]_T=335.0_0PSD',\
]

SN_ellipticity_335K_site6_1 = [
    r'..\20211206\sam1-1 site6_1 E field=[-3.0, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-2.9, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-2.8, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-2.7, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-2.6, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-2.5, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-2.4, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-2.3, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-2.2, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-2.1, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-2.0, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-1.9, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-1.8, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-1.7, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-1.6, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-1.5, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-1.4, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-1.3, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-1.2, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-1.1, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-1.0, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-0.9, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-0.8, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-0.7, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-0.6, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-0.5, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-0.4, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-0.3, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-0.2, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[-0.1, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[0.0, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[0.1, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[0.2, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[0.3, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[0.4, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[0.5, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[0.6, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[0.7, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[0.8, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[0.9, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[1.0, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[1.1, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[1.2, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[1.3, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[1.4, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[1.5, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[1.6, 6.0]_T=335.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 E field=[1.7, 6.0]_T=335.0_0PSD',\
]


SN_ellipticity_333K_site6_1 = [
    # r'..\20211206\sam1-1 site6_1 field=[-3.0, 5.0]_T=333.0_0PSD',\
    # r'..\20211206\sam1-1 site6_1 field=[-2.9, 5.0]_T=333.0_0PSD',\
    # r'..\20211206\sam1-1 site6_1 field=[-2.8, 5.0]_T=333.0_0PSD',\
    # r'..\20211206\sam1-1 site6_1 field=[-2.7, 5.0]_T=333.0_0PSD',\
    # r'..\20211206\sam1-1 site6_1 field=[-2.6, 5.0]_T=333.0_0PSD',\
    # r'..\20211206\sam1-1 site6_1 field=[-2.5, 5.0]_T=333.0_0PSD',\
    # r'..\20211206\sam1-1 site6_1 field=[-2.4, 5.0]_T=333.0_0PSD',\
    # r'..\20211206\sam1-1 site6_1 field=[-2.3, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-2.2, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-2.1, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-2.0, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-1.9, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-1.8, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-1.7, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-1.6, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-1.5, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-1.4, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-1.3, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-1.2, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-1.1, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-1.0, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-0.9, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-0.8, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-0.7, 5.0]_T=333.0_0PSD',\
#     r'..\20211206\sam1-1 site6_1 field=[-0.6, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-0.5, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-0.4, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-0.3, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-0.2, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[-0.1, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[0.0, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[0.1, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[0.2, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[0.3, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[0.4, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[0.5, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[0.6, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[0.7, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[0.8, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[0.9, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[1.0, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[1.1, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[1.2, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[1.3, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[1.4, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[1.5, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[1.6, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[1.7, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[1.8, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[1.9, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[2.0, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[2.1, 5.0]_T=333.0_0PSD',\
# r'..\20211206\sam1-1 site6_1 field=[2.2, 5.0]_T=333.0_0PSD',\
    r'..\20211206\sam1-1 site6_1 field=[2.3, 5.0]_T=333.0_0PSD',\
r'..\20211206\sam1-1 site6_1 field=[2.4, 5.0]_T=333.0_0PSD',\
r'..\20211206\sam1-1 site6_1 field=[2.5, 5.0]_T=333.0_0PSD',\
r'..\20211206\sam1-1 site6_1 field=[2.6, 5.0]_T=333.0_0PSD',
]

SN_ellipticity_333K_site6_1_b = [
    r'..\20211207\sam1-1 site6_1 back field=[4.5, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[4.4, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[4.3, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[4.2, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[4.1, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[4.0, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[3.9, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[3.8, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[3.7, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[3.6, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[3.5, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[3.4, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[3.3, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[3.2, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[3.1, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[3.0, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[2.9, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[2.8, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[2.7, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[2.6, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[2.5, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[2.4, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[2.3, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[2.2, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[2.1, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[2.0, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[1.9, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[1.8, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[1.7, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[1.6, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[1.5, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[1.4, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[1.3, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[1.2, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[1.1, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[1.0, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[0.9, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[0.8, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[0.7, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[0.6, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[0.5, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[0.4, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[0.3, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[0.2, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[0.1, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[0.0, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-0.1, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-0.2, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-0.3, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-0.4, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-0.5, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-0.6, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-0.7, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-0.8, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-0.9, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-1.0, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-1.1, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-1.2, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-1.3, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-1.4, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-1.5, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-1.6, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-1.7, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-1.8, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-1.9, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-2.0, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-2.1, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-2.2, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-2.3, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-2.4, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-2.5, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-2.6, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-2.7, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-2.8, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-2.9, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-3.0, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-3.1, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-3.2, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-3.3, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-3.4, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-3.5, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-3.6, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-3.7, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-3.8, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-3.9, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-4.0, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-4.1, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-4.2, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-4.3, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-4.4, -5.0]_T=333.0_0PSD',\
    r'..\20211207\sam1-1 site6_1 back field=[-4.5, -5.0]_T=333.0_0PSD',\
]


test = [
    r'..\20211207\test\sam1-1 site6_1 R field=[1.9, -9.0]_T=333.0_0PSD',\
    r'..\20211207\test\sam1-1 site6_1 R 2 field=[1.9, -9.0]_T=333.0_0PSD',\
    r'..\20211207\test\sam1-1 site6_1 R 3 field=[1.9, -9.0]_T=333.0_0PSD',\
    r'..\20211207\test\sam1-1 site6_1 R field=[1.8, -9.0]_T=333.0_0PSD',\
]

SN_rotation_330K_site6_2 = [
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-2.5, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-2.4, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-2.3, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-2.2, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-2.1, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-2.0, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-1.9, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-1.8, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-1.7, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-1.6, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-1.5, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-1.4, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-1.3, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-1.2, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-1.1, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-1.0, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-0.9, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-0.8, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-0.7, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-0.6, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-0.5, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-0.4, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-0.3, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-0.2, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[-0.1, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[0.0, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[0.1, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[0.2, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[0.3, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[0.4, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[0.5, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[0.6, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[0.7, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[0.8, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[0.9, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[1.0, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[1.1, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[1.2, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[1.3, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[1.4, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[1.5, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[1.6, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[1.7, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[1.8, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[1.9, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[2.0, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[2.1, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[2.2, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[2.3, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[2.4, 5.0]_0PSD',\
    r'..\20210117\sam1-1 site6_2 mode=111_field=[2.5, 5.0]_0PSD',\
]

# with aspherical lens
SN_rotation_330K_site6_3_pos = [
    r'..\20210118\sam1-1 site6_3 mode=111_field=[2.0, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.9, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.8, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.7, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.6, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.5, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.4, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.3, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.2, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.1, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.0, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.9, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.8, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.7, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.6, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.5, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.4, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.3, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.2, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.1, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.0, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.1, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.2, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.3, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.4, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.5, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.6, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.7, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.8, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.9, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-1.0, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-1.1, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-1.2, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-1.3, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-1.4, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-1.5, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-1.6, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-1.7, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-1.8, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-1.9, 3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-2.0, 3.0]_0PSD',\
]

# with aspherical lens
SN_rotation_330K_site6_3_neg = [
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-1.0, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.9, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.8, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.7, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.6, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.5, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.4, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.3, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.2, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[-0.1, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.0, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.1, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.2, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.3, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.4, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.5, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.6, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.7, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.8, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[0.9, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.0, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.1, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.2, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.3, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.4, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.5, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.6, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.7, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.8, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[1.9, -3.0]_0PSD',\
    r'..\20210118\sam1-1 site6_3 mode=111_field=[2.0, -3.0]_0PSD',\
]

