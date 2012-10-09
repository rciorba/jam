googlese = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd "\
    "de kr kd eoya kw aej tysr re ujdr lkgc jv y qee"
english = "our language is impossible to understand there are twenty six factorial possibilities "\
    "so it is okay if you want to just give up a zoo"


trans = {}
alph = u"abcdefghijklmnopqrstuvwxyz"

for g, e in zip(googlese, english):
    # if e in trans and trans[e] != g:
    #     import pdb; pdb.set_trace()
    trans[g] = e

set_alph = set(alph)
missing_input, = tuple(set_alph - set(trans.iterkeys()))
missing_expected, = tuple(set_alph - set(trans.itervalues()))
# import ipdb; ipdb.set_trace()
import string
trans = string.maketrans(googlese+missing_input, english+missing_expected)

import sys
data = open(sys.argv[1]).readlines()
case = 1
for line in data[1:]:
    print >> sys.stderr, line[0:-1]
    print "Case #%d: %s" % (case, line[0:-1].translate(trans))
    case += 1
