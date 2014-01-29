from collections import defaultdict
import sys

from blist import sortedlist


def not_really_anagrams(lines):
    data = defaultdict(sortedlist)
    for line in lines:
        word = line.strip()
        anagram = word[::-1]
        if anagram in data[len(word)]:
            print anagram, word
        else:
            data[len(word)].add(word)


def anagrams(lines):
    data = defaultdict(list)
    for line in lines:
        word = line.strip()
        key = "".join(sorted(word))
        data[key].append(word)
    for words in data.itervalues():
        print ", ".join(words)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        inf = open(sys.argv[1])
    else:
        inf = sys.stdin
    anagrams(inf.xreadlines())
