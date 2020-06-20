This folder contains files required to build MASIR and the 900 Loader.

MASIR1A        ASCII   MASIR ISS 3, TAPE 1A
MASIR1B        ASCII   MASIR ISS 4, TAPE 1B
MASIR1C        ASCII   MASIR ISS 3, TAPE 1C
MASIR234       ASCII   MASIR ISSUE 3 TAPES 2,3&4
MASIR5A        ASCII   MASIR ISS 3, TAPE 5A
MASIR5B        ASCII   MASIR ISSUE 3 TAPE 5B
MASIR67        ASCII   MASIR ISS 4, TAPES 6 & 7
MASIR8         ASCII   MASIR ISSUE 3 TAPE 8
LOADSRC        RAW     900 LOADER ISS 3 SOURCE (contains parity error at
                       end)

From the above we assume MASIR(181175) was intended as MASIR ISSUE 4,
although there is no evidence of Elliotts having issued this to users.

The SCRIPTS folder contains scripts to build MASIR(181175).BIN, 
MASIR(ISS3).BIN and LOADER(ISS3).BIN.

Terry Froggatt note on MASIR(181175):

I was reluctant to call my 18/11/75 MASIR "MASIR ISSUE 4" because
I've never seen an official MASIR ISSUE 4 binary tape (then or since).
In fact my 1982 notes say that, subsequently, my 18/11/75 tape
was found to be the same as "18/11/75 Pre-release Issue 4" and
another "ISS 4" tape, neither of which had legible headings.

Note on bug fixes in MASIR(181175):

MASIR1B:
(THIS CODE INSERTED TO CORRECT LITERAL GENERATED FOR +LOCAL)
(WHEN MODULE PATCHED TO ABSOLUTE LOCATION - SAN/7 -GRC 18/11/75)
MASIR67:
(THIS CODE INSERTED TO IGNORE COMMENTS INSIDE MACRO TEXT - GRC 18/11/75)

(See MASIRBLD.TXT in ORIGINALS/FROGGATT for full details).

AJH 15/11/15
