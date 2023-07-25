import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42



plt.rcParams["figure.figsize"] = (13,5.0)
plt.rcParams.update({'font.size': 14})



# make data
x = [r'$32^3$', "$80x32^2$", "$48^3$", "$80x64^2$", "$80^3$", "$96^3$"]

G_24 = [0.033485, 0.064337, 0.078677, 0.207939, 0.318074, 0.534816]
G_72 = [0.068051, 0.159311, 0.209396, 0.605547, 0.966475, 1.605493]

F_24 = [0.014435, 0.031197, 0.036908, 0.09639, 0.145938, 0.245777]
F_72 = [0.035474, 0.073093, 0.0942, 0.268703, 0.418207, 0.712403]

FP_24 = [0.013710329, 0.030467558, 0.036084748, 0.094831074, 0.142153569, 0.237960559]
FP_72 = [0.029860448, 0.070842855, 0.090591399, 0.256332261, 0.394499174, 0.674013764]


G_24_DP = [0.047983, 0.109056, 0.143062, 0.406282, 0.630805, 1.090251]
G_72_DP = [0.125366, 0.307859, 0.410969, 1.210522, 1.894097, 3.200741]

F_24_DP = [0.031326, 0.07085, 0.087803, 0.240179, 0.371648, 0.626418]
F_72_DP = [0.078996, 0.180131, 0.238624, 0.689622, 1.089421, 1.847857]

FP_24_DP = [0.030762667, 0.070762667, 0.087616, 0.240405333, 0.366186667, 0.620672]
FP_72_DP = [0.074453333, 0.179989333, 0.235072, 0.677312, 1.048853333, 1.80032]



#fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True, gridspec_kw={'height_ratios': [1, 1], 'hspace': 0.1})
#
fig = plt.figure()
# set height ratios for subplots
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1]) 
fig.set_tight_layout(True)


# plot

ax0 = fig.add_subplot(gs[0])
ax1 = fig.add_subplot(gs[1], sharey=ax0)

plt.setp(ax1.get_yticklabels(), visible=False)

fig.tight_layout()
ax0.set_ylim([0.01, 10])
ax1.set_ylim([0.01, 10])


g1=ax0.plot(x, G_24, c='#507a1f', linewidth=2.0, marker="s", 
       markersize=9, markeredgecolor='black', markeredgewidth=1,  label='GPU-24B')
g2=ax0.plot(x, G_72, c='#90c46e', linewidth=2.0, marker="s", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='GPU-72B')
f1=ax0.plot(x, F_24, c='#065693',linewidth=2.0, marker="^", 
       markersize=9, markeredgecolor='black', markeredgewidth=1,  label='FPGA-24B')
f2=ax0.plot(x, F_72, c='#6589cd',linewidth=2.0, marker="^", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,  label='FPGA-72B')

fp1=ax0.plot(x, FP_24, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', label='FPGA-Pred', zorder=1)
fp2=ax0.plot(x, FP_72, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', zorder=1)


g1=ax1.plot(x, G_24_DP, c='#507a1f', linewidth=2.0, marker="s", 
       markersize=9, markeredgecolor='black', markeredgewidth=1, label='GPU-24B')
g2=ax1.plot(x, G_72_DP, c='#90c46e', linewidth=2.0, marker="s", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='GPU-72B')
f1=ax1.plot(x, F_24_DP, c='#065693',linewidth=2.0, marker="^", 
       markersize=9, markeredgecolor='black', markeredgewidth=1, label='FPGA-24B')
f2=ax1.plot(x, F_72_DP, c='#6589cd',linewidth=2.0, marker="^", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-72B')


fp1=ax1.plot(x, FP_24_DP, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', label='FPGA-Pred', zorder=1)
fp2=ax1.plot(x, FP_72_DP, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', zorder=1)


props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax0.set_yscale('log')
ax0.grid(b=True, which='both', axis='both', linewidth=1.0)
handles, labels = ax0.get_legend_handles_labels()
print(labels)
handles = [handles[1], handles[0], handles[4], handles[3], handles[2]]
labels = [labels[1], labels[0], labels[4], labels[3], labels[2]]
ax0.legend(handles, labels, loc=2, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 12})
#ax0.set_xlabel('Mesh Size')
ax0.set_ylabel('Runtime (seconds)')
#ax0.set_title('$\mathregular{2D-FP32, v=8, f_{u}=3, N_{CU}=3}$')
ax0.text(2.5, 0.015 , '$\mathregular{3D\ ADI, FP32, v=8, N_{CU}=6}$', ha='center', size=14, bbox=props) 


ax1.set_yscale('log')
ax1.grid(b=True, which='both', axis='both', linewidth=1.0)
handles, labels = ax1.get_legend_handles_labels()
print(labels)
handles = [handles[1], handles[0], handles[4], handles[3], handles[2]]
labels = [labels[1], labels[0], labels[4], labels[3], labels[2]]
#ax1.legend(handles, labels, loc=2, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 12})
ax1.set_xlabel('Mesh Size')
#ax1.set_ylabel('Runtime (seconds)')
#ax1.set_title('$\mathregular{2D-FP64, v=8, f_{u}=2, N_{CU}=3}$')
ax1.text(2.5, 0.015 , '$\mathregular{3D\ ADI, FP64, v=8, N_{CU}=3}$', ha='center', size=14, bbox=props) 







plt.savefig("M-ADI-3D-SP-DP_log.pdf", bbox_inches='tight')

plt.show()










