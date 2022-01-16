import re
from collections import Counter


# sþółgloski samogloski
class TextAnalyzer:
    def numberOfLines(self, filename):
        file = open(filename, "rt")
        data = file.read()
        data = re.sub('[^\n]', '', data)
        file.close()
        return len(data) + 1

    def numberOfUppercase(self, filename):
        file = open(filename, "rt")
        data = file.read()
        data = re.sub('[^A-Z]', '', data)
        file.close()
        return len(data)

    def numberOfLowercase(self, filename):
        file = open(filename, "rt")
        data = file.read()
        data = re.sub('[^a-z]', '', data)
        file.close()
        return len(data)

    def numberOfWords(self, filename):
        file = open(filename, "rt")
        data = file.read()
        data = re.sub('[,]', '', data)
        words = data.split()
        file.close()
        return len(words)

    def numberOfAllCharacters(self, filename):
        file = open(filename, "rt")
        data = file.read()
        character = 0
        file.close()

        for word in data:
            character += len(word)

        return character

    def numberOfSpecialCharacters(self, filename):
        file = open(filename, "rt")
        data = file.read()
        data = re.sub('[A-Za-z0-9 \n]', '', data)
        file.close()
        return len(data)

    def countEachWord(self, filename):
        with open(filename) as file:
            t = Counter(file.read().lower().split())

        file.close()
        return t

    # samogłoski
    def countVowels(self, filename):
        file = open(filename, "rt")
        data = file.read()
        data = re.sub('[^AEIOUYaeiouy]', "", data)
        t = Counter(data)
        file.close()
        return t

    # sþółgloski
    def countConsonants(self, filename):
        file = open(filename, "rt")
        data = file.read()
        data = re.sub('[^BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz]', "", data)
        t = Counter(data)
        file.close()
        return t
