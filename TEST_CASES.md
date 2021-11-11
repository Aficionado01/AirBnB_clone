# Test Cases

## Test Cases To Cover
----------------------

### BaseModel

### FileStorage


### HBNBCommand

+ [x] The prompt should be `(hbnb)`.
+ [x] Running an empty line (composed of whitespaces) does nothing (does not print the output of the last command).
+ [x] Running `EOF` or `quit` causes the console to exit with a status code of 0.
+ [ ] Running `help` prints a help menu.
+ [ ] Running `help quit` prints a help message about `quit`.
+ [ ] Running `help quit 25` prints a help message about `quit`.
+ [ ] Running `help 25` prints a command not found error message.

#### create Command

+ [ ] Running `create` prints a missing class name error message.
+ [ ] Running `create 25` prints a non-existing class name error message.
+ [ ] Running `create 25 User` prints a non-existing class name error message.
+ [ ] Running `create User` creates a new User, stores it to the file storage, and prints the id of the newly created Model object.
+ [ ] Running `create "User"` creates a new User, stores it to the file storage, and prints the id of the newly created Model object.
+ [ ] Running `create User 25` creates a new User, stores it to the file storage, and prints the id of the newly created Model object.

#### all Command

+ [ ] Running `all` prints a list consisting of the string representation of all BaseModel instances.
+ [ ] Running `all 25` prints a non-existing class name error message.
+ [ ] Running `all 25 User` prints a non-existing class name error message.
+ [ ] Running `all User` prints a list consisting of the string representation of all User instances.
+ [ ] Running `all "User"` prints a list consisting of the string representation of all BaseModel instances.
+ [ ] Running `all User 25` prints a list consisting of the string representation of all BaseModel instances.

#### show Command

+ [ ] Running `show` prints a missing class name error message.
+ [ ] Running `show 25` prints a non-existing class name error message.
+ [ ] Running `show 25 User` prints a non-existing class name error message.
+ [ ] Running `show 49faff9a-6318-451f-87b6-910505c55907 User` prints a non-existing class name error message.
+ [ ] Running `show User` prints a missing id error message.
+ [ ] Running `show "User"` prints a missing id error message.
+ [ ] Running `show User 35` prints a non-existing instance id error message.
+ [ ] Running `show User 35 49faff9a-6318-451f-87b6-910505c55907` prints a non-existing instance id error message.
+ [ ] Running `show State 49faff9a-6318-451f-87b6-910505c55907` prints the string representation of a State model with the id `49faff9a-6318-451f-87b6-910505c55907`.
+ [ ] Running `show State 49faff9a-6318-451f-87b6-910505c55907 2dd6ef5c-467c-4f82-9521-a772ea7d84e9` prints only the string representation of a State model with the id `49faff9a-6318-451f-87b6-910505c55907`.
+ [ ] Running `show State 49faff9a-6318-451f-87b6-910505c55907 State 2dd6ef5c-467c-4f82-9521-a772ea7d84e9` prints only the string representation of a State model with the id `49faff9a-6318-451f-87b6-910505c55907`.
+ [ ] Running `show State 49faff9a-6318-451f-87b6-910505c55907 Place 2dd6ef5c-467c-4f82-9521-a772ea7d84e9` prints only the string representation of a State model with the id `49faff9a-6318-451f-87b6-910505c55907`.

#### destroy Command

+ [ ] Running `destroy` prints a missing class name error message.
+ [ ] Running `destroy 25` prints a non-existing class name error message.
+ [ ] Running `destroy 25 User` prints a non-existing class name error message.
+ [ ] Running `destroy 49faff9a-6318-451f-87b6-910505c55907 User` prints a non-existing class name error message.
+ [ ] Running `destroy User` prints a missing id error message.
+ [ ] Running `destroy "User"` prints a missing id error message.
+ [ ] Running `destroy User 35` prints a non-existing instance id error message.
+ [ ] Running `destroy User 35 49faff9a-6318-451f-87b6-910505c55907` prints a non-existing instance id error message.
+ [ ] Running `destroy State 49faff9a-6318-451f-87b6-910505c55907` deletes a State model with the id `49faff9a-6318-451f-87b6-910505c55907`.
+ [ ] Running `destroy State 49faff9a-6318-451f-87b6-910505c55907 2dd6ef5c-467c-4f82-9521-a772ea7d84e9` deletes only the State model with the id `49faff9a-6318-451f-87b6-910505c55907`.
+ [ ] Running `destroy State 49faff9a-6318-451f-87b6-910505c55907 State 2dd6ef5c-467c-4f82-9521-a772ea7d84e9` deletes only the State model with the id `49faff9a-6318-451f-87b6-910505c55907`.
+ [ ] Running `destroy State 49faff9a-6318-451f-87b6-910505c55907 Place 2dd6ef5c-467c-4f82-9521-a772ea7d84e9` deletes only the State model with the id `49faff9a-6318-451f-87b6-910505c55907`.
+ [ ] The output of `destroy` is always a blank line when the arguments are valid.

#### update Command

+ [ ] Running `update` prints a missing class name error message.
+ [ ] Running `update 25` prints a non-existing class name error message.
+ [ ] Running `update 25 User` prints a non-existing class name error message.
+ [ ] Running `update 49faff9a-6318-451f-87b6-910505c55907 User` prints a non-existing class name error message.
+ [ ] Running `update User` or `update "User"` prints a missing id error message.
+ [ ] Running `update User 35` prints a non-existing instance id error message.
+ [ ] Running `update User 35 49faff9a-6318-451f-87b6-910505c55907` prints a non-existing instance id error message.
+ [ ] Running `update User 49faff9a-6318-451f-87b6-910505c55907` prints a missing attribute name error message.
+ [ ] Running `update User 49faff9a-6318-451f-87b6-910505c55907 age` prints a missing attribute value error message.
+ [ ] Running `update User 49faff9a-6318-451f-87b6-910505c55907 age 34` adds the attribute `age` with a value of `34` to the `User` object with id `49faff9a-6318-451f-87b6-910505c55907`.
+ [ ] Running `update User 49faff9a-6318-451f-87b6-910505c55907 age 34 height 1.8m` adds the attribute `age` with a value of `34` to the `User` object with `id` `49faff9a-6318-451f-87b6-910505c55907` only.
+ [ ] Running `update User 49faff9a-6318-451f-87b6-910505c55907 id 34` doesn't change the `id` of the `User` object with `id` `49faff9a-6318-451f-87b6-910505c55907`.
+ [ ] Running `update User 49faff9a-6318-451f-87b6-910505c55907 created_at "datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)"` doesn't change the `created_at` attribute of the `User` object with `id` `49faff9a-6318-451f-87b6-910505c55907`.
+ [ ] Running `update User 49faff9a-6318-451f-87b6-910505c55907 updated_at "datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)"` doesn't change the `updated_at` attribute of the `User` object with `id` `49faff9a-6318-451f-87b6-910505c55907`.
+ [ ] The output of `update` is always a blank line when the arguments are valid.



### User


### State


### City


### Amenity


### Place


### Review

