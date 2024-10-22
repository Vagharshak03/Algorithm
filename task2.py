#Longest common subsequence
def lcs(text1, text2):
    len1 = len(text1)
    len2 = len(text2)

    sub = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if text1[i - 1] == text2[j - 1]:
                sub[i][j] = sub[i - 1][j - 1] + 1
            else:
                sub[i][j] = max(sub[i - 1][j], sub[i][j - 1])

    return sub[len1][len2]

text1 = str(input("Word1: "))
text2 = str(input("Word2: "))

print("Length of LCS is", lcs(text1, text2))
