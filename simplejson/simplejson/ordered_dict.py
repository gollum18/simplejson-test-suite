"""Drop-in replacement for collections.OrderedDict by Raymond Hettinger

http://code.activestate.com/recipes/576693/

"""

try:
    from UserDict import UserDict
    from UserDict import DictMixIn
except ImportError:
    from collections import UserDict
    from collections import MutableMapping as DictMixIn


class OrderedDict(dict, DictMixIn):

    def __init__(self, *args, **kwds):
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        try:
            self.__end
        except AttributeError:
            self.clear()
        self.update(*args, **kwds)

    def clear(self):
        self.__end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self.__map = {}                 # key --> [key, prev, next]
        dict.clear(self)

    def __setitem__(self, key, value):
        if key not in self:
            end = self.__end
            curr = end[1]
            curr[2] = end[1] = self.__map[key] = [key, curr, end]
        dict.__setitem__(self, key, value)

    def __delitem__(self, key):
        dict.__delitem__(self, key)
        key, prev, next = self.__map.pop(key)
        prev[2] = next
        next[1] = prev

    def __iter__(self):
        end = self.__end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.__end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def popitem(self, last=True):
        if not self:
            raise KeyError('dictionary is empty')
        try: # Python 2
            key = reversed(self).next() if last else iter(self).next()
        except AttributeError: # Python 3
            key = next(reversed(self)) if last else next(iter(self))

        value = self.pop(key)
        return key, value

    def __reduce__(self):
        items = [[k, self[k]] for k in self]
        tmp = self.__map, self.__end
        del self.__map, self.__end
        inst_dict = vars(self).copy()
        self.__map, self.__end = tmp
        if inst_dict:
            return self.__class__, (items,), inst_dict
        return self.__class__, (items,)

    def keys(self):
        return list(self)

    setdefault = DictMixIn.setdefault
    update = DictMixIn.update
    pop = DictMixIn.pop
    values = DictMixIn.values
    items = DictMixIn.items
    try: # Python2 support - returns live view of these values
        iterkeys = DictMixIn.iterkeys
        itervalues = DictMixIn.itervalues
        iteritems = DictMixIn.iteritems
    except AttributeError: # Python3 support - returns set based view
        iterkeys = DictMixIn.keys
        itervalues = DictMixIn.values
        iteritems = DictMixIn.items


    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, self.items())

    def copy(self):
        return self.__class__(self)

    @classmethod
    def fromkeys(cls, iterable, value=None):
        d = cls()
        for key in iterable:
            d[key] = value
        return d

    def __eq__(self, other):
        if isinstance(other, OrderedDict):
            return len(self)==len(other) and \
                   all(p==q for p, q in  zip(self.items(), other.items()))
        return dict.__eq__(self, other)

    def __ne__(self, other):
        return not self == other
