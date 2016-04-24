import csv

class NameScorer:
    def scoreLetter(self, letter):
        return ord(letter) - ord("A") + 1;

    def scoreName(self, name):
        score = 0
        for letter in name.upper():
            score += self.scoreLetter(letter)
        return score

    def scoreList(self, names):
        score = 0
        names.sort()
        for idx, name in enumerate(names):
            score += self.scoreName(name) * (idx + 1)
        return score

    def scoreFile(self, filePath):
        score = 0
        try:
            with open(filePath, 'rt') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in reader:
                    score += self.scoreList(row)
        except EnvironmentError:
            print("File " + filePath + " could not be opened.")
        return score

if __name__ == '__main__':
    print("[Begin]")
    print("Total File Score:", scoreFile("names.txt"))
