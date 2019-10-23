#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-Short-Identifier: MIT
# (c) 2019 Rifa I. Achrinza
# This code is licensed under MIT license (See LICENSE.txt for details)

__author__ = "Rifa I. Achrinza"
__copyright__ = "Copyright 2019, Rifa I. Achrinza"
__credits__ = ["Rifa I. Achrinza"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Rifa I. Achrinza"
__email__ = "rifa@achrinza.com"
__status__ = "Production"


from typing import List


SingaporeWest = [
'Western Water Catchment',
'Pioneer',
'Jurong West',
'Lim Chu Kang',
'Tuas',
'Choa Chu Kang',
'Bukit Batok',
'Western Islands Planning Area',
'Tengah',
'Jurong East',
'Clementi',
'Bukit Panjang',
'Boon Lay']

SingaporeEast = ['Changi Bay',
'Katong',
'Lorong Halus',
'Simei',
'Bedok Reservoir',
'Tanah Merah',
'East Coast',
'Pasir Ris',
'Marine Parade',
'Chai Chee',
'Bedok',
'Changi Village',
'Kembangan',
'Loyang',
'Tampines',
'Ubi',
'Siglap',
'Elias',
'Joo Chiat',
'Kaki Bukit',
'Changi East',
'Changi'
]


def Sort(sortable: List[str] = [], is_sort_descending: bool = False) -> List[str]:
    sortable.sort(reverse=is_sort_descending)
    return sortable


#Do not remove the next line
Sort(SingaporeWest, True)
