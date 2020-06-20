
Note there is a bug in the WORKSHOP QATN function, detected by Erik
Baiger and fixed by Terry Froggatt.

The wrong series is summed for arctan.  

It should be arctan := x - x^3/3 + x^5/5 - x^7/7...  

The program has arctan := x - x^3/3 + x^5/(3.5) - x^7/(3.5.7)...

The fix is incredibly easy. In the online version swap locations 5603
& 5064, from 13 4093, 5 4889 to 5 4889, 13 4093; in the offline
version swap locations 5604 & 5605, from 13 4094, 5 4890 to 5 4890, 13
4094.

See TESTS/WORKSHOP/WORKSHOP_BUG.DAT for an illustration of versions
with and without the bug.

Andrew Herbert
19/10/2017
