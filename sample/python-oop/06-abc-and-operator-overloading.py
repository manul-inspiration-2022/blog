from __future__ import annotations

import random
from abc import ABC, abstractclassmethod, abstractmethod
from typing import Iterable, Iterator, Protocol, Any, Sequence, Tuple, Type, Union, Mapping
from typing import overload

"""
In Python, we have two approaches to defining similar things: 
  • Duck typing: When two class definitions have the same attributes and methods, then instances of the two classes have the same protocol and can be used interchangeably. We often say, "When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck." 
  
  • Inheritance: When two class definitions have common aspects, a subclass can share common features of a superclass. The implementation details of the two classes may vary, but the classes should be interchangeable when we use the common features defined by the superclass. 
"""

class MediaPlayer(ABC):
    @abstractclassmethod
    def play(self) -> None:
        ...

    @property
    @abstractclassmethod
    def ext(self) -> None:
        ...

class Wav(MediaPlayer):
    pass

class Ogg(MediaPlayer):
    ext = 'something'

    def play(self):
        pass

"""
>>> x = Wav()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Wav with abstract methods ext, play
"""


"""
The ABC of collections
"""
from collections.abc import Container

class OddIntegers():
    def __contains__(self, x: int) -> bool:
        return x % 2 != 0

"""
>>> help(Container.__contains__)
Help on function __contains__ in module collections.abc:

__contains__(self, x)

>>> odd = OddIntegers()
>>> isinstance(odd, Container)
True
>>> issubclass(OddIntegers, Container)
True
>>> 1 in odd 
True 
>>> 2 in odd 
False 
"""


"""
Abstract base classes and type hints 

Generic classes and abstract base classes are not the same thing. The two concepts overlap, but are distinct: 
  • Generic classes have an implicit relationship with Any. This often needs to be narrowed using type parameters, like list[int]. The list class is concrete, and when we want to extend it, we'll need to plug in a class name to replace the Any type. The Python interpreter does not use generic class hints in any way; they are only checked by static analysis tools such as mypy. 
  
  • Abstract classes have placeholders instead of one or more methods. These placeholder methods require a design decision that supplies a concrete implementation. These classes are not completely defined. When we extend it, we'll need to provide a concrete method implementation. If we don't provide the missing methods, the interpreter will raise a runtime exception when we try to create an instance of an abstract class.

The definition of the Collection abstract class, in turn, depends on three other abstract base classes: Sized, Iterable, and Container. Each of these abstractions demands specific methods. 
  • The Sized abstraction requires an implementatio for __len__()  # E.i: len(x)
  • The Iterable abstraction requires an implemation for __iter__() # E.i: iter(x)
  • The Container abstraction requires an implementation for __contain__() # E.i: in or not in

  • The Mapping abstraction, based on Collection, requires, among other things, __getitem__(), __iter__(), and __len__(). It has a default definition for __contains__(), based on whatever __iter__() method we provide.

2 ways to constructing a dictionary are exemplified by the following:
>>> x = dict({"a": 42, "b": 7, "c": 6}) 
>>> y = dict([("a", 42), ("b", 7), ("c", 6)]) 
>>> x == y 
True 
"""

import collections.abc
import bisect

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ... 

BaseMapping = collections.abc.Mapping[Comparable, Any]

class Lookup(BaseMapping):
    @overload
    def __init__(
        self,
        source: Iterable[Tuple[Comparable, Any]],
    ) -> None:
        ...

    @overload
    def __init__(
        self,
        source: BaseMapping
    ) -> None:
        ...

    def __init__(self,
        source: Union[
            Iterable[Tuple[Comparable, Any]],
            BaseMapping,
            None] = None
    ) -> None:
        sorted_pairs: Sequence[Tuple[Comparable, Any]]
        if isinstance(source, Sequence):
            sorted_pairs = sorted(source)
        elif isinstance(source, Mapping):
            sorted_pairs = sorted(source.items())
        else:
            sorted_pairs = []

        self.key_list = [p[0] for p in sorted_pairs]
        self.value_list = [p[1] for p in sorted_pairs]

    
    def __len__(self) -> int:
        return len(self.key_list)
    
    def __iter__(self) -> Iterator[Comparable]:
        return iter(self.key_list)
    
    def __contains__(self, key: object) -> bool:
        index = bisect.bisect_left(self.key_list, key)

        return key == self.key_list[index]

    def __getitem__(self, key: Comparable) -> Any:
        index = bisect.bisect_left(self.key_list, key)
        if key == self.key_list[index]:
            return self.value_list[index]

        raise KeyError(key)

"""
x = Lookup([ 
    ["z", "Zillah"], 
    ["a", "Amy"], 
    ["c", "Clara"], 
    ["b", "Basil"], 
])
>>> x["c"]
'Clara'
>>> x["m"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise KeyError(key)
KeyError: 'm'
>>> x["m"] = "something"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Lookup' object does not support item assignment
"""

"""
The general approach to using abstract classes is this: 
  1. Find a class that does most of what you need. 
  
  2. Identify the methods in the collections.abc definitions that are marked as abstract. The documentation often gives a lot of information, but you'll also have to look at the source. 
  
  3. Subclass the abstract class, filling in the missing methods. 
  
  4. While it can help to make a checklist of the methods, there are tools to help with this. Creating a unit test (we'll cover testing in Chapter 13, Testing Object-Oriented Programs) means you need to create an instance of your new class. If you haven't defined all the abstract methods, this will raise an exception.
"""

class Die(ABC):
    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abstractmethod
    def roll(self) -> None:
        ...
    
    def __repr__(self) -> str:
        return f"{self.face}"

class D6(Die):
    def roll(self) -> None:
        self.face = random.randint(1, 6) 

class Dice(ABC):
    def __init__(self, n: int, die_class: Type[Die]) -> None:
        self.dice = [die_class() for _ in range(n)]

    @abstractmethod
    def roll(self) -> None:
        ...
    
    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice)

class SimpleDice(Dice):
    def roll(self) -> None:
        for d in self.dice:
            d.roll()

"""
sd = SimpleDice(6, D6)
>>> sd.roll()
>>> sd.total
22
"""