import math

def main():
    get_equations()
 

def get_equations():
    eq1 = ["5x1","-2x2","3x3","-1"]
    eq2 = ["-3x1","9x2","1x3","2"]
    eq3 = ["2x1","-1x2","7x3","3"]
    print("steps to enter equations : ")
    print("Enter each coeff of x1 x2 and so on as ")
    print("1 -1 2 0 0 1 and write 0 if there is no coeff " )
    print("and add a comma after every row like : ")
    print("1 2 -1 ,1 0 2,9 23 9")
    equat = input("Please Enter all the equation in above manner : ")
    equat = equat.lstrip()
    equat = equat.rstrip()
    equat_row = equat.split(",")
    # eq1 = ["1x1","-2x2","5x3","1"]
    # print(equat_row)
    
    equations_elems = [row.split(" ") for row in equat_row]
    print(equations_elems)
    for row in equations_elems:
        for i in range(len(equations_elems)):
            row[i] = row[i] + "x" + str(i+1)
    
    print(equations_elems)

    # eq2 = ["-3x1","9x2","1x3","2"]
    # eq3 = ["9x1","-1x2","7x3","3"]

    equations = equations_elems

    strictly_daignoally = reorder_eq(equations)
    print("Rows Rearranged after performing Row Operations.")
    print(strictly_daignoally)

    calculate(strictly_daignoally)



# 22 109 2 42 6 23,100 2 3 44 3 23,23 7 7 4 99 4,12 4 66 3 -1 34,32 45 9 145 9 34


def reorder_eq(equations):
    
    fullcoeffients = [extract_coeffs(equation) for equation in equations]
    coeffients = fullcoeffients

    print(coeffients,"coeffeints inside reorder_eq")
    new_coeffs=[]
    for coeff in coeffients:
        new_coeffs.append(coeff[0:-1])
    
    coeffients = new_coeffs # [[-4, 5], [1, 2]]
    print(coeffients," INSIDE ")


    
    reordered_matrix = [matrix for matrix in coeffients]
    print(reordered_matrix, "Re-ordered matrix ")
    # [[-4, 5], [1, 2]]
    temp_reordered_matrix = [matrix for matrix in coeffients]
    # index_counter = 0

    for coeffient in reordered_matrix:
        

        print("coeffient ", coeffient)# [-4 5], [3 2] 
        # print("index ", i)

        for i in range(len(coeffient)):
            rest = [c for c in coeffient]
            rest.pop(i)
            print(rest,"Rest")
            if math.fabs(coeffient[i]) > abs_of_rest(rest):
                temp_reordered_matrix.remove(coeffient)
                if len(temp_reordered_matrix) == (len(reordered_matrix) -1 ):
                    temp_reordered_matrix.append(coeffient)
                else:
                    temp_reordered_matrix.insert(i,coeffient)
            
            



    # for c in reordered_matrix:
    #     print("coeffient ", c)# [-4 5], [1 2] 
    #     # print("index ", i)
    #     coeffient = c
    #     if reordered_matrix.index(coeffient) == i  and coeffient[i] != 0:
    #         # print (True)
    #         num_index = 0
    #         for num in coeffient:
                
    #             if math.fabs(num) > abs_of_rest(c,num_index):
    #                 if c.index(num) == len(c):
    #                     # print("inside of if last ")
    #                     reordered_matrix.remove(c)
    #                     reordered_matrix.append(c)
    #                 else:
    #                     # print("inside of if not last ")
    #                     reordered_matrix.remove(c)
    #                     reordered_matrix.insert(coeffient.index(num),c)
    #     else:
    #         for num in coeffient:
                
    #             if math.fabs(num) > abs_of_rest(c,c.index(num)):
    #                 if c.index(num) == len(c):
    #                     # print("inside of if last ")
    #                     reordered_matrix.remove(c)
    #                     reordered_matrix.append(c)
    #                 else:
    #                     # print("inside of if not last ")
    #                     reordered_matrix.remove(c)
    #                     reordered_matrix.insert(coeffient.index(num),c) 

    # for i in range 
    # reordered_matrix = [[reordered_matrix.append(equation[-1]) if (equation[i] == reordered_matrix[i]) ] for i in range (len(reorder_eq) - 1) for equation in equations ]
    print(temp_reordered_matrix, "temp re orderd matrix")
    temp_reordered_list = []
    for re in temp_reordered_matrix:
        temp_row = []
        # print(re)
        for temp in fullcoeffients:
            # print(temp[0:-1])
            if re == temp[0:-1]:
                temp_row = re
                temp_row.append(temp[-1])
                temp_reordered_list.append(temp_row)
                # print(temp_row)
    reordered_matrix = temp_reordered_list
    return reordered_matrix

def extract_coeffs(equation):
    print(equation,"equation inside extract_coeff() method")
    # temp_eqs =  [equation[0].split("x")[0],equation[1].split("x")[0],equation[2].split("x")[0],equation[3]]
    # temp_eqs = []
    temp_eqs = []
    for elem in equation:

        if elem.find("x") != -1:
            e = elem.split("x")[0]
            temp_eqs.append(e)
        else:
            temp_eqs.append(elem)
    print("Temp Eqs",temp_eqs)

# this will generate theese values and pass to the calling function
    # Temp Eqs ['0', '-2', '5', '1']
    # Temp Eqs ['-3', '9', '1', '2']
    # Temp Eqs ['9', '-1', '7', '3']


    return [int(eq) for eq in temp_eqs]
    # return 

def abs_of_rest(nums):
    total = 0
    for num in nums : 
        total += math.fabs(num)
    return total
    

# 1 1 1 1,2 2 2 2,23 2 3 3
# 1 1 8 1 1,9 2 2 2 1,3 15 3 3 1 1,2 3 4 20 3
# 1 1 8 1 1 8,9 2 2 2 1 8,3 15 3 3 1 1 2,2 3 4 20 3 4,3 4 3 5 23 4

def calculate(matrix):
    print("inside calculate method")
    print(matrix," matrix")
    roeq = [e for e in matrix[-1]];
    functions = []
    rownum = 0
    print("Matrix",matrix)
    for row in matrix:
        print(row,"this is row")
        columnnum = 0
        leftofeq = 0
        rightofeq = []
        for coeff in row:
            # print("Row",row)
            # print(coeff,"coeffs")
            if rownum == columnnum:
                leftofeq = coeff
            elif columnnum == len(row)-1:
                # print("inside elif")
                rightofeq.insert(0,coeff)
            else:
                rightofeq.append(coeff*(-1))
                
            # print(rightofeq,"rightofeq")
            # print(leftofeq,"leftofeq")
            columnnum += 1;
        # print("loop Done")
        completeeq = []
        # completeeq = [n*0 or num/leftofeq for num in rightofeq if num != 0 for n in rightofeq if n == 0 ]
        for num in rightofeq:
            temp_value = 0
            if num != 0:
                temp_value =  num/leftofeq
                completeeq.append(temp_value)
            else:
                temp_value = 0
                completeeq.append(temp_value)
        # completeeq.insert(0,roeq[rownum]/leftofeq)
        
        
        # print("completeeq")
        # print(completeeq)
        functions.append(completeeq)
        rownum += 1
    
    # print("================ function = ==============")
    # print(functions);
    startCalculating(functions)


def startCalculating(equations):
    print("\n\n\n +++++++++++++++++ inside the calculating function ++++++++++++++++")
    matrixlen = len(equations)
    variables = [0 for matrixlen in equations]

    print(equations,"Equations \n\n")
    # print(variables)
#    [[0.1111111111111111, -0.1111111111111111, 0.7777777777777778],
#  [-0.2222222222222222, -0.3333333333333333, 0.1111111111111111], [1.0, 0.2, -0.4]]
#    [[0.1111111111111111, -0.1111111111111111, 0.7777777777777778]
    # [0, 0, 0]
    # [1, 2, 3]
    answer_array = []
    notdone = True
    while notdone:
        if len(answer_array) > 0:
            if variables == answer_array[-matrixlen*2:-matrixlen]:
                notdone = False
                
        if notdone == False:
            break

        counter = 0
        print("equations")
        print(equations)
        for equation in equations:
            result = equation[0] #1
            print(result,"result")
            tempeqs = equation[1:]
            tempvariables = [v for v in variables]
            print(variables,"normal variables")
            tempvariables.pop(equations.index(equation))
            print(tempeqs,"temp eqs")
            # print(tempvariables,"temp vars")
            for i in range(matrixlen-1):#0,1,2
                print(i)
                result += tempvariables[i] * tempeqs[i]#0.2 + 0 * 0.4 + 0 * .6\ 0.2 + 0.2 * 0.2 + 0* -1
            # print()
            # print(result,"result")
            variables[equations.index(equation)] = result  #[0]=0.4
            answer_array.append(result)#[0.4]
            counter += 1;
            # print(variables, "variables")



        
        # print(counter)
    # print(answer_array)

    tempasnarray = []
    for i in range(0,len(answer_array),matrixlen):
        tempasnarray.append(answer_array[i:i+matrixlen])
    
    # print(tempasnarray)

    # print(answer_array)
    for i in range(len(variables)):
        spaces = 21 * " "
        print("x",i+1,end=spaces)
    print()
    bars = (len(variables) * 22) *  "-"
    print(bars)
    counterrrr = 0
    for row in tempasnarray:
        for i in range(len(row)):
            print(row[i],end="  ,  ")
        print()
        counterrrr += 1



    print(variables)
    print(counterrrr) 

    



if __name__ == "__main__":
    main()