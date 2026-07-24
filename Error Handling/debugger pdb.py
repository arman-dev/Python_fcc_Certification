import pdb  # Python debugger module

def divide(a, b):
    pdb.set_trace()  # Execution এখানে থামবে; (Pdb) prompt থেকে a, b-এর মান দেখা, কোড step-by-step চালানো বা continue করা যাবে।
    return a / b

print(divide(10, 2))