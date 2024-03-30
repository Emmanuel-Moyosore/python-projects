# AND TRUTH TABLE
def generate_truth_table():
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    print("Input A | Input B | Output")
    print("-" * 26)
    for input_pair in inputs:
        result =  input_pair[0] and  input_pair[1]

        print(f"   {input_pair[0]}    |    {input_pair[1]}    |   {result}")
print('TRUTH TABLE FOR AND OPERATION')
# Generate the truth table for the AND operation
generate_truth_table()

# OR TRUTH TABLE
def generate_truth_table():
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    print("Input A | Input B | Output")
    print("-" * 26)
    for input_pair in inputs:
        result = input_pair[0]  or input_pair[1]
        
        print(f"   {input_pair[0]}    |    {input_pair[1]}    |   {result}")
print('Truth Tables for OR operation')
# Generate the truth table for the OR operation
generate_truth_table()


# NOT TRUTH TABLE
def generate_truth_table():
    inputs = [(0, 0)]
    print("Input A | Output")
    print("-" * 26)
    for input_pair in inputs:
        result = not input_pair[0] 
        
        print(f"   {input_pair[0]}    |  {result}")
print('Truth Tables for NOT operation')
# Generate the truth table for the OR operation
generate_truth_table()