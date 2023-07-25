import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter



plt.rcParams["figure.figsize"] = (8,5.5)
plt.rcParams.update({'font.size': 14})
plt.rcParams['hatch.linewidth'] = 3
plt.rcParams['hatch.color'] = '#6589cd'


# make data
xticks = ["$32^3$", "$32^2x50$", "$50^2x16$", "$50^2x32$", "$50^3$", "$50^2x200$", "$50^2x400$"]

GPU = [0.138056, 0.215500, 0.175447, 0.331792, 0.457383, 1.366103, 2.585701]
FPGA = [0.331113, 0.397877, 0.565685, 0.690383, 0.830591, 1.999264, 3.557081]
FPGA_Pred = [0.323678, 0.389885, 0.556800, 0.680533, 0.819733, 1.979733, 3.526400]













# plot
fig, ax = plt.subplots()

props = {'linestyle':'--', 'linewidth':'1.0'}
x = np.arange(7)
kwargs={'alpha': 1.0}
bar1=ax.bar(x+0.00, FPGA_Pred, color='white', width=0.25, hatch='//', label='FPGA-Pred')
bar1=ax.bar(x+0.00, FPGA_Pred, color='none', width=0.25, edgecolor='black', **props)
bar2=ax.bar(x+0.25, FPGA, color='#6589cd', width=0.25, label='FPGA', edgecolor='black')
bar3=ax.bar(x+0.50, GPU, color='#90c46e', width=0.25, label='GPU', edgecolor='black')
ax.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
# plt.tight_layout()
plt.xticks(x+0.250, xticks)



for ind, val in enumerate(FPGA):
       ax.text(x[ind]+0.15, val+0.08 , "{:.2f}".format(val), ha='center', size=14) 

for ind, val in enumerate(GPU):
       ax.text(x[ind]+0.60, val+0.05 , "{:.2f}".format(val), ha='center', size=14) 

# ax.set_yscale('log')
ax.set_axisbelow(True)
ax.grid(b=True, which='both', axis='y', linewidth=1, alpha=0.5)
handles, labels = ax.get_legend_handles_labels()



ax.legend(handles, labels, loc=2, ncol=3, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 14})

ax.set_xlabel('Mesh Size')
ax.set_ylabel('Runtime (seconds)')


plt.ylim([0.000000, 4.0])


fig.tight_layout()
plt.savefig("M_RTM_Base.pdf", bbox_inches='tight')

plt.show()










