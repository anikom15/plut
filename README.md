# plut.py

This program modifies a CUBE LUT in stdin to simulate a monochrome
phosphor display.

## Running the program

Python 3 is required.  The program should be ran from the command-line.
No arguments are taken.  Instead, the script should be edited directly.
The `phosphors` dictionary contains entries for x and y chromaticity
coordinates.  The key is used as the filename for the output LUT.  The
default configuration is to generate four LUTs for phosphors P1, P2, P3,
and P4.  P1 and P2 are green phosphors,  P3 is the famous amber
phosphor, and P4 is the phosphor used for black and white televisions
and some monochrome monitors.

For most use cases, the I.cube file should be redirected as stdin.  The
I.cube LUT is the identity LUT and is 65x65x65.  Identity LUTs of
different sizes is not provided, but any size LUT may be used.

## Bugs

Bugs can be reported to [W. M. Martinez](mailto:anikom15@outlook.com).

## Notice

1st Edition

Copyright 2022 W. M. Martinez

Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved.  This file is offered as-is,
without any warranty. 
