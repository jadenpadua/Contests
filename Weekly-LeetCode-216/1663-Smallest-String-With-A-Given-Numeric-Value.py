#Greedy Med
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        k -= n

        ht = defaultdict(str)
        
        for i, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
            ht[i] = char
            
        i = n - 1
        
        while k > 0:
            temp = min(k, 25)
            res[i] = ht[temp]
            k -= temp
            i -= 1
        
        return "".join(res)
