import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec


plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42



plt.rcParams["figure.figsize"] = (13.0, 5.0)
plt.rcParams.update({'font.size': 14})



# make data
x = ["$32^2$", "$48^2$", "$64^2$", "$80^2$", "$96^2$", "$112^2$", "$128^2$"]

G_1500 = [0.051926, 0.100185, 0.164678, 0.252945, 0.352306, 0.478392, 0.608963]
G_3000 = [0.08929, 0.185628, 0.311998, 0.490501, 0.694886, 0.946668, 1.21891]

F_1500 = [0.011768, 0.024065, 0.045064, 0.06177, 0.087886, 0.119968, 0.15678]
F_3000 = [0.020959, 0.044525, 0.084882, 0.118695, 0.169448, 0.23099, 0.304469]

FP_1500 = [0.011426849, 0.023794521, 0.040598356, 0.061838356, 0.087514521, 0.117626849, 0.152175342]
FP_3000 = [0.020193973, 0.043520548, 0.075666849, 0.116632877, 0.16641863, 0.22502411, 0.292449315]


G_1500_DP = [0.083552, 0.180618, 0.309131, 0.486596, 0.688309, 0.959437, 1.262698]
G_3000_DP = [0.158329, 0.35355, 0.627219, 0.975146, 1.3695, 1.908415, 2.448809]

F_1500_DP = [0.032777, 0.070323, 0.124069, 0.183378, 0.260491, 0.351374, 0.459245]
F_3000_DP = [0.0598, 0.13201, 0.236424, 0.352789, 0.503768, 0.682056, 0.894456]

FP_1500_DP = [0.032033333, 0.06821, 0.117826667, 0.180883333, 0.25738, 0.347316667, 0.450693333]
FP_3000_DP = [0.0587, 0.12821, 0.224493333, 0.34755, 0.49738, 0.673983333, 0.87736]


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


g1=ax0.plot(x, G_1500, c='#507a1f', linewidth=2.0, marker="s", 
       markersize=9, markeredgecolor='black', markeredgewidth=1,  label='GPU-1500B')
g2=ax0.plot(x, G_3000, c='#90c46e', linewidth=2.0, marker="s", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,label='GPU-3000B')
f1=ax0.plot(x, F_1500, c='#065693',linewidth=2.0, marker="^", 
       markersize=9, markeredgecolor='black', markeredgewidth=1, label='FPGA-1500B')
f2=ax0.plot(x, F_3000, c='#6589cd',linewidth=2.0, marker="^", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-3000B')

fp1=ax0.plot(x, FP_1500, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', label='FPGA-Pred', zorder=1)
fp2=ax0.plot(x, FP_3000, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', zorder=1)


g1=ax1.plot(x, G_1500_DP, c='#507a1f', linewidth=2.0, marker="s", 
       markersize=9, markeredgecolor='black', markeredgewidth=1,  label='GPU-1500B')
g2=ax1.plot(x, G_3000_DP, c='#90c46e', linewidth=2.0, marker="s", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,label='GPU-3000B')
f1=ax1.plot(x, F_1500_DP, c='#065693',linewidth=2.0, marker="^", 
       markersize=9, markeredgecolor='black', markeredgewidth=1, label='FPGA-1500B')
f2=ax1.plot(x, F_3000_DP, c='#6589cd',linewidth=2.0, marker="^", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-3000B')


fp1=ax1.plot(x, FP_1500_DP, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', label='FPGA-Pred', zorder=1)
fp2=ax1.plot(x, FP_3000_DP, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', zorder=1)


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
ax0.text(x[3], 0.015 , '$\mathregular{2D\ ADI, FP32, v=8, f_{u}=3, N_{CU}=3}$', ha='center', size=14, bbox=props) 


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
ax1.text(x[3], 0.015 , '$\mathregular{2D\ ADI, FP64, v=8, f_{u}=2, N_{CU}=3}$', ha='center', size=14, bbox=props) 






fig.tight_layout()
plt.savefig("M-ADI-2D-SP-DP_log.pdf", bbox_inches='tight')

plt.show()










