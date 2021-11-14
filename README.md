Archive of software for Elliott 900 Series of computers.

Andrew Herbert

This repository contains the original images of my collection of Elliott 900 series paper tapes alongside those of several
other Elliott 900 enthusiasts and processed versions that have been checked out using my Elliott 900 Series simulator
(see andrewjherbert/Elliott-900-simulator).

For those who want to explore the range of Elliott 900 software and how it was used go strainght to the ARCHIVE folder.

Fot those who want to look at exact binary images of the paper tapes go to the ORIGINALS folder.  This is sub-divided by
collections, and each collection has an IMAGES sub-folder with the paper tape image as read in and a SCANNED sub-folder
containing various processed representations of the corresponding image.

In the IMAGES sub-folders, files are named XXX.1,  XXX2.2 etc to represent successive input of the same tape.

These image files have then been processed and automatically classified as being in one of several representations:

Binary tapes -- these are converted to two formats:

  RAW -- the image unprocessed

  BIN -- the image represented as a sequence of decimal numbers.  If the image appears to have a legible header,
         it is represented in the file by a comment enclosed within ( * ... * )

Source tapes -- these are converted into one of two formats depending on the characters found in the original:

  920 -- tapes in Elliott 920 telecode

  900 -- tapes in Elliott 900 telecode

Files for 920 or 900 tapes are written in UTF-8 using ASCII characters for their equivalents in the Elliott code and,
where there are no equivalents, the nearest Unicode equivalent.

The details of these formats is explained in the manual for the simulator included in andrewjherbert/SIM900.

In simple terms, if you want to see the original bits, look at the RAW file: if you want to see a human-readable text
version look at the corresponding 900 or 920 file as appropriate.

Note the process of scanning tapes and producing the corresponding images is automated and sometimes makes mistakes.  In
all cases of doubt go back to the original images  XXXX.1, XXXX.2 etc.

All the software contained in this archive are thought to be orphaned works and/orotherwise free of copyright restrictions.
If this is not the case, the copyright owner is invited to contact me and ask for the copyright they hold to be acknowledged
and/or have the relevant documents removed.