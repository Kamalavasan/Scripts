import matplotlib.pyplot as plt
import numpy as np





plt.rcParams["figure.figsize"] = (7,5.5)
plt.rcParams.update({'font.size': 14})



# make data
x = ["$512$", "$1024$", "$2048$", "$4096$", "$8000$"]

G_15000 = [16.559892, 16.559892, 16.559892, 16.559892, 16.559892]
G_20000 = [29.372758, 29.372758, 29.372758, 29.372758, 29.372758]

F_15000 = [16.382018, 13.423097, 12.485196, 12.101947, 11.935253]
F_20000 = [29.451684, 23.98995, 22.157466, 21.853152, 21.172657]

FP_15000 = [15.122, 12.8960416, 12.0250144, 11.6378912, 11.4443296]
FP_20000 = [26.8186016, 22.9551776, 21.409808, 20.765904, 20.3795616]






# plot
fig, ax = plt.subplots()
fig.tight_layout()


g1=ax.plot(x, G_15000, c='#507a1f', linewidth=2.0, marker=" ", 
       markersize=9, markeredgecolor='black', markeredgewidth=1,  label='GPU-15000^2', ls='-.')
g2=ax.plot(x, G_20000, c='#90c46e', linewidth=2.0, marker=" ", 
       markersize=13, markeredgecolor='black', markeredgewidth=1,label='GPU-20000^2', ls='-.')
f1=ax.plot(x, F_15000, c='#065693',linewidth=1.0, marker="^", 
       markersize=9, markeredgecolor='black', markeredgewidth=1, label='FPGA-15000^2')
f2=ax.plot(x, F_20000, c='#6589cd',linewidth=1.0, marker="^", 
       markersize=13, markeredgecolor='black', markeredgewidth=1, label='FPGA-20000^2')

# g1=ax.plot(x, G_1500, c='#507a1f', linewidth=2.0, marker="s", 
#        markersize=9,  label='GPU-1500B', zorder=2)
# g2=ax.plot(x, G_3000, c='#90c46e', linewidth=2.0, marker="s", 
#        markersize=13, label='GPU-3000B', zorder=2)
# f1=ax.plot(x, F_1500, c='#065693',linewidth=2.0, marker="^", 
#        markersize=9,  label='FPGA-1500B', zorder=2)
# f2=ax.plot(x, F_3000, c='#6589cd',linewidth=2.0, marker="^", 
#        markersize=13,  label='FPGA-3000B', zorder=2)



fp1=ax.plot(x, FP_15000, c=((0/256, 0/256, 0/256, 1)),linewidth=1.5, ls='--', label='FPGA-Pred', zorder=1)
fp2=ax.plot(x, FP_20000, c=((0/256, 0/256, 0/256, 1)),linewidth=1.5, ls='--', zorder=1)

ax.set_yscale('log')
ax.grid(which='both', axis='both', linewidth=1.0)
handles, labels = ax.get_legend_handles_labels()
print(labels)

handles = [handles[1], handles[0], handles[4], handles[3], handles[2]]
labels = [labels[1], labels[0], labels[4], labels[3], labels[2]]



ax.legend(handles, labels, loc=1, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 14})

ax.set_xlabel('Tile Size')
ax.set_ylabel('Runtime (seconds)')


plt.ylim([10, 55])
fig.tight_layout()
plt.savefig("M-Poisson_Tiled_log.pdf", bbox_inches='tight')

plt.show()










