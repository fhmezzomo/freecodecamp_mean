import numpy as np

#def calculate(list):
def calculate(matrix_list):
    # Reshape the list into a 3x3 matrix
    matrix = np.array(matrix_list).reshape(3, 3)
    
    # Calculate statistics
    std_dev_row = matrix.std(axis=1)
    std_dev_col = matrix.std(axis=0)
    std_dev_flat = matrix.std()
    var_row = matrix.var(axis=1)
    var_col = matrix.var(axis=0)
    var_flat = matrix.var()
    max_row = matrix.max(axis=1)
    max_col = matrix.max(axis=0)
    max_flat = matrix.max()
    min_row = matrix.min(axis=1)
    min_col = matrix.min(axis=0)
    min_flat = matrix.min()
    sum_row = matrix.sum(axis=1)
    sum_col = matrix.sum(axis=0)
    sum_flat = matrix.sum()
    
    return {
        "std_dev_row": std_dev_row.tolist(),
        "std_dev_col": std_dev_col.tolist(),
        "std_dev_flat": std_dev_flat.item(),  # Convert to scalar for single value
        "var_row": var_row.tolist(),
        "var_col": var_col.tolist(),
        "var_flat": var_flat.item(),  # Convert to scalar for single value
        "max_row": max_row.tolist(),
        "max_col": max_col.tolist(),
        "max_flat": max_flat.item(),  # Convert to scalar for single value
        "min_row": min_row.tolist(),
        "min_col": min_col.tolist(),
        "min_flat": min_flat.item(),  # Convert to scalar for single value
        "sum_row": sum_row.tolist(),
        "sum_col": sum_col.tolist(),
        "sum_flat": sum_flat.item(),  # Convert to scalar for single value
    }

list = [0,1,2,3,4,5,6,7,8]

# Calling the calculate function with the correct variable name
stats = calculate(list)

# Printing the results
print("Statistics for the 3x3 matrix:")
for key, value in stats.items():
    print(f"{key}: {value}")
