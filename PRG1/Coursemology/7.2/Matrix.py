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


A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[2,0,0],
     [0,2,0],
     [0,0,2]]

def matrixmulti(m1: List[List[float]], m2: List[List[float]]) -> List[List[float]]:
    mf = []
    for m1_r in m1:
        # [1, 2, 3]
        mf_r = []

        # m2 = [[],[],[]]
        #*m2 = [],[],[]
        for m2_c in m2:
            mf_u = 0
            for x, y in zip(m1_r, m2_c):
                mf_u += x * y
            mf.append(mf_u)
        mf.append(mf_r)

    return mf

matrixmulti(A, B)
