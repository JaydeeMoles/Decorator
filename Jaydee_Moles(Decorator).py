def decorator(func):
    
    def uppercase():
        
        result = func()
        uppercase_function = result.upper()
        print (uppercase_function)
        
    return uppercase


def example_name():
    return "jaydee"
    
    
decorated_name = decorator(example_name)

decorated_name()