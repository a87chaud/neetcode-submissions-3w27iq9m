class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        print(dirs)
        final = []
        for d in dirs:
            print(final)
            if not d or d == '.':
                continue
            elif d != '..':
                final.append(d)
                # final.append('/')
            else:
                if final:
                    final.pop()
        res = ['/']
        for i, f in enumerate(final):
            res.append(f)
            if i != len(final) - 1:
                res.append('/')
        return ''.join(res)
    
    '''
    /./././neetcode
    /neetcode
    '''