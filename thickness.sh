#!/bin/bash

# Centering the membrane is needed to prevent possible drifting in the z-axis during the simulation
echo "0" | gmx trjconv -f md.xtc -s md.tpr -o membrane_ini.gro -b 0 -dump 0
echo "0" | gmx trjconv -f md.xtc -s membrane_ini.gro -o membrane_ini_nj.xtc -pbc nojump
echo "MEMB MEMB" | gmx trjconv -f membrane_ini_nj.xtc -s md.tpr -o membrane_nj_centered.xtc -center -boxcenter tric -pbc mol -n groups.ndx

# Enlarging the simulation box dimensions, in order to avoid calculating the distance through the water phase, instead of the transmembranial distance
echo "MEMB" | gmx convert-tpr -s md.tpr -o membrane.tpr -n groups.ndx 
echo "0" | gmx trjconv -f membrane_nj_centered.xtc -s membrane.tpr -o membrane_nj_centered_nobox.xtc -box 100 100 100

# Calculating the membrane thickness
echo -e "com of group 0 plus com of group 1" | gmx distance -f membrane_nj_centered_nobox.xtc -s md.tpr -oav thickness_IL.xvg -xvg xmgrace -n headgroups.ndx -b 0 -tu ns
