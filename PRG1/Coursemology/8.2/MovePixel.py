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

from sense_hat import SenseHat

sense = SenseHat()

pixel_pos = [0, 7]
pixel_color = (255, 255, 255)
bg_color = (000, 000, 000)
allow_wraparound = False

sense.clear(bg_color)

sense.set_pixel(pixel_pos[0], pixel_pos[1], pixel_color)

def move_pixel(event):
    if event.action in ["pressed", "held"]:
        sense.set_pixel(pixel_pos[0], pixel_pos[1], bg_color)
    
        if event.direction == "up":
            pixel_pos[1] -= 1
        elif event.direction == "down":
            pixel_pos[1] += 1
        elif event.direction == "left":
            pixel_pos[0] -= 1
        elif event.direction == "right":
            pixel_pos[0] += 1

        if allow_wraparound:
            if pixel_pos[0] < 0:
                pixel_pos[0] = 7
            elif pixel_pos[0] > 7:
                pixel_pos[0] = 0
                
            if pixel_pos[1] < 0:
                pixel_pos[1] = 7
            elif pixel_pos[1] > 7:
                pixel_pos[1] = 0
        else:
            if pixel_pos[0] < 0:
                pixel_pos[0] = 7
            elif pixel_pos[0] > 7:
                pixel_pos[0] = 0
                
            if pixel_pos[1] < 0:
                pixel_pos[1] = 7
            elif pixel_pos[1] > 7:
                pixel_pos[1] = 0

        sense.set_pixel(pixel_pos[0], pixel_pos[1], pixel_color)

while True:
    move_pixel(sense.stick.wait_for_event())