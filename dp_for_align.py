import numpy as np
import ast
seq1 = input()
seq2 = input()

l1 = len(seq1)
l2 = len(seq2)

#Adjust the following variables#
match = 1
mismatch = -1
gap_penalty = -1

mat = np.full( (l1+1,l2+1), np.nan)
back_track = [['' for j in range(l2+1)] for j in range(l1+1)]
def compare(char1,char2):
    if char1==char2:
        return match
    else:
        return mismatch

def score(i,j):
    if not np.isnan(mat[i][j]):
        return mat[i][j]
    else:
        mat[i][j] = max(score(i-1,j-1)+compare(seq1[i-1],seq2[j-1]), score(i-1,j)+gap_penalty, score(i,j-1)+gap_penalty)
        if mat[i][j] == score(i-1,j-1)+compare(seq1[i-1],seq2[j-1]):
            back_track[i][j] = str((i-1,j-1))
        elif mat[i][j] == score(i-1,j)+gap_penalty:
            back_track[i][j] = str((i-1,j))
        else:
            back_track[i][j] = str((i,j-1))
            
        return mat[i][j]

for i in range(l1+1):
    mat[i][0] = i*gap_penalty


for j in range(l2+1):
    mat[0][j] = j*gap_penalty

mat[l1][l2] = score(l1,l2)

align1 = ''
align2 = ''

start = (l1,l2)

while not (start[0]==0 or start[1]==0):
    if back_track[start[0]][start[1]]!='':
        new_index = ast.literal_eval(back_track[start[0]][start[1]])
        if new_index == (start[0]-1,start[1]-1):
            align1 = seq1[start[0]-1] + align1
            align2 = seq2[start[1]-1] + align2
        elif new_index == (start[0]-1,start[1]):
            align1 = seq1[start[0]-1] + align1
            align2 = '-' + align2
        else:
            align2 = seq2[start[1]-1] + align2
            align1 = '-' + align1
    start = new_index

if start[0]!=0:
    align1 = seq1[0:start[0]] + align1
    align2 = '-'*start[0] + align2
elif start[1]!=0:
    align2 = seq2[0:start[1]] + align2
    align1 = '-'*start[1] + align1

print(align1)
print(align2)