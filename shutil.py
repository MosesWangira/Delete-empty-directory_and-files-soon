import shutil
import os

#give a name of directory to delete
print("You will enter folder name below")
folder_name = input("Enter folder name : ")
print(folder_name + " will be deleted")

#deletes directories + all files
shutil.rmtree(r"I:\{0}".format(folder_name))
print("deleting directory + files!!")
