# AirBnB Clone

![Repo size](https://img.shields.io/github/repo-size/B3zaleel/AirBnB_clone)
![Code size](https://img.shields.io/github/languages/code-size/B3zaleel/AirBnB_clone.svg)
[![CodeStyle](https://github.com/B3zaleel/AirBnB_clone/actions/workflows/codestyle.yml/badge.svg)](https://github.com/B3zaleel/AirBnB_clone/actions/workflows/codestyle.yml)
![Latest commit](https://img.shields.io/github/last-commit/B3zaleel/AirBnB_clone/main?style=round-square)

## Description

This project is a clone of the **AirBnB** website. This project supports the serialization and deserialization of simple data sets using a simple file storage mechanism. The data sets are serialized to a JSON file format for the purpose of simplicity. This project also supports a simple console-based command interpreter for managing the supported data sets ([more below](#supported-data-sets)).

## The Command Interpreter

The command interpreter provides a simple REPL (Read-Evaluate-Print-Loop) for interacting with the models in this project only. You can find some examples [here](#examples).

### How To Use

You have to clone this repository to your system and change your working directory to the project's folder path on your system. The command interpreter can be started by running `./console.py` in your terminal. This would create an interactive REPL session which can be terminated by running `EOF` or `quit`. A non-interactive session exits after running the last command the interpreter received such as in `echo "all" | ./console.py`.

### Supported Commands

These are commands that can be executed by the command interpreter. They have the format `command [argument]...` but you could also use the format `ClassName.command([argument]...)`..

| Format | Description |
|:-|:-|
| `help [command]` | Prints helpful information about a command (`command`). If `command` is not provided, it prints the help menu. |
| `quit` | Closes the command interpreter. |
| `EOF` | Closes the command interpreter. |
| `create ClassName` | Creates a new instance of the `ClassName` class. |
| `count ClassName` | Prints the number of instances of the `ClassName` class. |
| `show ClassName id` | Prints the string representation of an instance of the `ClassName` class with the given `id`. |
| `destroy ClassName id` | Deletes an instance of the `ClassName` class with the given `id`. |
| `all [ClassName]` | Prints a list containing the string representation of all instances of the `ClassName` class. `ClassName` is optional and if it isn't provided, all the availble objects are printed. |
| `update ClassName id attr_name attr_value` | Updates an instance of the `ClassName` class with the given `id` by assigning the attribute value `attr_value` to its attribute named `attr_name`. Attributes having the names `__class__`, `id`, `created_at`, and `updated_at` are silently ignored. |
| `update ClassName id dict_repr` | Updates an instance of `ClassName` having the given `id` by storing the key, value pairs in the given `dict_repr` dictionary as its attributes. The keys `__class__`, `id`, `created_at`, and `updated_at` are silently ignored. |

### Supported Models

These are the models that are currently available.

| Class | Description |
|:-|:-|
| BaseModel | Represents the base class for all models (all models are instances of this class). |
| User | Represents a user account for this project. |
| State | Represents the geographical state in which a _User_ lives. |
| City | Represents an urban area in a _State_. |
| Amenity | Represents a useful feature of a _Place_. |
| Place | Represents a building containing rooms that can be rented by a _User_. |
| Review | Represents a review of a _Place_. |

### Examples

#### Example 1

```powershell
b3zaleel@BOCI-PC ~/AirBnB_clone (main)> ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) all Base
** class doesn't exist **
(hbnb) all User
[]
(hbnb) all BaseModel
["[BaseModel] (65b8d056-cf49-4c88-a260-5ac03b6a569a) {'id': '65b8d056-cf49-4c88-a260-5ac03b6a569a', 'created_at': datetime.datetime(2021, 11, 8, 22, 21, 16, 59389), 'updated_at': datetime.datetime(2021, 11, 8, 22, 21, 16, 59450), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (c2a59481-316b-4775-a176-13f6009e88a5) {'id': 'c2a59481-316b-4775-a176-13f6009e88a5', 'created_at': datetime.datetime(2021, 11, 8, 22, 21, 19, 150040), 'updated_at': datetime.datetime(2021, 11, 8, 22, 21, 19, 150088), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (761301fc-773f-4d26-adf9-78731f841d71) {'id': '761301fc-773f-4d26-adf9-78731f841d71', 'created_at': datetime.datetime(2021, 11, 9, 7, 6, 38, 601068), 'updated_at': datetime.datetime(2021, 11, 9, 7, 6, 38, 601088)}"]
(hbnb) show BaseModel "65b8d056-cf49-4c88-a260-5ac03b6a569a"
[BaseModel] (65b8d056-cf49-4c88-a260-5ac03b6a569a) {'id': '65b8d056-cf49-4c88-a260-5ac03b6a569a', 'created_at': datetime.datetime(2021, 11, 8, 22, 21, 16, 59389), 'updated_at': datetime.datetime(2021, 11, 8, 22, 21, 16, 59450), 'name': 'My_First_Model', 'my_number': 89}
(hbnb) BaseModel.count()
3
(hbnb)
(hbnb) quit
b3zaleel@BOCI-PC ~/AirBnB_clone (main)>
```

#### Example 2

```powershell
➜  AirBnB_clone git:(main) ./console.py
(hbnb) all User
["[User] (9548fe03-7e73-44ac-b830-0baab40b0db1) {'id': '9548fe03-7e73-44ac-b830-0baab40b0db1', 'created_at': datetime.datetime(2021, 11, 15, 0, 54, 37, 591952), 'updated_at': datetime.datetime(2021, 11, 15, 0, 59, 46, 850405), 'age': '23'}"]
(hbnb) User.count()
1
(hbnb) create User
80f5df59-9464-4342-a401-8f65146a5d48
(hbnb) User.destroy("9548fe03-7e73-44ac-b830-0baab40b0db1")
(hbnb) all User
["[User] (80f5df59-9464-4342-a401-8f65146a5d48) {'id': '80f5df59-9464-4342-a401-8f65146a5d48', 'created_at': datetime.datetime(2021, 11, 15, 1, 2, 57, 860397), 'updated_at': datetime.datetime(2021, 11, 15, 1, 2, 57, 860419)}"]
(hbnb) show User 9548fe03-7e73-44ac-b830-0baab40b0db1
** no instance found **
(hbnb) create
** class name missing **
(hbnb) create fg
** class doesn't exist **
(hbnb) quit
➜  AirBnB_clone git:(main)
```

## Contributing

We welcome any contribution to this project irrespective of the size. If you contribute to this project, please add your name to the [AUTHORS](AUTHORS) file. You should add your name whilst ensuring that the list of authors are in alphabetical order with the firstname provided first, an optional set of middle names, your last name, and your email address enclosed in angle brackets. An example is shown below.

```csharp
John Doe <john_doe@dogemail.com>
```

**NOTE:** Before you push any commit, please run the script `./test.sh` to ensure that no tests are failing and your code complies with this project's styling standard.
