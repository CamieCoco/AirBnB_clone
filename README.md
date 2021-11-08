### Airbnb Clone

## Table of Content
* [Description](#description)
* [Installation](#installation)
* [Functionality of console](#functionality-of-console)
* [Usage](#usage)
* [Environment](#environment)
* [Authors](#authors)

## Description
> This is the first phase of the Airbnb Clone: the console.
> This repository holds a command interpreter and classes (i.e. BaseModel class
> and several other classes that inherit from it: Amenity, City, State, Place,
> Review), and a command interpreter. The command interpreter, like a shell,
> can be activated, take in user input, and perform certain tasks
> to manipulate the object instances.

## Installation
```
git clone git@github.com/Jinnie506/AirBnB_clone.git
cd AirBnB_clone
```

## Functionality of console
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Usage
Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Environment
* Language: Python3
* OS: Ubuntu 14.04 LTS
* Style guidelines: [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/) \|| [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/l\atest/example_google.html)

## Authors
Ojini Ifeoma [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/jinnie50) / [Github](https://github.com/Jinnie506)
