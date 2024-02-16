# *와 ?를 어떻게 처리할 것인지

def match(w, s):
    idx = 0
    while ((idx < len(s) and idx < len(w)) and
           (w[idx] == "?" or w[idx] == s[idx])):
        idx += 1

    if idx == len(w):
        return idx == len(s)

    if w[idx] == "*":
        for skip in range(idx, len(s) + 1):
            if match(w[idx + 1:], s[idx + skip:]):
                return True
    return False

for _ in range(int(input())):
    wildcard = input()
    for _ in range(int(input())):
        s = input()
        if match(wildcard, s):
            print(s)
