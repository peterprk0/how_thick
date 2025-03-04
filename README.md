# Calculating membrane thickness in GROMACS
These scripts are for GROMACS users. First it will generate a .ndx file with the headgroups, and then it will calculate the membrane thickness.
Tested with GROMACS 2024.4.

These scripts assume your runnning simulation files are names as md.{xtc,tpr}

To run them:

```
python get_headgroups_ndx
bash thickness.sh
```
