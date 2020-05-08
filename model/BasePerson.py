class BasePerson():
    """
    BasePerson class

    constructor(name: str)

    name() as getter
    
    name(name: value) as setter
    """

    # constructor convention is __init__
    def __init__(self, name: str):
        # calling setter of property "name"
        # ref: https://www.youtube.com/watch?v=u4_ALw4KANc&list=PLlrxD0HtieHiXd-nEby-TMCoUNwhbLUnj&index=7
        self.name = name

    # declaring property (attribute)
    @property
    def name(self) -> str:
        # __name is like private attribute
        # ref: https://youtu.be/0xzbkiLKERM?t=409 
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self) -> int:  # self is passed in from object as in person.age()
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    def say_hello(self):
        """
        Say 'Hello NAME"
        
        parameters: none
        
        return: void
        """
        print(f"Hello {self.__name}")