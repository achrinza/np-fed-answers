#
# Copyright (c) 2019 Rifa I. Achrinza
# This document is licensed under MIT license (See LICENSE for details)
# SPDX-Short-Identifier: MIT
#

cal 1970 > /home/ict/WorkDir/Personal/MumBirthYear.txt \
    && cal 2002 > /home/ict/WorkDir/Personal/MyBirthYear.txt

mv /home/ict/WorkDir/Personal/MumBirthYear.txt /home/ict/WorkDir/Personal/MumBirthYear.dat \
    && mv /home/ict/WorkDir/Personal/MyBirthYear.txt /home/ict/WorkDir/Personal/MyBirthYear.dat

mkdir /home/ict/WorkDir/Personal/FamilyMatters \
    && cat /home/ict/WorkDir/Personal/MumBirthYear.dat >> /home/ict/WorkDir/Personal/MyBirthYear.dat \
    && mv /home/ict/WorkDir/Personal/MyBirthYear.dat /home/ict/WorkDir/Personal/FamilyMatters/FamilyBirthYear.dat
