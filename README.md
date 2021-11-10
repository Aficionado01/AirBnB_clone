# AirBnB Clone

![Repo size](https://img.shields.io/github/repo-size/B3zaleel/AirBnB_clone)
![Code size](https://img.shields.io/github/languages/code-size/B3zaleel/AirBnB_clone.svg)
![Pep8 style](https://img.shields.io/badge/PEP8-style%20guide-purple?style=round-square)
![Latest commit](https://img.shields.io/github/last-commit/B3zaleel/AirBnB_clone/main?style=round-square)

## Description

This project is the first part of an **AirBnB** clone web project that supports the serialization and deserialization of simple data sets using a simple file storage. The data sets are serialized to a JSON file format for the purpose of simplicity. This project supports a simple console-based command interpreter for managing the supported data sets ([more below](#supported_data_sets)).

## The Command Interpreter

The command interpreter provides a simple REPL (Read-Evaluate-Print-Loop) for interacting with the models in this project only.

### How To Use

The command interpreter can be started by running `./console.py` in your terminal. This would create an interactive REPL session which can be terminated by running `EOF` or `quit`. A non-interactive session exits after running the last command the interpreter received such as in `echo "all" | ./console.py`.

### Supported Commands

These are commands that can be executed by the command interpreter. They have the format `command [argument]...`.

| Format | Description |
|:-|:-|
| `help [command]` | Prints helpful information about a command (`command`). Default command: _help_. |
| `quit` | Closes the command interpreter. |
| `EOF` | Closes the command interpreter. |
| `create ClassName` | Creates a new instance of the `ClassName` class. |
| `show ClassName id` | Prints the string representation of an instance of the `ClassName` class with id `id`. |
| `destroy ClassName id` | Deletes an instance of the `ClassName` class with id `id`. |
| `all [ClassName]` | Prints a list of the string representation of all instances of the `ClassName` class. Default class name: `BaseModel`. |
| `update ClassName id attr_name attr_value` | Updates an instance of the `ClassName` class with id `id` by assigning the attribute value `attr_value` to its attribute named `attr_name`. Attributes having the names `id`, `created_at`, and `updated_at` are silently ignored. Only simple arguments like _integers_, _floats_, and _strings_ are supported. |

### Class-Based Actions

These are actions that are performed based on a given class. They have the format `ClassName.action([argument]...)`.

| Format | Description |
|:-|:-|
| `ClassName.all()` | Retrieves all objects that are instances of `ClassName`. |
| `ClassName.count()` | Retrieves the number of objects that are instances of `ClassName`. |
| `ClassName.show(id)` | Retrieves an object that is an instance of `ClassName` with the given `id`. |
| `ClassName.destroy(id)` | Removes an object that is an instance of `ClassName` with the given `id`. |
| `ClassName.update(id, attr_name, attr_value)` | Updates an object that is an instance of `ClassName` with the given `id`. Updates to `id`, `created_at`, and `updated_at` are ignored silently. |
| `ClassName.update(id, dict_repr)` | Updates an object that is an instance of `ClassName` with the key, value pairs in the given `dict_repr` dictionary. Updates to `id`, `created_at`, and `updated_at` are ignored silently. |

### Supported Data Sets

| Class | Description |
|:-|:-|
| BaseModel | Represents the base class for all data set models (All data set models are instances of this class). |
| User | Represents a user account for this project. |
| State | Represents the geographical state in which a _User_ lives. |
| City | Represents an urban area in a _State_. |
| Amenity | Represents the geographical state in which a _User_ lives. |
| Place | Represents a building that a _User_ can rent. |
| Review | Represents a review of a _Place_. |

### Examples
