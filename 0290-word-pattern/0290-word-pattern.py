class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(' ')
        print(words)

        if len(words) != len(pattern):
            return False

        word_to_char = {}
        char_to_word = {}

        for char , word in zip(pattern , words):
            if (char not in char_to_word) and (word not in word_to_char):
                word_to_char[word] = char
                char_to_word[char] = word

            # elif char_to_word[char] != word or word_to_char[word] != char: # 可能有對應不到的
            elif char_to_word.get(char) != word or word_to_char.get(word) != char:
                return False

        return True