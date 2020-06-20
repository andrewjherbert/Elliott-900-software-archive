HUNTER ALGOL FILES

ALG1(HUNTER)        SCB     "ALGOL TAPE 1 AS PATCHED 30/12/76" - 903 Algol 
                            Issue 6 Tape 1 with Hunter extensions.
ALG2(HUNTER)        SCB     "ALGOL TAPE 2 AS PATCHED 30/12/76" - 903 Algol 
                           Issue 6  Tape 2 with HUnter extensions.
ALG1(HUNTER)(COMPACT)(SRC1)
ALG1(HUNTER)(COMPACT)(SRC2)
ALG2(HUNTER)(COMPACT)
                    SCB     "COMPACT 903 ALGOL ISS 6 INTERPRETER 18 APR 75" - 
                            903 Algol Issue 6 Interpreter with minimal 
                            facilities.
ALG1(HUNTER)(COMPACT)(SRC1)
                    ASCII   Compact ALGOL Tape 2 18/04/1975.
FORPATCH(230978)    ASCII   Correction to TAPE2PATCH(301276).
LABELPATCH(1510883) ASCII   Patch for labels / switch lists
                            copied from LABELPATCH.
LIBRARY             RLB     Built-in library for Hunter ALGOLs.
M0.DAT, M1.DAT              "Module files" from Hunter simulator.
MODULE ASCII                Program to convert Algol intermediate code into form
                            suitable for loading as a seperately compiled 
                            procedure.
TAPE1PATCH1(301276) ASCII   Tape 1 patches for recursion and
                            formal procedure parameters 30/12/76
                            extracted from PATCHES(30DEC76).900.    
TAPE1PATCH2(151083)  SCB    Tape 1 patch for labels.
TAPE2PATCH(301276)   ASCII  Tape 2 patches for recursion and
                            formal procedure parameters 30/12/76
                            extracted from PATCHES(30DEC76).900.
TAPE2PATCH(151083)   ASCII  Corrections to TAPE2PATCH(301276)
                            Copied from ALG2PATCHREWORK.900.


COMPACT ALGOL:

18 APR 1975 Elliott 903 Algol Tape 2 Issue 6
600 extra locations available
3360 3940 instead of 3960 4540
WITHOUT: EXP,LN,CHECKB,CHECKI,CHECKR,CHECKS,
PARAMETER CHECKING, ARRAYS CALLED BY VALUE,
and the ^ symbol: all give run-time error 30.


RELATED FILES IN PAPER TAPE ARCHIVE, WRITTEN LABELS & NOTES

ALG2PATCHREWORK 
       MAY 1980 patch reworked for 8K system TAPE 2 part 15 OCT 1983
       Not in ALG2(HUNTER).
        Present in 16KLG system.

FORPATCH(230978)

       For block / actual parameters type proc problem source  
       FOR BLOCK/ACTUAL PARAMETERLESS TYPE PROCEDURE PROBLEM TAPE 2 PATCH 23 SEP 1978

MOD0PATCH / MOD1PATCH
       Patches to build load and go system.
        
       MODULE 0 PATCHES 19 AUG 1978 26 AUG 1978 needs  
       type proc patch.
       Has type proc patch and also load and go patch with 
       instructions written on tape.

       MODULE 1 PATCHES 19 AUG 1978 26 AUG 1978.
       Enter at 9 to copy translator to module 1.

TAPE1PATCH151083
       Remove need for labels to be declared in switch statement.
        N.B. overwrites DUMP routine. 

       TAPE 1 PATCH switch list Nov 77 + May 80 Fix Source 15 Oct 83 
