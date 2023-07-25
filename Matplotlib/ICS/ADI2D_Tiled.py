import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42



plt.rcParams["figure.figsize"] = (13.0,5.0)
plt.rcParams.update({'font.size': 14})



# make data
# make data
x = ["$256^2$", "$384^2$", "$512^2$", "$640^2$", "$768^2$", "$896^2$"]

G_12 = [0.089786, 0.142, 0.19506, 0.2532, 0.321498, 0.387086]
G_60 = [0.137726, 0.250878, 0.383688, 0.568991, 0.795465, 1.049155]
G_180 = [0.270218, 0.567759, 0.982022, 1.548083, 2.197039, 2.986251]

F_12 = [0.015729, 0.03157, 0.051094, 0.077999, 0.109692, 0.148295]
F_60 = [0.060961, 0.13298, 0.231108, 0.360772, 0.514358, 0.701884]
F_180 = [0.174262, 0.386244, 0.681082, 1.067558, 1.525821, 2.085651]

FP_12 = [0.015261333, 0.030717333, 0.049586667, 0.075453333, 0.106781333, 0.143570667]
FP_60 = [0.058952, 0.129021333, 0.224349333, 0.34852, 0.499997333, 0.678781333]
FP_180 = [0.168178667, 0.374781333, 0.661256, 1.031186667, 1.483037333, 2.016808]



#TH Th
G_12_TH = [0.089786, 0.142, 0.19506, 0.2532, 0.321498, 0.387086]
G_60_TH = [0.137726, 0.250878, 0.383688, 0.568991, 0.795465, 1.049155]
G_180_TH = [0.270218, 0.567759, 0.982022, 1.548083, 2.197039, 2.986251]

F_12_TH = [0.016794, 0.033331, 0.051978, 0.079304, 0.111366, 0.150252]
F_60_TH = [0.062061, 0.13553, 0.232126, 0.36213, 0.516121, 0.703584]
F_180_TH = [0.175236, 0.389155, 0.68165, 1.069117, 1.527731, 2.087249]

FP_12_TH = [0.015914667, 0.032064, 0.053674667, 0.080746667, 0.11328, 0.151274667]
FP_60_TH = [0.059605333, 0.130368, 0.228437333, 0.353813333, 0.506496, 0.686485333]
FP_180_TH = [0.168832, 0.376128, 0.665344, 1.03648, 1.489536, 2.024512]



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
ax0.set_ylim([0.01, 15])
ax1.set_ylim([0.01, 15])


g1=ax0.plot(x, G_12, c='#507a1f', linewidth=2.0, marker="s", 
       markersize=9, markeredgecolor='black', markeredgewidth=1,  label='GPU-12B')
g2=ax0.plot(x, G_60, c='#90c46e', linewidth=2.0, marker="s", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,label='GPU-60B')
g3=ax0.plot(x, G_180, c='#90c46e', linewidth=2.0, marker="D", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,label='GPU-180B')


f1=ax0.plot(x, F_12, c='#065693',linewidth=2.0, marker="^", 
       markersize=9, markeredgecolor='black', markeredgewidth=1, label='FPGA-12B')
f2=ax0.plot(x, F_60, c='#6589cd',linewidth=2.0, marker="^", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-60B')
f3=ax0.plot(x, F_180, c='#6589cd',linewidth=2.0, marker="v", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-180B')

fp1=ax0.plot(x, FP_12, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', label='FPGA-Pred', zorder=1)
fp2=ax0.plot(x, FP_60, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', zorder=1)
fp3=ax0.plot(x, FP_180, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', zorder=1)



g1=ax1.plot(x, G_12_TH, c='#507a1f', linewidth=2.0, marker="s", 
       markersize=9, markeredgecolor='black', markeredgewidth=1,  label='GPU-12B')
g2=ax1.plot(x, G_60_TH, c='#90c46e', linewidth=2.0, marker="s", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,label='GPU-60B')
g3=ax1.plot(x, G_180_TH, c='#90c46e', linewidth=2.0, marker="D", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,label='GPU-180B')


f1=ax1.plot(x, F_12_TH, c='#065693',linewidth=2.0, marker="^", 
       markersize=9, markeredgecolor='black', markeredgewidth=1, label='FPGA-12B')
f2=ax1.plot(x, F_60_TH, c='#6589cd',linewidth=2.0, marker="^", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-60B')
f3=ax1.plot(x, F_180_TH, c='#6589cd',linewidth=2.0, marker="v", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-180B')

fp1=ax1.plot(x, FP_12_TH, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', label='FPGA-Pred', zorder=1)
fp2=ax1.plot(x, FP_60_TH, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', zorder=1)
fp3=ax1.plot(x, FP_180_TH, c=((0/256, 0/256, 0/256, 1)),linewidth=2.0, ls='--', zorder=1)




props = dict(boxstyle='round', facecolor='white', alpha=1.0)
ax0.set_yscale('log')
ax0.grid(b=True, which='both', axis='both', linewidth=1.0)
handles, labels = ax0.get_legend_handles_labels()
print(labels)
handles = handles[0:3][::-1] + [handles[6]] + handles[3:6][::-1] 
labels = labels[0:3][::-1] + [labels[6]] + labels[3:6][::-1] 
ax0.legend(handles, labels, loc=2, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 12})
#ax0.set_xlabel('Mesh Size')
ax0.set_ylabel('Runtime (seconds)')
#ax0.set_title('$\mathregular{2D-FP32, v=8, f_{u}=3, N_{CU}=3}$')
ax0.text(2.5, 0.015 , '$\mathregular{Thomas \u2013 PCR, FP32, v=8, N_{CU}=6}$', ha='center', size=14, bbox=props) 

#locs,labes = plt.xticks();
#print(locs)


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
ax1.text(2.5, 0.015 , '$\mathregular{Thomas \u2013 Thomas, FP32, v=8, N_{CU}=6}$', ha='center', size=14, bbox=props) 






fig.tight_layout()
plt.savefig("M-ADI-Tiled-SP_log.pdf", bbox_inches='tight')

plt.show()










