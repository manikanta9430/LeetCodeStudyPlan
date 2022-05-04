class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []
        for d in path.split('/'):
            if not d or d == '.':
                continue
            elif d == '..':
                if dirs:
                    dirs.pop(-1)
            else:
                dirs.append(d)
        return '/' + '/'.join(dirs)
