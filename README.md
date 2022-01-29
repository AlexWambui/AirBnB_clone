# 0x00. AirBnB clone - The console
Command interpreter to manage the AirBnB objects...
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances.
- create a simple flow of serializaion / deserialization: instance <-> Dictionary <-> JSON string <-> file
- create all classess used for AirBnB (user, State, City, Place ...) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unit tests to validate all classes and the storage engine.

## The Command Interpreter:
Use cases include:
- Create a new object (ex: a new User or a new Place)
- retrieve an object from a file, a database etc...
- do operations on objects (count, compute stats, etc...)
- update attributes of an object
- destroy an object

