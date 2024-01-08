### Type Annotations and How to Use

Type annotations define the types of variables and indicate the expected types of function parameters and return values.

```
def add_numbers(a: int, b: int) -> int:
    return a + b
```

### Duck Typing

**Nominal vs Structural Subtyping:**

Subtyping means that a particular type or class can be used wherever another type is expected.

Previously, Python used "nominal subtyping," meaning a class A could be used where a class B was expected only if A was a subclass of B.

The class had to be explicitly marked to support them.

```
from collections.abc import Sized, Iterable, Iterator

class Bucket(Sized, Iterable[int]):
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
```

Now, Python has "structural subtyping." A class can be used without explicitly mentioning the base classes it supports.

```
from collections.abc import Iterator, Iterable

class Bucket:  # No need to mention base classes
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...

def collect(items: Iterable[int]) -> int: ...
result = collect(Bucket())  # This works without any issues
```

It makes it easier to use classes without having to declare in advance that they support certain features.

"If it looks like a duck and quacks like a duck, then it's a duck,".

### How to Validate Code with mypy

`mypy` identifies potential type-related issues.

Install: `pip install mypy`

Run: `mypy your_code.py`
