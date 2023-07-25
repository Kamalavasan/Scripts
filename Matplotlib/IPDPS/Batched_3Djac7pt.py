import matplotlib.pyplot as plt
import numpy as np





plt.rcParams["figure.figsize"] = (7,5.5)
plt.rcParams.update({'font.size': 14})



# make data
x = ["$50^3$", "$100^3$", "$150^3$", "$200^3$", "$250^3$"]

G_10 = [0.095170, 0.498283, 1.331192, 3.210194, 5.774286]
G_50 = [0.334188, 2.303245, 6.517967, None, None]

F_10 = [0.094334, 0.613718, 1.927346, 4.403692, 8.410590]
F_50 = [0.448523, 2.997540, 9.489546, None, None]

FP_10 = [0.092839, 0.608932, 1.914211, 4.374532, 8.355746]
FP_50 = [0.444579, 2.977322, 9.427707, None, None]






# plot
fig, ax = plt.subplots()
fig.tight_layout()


g1=ax.plot(x, G_10, c='#507a1f', linewidth=1.0, marker="s", 
       markersize=9, markeredgecolor='black', markeredgewidth=1,  label='GPU-10B')
g2=ax.plot(x, G_50, c='#90c46e', linewidth=1.0, marker="s", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,label='GPU-50B')
f1=ax.plot(x, F_10, c='#065693',linewidth=1.0, marker="^", 
       markersize=9, markeredgecolor='black', markeredgewidth=1, label='FPGA-10B')
f2=ax.plot(x, F_50, c='#6589cd',linewidth=1.0, marker="^", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-50B')

# g1=ax.plot(x, G_1500, c='#507a1f', linewidth=2.0, marker="s", 
#        markersize=9,  label='GPU-1500B', zorder=2)
# g2=ax.plot(x, G_3000, c='#90c46e', linewidth=2.0, marker="s", 
#        markersize=13, label='GPU-3000B', zorder=2)
# f1=ax.plot(x, F_1500, c='#065693',linewidth=2.0, marker="^", 
#        markersize=9,  label='FPGA-1500B', zorder=2)
# f2=ax.plot(x, F_3000, c='#6589cd',linewidth=2.0, marker="^", 
#        markersize=13,  label='FPGA-3000B', zorder=2)



fp1=ax.plot(x, FP_10, c=((0/256, 0/256, 0/256, 1)),linewidth=1.5, ls='--', label='FPGA-Pred', zorder=1)
fp2=ax.plot(x, FP_50, c=((0/256, 0/256, 0/256, 1)),linewidth=1.5, ls='--', zorder=1)

ax.set_yscale('log')
ax.grid(b=True, which='both', axis='both', linewidth=1.0)
handles, labels = ax.get_legend_handles_labels()
print(labels)

handles = [handles[1], handles[0], handles[4], handles[3], handles[2]]
labels = [labels[1], labels[0], labels[4], labels[3], labels[2]]



ax.legend(handles, labels, loc=2, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 14})

ax.set_xlabel('Mesh Size')
ax.set_ylabel('Runtime (seconds)')


plt.ylim([0.08, 80])
fig.tight_layout()
plt.savefig("M-3Djac7pt_batching_log.pdf", bbox_inches='tight')

plt.show()










