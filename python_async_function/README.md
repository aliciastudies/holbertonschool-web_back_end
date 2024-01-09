# Learning Objectives

### Async and Await Syntax

**Async** is a way of writing programs that can do multiple things at once. When something is marked as **async**, it means it can pause while waiting for something without stopping the entire program.

**Await** is used with **async** to tell the program to wait for a specific task to finish before moving on.

### Executing an Async Program with asyncio

- Import the `asyncio` module in Python
- Use `async def` for functions to make them asynchronous
- Run the async functions using `asyncio.run(your_async_function())` to start the async program

### Running Concurrent Coroutines

- Use `asyncio.gather()` to run multiple async functions concurrently
- Pass the async functions as arguments to `asyncio.gather()`

### Creating Asyncio Tasks

`asyncio.create_task(your_async_function())` allows the task to run concurrently with other tasks.

### Using the Random Module

The `random` module in Python helps generate random numbers.

e.g `random.choice(your_list)` picks a random item from a list and `random.randint(min_value, max_value)` picks a random int within a range.
