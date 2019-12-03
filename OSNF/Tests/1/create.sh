#
# Copyright (c) 2019 Rifa I. Achrinza
# This document is licensed under MIT license (See LICENSE for details)
# SPDX-Short-Identifier: MIT
#

mkdir WorkDir
cd WorkDir

mkdir -p Personal \
    School_Matters/Modules/INS \
    School_Matters/Modules/NI \
    School_Matters/Modules/DB \
    School_Matters/Modules/OSF/LectureTutorial \
    School_Matters/Modules/OSF/Activities \
    School_Matters/Modules/OSF/Assessment \
    School_Matters/Course\ Information/General \
    School_Matters/Course\ Information/Diploma

touch School_Matters/Modules/DB/Database_101.txt
chmod 555 School_Matters/Modules/DB/Database_101.txt

touch Personal/Private\ Bill\ Info
chmod 625 Personal/Private\ Bill\ Info

echo "I ought to save more else I fall into debt." >> Personal/Private\ Bill\ Info
