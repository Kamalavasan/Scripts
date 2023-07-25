import matplotlib.pyplot as plt
import numpy as np





plt.rcParams["figure.figsize"] = (7,5.5)
plt.rcParams.update({'font.size': 14})



# make data
x = ["$200x100$", "$200x200$", "$300x150$", "$300x300$", "$400x200$", "$400x400$"]

G_100 = [2.211600, 3.844530, 4.168390, 7.604130, 6.660650, 12.760100]
G_1000 = [17.004400, 33.378830, 36.199920, None, None, None]

F_100 = [1.120660, 2.166440, 2.397000, 4.686090, 4.320760, 8.496500]
F_1000 = [11.078800, 21.520300, 23.815800, None, None, None]

FP_100 = [1.073280, 2.113280, 2.328640, 4.608640, 4.064000, 8.064000]
FP_1000 = [10.620480, 21.020480, 23.122240, None, None, None]




# plot
fig, ax = plt.subplots()
fig.tight_layout()


g1=ax.plot(x, G_100, c='#507a1f', linewidth=1.0, marker="s", 
       markersize=9, markeredgecolor='black', markeredgewidth=1,  label='GPU-100B')
g2=ax.plot(x, G_1000, c='#90c46e', linewidth=1.0, marker="s", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,label='GPU-1000B')
f1=ax.plot(x, F_100, c='#065693',linewidth=1.0, marker="^", 
       markersize=9, markeredgecolor='black', markeredgewidth=1, label='FPGA-100B')
f2=ax.plot(x, F_1000, c='#6589cd',linewidth=1.0, marker="^", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-1000B')

# g1=ax.plot(x, G_1500, c='#507a1f', linewidth=2.0, marker="s", 
#        markersize=9,  label='GPU-1500B', zorder=2)
# g2=ax.plot(x, G_3000, c='#90c46e', linewidth=2.0, marker="s", 
#        markersize=13, label='GPU-3000B', zorder=2)
# f1=ax.plot(x, F_1500, c='#065693',linewidth=2.0, marker="^", 
#        markersize=9,  label='FPGA-1500B', zorder=2)
# f2=ax.plot(x, F_3000, c='#6589cd',linewidth=2.0, marker="^", 
#        markersize=13,  label='FPGA-3000B', zorder=2)



fp1=ax.plot(x, FP_100, c=((0/256, 0/256, 0/256, 1)),linewidth=1.5, ls='--', label='FPGA-Pred', zorder=1)
fp2=ax.plot(x, FP_1000, c=((0/256, 0/256, 0/256, 1)),linewidth=1.5, ls='--', zorder=1)

ax.set_yscale('log')
ax.grid(b=True, which='both', axis='both', linewidth=1.0)
handles, labels = ax.get_legend_handles_labels()
print(labels)

handles = [handles[1], handles[0], handles[4], handles[3], handles[2]]
labels = [labels[1], labels[0], labels[4], labels[3], labels[2]]



ax.legend(handles, labels, loc=1, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 14})

ax.set_xlabel('Mesh Size')
ax.set_ylabel('Runtime (seconds)')


plt.ylim([0.9, 140])
fig.tight_layout()
plt.savefig("M-Poisson_batching_log.pdf", bbox_inches='tight')

plt.show()










