class HashFunction:
    def __init__(self, initial_capacity=40):
        self.table = [[] for _ in range(initial_capacity)]

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        for kv in self.table[bucket]:
            if kv[0] == key:
                kv[1] = item
                return
        self.table[bucket].append([key, item])

    def search(self, key):
        bucket = hash(key) % len(self.table)
        for kv in self.table[bucket]:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        for kv in self.table[bucket]:
            if kv[0] == key:
                self.table[bucket].remove(kv)