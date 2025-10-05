def get_minor(matrix, r, c):
    return [row[:c] + row[c+1:] for row in matrix[:r] + matrix[r+1:]]

def get_determinant(matrix):
    determinant = 0
    size = len(matrix)
    if size == 2:
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for col in range(size):
            minor = get_minor(matrix, 0, col)
            determinant += (-1) ** col * matrix[0][col] * get_determinant(minor)
    return determinant

def get_inverse_by_determinant(matrix):
    determinant = get_determinant(matrix)
    if determinant == 0:
        return "역행렬이 존재하지 않습니다"
    cofactor = [[0] * size for _ in range(size)]
    for row in range(size):
        for col in range(size):
            minor = get_minor(matrix, row, col)
            cofactor[row][col] = (-1) ** (row+col) * get_determinant(minor)
            cofactor[row][col] /= determinant
    inverse = [[cofactor[j][i] for j in range(size)] for i in range(size)]
    return inverse
def get_inverse_by_gauss_jordan(matrix):
    identity = [[0 if i != j else 1 for j in range(size)] for i in range(size)]

    aug_matrix = [matrix[i] + identity[i] for i in range(size)]
    for i in range(size):
        pivot_row = i
        pivot_val = aug_matrix[i][i]
        if pivot_val == 0:
            return "역행렬이 존재하지 않습니다"
        for j in range(i, 2*size):
            aug_matrix[i][j] /= pivot_val
        for j in range(size):
            if i != j:
                factor = aug_matrix[j][i]
                for k in range(i, 2*size):
                    aug_matrix[j][k] -= factor*aug_matrix[i][k]

    inverse = [row[size:] for row in aug_matrix]
    return inverse

size = int(input("정방행렬의 크기 입력: "))
matrix = [[0] * size for _ in range(size)]
for i in range(size):
    while True:
        row_input = list(map(int,input(f"정방행렬의 {i+1}행 입력: ").split()))
        if len(row_input) != size:
            print("데이터를 정확히 입력하세요.")
        else:
            break
    matrix[i] = row_input
inverse_by_determinant = get_inverse_by_determinant(matrix)
print("행렬식 이용하여 구한 역행렬")
if type(inverse_by_determinant) == str:
    print(inverse_by_determinant)
else:
    for i in range(size):
        for j in range(size):
            print(inverse_by_determinant[i][j], end = ' ')
        print()
print("가우스-조던 소거법 이용하여 구한 역행렬")
inverse_by_gauss_jordan = get_inverse_by_gauss_jordan(matrix)
if type(inverse_by_gauss_jordan) == str:
    print(inverse_by_gauss_jordan)
else:
    for i in range(size):
        for j in range(size):
            print(inverse_by_gauss_jordan[i][j], end = ' ')
        print()
if inverse_by_determinant == inverse_by_gauss_jordan:
    print("두 역행렬이 일치합니다")
else:
    print("두 역행렬이 일치하지 않습니다")
print("역행렬을 이용하여 원본 행렬 구하기")
if type(inverse_by_determinant) == str:
    print("역행렬이 존재하지 않아 원본 행렬을 구할 수 없음")

else:
    new_matrix = get_inverse_by_determinant(inverse_by_determinant)
    for i in range(size):
        for j in range(size):
            print(new_matrix[i][j], end = ' ')
        print()
