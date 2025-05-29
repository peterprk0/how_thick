# Calculating membrane thickness in GROMACS
These scripts are for GROMACS users. First it will generate a .ndx file with the headgroups, and then it will calculate the membrane thickness.
Tested with GROMACS 2024.4.

These scripts assume your runnning simulation files are names as md.{xtc,tpr,gro}

Also, you will need a .ndx file (in this case, I named it as *groups.ndx*), with `MEMB` as the group containing your whole bilayer.

To run them:

```
python3 get_headgroups_ndx.py (output: headgroups.ndx)
bash thickness.sh
```

In `get_headgroups_ndx.py`, you can input the lipid and its headgroup (in this case `POPC` and `PO4`) of which will be used to calculate the headgroup distance.
