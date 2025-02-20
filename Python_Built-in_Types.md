# Python 3 Built-in Objects

Python 3 has several built-in objects optimized and implemented in **C** for efficiency. Below is a list of the most important ones.

---

## 🔹 Basic Data Types
1. **Integers (`int`)** – Arbitrary-precision signed integers  
   ```python
   x = 42
   ```

2. **Floating-Point Numbers (`float`)** – Double-precision floating-point numbers  
   ```python
   y = 3.14
   ```

3. **Complex Numbers (`complex`)** – Complex numbers with real and imaginary parts  
   ```python
   z = 2 + 3j
   ```

4. **Booleans (`bool`)** – Subclass of `int`, only `True` and `False`  
   ```python
   is_active = True
   ```

5. **Strings (`str`)** – Immutable sequences of Unicode characters  
   ```python
   text = "Hello, world!"
   ```

6. **Bytes (`bytes`)** – Immutable sequences of bytes (binary data)  
   ```python
   b = b"hello"
   ```

7. **Bytearrays (`bytearray`)** – Mutable sequences of bytes  
   ```python
   ba = bytearray([65, 66, 67])
   ```

8. **Memory Views (`memoryview`)** – A way to access the memory of other binary objects  
   ```python
   mv = memoryview(b"hello")
   ```

---

## 🔹 Collections (Data Structures)
9. **Lists (`list`)** – Mutable dynamic arrays  
   ```python
   my_list = [1, 2, 3]
   ```

10. **Tuples (`tuple`)** – Immutable ordered sequences  
    ```python
    my_tuple = (1, 2, 3)
    ```

11. **Dictionaries (`dict`)** – Hash table (key-value pairs)  
    ```python
    my_dict = {"name": "Alice", "age": 25}
    ```

12. **Sets (`set`)** – Unordered collection of unique elements  
    ```python
    my_set = {1, 2, 3}
    ```

13. **Frozen Sets (`frozenset`)** – Immutable version of sets  
    ```python
    frozen = frozenset([1, 2, 3])
    ```

---

## 🔹 Special Objects
14. **None (`NoneType`)** – Represents the absence of a value  
    ```python
    result = None
    ```

15. **Ellipsis (`Ellipsis`)** – Represented by `...`, often used in slicing  
    ```python
    x = ...
    ```

16. **NotImplemented (`NotImplementedType`)** – Used for operator overloading  
    ```python
    y = NotImplemented
    ```

---

## 🔹 Callable Objects
17. **Functions (`function`)** – Defined using `def` or `lambda`  
    ```python
    def my_func():
        return "Hello"
    ```

18. **Methods (`method`)** – Functions bound to a class  
    ```python
    class MyClass:
        def method(self):
            return "Hello"
    ```

19. **Generators (`generator`)** – Functions that yield values lazily  
    ```python
    def gen():
        yield 1
        yield 2
    ```

20. **Coroutines (`coroutine`)** – Asynchronous functions using `async def`  
    ```python
    async def my_coroutine():
        await some_task()
    ```

21. **Classes (`type`)** – Custom object blueprints  
    ```python
    class MyClass:
        pass
    ```

22. **Modules (`module`)** – Python files loaded as modules  
    ```python
    import math  # math is a module
    ```

---

## 🔹 File & I/O Objects
23. **File Objects (`io.TextIOWrapper`)** – File handles returned by `open()`  
    ```python
    f = open("file.txt", "r")
    ```

---

## 🔹 Iterables & Iterators
24. **Range (`range`)** – Immutable sequence of numbers  
    ```python
    r = range(10)
    ```

25. **Enumerate (`enumerate`)** – Returns index-value pairs from an iterable  
    ```python
    e = enumerate(["a", "b", "c"])
    ```

26. **Zip (`zip`)** – Combines multiple iterables into tuples  
    ```python
    z = zip([1, 2, 3], ["a", "b", "c"])
    ```

27. **Map (`map`)** – Applies a function to an iterable  
    ```python
    m = map(str.upper, ["hello", "world"])
    ```

28. **Filter (`filter`)** – Filters elements of an iterable  
    ```python
    f = filter(lambda x: x > 10, [5, 15, 20])
    ```

29. **Slice (`slice`)** – Represents a slice of a sequence  
    ```python
    s = slice(1, 5, 2)
    ```

30. **Property (`property`)** – Used for defining class properties  
    ```python
    class Example:
        def __init__(self):
            self._x = 10
        def get_x(self):
            return self._x
        x = property(get_x)
    ```

---

## 🔥 Summary
Python’s built-in types are **highly optimized and implemented in C** for speed. The key built-in types fall into these categories:

✅ **Basic Types**: `int`, `float`, `complex`, `str`, `bool`, `bytes`  
✅ **Collections**: `list`, `tuple`, `dict`, `set`, `frozenset`  
✅ **Special Objects**: `None`, `Ellipsis`, `NotImplemented`  
✅ **Iterables & Iterators**: `range`, `enumerate`, `zip`, `map`, `filter`  
✅ **Callable Objects**: `function`, `method`, `generator`, `coroutine`  
✅ **File & I/O**: `open()` (file objects)  
