import numpy as np
import itertools as it


class Itemset:
    """Takes in a set and support count for said set"""

    def __init__(self, s, sc):
        self.itemset = s
        self.support = sc

    def __len__(self):
        return len(self.itemset)

    def __repr__(self) -> str:
        return str(self.itemset)

    def __eq__(self, other):
        if isinstance(other, Itemset):
            return self.itemset == other.itemset
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Itemset):
            return self.support > other.support
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Itemset):
            return self.support >= other.support
        else:
            return NotImplemented

    def subs(self):
        sub = []
        for t in list(it.combinations(self.itemset, len(self.itemset)-1)):
            sub.append(Itemset(set(t), self.support))
        return sub


i4 = Itemset({"a", "c", "d", "e"}, 5)
i3b = Itemset({"a", "c", "d"}, 6)
i3a = Itemset({"a", "b", "e"}, 7)
i3c = Itemset({"b", "d", "e"}, 4)
i2a = Itemset({"a", "d"}, 11)
i2b = Itemset({"b", "d"}, 7)
i2c = Itemset({"b", "e"}, 8)
i2d = Itemset({"d", "e"}, 6)
i1a = Itemset({"b"}, 10)
i1b = Itemset({"d"}, 13)

c = {
    4: [],
    3: [],
    2: [],
    1: []
}

c[len(i4)].append(i4)
c[len(i3b)].append(i3b)
c[len(i3a)].append(i3a)
c[len(i3c)].append(i3c)
c[len(i2a)].append(i2a)
c[len(i2b)].append(i2b)
c[len(i2c)].append(i2c)
c[len(i2d)].append(i2d)
c[len(i1a)].append(i1a)
c[len(i1b)].append(i1b)

kmax = 4
for k in range(kmax, 1, -1):
    subs = []
    for i in c[k]:  # iterate through all itemsets with length k
        for s in i.subs():  # Extract all subsets from itemset i
            if s not in c[k-1]:  # Check if it already is in c
                if s in subs:
                    loc = subs.index(s)
                    if s.support > subs[loc].support:
                        subs[loc] = s  # Set itemset with largest support count.
                else:
                    subs.append(s)

    c[k-1].extend(subs)  # Extend set of closed itemsets to include all freq i.s.

for k in range(1, 5):
    # print('\nk =', k, '\nItemset{:<15}Support Count'.format(""))
    for i in sorted(c[k]):
        print('{:<25}{}'.format(str(sorted(i.itemset)), i.support))
