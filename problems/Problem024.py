
class PermutationFinder:
    def __init__(self, permList = []):
        self.permList = permList

    def getFactoradic(self, number):
        factoradic = []
        index = 1
        while number != 0:
            remainder = number % index
            factoradic.insert(0, remainder)
            number = number // index
            index = index + 1
        return factoradic

    def find(self, index):
        result = []
        for x in self.getFactoradic(index-1):
            result.append(self.permList[x])
            self.permList.pop(x)
        return result

if __name__ == '__main__':
    print("[Begin]")
    finder = PermutationFinder([0,1,2,3,4,5,6,7,8,9])
    print("One Millionth Permutation:", finder.find(1000000))
