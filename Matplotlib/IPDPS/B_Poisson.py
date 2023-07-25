import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter



plt.rcParams["figure.figsize"] = (7,5.5)
plt.rcParams.update({'font.size': 14})
plt.rcParams['hatch.linewidth'] = 3
plt.rcParams['hatch.color'] = '#6589cd'


# make data
xticks = ["$200x100$", "$200x200$", "$300x150$", "$300x300$", "$400x200$", "$400x400$"]

GPU = [0.506456, 0.557750, 0.434420, 0.588450, 0.577390, 0.618230]
FPGA = [0.025010, 0.035380, 0.040370, 0.063450, 0.062740, 0.104500]
FPGA_Pred = [0.023088, 0.033488, 0.041344, 0.064144, 0.064400, 0.104400]











# plot
fig, ax = plt.subplots()

props = {'linestyle':'--', 'linewidth':'1.0'}
x = np.arange(6)
kwargs={'alpha': 1.0}
bar1=ax.bar(x+0.00, FPGA_Pred, color='white', width=0.25, hatch='//', label='FPGA-Pred')
bar1=ax.bar(x+0.00, FPGA_Pred, color='none', width=0.25, edgecolor='black', **props)
bar2=ax.bar(x+0.25, FPGA, color='#6589cd', width=0.25, label='FPGA', edgecolor='black')
bar3=ax.bar(x+0.50, GPU, color='#90c46e', width=0.25, label='GPU', edgecolor='black')
ax.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
# plt.tight_layout()
plt.xticks(x+0.250, xticks)



for ind, val in enumerate(FPGA):
       ax.text(x[ind]+0.15, val+0.008 , "{:.2f}".format(val), ha='center', size=14) 

for ind, val in enumerate(GPU):
       ax.text(x[ind]+0.55, val+0.005 , "{:.2f}".format(val), ha='center', size=14) 

# ax.set_yscale('log')
ax.set_axisbelow(True)
ax.grid( which='both', axis='y', linewidth=1, alpha=0.5)
handles, labels = ax.get_legend_handles_labels()



ax.legend(handles, labels, loc=2, ncol=3, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 14})

ax.set_xlabel('Mesh Size')
ax.set_ylabel('Runtime (seconds)')


plt.ylim([0.000000, 0.7])


fig.tight_layout()
plt.savefig("M_Poisson_Base.pdf", bbox_inches='tight')

plt.show()










