from enum_adt import ADT, ADTMeta


def test_adt():
    class MyEnum(ADT):
        class Foo: ...

        class Bar:
            name: str

    foo = MyEnum.Foo()
    bar = MyEnum.Bar("bar")
    assert issubclass(MyEnum.Foo, MyEnum)
    assert issubclass(MyEnum.Bar, MyEnum)
    assert isinstance(foo, MyEnum)
    assert isinstance(bar, MyEnum)

    class MyEnum2(metaclass=ADTMeta):
        class Baz: ...

    baz = MyEnum2.Baz()
    assert issubclass(MyEnum2.Baz, MyEnum2)
    assert isinstance(baz, MyEnum2)
    assert not issubclass(MyEnum2.Baz, MyEnum)
