import numpy as np
from PIL import Image

#The goal of this file is to implement the prime number distance encrypting of picture
#That consist in reordering the column and line by wich column number is the closest to a prime number

def list_prime(n): #makes the list of the prime numbers beetween 2 and 2*n
    l=[2]
    for k in range(3, 2*n):
        prime = 0
        for i in range(len(l)):
            if (k % l[i]==0):
                prime = 1
        if prime==0:
            l.append(k)
    return l
def asso_prime(n):#finds the closest prime number for each number beetween 1 and n
    l = []
    l_prime = list_prime(n)
    for k in range(n):
        prime=l_prime[0]
        for i in range(1,len(l_prime)):
            if(abs(k-prime)>abs(k-l_prime[i])):
                prime=l_prime[i]
        l.append([k,prime])
    return l
def sort_prime(n):
    #sorts the numbers beetwen 1 and n by the distance with their closest prime number
    #if two numbers have an equal distance, the one with the smalest prime number is the smallest
    l_asso=asso_prime(n)
    l=[]
    while len(l_asso)>0 :
        asso_min = l_asso[0]
        for k in range(1,len(l_asso)):
            dmin = abs(asso_min[0]-asso_min[1])
            dprime = abs(l_asso[k][0]-l_asso[k][1])
            if(dmin > dprime):
                asso_min = l_asso[k]
            elif(dmin == dprime and asso_min[1] > l_asso[k][1]):
                asso_min = l_asso[k]
                print(asso_min)
            elif(dmin == dprime and asso_min[1] == l_asso[k][1] and asso_min[0] > l_asso[k][0]):
                asso_min = l_asso[k]
                print(asso_min)
        l.append(asso_min[0])
        l_asso.remove(asso_min)
    return l
#ça buggue
def encrypt(mat):#permutates the lines and column acording to the prime sorting
    abs=sort_prime(len(mat))
    ord=sort_prime(len(mat[0]))
    mat_e=[[0]*len(mat[0]) for i in range(len(mat))]
    for a in range(len(abs)):
        for o in range(len(ord)):
            mat_e[abs[a]][ord[o]]=mat[a][o]
    return mat_e
def decrypt(mat):#permutates back into the right order
    abs=sort_prime(len(mat))
    ord=sort_prime(len(mat[0]))
    mat_d=[]
    for a in range(len(abs)):
        ord_d=[]
        for o in range(len(ord)):
            ord_d.append(mat[abs[a]][ord[o]])
        mat_d.append(ord_d)
    return mat_d

def print_matrix(mat):
    for row in mat:
        line = ""
        for column in row:
            line = line + f"{column} "
        print(line)
    print()

def process_image(path, action):
    img = Image.open(path)
    mat = np.array(img).tolist()

    if action == "encrypt":
        result_mat = encrypt(mat)
    elif action == "decrypt":
        result_mat = decrypt(mat)
    else:
        raise ValueError("Action must be 'encrypt' or 'decrypt'.")

    result_img = Image.fromarray(np.array(result_mat, dtype=np.uint8))
    output_path = path.replace(".png", f"_{action}.png")
    result_img.save(output_path)
    print(f"{action.capitalize()}ed image saved to {output_path}")

#process_image("ender_pearl.png", "encrypt")
#process_image("ender_pearl_encrypt.png", "decrypt")