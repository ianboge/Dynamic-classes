'''function to change class names'''



def renameClass(cls,newname):
    '''
      cls: The class to rename.
      new_name: The new name for the class.
      '''
    cls.__name__=newname
    cls.__qualname__=newname

    return cls

class oldName:
    def __init__(self,value):
        self.value=value


newname=renameClass(oldName,"newName")

obj=newname(10)

print(type(obj))
print("run complete")
