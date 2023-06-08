from collections.abc import Iterable
from typing import Iterable, Any

class not_tuple(tuple):
    def __new__(cls, __iterable: Iterable = ...):
        new_iterable = (
            el.capitalize() if isinstance(el, str) else el
                for el in __iterable 
        )
    


        temp = []
        for el in __iterable:
            if isinstance(el, str):
                el = el.capitalize()
            temp.append(el)

        return super().__new__(cls, temp)
    
    def __init__(self, *args, **kwargs) -> None:
        print(f'INIT {self}')

class not_list(list):
    def __init__(self):
        super().__init__()

    def append(self, __object: Any) -> None:
        if isinstance(__object, str):
            __object = __object.capitalize()
        return super().append(__object)
    
        
    
Ex = not_list()
Ex.append("asdsdsdsd")
print(Ex)

Ex2 = not_tuple(('123', 'asdsd', 32))
print(Ex2)
"""
class Examp():
    def __init__(self) -> None:
        self.tup = ()
    def __add__(self, Object):
        self.tup += (Object) """

