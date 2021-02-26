
class HashTable:

    def __init__(self, table_size=100):
        self.data = [[] for i in range(table_size)]
        self.n = table_size

    def get_hash(self, v):
        #オブジェクトのハッシュ値の計算（１００のあまり）
        return hash(v) % 100

    def search(self, key):
        i = self.get_hash(key)
        for j, v in enumerate(self.data[i]):
            if v[0] == key:
                return (i, j)
        return (i, -1)

    def set(self, key, value):
        i, j = self.search(key)
        if j != -1:
            #すでにあるキーの値を更新
            self.data[i][j][1] = value
        else:
            self.data[i].append([key, value])

    def get(self, key):
        i, j = self.search(key)
        if j != -1:
            return self.data[i][j][1]
        #キーが見つからない時にエラーを返す
        raise KeyError(f'{key} was not found in this HashTable')
