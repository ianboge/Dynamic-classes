import re

class ReNameAbleClass:
    @classmethod
    def change_class_name(cls, newname):
        '''
        Change the class name to a new name that meets specific criteria.
        
        newname: The new name for the class.
        '''
        # Check if the new name is valid
        if not re.match(r'^[A-Z][a-zA-Z0-9]*$', newname):
            raise ValueError("New name must start with an uppercase letter and contain only alphanumeric characters.")
        
        cls.__name__ = newname
        cls.__qualname__ = newname
    
    def __str__(self):
        return f"Class name is: {self.__class__.__name__}"

# how to use the ReNameAbleClass
class OldClass(ReNameAbleClass):
    def __init__(self, value):
        self.value = value

try:
    OldClass.change_class_name("NewClass")
    obj = OldClass(10)
    print(type(obj))
    print(str(obj))
    print("run complete")
except ValueError as e:
    print(f"Error: {e}")
