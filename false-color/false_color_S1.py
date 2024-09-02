#!/usr/bin/env python
# coding: utf-8

# In[1]:


from osgeo import gdal
import pathlib
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


# define path to data dir
feature_dir   = pathlib.Path('/media/Data/FYS_3023/Sentinel-1/features').absolute()

# select S1 product
S1_base = 'S1A_EW_GRDM_1SDH_20240729T175706_20240729T175756_054979_06B293_FD70'


# In[3]:


# build path to intensity imaage files
HH_path    = feature_dir / S1_base / 'Sigma0_HH.img'
HV_path    = feature_dir / S1_base / 'Sigma0_HV.img'


# In[4]:


# read intensities
HH = gdal.Open(HH_path.as_posix()).ReadAsArray()
HV = gdal.Open(HV_path.as_posix()).ReadAsArray()


# In[5]:


# dB conversion
HH_dB    = 10*np.log10(HH)
HV_dB    = 10*np.log10(HV)


# In[6]:


# create 8-bit false_color RGB

# min/max values for sclaing of HH and HV
vmin_HH = -30
vmax_HH = -5
vmin_HV = -35
vmax_HV = -10

# new 8-bit min/max values
new_min = 0
new_max = 255

# linear map from sigma0 in dB to new_min and new_max
HH_scaled = (HH_dB - (vmin_HH)) * ((new_max - new_min) / ((vmax_HH) - (vmin_HH))) + new_min
HV_scaled = (HV_dB - (vmin_HV)) * ((new_max - new_min) / ((vmax_HV) - (vmin_HV))) + new_min

# clip values
HH_scaled = np.clip(HH_scaled, new_min, new_max)
HV_scaled = np.clip(HV_scaled, new_min, new_max)

# stack scaled channels to fals-color RGB
RGB = np.stack((HV_scaled,HH_scaled,HH_scaled),2)


# In[7]:


step = 3
fig, axes = plt.subplots(1,3,sharex=True, sharey=True, figsize=((12,5)))
axes = axes.ravel()
axes[0].imshow(HH_dB[::step,::step], cmap='gray', vmin=vmin_HH, vmax=vmax_HH)
axes[1].imshow(HV_dB[::step,::step], cmap='gray', vmin=vmin_HV, vmax=vmax_HV)
axes[2].imshow(RGB[::step,::step,:]/255)

