# *******************************************************************************
# Copyright (C) 2020-2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

from sagsci.tools.plotting import SkyImage

# DL3 file
obs = './data/crab_offax.fits'
sky = './data/crab_offax_ctsmap.fits'

# params counts map
trange = [0, 1200]
erange = [0.03, 150]
roi = 5
pixelsize = 0.02
target = {'ra': 83.6331, 'dec': 22.0145}
pointing = {'ra': 83.6331, 'dec': 22.5145}

# params plot
figsize = (5, 5)
fontsize = 10

# compute and plot
plot = SkyImage()
img = obs.replace('.fits', '_sky2.png')
plot.set_target_from_dict(target=target).set_pointing_from_dict(pointing=pointing)
# map cartesian plane
plot.counts_map(file=obs, trange=trange, erange=erange, pixelsize=pixelsize, roi=roi, name=img, figsize=figsize, fontsize=fontsize)
# map with wcs celestial projection
img = obs.replace('.fits', '_sky3.png')
plot.plot_fits_skymap(file=sky, name=img, figsize=figsize, fontsize=fontsize)
#plot.counts_map_with_wcs(file=obs, trange=trange, erange=erange, pixelsize=pixelsize, roi=roi, name=img, figsize=figsize, fontsize=fontsize)

