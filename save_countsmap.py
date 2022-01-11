# *******************************************************************************
# Copyright (C) 2020-2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

from sagsci.tools.fits import Fits
from sagsci.tools.plotting import SkyImage

dl3 = './data/crab_offax.fits'
template = './data/counts_map_template.fits'
maproi = 5
pixelsize = 0.02

m = Fits()
dl4 = m.get_countmap_in_fits(dl3_file=dl3, template=template, maproi=maproi, pixelsize=pixelsize)

plot = SkyImage()
plot.set_target(ra=83.6331, dec=22.0145).set_pointing(ra=83.6331, dec=22.5145)
regions = [{'ra': 84.1205639560909, 'dec': 22.62576046697816, 'rad': 0.2}, {'ra': 83.85004186955878, 'dec': 22.964984433951212, 'rad': 0.2}, {'ra': 83.41615813044122, 'dec': 22.964984433951212, 'rad': 0.2}, {'ra': 83.1456360439091, 'dec': 22.625760466978157, 'rad': 0.2}]
plot.plot_fits_skymap_with_regions(file=dl4, regions=regions, name='./data/test.png', figsize=(5,5), fontsize=10)

del m, plot