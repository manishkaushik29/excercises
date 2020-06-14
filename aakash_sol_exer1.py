def lols(s):
    i = 0
    j = 0
    d = {}
    ans = 0
    while i < len(s):
        if s[i] not in d or j > d[s[i]]:
            ans = max(ans, (i - j + 1))
            d[s[i]] = i
        else:
            j = d[s[i]] + 1
            ans = max(ans, (i - j + 1))
            i -= 1
        i += 1

    return ans


p = lols("abcabcbb")
q=lols("bbbbbb")
w=lols("pwkeeertrr")
print(p)