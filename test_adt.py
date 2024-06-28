import pytest

from enum_adt import ADT, ADTMeta


def test_adt():
    class MyEnum(ADT):
        class Foo: ...

        class Bar:
            name: str

        def __str__(self) -> str:
            if isinstance(self, MyEnum.Foo):
                return "Foo"
            else:
                return f"Bar({self.name})"

    foo = MyEnum.Foo()
    bar = MyEnum.Bar("bar")
    assert issubclass(MyEnum.Foo, MyEnum)
    assert issubclass(MyEnum.Bar, MyEnum)
    assert isinstance(foo, MyEnum)
    assert isinstance(bar, MyEnum)
    assert str(foo) == "Foo"
    assert str(bar) == "Bar(bar)"

    class MyEnum2(metaclass=ADTMeta):
        class Baz: ...

    baz = MyEnum2.Baz()
    assert issubclass(MyEnum2.Baz, MyEnum2)
    assert isinstance(baz, MyEnum2)
    assert not issubclass(MyEnum2.Baz, MyEnum)

    with pytest.raises(TypeError):
        MyEnum()
