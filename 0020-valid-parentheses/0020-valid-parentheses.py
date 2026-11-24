class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_para = {
        '(':')',
        '[':']',
        '{':'}'
    }
        for ch in s:
            if ch in valid_para:
                stack.append(valid_para[ch])
            else:
                if not stack:
                    return False
                out = stack.pop()

                if ch != out:
                    return False
        return not stack
