#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = "(hbnb)"
    classes = {"BaseModel", "State", "City",
               "Amenity", "Place", "Review", "User"}

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        print()
        return True

    def do_quit(self, line):
        """Exit on quit"""
        return True

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_create(self, line):
        """Create instance specified by user"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Print string representation: name and id"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Destroy instance specified by user; Save changes to JSON file"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """Print all objects or all objects of specified class"""
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, line):
        """Display count of instances specified"""
        if line in HBNBCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """Accepts class name followed by arguement"""
        args = line.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                HBNBCommand.do_all(self, class_arg)
            elif command == 'count':
                HBNBCommand.do_count(self, class_arg)
            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                #!/usr/bin/python3
"""Command line console for HBNB"""


import ast
import shlex
import json
import cmd
import readline
import models
BaseModel = models.user.BaseModel
User = models.user.User
Place = models.place.Place
State = models.state.State
Amenity = models.amenity.Amenity
Review = models.review.Review
City = models.city.City
storage = models.storage


class HBNBCommand(cmd.Cmd):
    """Command line console for HBNB. Use 'help' or '?' in console
    for command documentation.
    """
    prompt = '(hbnb) '
    __validclasses = ["BaseModel", "User", "Place", "Amenity", "Review",
                      "City", "State"]

    def do_create(self, arg):
        """Create an instance of a class.
        Usage: create <classname>
        """
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] == "BaseModel":
            newmodel = BaseModel()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "User":
            newmodel = User()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "Place":
            newmodel = Place()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "Amenity":
            newmodel = Amenity()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "Review":
            newmodel = Review()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "City":
            newmodel = City()
            print(newmodel.id)
            storage.new(newmodel)
        elif arg[0] == "State":
            newmodel = State()
            print(newmodel.id)
            storage.new(newmodel)
        else:
            print("** class doesn't exist **")
            return
        storage.save()

    def do_show(self, arg):
        """Show an instance of a class.
        Usage: show <classname> <uuid>
        """
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
            return
        if arg[0] not in self.__validclasses:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
        else:
            obj = storage.get_object(arg[1])
            if obj is None or obj.__class__.__name__ != arg[0]:
                print("** no instance found **")
            else:
                print(str(obj))

    def do_destroy(self, arg):
        """Destroy a class instance by uuid.
        Usage: destroy <classname> <uuid>
        """
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
        else:
            if arg[0] in self.__validclasses:
                if len(arg) < 2:
                    print("** instance id missing **")
                else:
                    try:
                        del storage.all()[arg[0] + "." + arg[1]]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all instances of a class, or all instances with no args.
        Usage: all [classname]
        """
        arg = shlex.split(arg)
        objects = storage.all()
        if len(arg) < 1:
            print("[\"", end="")
            print("\", \"".join(str(objects[obj])
                                for obj in objects), end="")
            print("\"]")
        else:
            if arg[0] in self.__validclasses:
                listclass = [str(objects[obj]) for obj in objects
                             if objects[obj].__class__.__name__ == arg[0]]
                print("[\"", end="")
                print("\", \"".join(listclass), end="")
                print("\"]")
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance of a class based on uuid
        Usage: update <classname> <uuid> <attribute> <value>
        """
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
            return
        if arg[0] not in self.__validclasses:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        obj = storage.get_object(arg[1])
        if obj:
            if len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                """Might want to check invalid data type here"""
                try:
                    setattr(obj, arg[2], ast.literal_eval(arg[3].strip()))
                except (ValueError, SyntaxError):
                    setattr(obj, arg[2], arg[3])
                obj.save()
        else:
            print("** no instance found **")

    def _do_count(self, arg):
        """prints the number of a type of instance in storage.
        Usage: count <classname>
        """
        arg = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
            return
        count = 0
        objects = storage.all()
        for key in objects:
            if objects[key].__class__.__name__ == arg[0]:
                count += 1
        print(count)

    def default(self, line):
        """Parse function style syntax for some commands. Regular error
        message otherwise.
        """
        classname = line.split(".", 1)
        if len(classname) < 2:
            print("** Unknown syntax:", line)
            return
        if classname[0] not in self.__validclasses:
            print("** class doesn't exist **")
            return
        methodname = classname[1].split("(", 1)
        if methodname[0] not in ["count", "all", "show", "destroy", "update"]\
           or len(methodname) < 2:
            print("** Unknown syntax:", line)
            return
        methodname[1] = methodname[1].strip()
        if len(methodname[1]) < 1 or methodname[1][-1] != ')':
            print("** Unknown syntax:", line)
            return
        args = methodname[1][:-1]
        if methodname[0] == "show":
            return self.do_show(classname[0] + " " + args)
        if methodname[0] == "all":
            return self.do_all(classname[0])
        if methodname[0] == "destroy":
            return self.do_destroy(classname[0] + " " + args)
        if methodname[0] == "count":
            return self._do_count(classname[0])
        if methodname[0] == "update":
            if len(args) < 1:
                print("** no instance found **")
                return
            attrchk = args.split(",", 1)
            if len(attrchk) < 2:
                print("** attribute not found **")
                return
            if attrchk[1].strip()[0] == "{":
                return self.update_dict(args, classname[0])
            else:
                args = args.split(",", 2)
                return self.do_update(" ".join([classname[0]] + args))

    def update_dict(self, args, classname):
        """Loads dictionary from args string then updates instance.
        Input args should be id then dict
        """
        args = args.split(",", 1)
        try:
            dicty = ast.literal_eval(args[1].strip())
            if type(dicty) is not dict:
                print("** bad dictionary **")
        except Exception:
            print("** bad dictionary **")
            return
        else:
            obj = storage.get_object(args[0].strip("'\""))
            if obj is None or obj.__class__.__name__ != classname:
                print("** no instance found **")
                return
            for attr in dicty:
                setattr(obj, attr, dicty[attr])

    def do_quit(self, arg):
        """Quit the shell"""
        return 1

    def do_EOF(self, arg):
        """Quit the shell"""
        print()
        return 1

    def emptyline(self):
        """Don't do anything if there's an empty line"""
        return 0


if __name__ == "__main__":
    HBNBCommand().cmdloop()
