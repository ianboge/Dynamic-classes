Question one
  create a function that will change class names;
  Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers), but starting only with upper case letter. In other   case it should raise an exception.


Question two
  Build class that could be inherited, and could provide some class method to modify name of already existing classes


Question Three
  Tim's boss excitedly informs him about a new secret contract from the army requiring the creation of dynamic classes with properties and methods specified   as parameters, without knowing their names in advance. 
  Despite Tim's initial doubts about the feasibility of such a task, you, his guru, remind him that in Python, everything is possible. Your task is to         implement a function create_class that accepts a class name and a secret dictionary, and returns a dynamically created class based on these inputs. 
  If the class name is empty, the function should return None, and it should handle cases where no dictionary is provided by using an empty dictionary as       the default. 
  The function should generate a new-style class, inheriting only the base methods of the object class. This solution leverages Python's type function to       create the class dynamically, ensuring the requirements are met flexibly and efficiently.
