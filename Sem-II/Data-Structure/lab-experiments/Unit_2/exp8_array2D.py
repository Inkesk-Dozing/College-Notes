class Array2D:
    def __init__(self, mat):
        self.mat = mat
        self.rows = len(mat)
        self.cols = len(mat[0])
        
    def row_sum(self, row):
        sum = 0
        if row > self.rows or row < 0:
            return "Invalid Row"
        for i in range(self.cols):
            sum += self.mat[row][i]
        return sum
    
    def col_sum(self, col):
        sum = 0
        if col > self.cols or col < 0:
            return "Invalid Column"
        for i in range(self.rows):
            sum += self.mat[i][col]
        return sum
    
    def search(self, val):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.mat[i][j] == val:
                    print(f"Element found at row: {i} column: {j}")
                    return
        print("Element not found")
    
    def transpose(self):
        newMat = []
        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append(self.mat[j][i])
            newMat.append(row)
        print(newMat)
    
    

def main():
    mat = [[1,2],[4,5],[7,8]]
    matObj = Array2D(mat)
    print(matObj.row_sum(0))
    print(matObj.col_sum(0))
    matObj.search(9)
    matObj.transpose()
    
if __name__ == "__main__":
    main()