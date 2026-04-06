class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        a   d   c   d   g
        e   z   f   x   b

        map for s -> t and t -> s and they both need to match

        s map 
        {a: e
        d: z
        c: f
        }
        '''
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            if s[i] in sMap and sMap[s[i]] != t[i]:
                return False
            elif t[i] in tMap and tMap[t[i]] != s[i]:
                return False
            sMap[s[i]] = t[i]
            tMap[t[i]] = s[i]
        return True