#Nom, matricule
#Nom, matricule

#Fonction à compléter. Ne modifiez pas sa signature.
#N : Force maximale
#k : Nombre de fenêtres disponibles
#Valeur de retour : le nombre minimal de tests qu'il faut faire 
#                   en pire cas pour déterminer le seuil de solidité 
#                   d'une fenêtre
#Doit retourner la réponse comme un int.
#
#Function to complete. Do not change its signature.
#N : Maximum force
#k : Number of windows available
#return value : Minimum number of tests needed in the worst case
#               to find the solidity threshold of a window
#Must return the answer as an int. 

import math
import sys

 # for k=2, the minimum tests needed is
def minTests2(b):
    return math.ceil((-1+math.sqrt(8*b+1))/2)

def vitre(N, k):

    # if k >= floor(lg(N)), then minimum number of tests needed is ceil(lg(N)).
    if k>= math.floor(math.log2(N)):
        return math.ceil(math.log2(N))
    


    table = [[0 for _ in range(k+1)] for _ in range(N)]       #[b,k], b: nb of forces to test, k: nb of windows available 

    for i in range(len(table)):
        table[i][1]=i           # if k=1, we need b tests in worst case to find the solidity threshold of a window
        if len(table[i])>2:
            table[i][2]=minTests2(i)

    for i in range(len(table)):
        for j in range(3, k+1):
            if i<j:
                table[i][j]= table[i][j-1]
            
            else:
                 table[i][j]= min(table[math.floor(i/j)][j-1]+1, table[i-math.floor(i/j)][j]+1)

    #        print("b=", str(i), "a=", str(j), "b/a, a-1=", str(table[math.floor(i/j)][j-1]+1), " b-b/a, a= ", str(table[i-math.floor(i/j)][j]+1))

    print(table)
    
    return table[-1][-1]



#Fonction main, vous ne devriez pas avoir à modifier
#Main function, you shouldn't have to modify it
def main(args):
    N = int(args[0])
    k = int(args[1])
 

    answer = vitre(N,k)
    print(answer)

if __name__ == '__main__':
    main(sys.argv[1:])