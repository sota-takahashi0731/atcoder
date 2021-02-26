
class UnionFind():
    ##作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が気の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        #木をくっつけるときにアンバランスにならないように調整する
        self.rnk = [0]*(n+1)

    #ノードxのrootノードを見つける
    def Find_Root(self, x):
        if (self.root[x]<0):
            return x
        else:
            #ここで代入しておくことで後の繰り返しを避ける
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    #木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        #入力ノードのrootノードを見つける
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        #すでに同じ木に属していた場合
        if (x==y):
            return
        #違う木に属していた場合rnkを見てくっつける方を決める
        elif(self.rnk[x] > self.rnk[y]):
            #rootに要素数を加算（要素数はrootノードで負の値として格納）
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            #rootに要素数を加算（要素数はrootノードで負の値として格納）
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ(深さに差がない場合)は１増やす
            if (self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    #xとyが同じグループに属するか判断]
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def Count(self, x):
        return -self.root[self.Find_Root(x)]
