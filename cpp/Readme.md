Exercises
======

* [Odd occurrences in an
array](https://codility.com/programmers/task/odd_occurrences_in_array/): find
the unpaired integer in an array.
* Binary tree: create and parse a tree in a couple of different ways
  (interesting: the test file shows how to capture `stdout` in GoogleTest).
* Linked list: build a linked list from a `vector` of `string` and carry out
some manipulations on it.
* [CyclicRotation](https://codility.com/programmers/task/cyclic_rotation/)
Rotate a `vector<int>` by a certain amount.
* [FrogRiverOne](https://codility.com/programmers/task/frog_river_one/) Find
the earliest point at which we have seen all `X` integers in an array.

GoogleTest
----
To run the tests you first need to build
[GoogleTest](https://github.com/google/googletest), then update the variable
`GTEST_DIR` in the `Makefile` in this directory to point at its source.

You can use `make run` (from this directory) to build and run the tests.
