def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*added fudge*")
        return func(*args, **kwargs)  # Call and return the result of the original function
    return wrapper  # Return the wrapper function without calling it

def add_sprinkle(func):
    def wrapper(*args, **kwargs):
        print("*added sprinkle*")
        return func(*args, **kwargs)  # Call and return the result of the original function
    return wrapper  # Return the wrapper function without calling it

@add_fudge
@add_sprinkle
def get_ice_cream(flavor):
    print(f"here is your {flavor} ice cream")

# Call the decorated function
get_ice_cream("vanilla")