
class DiagonalSum:
    vertices = 4

    @staticmethod
    def find(dimensions):
        diagonalSum = 1
        currentVal = 1
        for d in range(3, dimensions+1, 2):
            for v in range(0, DiagonalSum.vertices):
                currentVal += d - 1
                diagonalSum += currentVal
        return diagonalSum

if __name__ == '__main__':
    print("[Begin]")
    print("Diagonl Sum of 1001x1001:", DiagonalSum.find(1001))
