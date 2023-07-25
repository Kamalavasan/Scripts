import matplotlib.pyplot as plt
import numpy as np





plt.rcParams["figure.figsize"] = (7,5.5)
plt.rcParams.update({'font.size': 14})



# make data
x = ["$256$", "$384$", "$512$", "$640$", "$768$"]

G_600= [0.492143, 0.492143, 0.492143, 0.492143, None]
G_1800 = [0.798848, 0.798848, 0.798848, 0.798848, 0.798848]

F_600 = [0.890816, 0.731525, 0.738536, 0.710701, None]
F_1800 = [1.25812, 1.25056, 1.153999, 1.140489, 1.141086]

FP_600 = [0.778627, 0.642515, 0.642515, 0.636175, None]
FP_1800 = [1.082243, 1.071679, 1.001397, 0.998096, 0.998096]






# plot
fig, ax = plt.subplots()
fig.tight_layout()


g1=ax.plot(x, G_600, c='#507a1f', linewidth=2.0, marker=" ", 
       markersize=9, markeredgecolor='black', markeredgewidth=1,  label='GPU-600^3', ls='-.')
g2=ax.plot(x, G_1800, c='#90c46e', linewidth=2.0, marker=" ", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,label='GPU-1800^2x100', ls='-.')
f1=ax.plot(x, F_600, c='#065693',linewidth=1.0, marker="^", 
       markersize=9, markeredgecolor='black', markeredgewidth=1, label='FPGA-600^3')
f2=ax.plot(x, F_1800, c='#6589cd',linewidth=1.0, marker="^", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-1800^2x600')

# g1=ax.plot(x, G_1500, c='#507a1f', linewidth=2.0, marker="s", 
#        markersize=9,  label='GPU-1500B', zorder=2)
# g2=ax.plot(x, G_3000, c='#90c46e', linewidth=2.0, marker="s", 
#        markersize=13, label='GPU-3000B', zorder=2)
# f1=ax.plot(x, F_1500, c='#065693',linewidth=2.0, marker="^", 
#        markersize=9,  label='FPGA-1500B', zorder=2)
# f2=ax.plot(x, F_3000, c='#6589cd',linewidth=2.0, marker="^", 
#        markersize=13,  label='FPGA-3000B', zorder=2)



fp1=ax.plot(x, FP_600, c=((0/256, 0/256, 0/256, 1)),linewidth=1.5, ls='--', label='FPGA-Pred', zorder=2)
fp2=ax.plot(x, FP_1800, c=((0/256, 0/256, 0/256, 1)),linewidth=1.5, ls='--', zorder=2)

ax.set_yscale('log')
ax.grid( which='both', axis='both', linewidth=1.0)
handles, labels = ax.get_legend_handles_labels()
print(labels)

handles = [handles[1], handles[0], handles[4], handles[3], handles[2]]
labels = [labels[1], labels[0], labels[4], labels[3], labels[2]]



ax.legend(handles, labels, loc=1, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 14})

ax.set_xlabel('Tile Size')
ax.set_ylabel('Runtime (seconds)')


plt.ylim([0.4, 2.9])
fig.tight_layout()
plt.savefig("M-3Djac7pt_Tiled_log.pdf", bbox_inches='tight')

plt.show()










