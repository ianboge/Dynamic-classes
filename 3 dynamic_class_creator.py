def create_class(class_name, secret_dict=None):
    # If class_name is empty, return None
    if not class_name:
        return None

    # Use an empty dictionary if secret_dict is not provided
    if secret_dict is None:
        secret_dict = {}

    # Create a new class with the given name and attributes/methods
    new_class = type(class_name, (object,), secret_dict)
    return new_class

# Example usage
def army_get_secret_from_file():
    # This function simulates reading a secret dictionary from a file
    # For demonstration purposes, we will return a sample dictionary
    return {
        'prop1': 'value1',
        'prop2': 'value2',
        'method1': lambda self: 'This is method1',
        'method2': lambda self, x: f'This is method2 with argument {x}'
    }

# Simulate reading the secret dictionary from a file
secret_dict = army_get_secret_from_file()

# Create a new class with the secret dictionary
MyClass = create_class("MyClass", secret_dict)

if MyClass:
    # Create an instance of the new class
    obj = MyClass()
    # Access properties
    print(obj.prop1)
    print(obj.prop2)
    # Call methods
    print(obj.method1())
    print(obj.method2(10))
else:
    print("Class name is empty. No class created.")
