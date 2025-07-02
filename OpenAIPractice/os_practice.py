import os

'''
os.getcwd() - Get the current working directory(where the script is run from)
os.path.dirname(__file__) - Get the folder that contains the current Python script
os.path.join() - Combine path is a safe, cross-platform way
os.path.abspath() - Convert a relative path to an absolute path
os.path.exists() - Check whether a file or folder exists
os.makedirs() - Create a folder (and any parent folders if necessary)

os.curdir - Get the current working directory (same as os.getcwd())
os.pardir() - Get the parent directory of the current working directory
'''

# Get the current working directory using os.curdir
current_dir = os.curdir
print("Current Working Directory (os.curdir):", current_dir)

parent_dir = os.pardir
print("Parent Directory (os.pardir()):", parent_dir)

# Get the current working directory
current_dir = os.getcwd()
print("Current Working Directory:", current_dir)

# Get the directory of the current Python file
script_dir = os.path.dirname(os.path.abspath(__file__))
print("Directory of the current script:", script_dir)

# Join path components into a full path (e.g., script_dir/data/output.txt)
target_file = os.path.join(script_dir, "data","output.txt")
print("Joined target file path:", target_file)

# Get the absolute path of the target file
abs_path = os.path.abspath(target_file)
print("Absolute path of target file:", abs_path)

# Check if the directory 'data' exists
data_dir = os.path.join(script_dir, "data")
if not os.path.exists(data_dir):
    print("Directory 'data' does not exist. Creating it...")
    os.makedirs(data_dir)
else:
    print("Directory 'data' already exists.")

# Now you can write somthing to the file (optional)
with open(target_file, "w") as f:
    f.write("This is a test.\n")

print("File has been created and written to.")