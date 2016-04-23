from problems.Problem022 import NameScorer
import unittest

class test_problem022(unittest.TestCase):

    def test_scoreLetter(self):
        scorer = NameScorer()
        self.assertEqual(1, scorer.scoreLetter("A"))
        self.assertEqual(26, scorer.scoreLetter("Z"))

    def test_scoreName_kyle(self):
        name = "kyle"
        expectedScore = 11 + 25 + 12 + 5;

        scorer = NameScorer()
        self.assertEqual(expectedScore, scorer.scoreName(name))

    def test_scoreName_hannah(self):
        name = "hannah"
        expectedScore = 8 + 1 + 14 + 14 + 1 + 8;

        scorer = NameScorer()
        self.assertEqual(expectedScore, scorer.scoreName(name))

    def test_scoreList(self):
        names = ["kyle", "hannah"]
        expectedScore = (46 * 1) + (53 * 2)

        scorer = NameScorer()
        self.assertEqual(expectedScore, scorer.scoreList(names))

    def test_scoreFile(self):
        filePath = "data/names.txt"
        expectedScore = 871198282

        scorer = NameScorer()
        self.assertEqual(expectedScore, scorer.scoreFile(filePath))



if __name__ == '__main__':
    unittest.main()
