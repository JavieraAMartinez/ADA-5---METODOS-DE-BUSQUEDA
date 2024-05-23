class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

tabla_hash = HashTable(10)
tabla_hash.insert("clave1", 10)
tabla_hash.insert("clave2", 20)
tabla_hash.insert("clave3", 30)

print(tabla_hash.search("clave2"))
print(tabla_hash.search("clave4"))

