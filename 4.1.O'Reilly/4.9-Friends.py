#checkio_SolveStripedWords


##########
#Answer

class Friends:
    def __init__(self, conns=[]):
        self.conns=list(conns)

    def add(self, conn):
        if conn in self.conns:
            return False
        else:
            self.conns.append(conn)
            return True

    def remove(self, conn):
        if conn in self.conns:
            self.conns.remove(conn)
            return True
        else:
            return False

    def names(self):
        _d=set()
        for s in self.conns:
            _d=_d.union(s)
        return _d

    def connected(self, name):
        _d = set()
        for s in self.conns:
            if name in s:
                _d=_d.union(s)
        _d.discard(name)
        return _d
        


##########
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
