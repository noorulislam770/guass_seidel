for c in reordered_matrix:
        

        print("coeffient ", c)# [-4 5], [1 2] 
        # print("index ", i)
        coeffient = c
        
        if i == reordered_matrix.index(coeffient):
            for nums in coeffient:
                if math.fabs(nums[i]) > abs_of_rest()
