def permutations(lst):  
    # Check if the input list is empty  
    if len(lst) == 0:  
        return []  
    # Check if the input list has only one element  
    elif len(lst) == 1:  
        return [lst]  
    else:  
        # Initialize an empty list to store permutations  
        result = []  
        # Iterate through each element of the input list  
        for i in range(len(lst)):  
            # Remove the current element from the list and store it in a variable  
            temp = lst[i]  
            remaining = lst[:i] + lst[i+1:]  
            # Recursively call the function on the remaining list  
            for p in permutations(remaining):  
                # Append the current element to the beginning of each permutation and add it to the result list  
                result.append([temp] + p)  
        # Return the final list of permutations  
        return result
print(permutations([1,2,3]))