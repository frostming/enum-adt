from __future__ import annotations

import dataclasses
import inspect
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from typing import TypedDict, Unpack

    class DataClassAttrs(TypedDict):
        init: bool = True
        repr: bool = True
        eq: bool = True
        order: bool = False
        unsafe_hash: bool = False
        frozen: bool = False
        match_args: bool = True
        kw_only: bool = False
        slots: bool = False
        weakref_slot: bool = False


class ADTMeta(type):
    """Create an enum ADT.

    Example:
    class MyEnum(metaclass=ADTMeta):
        class Foo: ...

        class Bar:
            name: str

    foo = MyEnum.Foo()
    bar = MyEnum.Bar("bar")
    assert isinstance(foo, MyEnum)
    assert isinstance(bar, MyEnum)
    """

    def __new__(
        cls,
        name: str,
        bases: tuple[type, ...],
        ns: dict[str, Any],
        **kwargs: Unpack[DataClassAttrs],
    ) -> type:
        common_methods: dict[str, Any] = {}
        variants: list[type] = []
        for key, value in ns.items():
            if inspect.isclass(value):
                ns[key] = dataclasses.dataclass(value, **kwargs)
                variants.append(value)
            elif inspect.isfunction(value):
                common_methods[key] = value
            elif not key.startswith("_"):
                raise TypeError("Attributes are not allowed in ADT")
        for variant in variants:
            for key, value in common_methods.items():
                setattr(variant, key, value)
        return super().__new__(cls, name, bases, ns)

    def __subclasscheck__(self, subclass: type) -> bool:
        return subclass in self.__dict__.values() and dataclasses.is_dataclass(subclass)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        raise TypeError("ADT cannot be instantiated")

    def __instancecheck__(self, instance: Any) -> bool:
        return self.__subclasscheck__(instance.__class__)


class ADT(metaclass=ADTMeta):
    """Create an enum ADT(Algebraic Data Type).

    Example:
    class MyEnum(ADT):
        class Foo: ...

        class Bar:
            name: str

    foo = MyEnum.Foo()
    bar = MyEnum.Bar("bar")
    assert isinstance(foo, MyEnum)
    assert isinstance(bar, MyEnum)
    """
