import matplotlib.pyplot as plt
import numpy as np





plt.rcParams["figure.figsize"] = (8,5.5)
plt.rcParams.update({'font.size': 14})



# make data
x = ["$32^3$", "$32^2x50$", "$50^2x16$", "$50^2x32$", "$50^3$"]

G_20 = [0.120959, 0.222077, 0.181801, 0.415573, 0.642531]
G_40 = [0.231278, 0.427226, 0.334811, 0.804417, 1.262631]

F_20 = [0.318709, 0.453378, 0.416621, 0.668576, 0.952004]
F_40 = [0.618231, 0.887511, 0.794693, 1.298273, 1.864900]

FP_20 = [0.311908, 0.444322, 0.408320, 0.655787, 0.934187]
FP_40 = [0.606161, 0.870989, 0.779520, 1.274453, 1.831253]










# plot
fig, ax = plt.subplots()
fig.tight_layout()


g1=ax.plot(x, G_20, c='#507a1f', linewidth=1.0, marker="s", 
       markersize=9, markeredgecolor='black', markeredgewidth=1,  label='GPU-20B')
g2=ax.plot(x, G_40, c='#90c46e', linewidth=1.0, marker="s", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,label='GPU-40B')
f1=ax.plot(x, F_20, c='#065693',linewidth=1.0, marker="^", 
       markersize=9, markeredgecolor='black', markeredgewidth=1, label='FPGA-20B')
f2=ax.plot(x, F_40, c='#6589cd',linewidth=1.0, marker="^", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-40B')

# g1=ax.plot(x, G_1500, c='#507a1f', linewidth=2.0, marker="s", 
#        markersize=9,  label='GPU-1500B', zorder=2)
# g2=ax.plot(x, G_3000, c='#90c46e', linewidth=2.0, marker="s", 
#        markersize=13, label='GPU-3000B', zorder=2)
# f1=ax.plot(x, F_1500, c='#065693',linewidth=2.0, marker="^", 
#        markersize=9,  label='FPGA-1500B', zorder=2)
# f2=ax.plot(x, F_3000, c='#6589cd',linewidth=2.0, marker="^", 
#        markersize=13,  label='FPGA-3000B', zorder=2)



fp1=ax.plot(x, FP_20, c=((0/256, 0/256, 0/256, 1)),linewidth=1.5, ls='--', label='FPGA-Pred', zorder=1)
fp2=ax.plot(x, FP_40, c=((0/256, 0/256, 0/256, 1)),linewidth=1.5, ls='--', zorder=1)

ax.set_yscale('log')
ax.grid(b=True, which='both', axis='both', linewidth=1.0)
handles, labels = ax.get_legend_handles_labels()
print(labels)

handles = [handles[1], handles[0], handles[4], handles[3], handles[2]]
labels = [labels[1], labels[0], labels[4], labels[3], labels[2]]



ax.legend(handles, labels, loc=2, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 14})

ax.set_xlabel('Mesh Size')
ax.set_ylabel('Runtime (seconds)')


plt.ylim([0.05, 6])
fig.tight_layout()
plt.savefig("M-RTM_batching_log.pdf", bbox_inches='tight')

plt.show()










