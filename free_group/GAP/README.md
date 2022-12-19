# Investigation of subgroup structure with GAP

We use the computational group theory code `GAP` (https://www.gap-system.org/) to analyse the structure of normal subgroups of the free group.

## Requirements

* `GAP-4.12.`(https://www.gap-system.org/)
* `LINS-0.5` package for `GAP` (https://github.com/FriedrichRober/LINS).
* `Mathematica 13.1`

The scripts will likely run also for versions other than the indicated ones, but this was not tested.

## Installation

These instructions work under `Windows 10`. 

1. Install the `GAP` software.
2. Install the `LINS` package for `GAP` (https://github.com/FriedrichRober/LINS).
3. Install `cmder` terminal emulator.
4. Place `run-gap-local-vars.sh` script in the `\GAP-<version>\runtime\` folder.

## Running the code

Run `gap free_group.g` in `cmder` to start the `LINS` search for normal subgroups. The coset tables are computed and stored to `coset_tables.csv`, while the classification of the quotients can be found in `quotients.csv`. The `Mathematica` script `coset_tables.wls` can be used to read and analyze these files. Running `wolramscript.exe` in `cmder` will produce the figures which can be found in the `output` folder (the `output` folder needs to exist).