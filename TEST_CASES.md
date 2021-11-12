# Test Cases

This is a listing of the test cases to cover in the unittets of this project.

## Test Cases To Cover

### BaseModel

+ [x] `BaseModel` contains the public instance attributes: `id` (str), `created_at` (datetime), and `updated_at` (datetime).
+ [x] `BaseModel()` creates a `BaseModel` object using the current datetime for `created_at` and `updated_at`, and creates a unique `id` for the object.
+ [x] `BaseModel(None)` creates a `BaseModel` object using the current datetime for `created_at` and `updated_at`, and creates a unique `id` for the object.
+ [x] `BaseModel('56d43177-cc5f-4d6c-a0c1-e167f8c27337')` creates a `BaseModel` object using the current datetime for `created_at` and `updated_at`, and creates a unique `id` for the object that is not `56d43177-cc5f-4d6c-a0c1-e167f8c27337`.
+ [x] `BaseModel(**{})` creates a `BaseModel` object using the current datetime for `created_at` and `updated_at`, and creates a unique `id` for the object.
+ [x] `BaseModel('78', datetime.now(), datetime.now(), **{})` creates a `BaseModel` object using the current datetime for `created_at` and `updated_at`, and creates a unique `id` for the object.
+ [x] `BaseModel(**{'id': None})` creates a `BaseModel` object without the `created_at` and `updated_at` attributes, and the `id` attribute is `None`.
+ [x] `BaseModel(**{'id': 45})` creates a `BaseModel` object without the `created_at` and `updated_at` attributes, and the `id` attribute is `45`.
+ [x] `BaseModel(**{'id': 45, '__class__': 'Foo'})` creates a `BaseModel` object without the  `created_at` and `updated_at` attributes, and the `id` attribute is `45`.
+ [x] `BaseModel(**{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime(2017, 9, 28, 21, 3, 54, 52298)})` throws a `TypeError` for `created_at`.
+ [x] `BaseModel(**{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'updated_at': datetime(2017, 9, 28, 21, 3, 54, 52298)})` throws a `TypeError` for `updated_at`.
+ [x] `str(BaseModel())` works correctly.
+ [x] `BaseModel().save()` works correctly.
+ [x] `BaseModel().to_dict()` works correctly.

### FileStorage

+ [x] `FileStorage` contains the private class attributes: `__file_path` (str) and `__objects` (dict).
+ [x] `FileStorage().all()` works correctly.
+ [x] `FileStorage().new(obj)` works correctly.
+ [x] `FileStorage().save()` works correctly.
+ [x] `FileStorage().reload()` works correctly.
+ [x] All the tests above should be working for all models, which include `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, and `Review`.

### HBNBCommand

+ [x] The prompt should be `(hbnb)`.
+ [x] Running an empty line (composed of whitespaces) does nothing (does not print the output of the last command).
+ [x] Running `EOF` or `quit` causes the console to exit with a status code of 0.
+ [x] Running `help` prints a help menu.
+ [x] Running `help quit` prints a help message about `quit`.
+ [x] Running `help quit 25` prints a help message about `quit`.
+ [x] Running `help 25` prints a no help found error message.

#### _create_ Command

+ [x] Running `create` prints a missing class name error message.
+ [x] Running `create 25` prints a non-existing class name error message.
+ [x] Running `create 25 User` prints a non-existing class name error message.
+ [x] Running `create User` creates a new User.
+ [x] Running `create "User"` creates a new User.
+ [x] Running `create User 25` creates a new User.
+ [x] The `create` class action always commits its changes and prints the id of the newly created model object to `stdout` upon a successful execution.

#### _all_ Command

+ [x] Running `all` prints a list consisting of the string representation of all BaseModel instances.
+ [x] Running `all 25` prints a non-existing class name error message.
+ [x] Running `all 25 User` prints a non-existing class name error message.
+ [x] Running `all User` prints a list consisting of the string representation of all `User` instances.
+ [x] Running `all "User"` prints a list consisting of the string representation of all `BaseModel` instances.
+ [x] Running `all User 25` prints a list consisting of the string representation of all `User` instances.

#### _show_ Command

+ [x] Running `show` prints a missing class name error message.
+ [x] Running `show 25` prints a non-existing class name error message.
+ [x] Running `show 25 User` prints a non-existing class name error message.
+ [x] Running `show 49faff9a-6318-451f-87b6-910505c55907 User` prints a non-existing class name error message.
+ [x] Running `show User` prints a missing id error message.
+ [x] Running `show "User"` prints a missing id error message.
+ [x] Running `show User 35` prints a non-existing instance id error message.
+ [x] Running `show User 35 49faff9a-6318-451f-87b6-910505c55907` prints a non-existing instance id error message.
+ [x] Running `show State 49faff9a-6318-451f-87b6-910505c55907` prints the string representation of a State model with the id `49faff9a-6318-451f-87b6-910505c55907`.
+ [x] Running `show State 49faff9a-6318-451f-87b6-910505c55907 2dd6ef5c-467c-4f82-9521-a772ea7d84e9` prints only the string representation of a State model with the id `49faff9a-6318-451f-87b6-910505c55907`.
+ [x] Running `show State 49faff9a-6318-451f-87b6-910505c55907 State 2dd6ef5c-467c-4f82-9521-a772ea7d84e9` prints only the string representation of a State model with the id `49faff9a-6318-451f-87b6-910505c55907`.
+ [x] Running `show State 49faff9a-6318-451f-87b6-910505c55907 Place 2dd6ef5c-467c-4f82-9521-a772ea7d84e9` prints only the string representation of a State model with the id `49faff9a-6318-451f-87b6-910505c55907`.

#### _destroy_ Command

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
+ [ ] The `destroy` class action always commits its changes and prints nothing to `stdout` upon a successful execution.

#### _update_ Command

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
+ [ ] The `update` command always commits its changes and prints nothing to `stdout` upon a successful execution.



#### General Class Actions

+ [x] Running `foo.a` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `User.a` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `User.all` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `User.all(` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `User.all)` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `User.all(")` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `User.all(1 23)` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `User.foo()` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `.foo()` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `User.()` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `User()` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `User.show "49faff9a-6318-451f-87b6-910505c55907"` throws the invalid syntax error message from the `cmd.CMD` class.
+ [x] Running `foo.all()` throws the class doesn't exist error message.

#### _all_ Class Action

+ [ ] Running `User.all()` prints a list consisting of the string representation of all `User` objects, not enclosed by quotes but separated by a comma.
+ [ ] Running `User.all("49faff9a-6318-451f-87b6-910505c55907")` prints a list consisting of the string representation of all `User` objects, not enclosed by quotes but separated by a comma.
+ [ ] Running `User.all(None)` prints a list consisting of the string representation of all `User` objects, not enclosed by quotes but separated by a comma.
+ [ ] Running `User.all(12, '34')` prints a list consisting of the string representation of all `User` objects, not enclosed by quotes but separated by a comma.

#### _count_ Class Action

+ [x] Running `User.count()` prints the number of all `User` objects.
+ [x] Running `User.count("49faff9a-6318-451f-87b6-910505c55907")` prints the number of all `User` objects.
+ [x] Running `User.count(None)` prints the number of all `User` objects.
+ [x] Running `User.count(12, '34')` prints the number of all `User` objects.


#### _show_ Class Action

+ [x] Running `User.show()` prints an instance id missing error message.
+ [x] Running `User.show(34)` prints an instance not found error message.
+ [x] Running `User.show(3.4)` prints an instance not found error message.
+ [x] Running `User.show("246c227a-d5c1")` prints an instance not found error message.
+ [x] Running `User.show("49faff9a-6318-451f-87b6-910505c55907")` prints the string representation of a `User` object with the `id` `49faff9a-6318-451f-87b6-910505c55907` if it exists, otherwise it prints an instance not found error message.
+ [x] Running `User.show("49faff9a-6318-451f-87b6-910505c55907", "246c227a-d5c1-403d-9bc7-6a47bb9f0f68")` prints only the string representation of a `User` object with the `id` `49faff9a-6318-451f-87b6-910505c55907` if it exists, otherwise it prints an instance not found error message.

#### _destroy_ Class Action

+ [ ] Running `User.destroy(34)` prints an instance not found error message.
+ [ ] Running `User.destroy(3.4)` prints an instance not found error message.
+ [ ] Running `User.destroy("246c227a-d5c1")` prints an instance not found error message.
+ [ ] Running `User.destroy("49faff9a-6318-451f-87b6-910505c55907")` deletes the `User` object with the `id` `49faff9a-6318-451f-87b6-910505c55907` if it exists, otherwise it prints an instance not found error message.
+ [ ] Running `User.destroy("49faff9a-6318-451f-87b6-910505c55907", "246c227a-d5c1-403d-9bc7-6a47bb9f0f68")` deletes only the `User` object with the `id` `49faff9a-6318-451f-87b6-910505c55907` if it exists, otherwise it prints an instance not found error message.
+ [ ] The `destroy` class action always commits its changes and prints nothing to `stdout` upon a successful execution.

#### _update_ Class Action

+ [ ] Running `User.update(34)` prints an instance not found error message.
+ [ ] Running `User.update(3.4)` prints an instance not found error message.
+ [ ] Running `User.update("246c227a-d5c1")` prints an instance not found error message.
+ [ ] Running `User.update("49faff9a-6318-451f-87b6-910505c55907")` prints an attribute name missing error message if the `User` object `id` exists, otherwise it prints an instance not found error message.
+ [ ] Running `User.update("49faff9a-6318-451f-87b6-910505c55907", "age")` prints an attribute value missing error message if the `User` object `id` exists, otherwise it prints an instance not found error message.
+ [ ] Running `User.update("49faff9a-6318-451f-87b6-910505c55907", "age", 74)` sets the value of the `age` attribute to `74` of the `User` object with `id == "49faff9a-6318-451f-87b6-910505c55907"` if it exists, otherwise it prints an instance not found error message.
+ [ ] Running `User.update("49faff9a-6318-451f-87b6-910505c55907", "age", 74, 33)` sets the value of the `age` attribute to `74` of the `User` object with `id == "49faff9a-6318-451f-87b6-910505c55907"` if it exists, otherwise it prints an instance not found error message.
+ [ ] Running `User.update("49faff9a-6318-451f-87b6-910505c55907", "age", 74, "height", "1.67m")` sets only the value of the `age` attribute to `74` of the `User` object with `id == "49faff9a-6318-451f-87b6-910505c55907"` if it exists, otherwise it prints an instance not found error message.
+ [ ] Running `User.update("49faff9a-6318-451f-87b6-910505c55907", {})` performs no update to the `User` object with the `id` `49faff9a-6318-451f-87b6-910505c55907` if it exists, otherwise it prints an instance not found error message.
+ [ ] Running `User.update("49faff9a-6318-451f-87b6-910505c55907", {"age": 74})` sets only the value of the `age` attribute to `74` of the `User` object with the `id` `49faff9a-6318-451f-87b6-910505c55907` if it exists, otherwise it prints an instance not found error message.
+ [ ] Running `User.update("49faff9a-6318-451f-87b6-910505c55907", {"age": 74}, "hair_color", "pink")` sets only the value of the `age` attribute to `74` of the `User` object with the `id` `49faff9a-6318-451f-87b6-910505c55907` if it exists, otherwise it prints an instance not found error message.
+ [ ] The `update` class action always commits its changes and prints nothing to `stdout` upon a successful execution.
+ [ ] All the tests above should be working for all models, which include `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, and `Review`.

### User

+ [x] `User` is an instance of `BaseModel`.
+ [x] `User` contains the public class attributes: `email` (str), `password` (str), `first_name` (str), and `last_name` (str).
+ [ ] `str(User())` works correctly.
+ [ ] `User().save()` works correctly.
+ [ ] `User().to_dict()` works correctly.

### State

+ [x] `State` is an instance of `BaseModel`.
+ [x] `State` contains the public class attribute `name` (str).
+ [ ] `str(State())` works correctly.
+ [ ] `State().save()` works correctly.
+ [ ] `State().to_dict()` works correctly.

### City

+ [x] `City` is an instance of `BaseModel`.
+ [x] `City` contains the public class attributes: `state_id` (str) and `name` (str).
+ [ ] `str(City())` works correctly.
+ [ ] `City().save()` works correctly.
+ [ ] `City().to_dict()` works correctly.

### Amenity

+ [x] `Amenity` is an instance of `BaseModel`.
+ [x] `Amenity` contains the public class attribute `name` (str).
+ [ ] `str(Amenity())` works correctly.
+ [ ] `Amenity().save()` works correctly.
+ [ ] `Amenity().to_dict()` works correctly.

### Place

+ [x] `Place` is an instance of `BaseModel`.
+ [x] `Place` contains the public class attributes: `city_id` (str), `user_id` (str), `name` (str), `description` (str), `number_rooms` (int), `number_bathrooms` (int), `max_guest` (int), `price_by_night` (int), `latitude` (float), `longitude` (float), and `amenity_ids` (list).
+ [ ] `str(Place())` works correctly.
+ [ ] `Place().save()` works correctly.
+ [ ] `Place().to_dict()` works correctly.

### Review

+ [x] `Review` is an instance of `BaseModel`.
+ [x] `Review` contains the public class attributes: `place_id` (str), `user_id` (str), and `text` (str).
+ [ ] `str(Review())` works correctly.
+ [ ] `Review().save()` works correctly.
+ [ ] `Review().to_dict()` works correctly.

