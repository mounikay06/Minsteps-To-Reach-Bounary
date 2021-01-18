from collections import deque

#function to check validity
def valid (i, j, n, m):
    return (0 <= i< n) and (0 <= j< m)

#function to find out min steps to reach boundary
def findMinSteps(matrix, x, y):
    q = deque([[0, x ,y]])    
    visited = {}

    n, m = len(matrix), len(matrix[0])

    ans = float('inf')

    while q:
        w, i, j  = q.popleft()

        if (visited.get((i, j), False)):
            continue

        visited[(i, j)] = True

        #print(ans, [w, i, j])

        if i == 0 or j == 0:
            ans = min(ans, w)
        
        if valid(i+1, j, n, m) and matrix[i +1][j] == 0:
            q.append([w+1, i+1, j])
        if valid(i-1, j, n, m) and matrix[i-1][j] == 0:
            q.append([w+1, i-1, j])
        if valid(i, j +1, n, m) and matrix[i][j+1] == 0:
            q.append([w+1, i, j +1])
        if valid(i, j-1, n, m) and matrix[i][j-1] == 0:
            q.append([w+1, i, j-1])    

    return ans
#Input 
r=1
c=2
matrix=[[1,1,1,0,1],
        [1,0,0,0,1],
        [0,0,1,0,1],
        [1,0,1,1,0]];
print(findMinSteps(matrix,r,c))
