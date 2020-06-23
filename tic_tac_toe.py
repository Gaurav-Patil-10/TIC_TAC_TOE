import string
def horizontal(l1):
    if l1[0] == l1[1] == l1[2]:
        return f"{l1[0]} wins"
    elif l1[3] == l1[4] == l1[5]:
        return f"{l1[3]} wins"
    elif l1[6] == l1[7] == l1[8]:
            return f"{l1[6]} wins"
    else:
        return False

def vertical(l1):
    if l1[0] == l1[3] == l1[6]:
        return f"{l1[0]} wins"
    elif l1[1] == l1[4] == l1[7]:
        return f"{l1[1]} wins"
    elif l1[2] == l1[5] == l1[8]:
            return f"{l1[2]} wins" 
    else:
        return False

def diagonal (l1):
    if l1[0] == l1[4] == l1[8]:
        return f"{l1[0]} wins"
    elif l1[2] == l1[4] == l1[6]:
        return f"{l1[2]} wins"
    else:
        return False

def impossible(l1):
    count1 = 0 # X
    count2 = 0 # o
    for x in l1:
        if x == "X":
            count1 += 1
        elif x == "O":
            count2 += 1
        else:
            continue
    if (count2 - count1) >= 2 or (count1 - count2) >= 2:
        print("Impossible")
    else:
        return True

def duplicate(l1):
    if l1[0] == l1[1] == l1[2] and l1[3] == l1[4] == l1[5] :
        print("Impossible")
    elif l1[3] == l1[4] == l1[5] and l1[6] == l1[7] == l1[8] :
        print("Impossible")
    elif l1[0] == l1[3] == l1[6] and l1[1] == l1[4] == l1[7] :
        print("Impossible")
    elif l1[1] == l1[4] == l1[7] and l1[2] == l1[5] == l1[8] :
        print("Impossible")
    else:
        return True


def print1(m):
    print(f'''---------
| {m[0]} {m[1]} {m[2]} |
| {m[3]} {m[4]} {m[5]} |
| {m[6]} {m[7]} {m[8]} |
---------''')
    

def table_val (m  , k1 , k2 , val):
        if k1 == 1 and k2 == 3:
            if m[0] != "_":
                return False
            else:
                m[0] = val
        elif k1 == 2 and k2 == 3:
            if m[1] != "_":
                return False
            else:
                m[1] = val
        elif k1 == 3 and k2 == 3:
            if m[2] != "_":
                return False
            else:
                m[2] = val
        elif k1 == 1 and k2 == 2:
            if m[3] != "_":
                return False
            else:
                m[3] = val
        elif k1 == 2 and k2 == 2:
            if m[4] != "_":
                return False
            else:
                m[4] = val
        elif k1 == 3 and k2 == 2:
            if m[5] != "_":
                return False
            else:
                m[5] = val
        elif k1 == 1 and k2 == 1:
            if m[6] != "_":
                return False
            else:
                m[6] = val
        elif k1 == 2 and k2 == 1:
            if m[7] != "_":
                return False
            else:
                m[7] = val
        elif k1 == 3 and k2 == 1:
            if m[8] != "_":
                return False
            else:
                m[8] = val
        else:
            return 5

        
            



    # (1, 3) (2, 3) (3, 3)
    # (1, 2) (2, 2) (3, 2)
    # (1, 1) (2, 1) (3, 1)

if __name__ == "__main__":
    m = ["_"] * 9
    print1(m)
    x = 1
    while x != 10:
        try: 
            k = input("Enter the Coordinates: ").split(" ")
            k1 = [int(x) for x in k]
            if x%2 == 0 or x < 1:
                d = table_val(m , k1[0] , k1[1] , "O")
            else:
                d = table_val(m , k1[0] , k1[1] , "X")

            if d == False:
                print("This cell is occupied! Choose another one!")
                
                
                
                
            elif d == 5:
                print("Coordinates should be from 1 to 3!")
                
                
                
                
            else:
                
                print1(m)
                x = x + 1
                

        except Exception as e:
            print("You should enter numbers!")
            
            

        ans1 = horizontal(m)
        ans2 = vertical(m)
        ans3 = diagonal(m)
        count_ = 0
        for xs in m :
            if xs == "_":
                count_ += 1
        if ans1 == "X wins" or ans1 == "O wins":
            print(ans1)
            break
            
        elif ans2 == "X wins" or ans2 == "O wins":
            print(ans2)
            break
            
        elif ans3 == "X wins" or ans3 == "O wins":
            print(ans3)
            break

        if ans1 == False and ans2 == False and ans3 == False:
            if count_ == 0:
                print("Draw")
            else:
                continue
        

        


               

        
        

        


    
            

    
                
            
                
                        
            
            

            
        
        

       


        
        
    
        

        
            

             
               

                 

        








                    # ans1 = horizontal(m)
                    # ans2 = vertical(m)
                    # ans3 = diagonal(m)
                    # if ans1 == "X wins" or ans1 == "O wins":
                    #     print(ans1)
                    #     cont = False
                    # elif ans2 == "X wins" or ans2 == "O wins":
                    #     print(ans2)
                    #     cont = False
                    # elif ans3 == "X wins" or ans3 == "O wins":
                    #     print(ans3)
                    #     cont = False      
       
                    # k = input("Enter the Coordinates: ").split(" ")
                    # k1 = [int(x) for x in k]
                    # d = table_val(m , k1[0] , k1[1] , "O")
                    # if d == False:
                    #     print("The cell is occupied")
                    # elif d == 5:
                    #     print("Co-ordinates must be in 1 to 3")
                    # else:
                    #     print1(m)
                    #     b2 = False
                    #     cont = True




    
   
#         if k == "1 3":
#             if m[0] == "_":
#                 m[0] = 'X'
#                 break

#             else:
#                 print('This cell is occupied! Choose another one!')


#         elif k == "2 3":
#             if m[1] == "_":
#                 m[1] = 'X'
#                 break

#             else:
#                 print('This cell is occupied! Choose another one!')


#         elif k == "3 3":
#             if m[2] == "_":
#                 m[2] = 'X'
#                 break

#             else:
#                 print('This cell is occupied! Choose another one!')


#         elif k == "1 2":
#             if m[3] == "_":
#                 m[3] = 'X'
#                 break

#             else:
#                 print('This cell is occupied! Choose another one!')


#         elif k == "2 2":
#             if m[4]== "_":
#                 m[4] = 'X'
#                 break

#             else:
#                 print('This cell is occupied! Choose another one!')

#         elif k == "3 2":
#             if m[5] == "_":
#                 m[5] = 'X'
#                 break

#             else:
#                 print('This cell is occupied! Choose another one!')


#         elif k == "1 1":
#             if m[6] == "_":
#                 m[6] = 'X'
#                 break
#             else:
#                 print('This cell is occupied! Choose another one!')


#         elif k == "2 1":
#             if m[7] == "_":
#                 m[7] = 'X'
#                 break

#             else:
#                 print('This cell is occupied! Choose another one!')


#         elif k == "3 1":
#             if m[8] == "_":
#                 m[8] = 'X'
#                 break
#             else:
#                 print('This cell is occupied! Choose another one!')
#                 continue

#         elif (len(k) < 2 and k[0] not in nums ) or (len(k) > 3 and k[0] not in nums ):
#             print("You Should enter numbers!")
#             continue

#         elif k = "4 1":
#             print("Coordinates should be from 1 to 3!")
#         elif (len(k) == 3 and k[0] not in nums):
#             print("You Should enter numbers!")
#             continue


#         else:
#             print("Coordinates should be from 1 to 3!")
#             continue

#     print(f'''---------
# | {m[0]} {m[1]} {m[2]} |
# | {m[3]} {m[4]} {m[5]} |
# | {m[6]} {m[7]} {m[8]} |
# ---------''')


    
    
        



    # count_ = 0
    # for x in m :
    #     if x == "_":
    #         count_ += 1



    # if impossible(m) and duplicate(m):
    #     h = horizontal(m)
    #     if h == False:
    #         v = vertical(m)
    #         if v == False:
    #             d = diagonal(m)
    #             if d == False:
    #                 if count_ == 0 :
    #                     print("Draw")
    #                 else:
    #                     print("Game not finished")
                