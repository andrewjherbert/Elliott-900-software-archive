This folder contains versions of various software tools, inspired by
Kernighan & Plauger's book "Software Tools", Addison_Wesley, 2000.

The tools are based on a set of Algol code procedures for reading and
writing paper tape.  These are derived from the ACD CHIO library 
routines written by Terry Froggatt.

To use the routines, first call CHIOAL to initialize the system.

The routine CH900 should be called if 900 telecode output is desired
(and this is the default).  If 920 telecode is desired, call CH920
instead.

Input must start with newline which is decoded to decide the
telecode of the succeeding characters.

The routine GETC reads and returns the next character from paper tape.
Blank tape, carriage returns and erases are automatically ignored.  All
other characters are converted to their ACD telecode form.  If a halt
code is read the system automatically resets and if GETC is called 
again a newline will be expected to enable the format of the next
tape to be decoded.  (Thus successive tapes can be in differnt codes).

The routine PUTC punches its argument to paper tape.  The argument is 
assumed to be a character is ACD telecode. Unlike CHIOL, tab (9) is 
punched a tab character with no preceeding space.  Newline (10) is 
punched as carriage return newline in 900 telecode.  Halt (20) is 
punched as a halt code followed by blank runout.

The following tools have been written in Algol, mimicking the RATFOR
code given in Kernighna & Plauger's book.

In several cases the corresponding SCRIPTS/SWTOOLS folder has a script
to run the tool with two parameters for the file names of the input
and output tapes.

CHARCOUNT      Counts the number of characters on a tape.
DETABN         Replaces tabs by spaces according to Microsoft NOTEBOOK
               tab spacing.
DETABS         Replaces tabs by spaces according to SIR conventions
               (columns, 11, 17, 27, ...).
ENTABN         Replaces blanks by tabs according to Microsoft NOTEBOOK
               tab spacing.
ENTABNS        SIR version of ENTABN.
ENTABS         Replaces blanks by tabs according to SIR conventions
               (columns 11, 17, 27, ...).
ENTABSS        SIR version of ENTABS.
LINECOUNT      Counts the number of lines on a tape.
SIRTIDY        Tidies up SIR source code.
SIRTIDYS       SIR version of SIRTIDY.
WORDCOUNT      Counts the number of words on a tape.


Note (1) SIRTIDYS is a variant of SIRTIDY and therefore there are some 
differences between them.  SIRTIDYS is the better program.

Note (2) On a real 903 the Algol programs run painfully slowly due to
the overhead of using an interpreter.
