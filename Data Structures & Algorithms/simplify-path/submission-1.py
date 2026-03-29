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
            else:
                if final:
                    final.pop()
        return '/' + '/'.join(final)
    
    '''
    /./././neetcode
    /neetcode
    '''