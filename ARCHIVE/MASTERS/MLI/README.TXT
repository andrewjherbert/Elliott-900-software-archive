ML/I Notes
==========

This is an Elliott 905 port of ML/I by Harold Thimbleby 
taken from his archive of Elliott paper tapes.

The original source is a MASIR program much of
which wasm acrogenerated from the LOWL source.  
It also came with routines to enable to program 
be be run on a 905 under the RADOS operating system.

(The source used here is dated the same as a similar
file in Terry Froggatt's collection but upon inspection
Thimbleby's version is a hand optimized version of the
directly translated ML/I LOWL in Terry's files.)

To make a standalone paper tape version I had to
make some minor modifications to the original.

1) I wrote a minimal EXEC program which modified QCHIN 
   and QCHOP to work as required with the ML/I 
   system - additional handling for tab characters, 
   parity errors / invalid characters as code -1, 
   halt code as -2.
2) I set DISC=NO to cancel out the disc macros.
3) I added code in MDREAD to handle halt code.
4) I added a call to QCLOSE in MDQUIT to punch
   a halt code on the output tape.
5) Various other small changes to conditionally skip
   over code only required when reading data from disc.

Note: a closing round bracket on a line by itself is treated 
as an end-of-file mark by Rados. This has been carried over
to the paper tape version here. 

This standalone version runs on a 16K 905/920C.

I have run this version against the ML/I test battery
from Harold Thimbleby's tape collection which it passes
ok.

There is scope to tidy up the implementation: my aim
was to do the least damage to the original source to 
get the program running again rather than produce a
robust version of the system.

The 900 telecode version of the edited MASIR source can be
found in the SCRIPTS/MLI folder.

A reconstruction of the tool chain developed by Thimbleby can
be found in the LOWL folder.  This includes the sources for the
current version of ML/I at the time of writing (August 2015, 
version AJB), where the version in this folder dates from 
November 1976, version AIG.  The differences are cosmetic.



FILES
=====

EXEC.900        ASCII  paper tape I/O routines for ML/I.

DOCUMENT.900    ASCII  905 ML/I notes by H. Thimbleby.

MLI_EDIT.900    ASCII  BOWDLER steering tape to edit ML/I
                       MASIR source to work with EXEC from
                       LOWL folder.

THIMBLEBY_T4    ASCII  905 format file from H. Thimbleby
                       collection containing MASIR source
                       of ML/I.


Andrew Herbert
2 August 2015

