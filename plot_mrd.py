# -*- coding: utf-8 -*-
import utils
import numpy as np
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc,rcParams

# Set seaborn contexts:
sns.set_context("talk")
sns.set_style("ticks")

# Fonts:
rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
matplotlib.rcParams.update({'font.size':11})
plt.rc('legend', **{'fontsize':7})

# Ticks to the outside:
rcParams['axes.linewidth'] = 1.2 
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'

M,Merr,R,Rerr,Teff,Rstar,sep = utils.get_planets()

# Erase datapoints with no data:
idx = np.where((M!=-1)&(R!=-1))[0]
M = M[idx]
Merr = Merr[idx]
R = R[idx]
Rerr = Rerr[idx]
Teff = Teff[idx]
sep = sep[idx]
Rstar = Rstar[idx]

# Erase datapoints with zero mass:
idx = np.where((M!=0.))[0]
M = M[idx]
Merr = Merr[idx]
R = R[idx]
Rerr = Rerr[idx]
Teff = Teff[idx]
sep = sep[idx]
Rstar = Rstar[idx]

# Erase datapoints with zero radii:
idx = np.where((R!=0.))[0]
M = M[idx]
Merr = Merr[idx]
R = R[idx]
Rerr = Rerr[idx]
Teff = Teff[idx]
sep = sep[idx]
Rstar = Rstar[idx]

# Erase datapoints with errors lower than 20% on mass:
idx = np.where(Merr/M<0.2)[0]
M = M[idx]
Merr = Merr[idx]
R = R[idx]
Rerr = Rerr[idx]
Teff = Teff[idx]
sep = sep[idx]
Rstar = Rstar[idx]

# Erase datapoints with errors lower than 20% on radius:
idx = np.where(Rerr/R<0.2)[0]
M = M[idx]
Merr = Merr[idx]
R = R[idx]
Rerr = Rerr[idx]
Teff = Teff[idx]
sep = sep[idx]
Rstar = Rstar[idx]

# Compute equilibrium temperature:
Rsun = 6.957e5  # km
AU = 149597871. # km
Teq = Teff*np.sqrt(Rstar*Rsun/(2.*sep*AU))

# Erase nans:
idx = np.where(~np.isnan(Teq))[0]
M = M[idx]
Merr = Merr[idx]
R = R[idx]
Rerr = Rerr[idx]
Teq = Teq[idx]

# Change zorder:
scatter_kwargs = {"zorder":100}
error_kwargs = {"zorder":0}

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
plt.errorbar(M,R,xerr=Merr,yerr=Rerr,fmt='o',markersize=1,elinewidth=1,color='grey',**error_kwargs)
plt.scatter(M,R,c=Teq,edgecolor='grey',cmap=cm.plasma,**scatter_kwargs)
cb = plt.colorbar()
cb.set_label('Equilibrium Temperature')
plt.xlabel(r'Planet Mass ($M_J$)')
plt.ylabel(r'Planet Radius ($R_J$)')

plt.plot([0.299409946],[0.842983317],'o',markerfacecolor='cornflowerblue',markeredgewidth=1,markersize=20,markeredgecolor='black')

plt.xscale('log')
plt.yscale('log')

plt.xlim([0.2,2.5])
plt.ylim([0.6,2.5])

# Supress scientific notation:
from matplotlib.ticker import ScalarFormatter
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())
    axis.set_minor_formatter(ScalarFormatter())
    #axis.set_minor_formatter(matplotlib.ticker.FormatStrFormatter("%.0f"))

plt.tight_layout()
plt.savefig("mrd.pdf", dpi=300)
plt.savefig("mrd.png", dpi=300)
