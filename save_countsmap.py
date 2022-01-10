# *******************************************************************************
# Copyright (C) 2020-2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

from sagsci.tools.fits import Fits

dl3 = './data/crab_offax.fits'
template = './data/counts_map_template.fits'
maproi = 5
pixelsize = 0.02

m = Fits()
dl4 = m.get_countmap_in_fits(dl3_file=dl3, template=template, maproi=maproi, pixelsize=pixelsize)
