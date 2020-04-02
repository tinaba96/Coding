#https://qiita.com/maebaru/items/ace4de6272ddc1c18734

class MyHashSet(object):
    def __init__(self):
        self.hashset = [None]*10000
    # keyを10000で割った剰余を配列の添え字として返すハッシュ関数
    def hash(self, key):
        return key%10000

    def add(self, key):
        if self.contains(key):
            return
        idx = self.hash(key)
        if self.hashset[idx] is None:
            # 同じ位置に別のデータが保存される可能性があるため、配列として格納しておく
            self.hashset[idx] = [key]
        else:
             # すでに同じ位置に別のキーが格納されている場合、末尾に追加する
            self.hashset[idx].append(key)

    def remove(self, key):
        if not self.contains(key):
            return
        idx = self.hash(key)
        if self.hashset[idx] is not None:
            arr = self.hashset[idx]
            del arr[arr.index(key)]

    def contains(self, key):
        idx = self.hash(key)
        if self.hashset[idx] is None:
            return None
        else:
            arr = self.hashset[idx]
            return any(val == key for val in arr)

class MyHashMap(object):
    def __init__(self):
        self.hashmap = [None] * 10000

    def hash(self, key):
        return key%10000

    def put(self, key, value):
        idx = self.hash(key)
        if self.hashmap[idx] is None:
            self.hashmap[idx] = [(key, value)]
        else:
            arr = self.hashmap[idx]
            for i in range(len(arr)):
                pair = arr[i]
                if pair[0] == key:
                    del arr[i]
                    break
            arr.append((key, value))

    def get(self, key, value):
        idx = self.hash(key)
        if self.hashmap[idx] is None:
            return -1
        else:
            arr = self.hashmap[idx]
            for pair in arr:
                if pair[0] == key:
                    return pair[1]
            return -1

    def remove(self, key):
        if not self.contains(key):
            return
        idx = self.hash(key)
        arr = self.hashmap[idx]
        for i in range(len(arr)):
            pair = arr[i]
            if pair[0] == key:
                del arr[i]
                break

        '''
        for pair in arr:
            #print(pair)
            #print(arr[0])
            if pair[0] == key:
                #delはインデックスを用いた指定が必要
                arr.remove(pair)
                #del arr[0]
                break
        '''

    def contains(self, key):
        idx = self.hash(key)
        if self.hashmap[idx] is None:
            return None
        else:
            arr = self.hashmap[idx]
            for pair in arr:
                if pair[0] == key:
                    return True
            return False

s = MyHashMap()
s.put(10001, 1)
s.put(20001, 21)
s.put(10002, 2)
print(s.hashmap[:3])
s.remove(10001)
print(s.hashmap[:3])




