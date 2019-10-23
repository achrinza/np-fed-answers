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


# 1. Imported math module
import math

#Python program to calculate surface area of time capsule
radius_Sphere = float(input("Radius of the sphere: "))

# 2. Encapsulated input() inside float()
# Original line:
#     height_Column = input("Height of the column: "))
height_Column = float(input("Height of the column: "))

# 3. Fixed typo "Widthof the..."
# 4. Change str() to float()
# Original line:
#     width_Cube = str(input("Widthof the cube: "))
width_Cube = float(input("Width of the cube: "))

# 5. Fixed missing 2nd parameter for math.pow()
# Original line:
#     surfacearea_Sphere = 4 * math.pi * math.pow(radius_Sphere)
surfacearea_Sphere = 4 * math.pi * math.pow(radius_Sphere, 2)

# 6. Added missing "divide sphere radius by half" logic
# 7. Replaced "r" with "radius_Sphere"
# Original line:
#     surfacearea_Column = (2 * math.pi * (radius_Sphere) * height_Column) \
#         + (2 * math.pi * ((r/2) ** 2))
surfacearea_Column = (2 * math.pi * (radius_Sphere/2) * height_Column) \
    + (2 * math.pi * ((radius_Sphere/2) ** 2))
# 8. Replaced "width_Block" with "width_Cube"
#     surfacearea_Cube = 6 * (width_Block ** 2)
surfacearea_Cube = 6 * (width_Cube ** 2)

# 9. Moved this line to before the print() statement below.
total_SurfaceArea = surfacearea_Sphere + surfacearea_Column + surfacearea_Cube
# 10. Fixed typo in "...surface areaof the..."
# Original line:
#     print("The total surface areaof the Time Capsule is {:2f}".format(total_SurfaceArea))
print("The total surface area of the Time Capsule is {:2f}".format(total_SurfaceArea))