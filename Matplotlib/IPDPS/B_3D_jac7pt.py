import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter



plt.rcParams["figure.figsize"] = (9,5.5)
plt.rcParams.update({'font.size': 14})
plt.rcParams['hatch.linewidth'] = 3
plt.rcParams['hatch.color'] = '#6589cd'


# make data
xticks = ["$50x50x50$", "$100x100x100$", "$150x150x150$", "$200x200x200$", "$250x250x250$"]

GPU = [0.324091, 0.759514, 1.607409, 3.485957, 6.038951]
FPGA = [0.143326, 0.770618, 2.256494, 4.968952, 9.276083]
FPGA_Pred = [0.136976, 0.760439, 2.236748, 4.931756, 9.211317]








# plot
fig, ax = plt.subplots()

props = {'linestyle':'--', 'linewidth':'1.0'}
x = np.arange(5)
kwargs={'alpha': 1.0}
bar1=ax.bar(x+0.00, FPGA_Pred, color='white', width=0.25, hatch='//', label='FPGA-Pred')
bar1=ax.bar(x+0.00, FPGA_Pred, color='none', width=0.25, edgecolor='black', **props)
bar2=ax.bar(x+0.25, FPGA, color='#6589cd', width=0.25, label='FPGA', edgecolor='black')
bar3=ax.bar(x+0.50, GPU, color='#90c46e', width=0.25, label='GPU', edgecolor='black')
ax.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
# plt.tight_layout()
plt.xticks(x+0.250, xticks)



for ind, val in enumerate(FPGA):
       ax.text(x[ind]+0.18, val+0.12 , "{:.2f}".format(val), ha='center', size=14) 

for ind, val in enumerate(GPU):
       ax.text(x[ind]+0.55, val+0.10 , "{:.2f}".format(val), ha='center', size=14) 

# ax.set_yscale('log')
ax.set_axisbelow(True)
ax.grid(b=True, which='both', axis='y', linewidth=1, alpha=0.5)
handles, labels = ax.get_legend_handles_labels()



ax.legend(handles, labels, loc=2, ncol=3, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 14})

ax.set_xlabel('Mesh Size')
ax.set_ylabel('Runtime (seconds)')


plt.ylim([0.000000, 10])


fig.tight_layout()
plt.savefig("M_3DJac7pt_Base.pdf", bbox_inches='tight')

plt.show()










