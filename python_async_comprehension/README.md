### How to write an asynchronous generator

`async def` defines a function and the `yield` statement produces values asynchronously.

     ```
     import asyncio

     async def async_generator():
         for i in range(5):
             await asyncio.sleep(1)  # Simulating asynchronous operation
             yield i

     # Example usage:
     async def main():
         async for value in async_generator():
             print(value)

     asyncio.run(main())
     ```

### How to use async comprehensions

`async for` iterates over asynchronous sequences.

     ```
     import asyncio

     async def async_comprehension_example():
         return [i async for i in async_generator()]

     # Example usage:
     async def main():
         result = await async_comprehension_example()
         print(result)

     asyncio.run(main())
     ```

### How to type-annotate generators

Use `Generator` type from `typing` module. Specify the types of values yielded and returned using `yield` and `return` statements.

     ```
     from typing import Generator

     def number_generator(n: int) -> Generator[int, None, None]:
     # yields integers and does not return anything (`None`) at the end.
         for i in range(n):
             yield i

     # Example usage:
     gen = number_generator(5)
     for value in gen:
         print(value)
     ```
