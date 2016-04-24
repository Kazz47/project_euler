import math

class PermutationFinder:
    def __init__(self, permList = []):
        self.permList = permList

    def find(self, index):
        numPerms = math.factorial(len(self.permList))
        if index > numPerms:
            raise ValueError("List only has " + str(numPerms) + " permutations.")

        listCopy = list(self.permList);
        result = []
        for x in self.getFactoradic(index-1):
            result.append(listCopy[x])
            listCopy.pop(x)
        return result

    @staticmethod
    def getFactoradic(number):
        factoradic = []
        index = 1
        while number != 0:
            remainder = number % index
            factoradic.insert(0, remainder)
            number = number // index
            index = index + 1
        return factoradic

if __name__ == '__main__':
    print("[Begin]")
    finder = PermutationFinder([0,1,2,3,4,5,6,7,8,9])
    print("One Millionth Permutation:", finder.find(1000000))
