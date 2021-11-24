# Fizz buzz

My personal take on the [Fizz buzz](https://en.wikipedia.org/wiki/Fizz_buzz) programming challenge.

## Usage

``` bash
$ python script.py
1
2
Fizz
# ...
98
Fizz
Buzz
```

Can also be imported as a standalone Python module:

``` python
>>> from fizzbuzz import FizzBuzz
>>> fb = FizzBuzz()
>>> fb.print()
1
2
Fizz
# ...
98
Fizz
Buzz
```

Accepts keyword arguments `start`, `stop`, `factor_1`, `factor_2`, `word_1`, and `word_2`.

``` python
>>> fb = FizzBuzz(start=10, stop=20, factor_1=2, factor_2=4, word_1="Foo", word_2="Bar")
>>> fb.print()
Foo
11
FooBar
13
Foo
15
FooBar
17
Foo
19
FooBar
```

## Tests

``` bash
$ python -m unittest discover
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```
