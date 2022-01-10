# *******************************************************************************
# Copyright (C) 2020-2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

from sagsci.tools.fits import Fits

skymap = './data/crab_offax_sky.fits'
template = './data/counts_map_template.fits'

countmap = Fits()
countmap.convert_countmap_in_template(skymap=skymap, template=template)