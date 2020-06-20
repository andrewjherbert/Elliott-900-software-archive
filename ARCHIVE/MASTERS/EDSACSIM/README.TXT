EDSACSIM
========

EDSACSIM.900 is derived from Don Hunter's EDSAC simulator for the Elliott 903 
(EDSACSIMULATOR.900).  It models EDSAC as it was in 1949/50.


I have extended the simulator in several ways.

1) Teleprinter output is immediate rather than delayed.

2) An error in the code for the I instruction due to a mispunch on Don's tape
   has been fixed.

3) Input compatible with Martin Campbell-Kelly's EDSAC simulator is permitted.

4) Initial orders 1 and 2 are available.  Initial Orders 2 are presumed.

5) Spaces can be treated as runout (as in Don's simulator) or ignored (as in
   Martin's).  Spaces to be ignored is presumed.

6) The telephone dial is supported.

7) Additional entry points:

       32: START - in a program under initial orders.
       33: Resume reading input tape after a halt code.
       34: RESET - obey next instruction after a stop (Z F).
       35: CLEAR - clear the store.
       36: Select initial orders 1.
       37: Select initial orders 2. (Presumed).
       38: Spaces to be ignored. (Presumed).
       39: Spaces to be treated as runout.
       40: Set five hole tape input (i.e., EDSAC code).
       41: Set eight hole tape input (i.e., telecode).
       42: Translate telecode to EDSAC code.

       65: Dial 1 (and RESET)
       66: Dial 2 (and RESET)
           ...
       74: Dial 0 (and RESET)
       

8) Machine state is output for each entry point, e.g., CLEAR, DIAL, RESET, 
START, STOP.

9) Undefined instructions produce an error message (they stopped silently
on the original, as on EDSAC).

Input should be in 900 telecode:

       A-Z, 0-9, +, - stand for themselves.
       *    = erase.
       .    = blank runout  (also space if enabled by entry at 39).
       #, " = pi.
       @, ( = theta.
       !, ) = phi.
       &, < = delta.

Output should also be in 900 telecode.  Note EDSAC # is output as 900
telecode \.

Note: generally in the table above the first symbol is that used by Martin's
EDSAC simulator and the second is that used by Don's simulator.

Runout, carriage return, erase, space, tab, newline are all ignored.

[] can be used to add comments, which are also ignored.

Files
=====

AIRY_ALGOL     ALGOL version of Wilkes Airy Integral program.
COORDINATING_ORDERS
              Initial orders 2 in a form suitable for loading under initial
               orders 1.
CPG51.900      Possibly WWG page 51 in ALGOL, but needs DGNH multi-precision
               arithmetic?
EDSACDEMO.BIN  EDSACSIM plus table of squares and table of primes
               demos.
EDSACSIM.900   SIR source.
EDSACSIM.BIN   Assembled binary.

IO1.900        Initial Orders 1 in initial orders 2 format.
IO2.900        Initial orders 2 in initial orders 2 format.
IO1_FOR_IO2.900
               Program to load IO1 code using IO2.

PG51A.900      ALGOL version of WWG page 51 example PG51B.900.
PG51C.900      ALGOL version of WWG page 51 example PG51D.900.

PURVIS.TXT     "BIN" form of sample EDSAC paper tape for Bill Purvis.


LIBRARY SUBROUTINES
===================

Note: LIBRARY_DGNH contains programs in Don Hunter format, LIBRARY_MCK in 
Martin Campbell-Kelly format.

       C7, C10
       D6, D7, D11
       E2, E3
       G1      
       M1, M3, M20
       P1, P6, P7, P11, P14
       PM1, PM2, PM3, PM4, PM5
       Q1, Q2, Q3
       R1, R2, R5, R9
       S2, S3
       T1

Note: DGNH tape collection has two identical G1 tapes, one labelled
"release 1", the other "release 2".


PROGRAMS
========

Note: PROGRAMS_DGNH contains programs in Don Hunter format, PROGRAMS_MCK in 
Martin Campbell-Kelly format.

ACCTEST.900    Double length accumulator test (Martin Campbell-Kelly).
AIRY.900       Simplified and debugged version of Don Hunter's versions
               of Wilkes Airy Integral example.
AIRY_ALGOL.900 Airy Integral in ALGOL.
AIRY1.900      Airy Integral to 5 places by Don Hunter (corrected).
AIRY2.900      Airy Integral to 7 places by Don Hunter (corrected).
CHAPMAN.900    Don Hunter Chapman integral.
CHAPMANXSINX.900
               Modified version of CHAPMAN.900 including x sin chi term.
DODDGLENNIE.900
               Example from Dodd & Glennie report for Armament Research
               Laboratory.
HORN.900       Don Hunter loud speaker horn calculation.
MULTIPLYTEST.900
               Multiplication tests.
PG51B.900      Calculation of pi, based on Wilkes, Wheeler and Gill,
               page 51.  Prints intermediate results.
PG51D.900      As PG51B.900 without intermediate result printing.  Note
               original had halt codes for insertion of library routines.
               These have been replaced by the routines in this version.
PG61A.900      Evaluation of Chapman Integral, based on Wilkes,
               Wheeler and Gill page 61, uses Q1.
PG61B.900      Evaluation of Chapman Integral, based on Wilkes,
               Wheeler and Gill page 61, uses Q2.
PG61C.900      Evaluation of a definite integral, based on Wilkes,
               Wheeler and Gill page 61, uses Q1.  
PRIMES.900     Primes program (initial orders 1).
SINETEST1.900  Test program for S2?  Needs debugging.
SINETEST2.900  Test program for S2?  Needs debugging.
SQUARES.900    Squares program (initial orders 1).

NOTES
=====

Airy Integral
-------------

AIRY1 and AIRY2 original tapes didn't run.  Corrections noted in PROGRAMS_MCK
versions.  (AIRY1 had a mispunched instruction, both lacked Y2:=Y1:=EPS order,
and a consequential change to a jump.)  Both fail to initialize Y2 and EPS, 
and both unecessarily force P11 to start a new block at the outset.

AIRY_AJH is my own version which is somewhat simpler and produces output 
closer to Wilkes' original program.

Chapman Integral
----------------

The tapes CHAPMAN, CHAPMANXSINX, PG61A, PG61B and PG61C all deal with the
Chapman Integral, a topic of interest to M.V. Wilkes. Wilkes published a table 
of Chapman's Integral computed on EDSAC ("A Table of Chapman's Grazing Incidence
Function.",  Proc. Phys. Soc. B vol 67 page 304, 1954). Additionally, an example
based on the Chapman Integral is given on page 61 et seq of Wilkes, Wheeler and
Gill.  The integral used in WWG is a simplified version of the Chapman Integral.
The full Chapman Integral consists of an integral multiplied by a factor
by x . sin chi.  

PG61C is the closest to WWG in that it uses Q1 for the integration.  There are
some differences to do with the reading of constants and how summation of the
integrand is handled.  PG61A is the same program with the x sin chi term 
included.  The results of PG61A start in agreement with the published table but
as x diminishes they start to diverge noticeably.

PG61B uses Q2 (Five point Gauss) and again includes the x sin chi term.  It
produces a more consistent of results than the A and C programs. 

In his paper Wilkes says he computed his results first using Q1, which was slow,
then with Q2 which was faster.  In both cases he says he had to use an 
adaptive strategy that adjusted the strip length to control errors.  Wilkes
wrote a later paper about this for a conference in Darmstadt, but no copy
has yet been found.

CHAPMAN appears to be an attempt by Don Hunter to recreate Wilkes' program.  It
uses Q3 (six point Gaussian quadrature) and has an adaptive strategy based on
reducing the range of the integrand to prevent the asymptope of the curve 
dominating the fitting off the six Gaussian points.  CHAPMANXSINX is a copy
of CHAPMAN extended by the author to include the x . sin chi term.  It 
produces results in good agreement with Wilkes' published table.


Andrew Herbert
11 November 2013
