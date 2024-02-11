# AirBnB Clone - The Console

Welcome to the AirBnB Clone project! This is the first step towards building  a full web application: the AirBnB clone. In this project, we are going to create a command interpreter known as "The Console" which allows us to manage AirBnB objects.

## Background Context

This project is designed to teach us various fundamental concepts in Python, such as:

+ Python packages and modules.
+ Object-Oriented Programming (OOP).
+ Creating a command interpreter using the cmd module.
+ Serialization and deserialization.
+ Writing and reading a JSON file.
+ Unit testing using the unittest framework.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tekna28/AirBnB_clone.git
```

2. Navigate to the project directory:

```bash
cd AirBnB_clone
```

3. Run the console:

```bash
./console.py
```

## Usage

Once the console is launched, you can start using various commands to manage your AirBnB objects. You can type help or help "command" to get more information about specific commands.

## Console Commands

The console supports the following commands:

+ create:

      Usage: create <class>
Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.

+ show
       
      Usage: show <class> <id> or <class>.show(<id>)
Prints the string representation of a class instance based on a given id.

+ destroy

      Usage: destroy <class> <id> or <class>.destroy(<id>)
Deletes a class instance based on a given id. The storage file file.json is updated accordingly.

+ all

      Usage: all or all <class> or <class>.all()
Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.

+ count

      Usage: count <class> or <class>.count()
Retrieves the number of instances of a given class.

+ update

      Usage: update <class> <id> <attribute name> "<attribute value>" or <class>.update(<id>, <attribute name>, <attribute value>) or <class>.update( <id>, <attribute dictionary>).
Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at). However, any attribute can be updated by providing a dictionary.

## Contributor:

+ Jeghloul Salma - [Github](https://github.com/tekna28)
