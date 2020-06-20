LOWL Notes
==========

This folder relates to Peter Brown's LOWL system for
portable software.  LOWL is a system independent assembly
code designed for easy translation to any specific machine
assembly code.

Brown used LOWL to provide portable implementations of ML/I,
ALEGBRA, SCAN and UNRAVEL.

A tool chain for mapping LOWL to Elliott 900 MASIR is provided,
following the approach used by Harold Thimbleby to port ML/I
to the 905 in 1976, as a student project.

The first tool is a program to read LOWL and convert it in a form
amenable to processing by GPM: LOWL2GPM.

The second tool is a LOWL translator written for a customized
version of GPM, based on Thimbleby's version. LOWL_TRANSLATOR, 
LOWL_GPM.

The result of translation of a LOWL program should be assembled
togther with the system specific code and executive comprising
the 905 LOWL environment.

Because MASIR does not allow the address literal "=0 LABEL", 
references have to be manually generated.  A file xxx_REFS 
is expected for each LOWL application xxx.


ML/I Hash Tables
================

The LOWL for ML/I includes two additional macros, HASH and THASH
for generating hash table entries for build-in macro names.  The
SIR program MLI_HASH contains simplified copies of the ML/I input,
output and hashing routines. It reads in a series of identifiers
one to a line, terminated by halt code.  The output consists of 
a macro definition for each identifier to generate the hash 
table entry for that identifier (for use in defining the HASH 
macro) together with a definition for the THASH macro to output
the hash table.


FILES
=====


ALGEBRA_MDLOGIC    ASCII  machine dependent code for ALGEBRA.

ALGEBRA_MILOGIC    ASCII   Peter Brown's ALGEBRA application.
                   SCB

ALGEBRA_REFS       ASCII   Variable references for ALGEBRA.

EXEC
                   ASCII   Paper tape executive for LOWL applications.

EDIT_MLI_MILOGIC
                   ASCII   Edits to ML/I MI LOGIC MASIR to add overflow
                           detection.

LOWL_GPM           ASCII   Version of TGPM with additional macros
                   SCB     for LOWL translation (ALPHA, COND, STR).

LOWL_TESTS         SCB     LOWL test suite.

LOWL_TESTS_MDLOGIC
                   ASCII   Machine dependent code for LOWL test suite.

LOWL_TESTS_MILOGIC
                   ASCII   Machine independent logic of LOWL test suite.

LOWL_TESTS_REFS    ASCII   Variable references for LOWL_TESTS_MILOGIC.

LOWL_TRANSLATOR    ASCII   Reconstructed GPM macros to convert 
                           LOWL to MASIR.  Includes macro definitions
                           for ML/I hash table entries.

LOWL2GPM           ASCII   Preprocessor to convert LOWL to GPM format.
                   SCB

MLI                SCB     ML/I Version AJB.

MLI_HASH           ASCII   Program to print hash values of ML/I built-in
                           identifiers.

MLI_MDLOGIC        ASCII   Machine dependent logic for ML/I.

MLI_MILOGIC        ASCII   LOWL for ML/I machine independent logic, version AJB.

MLI_REFS           ASCII   Variable references for ML/I.




Andrew Herbert
6 August 2015

