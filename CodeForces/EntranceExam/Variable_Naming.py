# input
# 7
# 1 3 1 2 1 5 5

# output
# 1 3 2 4 5 10 15

def variable_naming(var_names):



    # Create a set to store used variable names
    mapping = set()
    # Create a list to store the output variable names
    output = []

    # Iterate through the given variable names
    for var in var_names:
        i = 1
        # Keep incrementing i until a unique variable name is found
        while var * i in mapping:
            i += 1

        # Add the unique variable name to the set and the output list
        mapping.add(var * i)
        output.append(var * i)
    
    # Return the list of generated variable names
    return output


if __name__ == "__main__":
    n = int(input())
    var_names = list(map(int, input().split()))

    print(*variable_naming(var_names))

     
    

   