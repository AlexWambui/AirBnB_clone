#!/usr/bin/python3
"""
Building a command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
	"""
	Command interpreter for the HBNB console.
	"""
	prompt = "(hbnb) "
#	intro = '''
#	|+-----------------------------------------+|
#	|                                           |
#	| Welcome to the HBNB Console!              |
#	| Enter 'help' to see a list of commands.   |
#	|                                           |
#	|+-----------------------------------------+|
#	|
#	|
#	'''
	
	def do_quit(self, line):
		"""Quit command to exit the program."""
		raise SystemExit

	def do_EOF(self, line):
		"""Exit with Ctrl+D."""
		return True

	def do_help(self, line):
		"""
		Get help on commands.
		Usage: help <command>
		"""
		cmd.Cmd.do_help(self, line)

	def emptyline(self):
		"""Do nothing on empty input."""
		pass

if __name__ == "__main__":
	HBNBCommand().cmdloop()

