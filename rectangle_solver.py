from typing import List

def largest_rectangle(matrix: List[List[int]]) -> tuple:
    if not matrix or not matrix[0]:
        return 0, 0

    rows, cols = len(matrix), len(matrix[0])
    max_area = 0
    result_number = None

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != -9:  
                number = matrix[row][col]
                area = 0

                
                stack = [(row, col)]
                while stack:
                    r, c = stack.pop()
                    if 0 <= r < rows and 0 <= c < cols and matrix[r][c] == number:
                        area += matrix[r][c]
                        matrix[r][c] = -9  
                        stack.append((r + 1, c))  
                        stack.append((r, c + 1))  
                        stack.append((r - 1, c))  
                        stack.append((r, c - 1))  

                
                if area > max_area:
                    max_area = area
                    result_number = number

    return result_number, max_area
