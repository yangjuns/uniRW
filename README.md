# uniRW [![pypi](https://badge.fury.io/py/uniRW.svg)](https://badge.fury.io/py/uniRW) [![Build Status](https://travis-ci.org/law-liet/uniRW.svg?branch=master)](https://travis-ci.org/law-liet/uniRW) [![codecov](https://codecov.io/gh/law-liet/uniRW/branch/master/graph/badge.svg)](https://codecov.io/gh/law-liet/uniRW)

**uniRW** is a universal reader & writer package for complex, stateful data file processing.

* **Declarative:** Declare value structures and hierarchies, declare the state to be kept track of, declare the file structure, and **uniRW** will take care the details and process data in a predictable way. Declarative processing enables easy debugging and focuses on logic. 
* **Reusable:** Reuse a reader/writer in reading/writing multiple files. Reuse common value structures in different readers/writers. Compose simple hierarchies into more complex hierarchies. Focus on common patterns in input files and standardize output files.
* **Universal:** Process any files with lines split by any regular expressions. Apply user-defined map, filter and reduce, keep track of evolving state during processing. Store and output data in a user-defined hierarchy of values.  


# Installation
Easy to install with [pip](https://pip.pypa.io/en/stable/).
```
pip install uniRW
```

# Quick Start
See [examples](https://github.com/law-liet/uniRW/tree/master/examples) for more examples.

Import the package:
```Python
>>> import uniRW as RW
```

## Read

Suppose we want to read the following file named *example.csv* into a dictionary of maximum grades of different subjects:

    Name,Subject,Grade
    Alice,Math,4.0
    Alice,CS,3.0
    Alice,Math,3.8

Define the value structures and hierarchy:

``` python
>>> name, subject = RW.Value('Name'), RW.Value('Subject')
>>> grade = RW.Value('Grade', map_f=lambda _, x: float(x), reduce_f=max)
>>> hierarchy = {name: {subject: [grade]}}
```

Define the input file:

```python
>>> grade_file = RW.DataFile('example1.csv', RW.Line(','), header_lineno=0)
```

Create the reader and read the file:

```python
>>> grade_dict, _ = RW.HReader(hierarchy).read(grade_file)
>>> print(grade_dict)
{'Alice': {'Math': {'Grade': 4.0}, 'CS': {'Grade': 3.0}}}
```

## Write

Suppose we want to write the above `grade_dict` to a new file *new_example.csv* that looks like this:

    Name,Subject,Grade
    Alice,CS,3.0
    Alice,Math,4.0

Define the value line (with `name`, `subject`, and `grade` the same as above):

```python
>>> value_line = [name, subject, grade]
```

Define the output file:

```python
>>> output_file = RW.OutputFile('new_example.csv', RW.OutputLine(','))
```

Create the writer and write the file (with `hierarchy` the same as above):

```python
>>> RW.HWriter(hierarchy, value_line).write(output_file, grade_dict, sort_by='Grade')
```

# Documentation
See [wiki](https://github.com/law-liet/uniRW/wiki) for documentation.
    
# Future Work
- Better abstraction/structure
- Hierarchy Generalization
- Optimization
- Add type checker (Python 3.5 typing module + Mypy ?)

# Change Log
See [Change Log](https://github.com/law-liet/uniRW/blob/master/change_log.md).

# License
Read [License](https://github.com/law-liet/uniRW/blob/master/LICENSE) file.
