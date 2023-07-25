import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
from matplotlib import gridspec

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42


plt.rcParams["figure.figsize"] = (8,4.0)
plt.rcParams.update({'font.size': 14})
plt.rcParams['hatch.linewidth'] = 1
plt.rcParams['hatch.color'] = '#6589cd'


# make data
yticks = ["$30$", "$300$", "$3000$"]


#SLV 40x20
GPU = [0.008342, 0.014189, 0.031037]
FPGA = [0.001705, 0.004655, 0.033508]
FPGA_Pred = [0.001357957, 0.004187033, 0.0324778]


#SLV 100x50
GPU_L = [0.060663, 0.202378, 1.20224]
FPGA_L = [0.053073, 0.23719, 2.077623]
FPGA_Pred_L = [0.052469941, 0.236359921, 2.075259725]


# plot
fig = plt.figure()
# set height ratios for subplots
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1]) 
fig.set_tight_layout(True)




ax0 = fig.add_subplot(gs[0])
ax1 = fig.add_subplot(gs[1], sharey=ax0)
plt.setp(ax1.get_yticklabels(), visible=False)

propsbox = dict(boxstyle='round', facecolor='white', alpha=1.0)
props = {'linestyle':'--', 'linewidth':'0.5'}
y = np.arange(3)
kwargs={'alpha': 1.0}

width=0.25
# plot1
#c8f4ff
bar1=ax0.barh(y+0.00, FPGA_Pred,  width ,facecolor='white', hatch='/////', edgecolor='#a0c4e4',linewidth=0, label='FPGA-Pred',zorder=1)
bar1=ax0.barh(y+0.00, FPGA_Pred, width,  color='none',  edgecolor='black', **props, zorder=2)
bar2=ax0.barh(y+0.25, FPGA, width,  color='#6589cd',  label='FPGA', edgecolor='black')
bar3=ax0.barh(y+0.50, GPU, width,  color='#90c46e',  label='GPU', edgecolor='black')
ax0.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
ax0.set_xlim([0.000000, 0.045])
ax0.set_yticks(y+0.250)
ax0.set_yticklabels(yticks)

for ind, val in enumerate(FPGA):
       ax0.text( val+0.0055,y[ind]+0.17, "{:.4f}".format(val), ha='center', size=14) 

for ind, val in enumerate(GPU):
       ax0.text(val+0.0055 ,y[ind]+0.45,  "{:.4f}".format(val), ha='center', size=14) 

# ax.set_yscale('log')
ax0.set_axisbelow(True)
ax0.grid(b=True, which='both', axis='x', linewidth=1, alpha=0.5)
handles, labels = ax0.get_legend_handles_labels()
handles.reverse()
labels.reverse()

ax1.legend(handles, labels, loc=4, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 14})
ax0.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#ax0.set_yticks(y, yticks)
#ax0.set_yticks('Number of Batches')
ax0.set_xlabel('Runtime (seconds)')
ax0.set_ylabel('Number of Batches')
#ax0.text(y[1]+0.20, 0.035 , '$Mesh:40x20, itr=11$', ha='center', size=14, bbox=propsbox) 
ax0.set_title('$Mesh:40x20, itr=11$')



#plot2
bar1=ax1.barh(y+0.00, FPGA_Pred_L, width,  color='white',  hatch='/////', edgecolor='#a0c4e4', linewidth=0, label='FPGA-Pred',zorder=1)
bar1=ax1.barh(y+0.00, FPGA_Pred_L, width,  color='none',  edgecolor='black', **props, zorder=2)
bar2=ax1.barh(y+0.25, FPGA_L, width, color='#6589cd',  label='FPGA', edgecolor='black')
bar3=ax1.barh(y+0.50, GPU_L, width, color='#90c46e',  label='GPU', edgecolor='black')
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax1.set_xlim([0.000000, 2.75])
""" ax1.set_yticks(y+0.250)
ax1.set_yticklabels(yticks) """

""" 

ax1.set_xticks(x+0.250)
ax1.set_xticklabels(xticks) """

for ind, val in enumerate(FPGA_L):
       ax1.text(val+0.35 , y[ind]+0.17, "{:.4f}".format(val), ha='center', size=14) 

for ind, val in enumerate(GPU_L):
       ax1.text(val+0.35 , y[ind]+0.45, "{:.4f}".format(val), ha='center', size=14) 

# ax.set_yscale('log')
ax1.set_axisbelow(True)
ax1.grid(b=True, which='both', axis='x', linewidth=1, alpha=0.5)
handles, labels = ax1.get_legend_handles_labels()

#ax1.legend(handles, labels, loc=2, ncol=3, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 14})
#ax1.set_ylabel('Number of Batches')
ax1.set_xlabel('Runtime (seconds)')
#ax1.text(y[1]+0.20, 2.1875 , '$Mesh:100x50, itr=104$', ha='center', size=14, bbox=propsbox) 
ax1.set_title('$Mesh:100x50, itr=104$')




fig.tight_layout()
plt.savefig("M-SLV-both.pdf", bbox_inches='tight')

plt.show()










