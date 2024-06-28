# enum-adt

Enum Algebraic Data Types (ADTs) for Python.

## Installation

Run the following command to install the Python package on Python 3.8 or later:

```bash
pip install enum-adt
```

Or you can simply copy the `enum_adt.py` file anywhere in your project.

## Usage

```python
from enum_adt import ADT

class MyEnum(ADT):
    class Foo: ...

    class Bar:
        name: str

foo = MyEnum.Foo()
bar = MyEnum.Bar("bar")
assert isinstance(foo, MyEnum)
assert isinstance(bar, MyEnum)
```

Alternatively, you can use metaclass:

```python
from enum_adt import ADTMeta

class MyEnum(metaclass=ADTMeta):
    class Foo: ...

    class Bar:
        name: str
```

Each internal class will be created as a `dataclass` with the same attributes. You can customize the dataclass by passing arguments to the class:

*All enum variants get the same arguments.*

```python
from enum_adt import ADT

class MyEnum(ADT, frozen=True, kw_only=True):
    class Foo: ...

    class Bar:
        name: str
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
