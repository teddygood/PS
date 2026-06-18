class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_set = set("aeiouAEIOU")

        s = list(s)
        vowel_idx = []
        vowels = []

        for i, c in enumerate(s):
            if c in vowels_set:
                vowel_idx.append(i)
                vowels.append(c)

        vowels.reverse()

        for i in range(len(vowel_idx)):
            s[vowel_idx[i]] = vowels[i]

        return "".join(s)