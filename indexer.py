# INDEXER - program to insert HTML index files in a directory tree
#
# Andrew Herbert 19/06/2020

import os.path
import sys

def fullName (path, name):
    return path + '/' + name

def indexPath (path):
    outfile = open (path + '/index.html', 'w')
    outfile.write ('<html>\n')
    outfile.write ('<body>\n')
    outfile.write ('<table>\n')
    filenames = os.listdir (path)
    filenames.sort()
    count = 0
    for n in filenames:
        if n.startswith ('.'):
            continue
        pn = fullName (path, n)
        if n == 'index.htm' or n == 'index.html' or n == 'indexer.py':
            continue
        if count % 5 == 0:
            outfile.write ('<tr>\n')
        if os.path.isfile (pn):
            outfile.write ('<td style="padding:10px"><a href="' +
                               n + '">' + n + '</a></td>\n')
        if os.path.isdir (pn):
            outfile.write ('<td style="padding:10px"><a href="' +
                               n + '/index.html">' + n + '</a></td>\n')
            indexPath (pn)
        if count % 5 == 4:
            outfile.write ('</tr>\n')
        count = count + 1
    if count % 5 != 4:
        outfile.write ('</tr>\n')
    outfile.write ('</table>\n')
    outfile.write ('</body>\n')
    outfile.write ('</html>\n')
    outfile.close ()

# Main program
if len (sys.argv) < 2:
    indexPath ('.')
else:
    path = sys.argv[1]
    indexPath (path)
