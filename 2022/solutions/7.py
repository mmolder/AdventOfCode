# Parse the input data to create a tree representation of the filesystem
# This example assumes that the input data is stored in a list of strings called "lines"

from utils.utils import readFile

lines = [x for x in readFile('dummy_7.txt')]

class File:
	def __init__(self, name, size):
		self.name = name
		self.size = size

class Directory:
	def __init__(self, name):
		self.name = name
		self.children = []

current_dir = Directory("/")  # The outermost directory
dir_stack = [current_dir]  # Stack to keep track of the current directory

for line in lines:
	print(line)
	if line.startswith("$ cd"):
		# Change directory
		parts = line.split()
		if parts[2] == "..":
			# Move up one level
			dir_stack.pop()
		elif parts[2] == "/":
			# Move to the outermost directory
			current_dir = Directory("/")
			dir_stack = [current_dir]
		else:
			# Move into a child directory
			for child in current_dir.children:
				if child.name == parts[2]:
					current_dir = child
					dir_stack.append(current_dir)
					break
	elif line.startswith("$ ls"):
		# List the contents of the current directory
		parts = line.split()
		print(parts)
		i = 1
		while i < len(parts):
			if parts[i] == "dir":
				# Add a new directory as a child of the current directory
				current_dir.children.append(Directory(parts[i+1]))
			else:
				# Add a new file as a child of the current directory
				current_dir.children.append(File(parts[i+1], int(parts[i])))
			i += 2

# Define a recursive function that calculates the total size of a directory
def total_size(dir):
	size = 0
	for child in dir.children:
		if isinstance(child, Directory):
			# If the child is a directory, calculate its total size recursively
			size += total_size(child)
		else:
			# If the child is a file, add its size to the total
			size += child.size
	return size

# Calculate the total sizes of all of the directories
sizes = []
for dir in dir_stack[0].children:
	sizes.append(total_size(dir))

# Sum the sizes of the directories with a total size of at most 100000
result = 0
for size in sizes:
	if size <= 100000:
		result += size

print(result)