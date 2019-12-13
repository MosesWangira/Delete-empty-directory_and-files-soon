import shutil
import os
from os import path

#show list of all directories in labelled volume
print("************************************************************************")
volume_name = input("Enter Local disk letter to check : ")
directories = os.listdir(r"{0}:".format(volume_name))
print("\n".join(directories))
print("************************************************************************")


#listing files using for loop
print("*****************************************")
path_dir = os.listdir(r"{}:".format(volume_name))
for files in path_dir:
    count = 0
    #checking if directory is empty
    try:
       if not os.listdir(r"{0}:\{1}".format(volume_name,files)):
           #print("directory empty")
           #print("directory is emty !!Deleting!! ")
           #print("*************************")
           shutil.rmtree(r"{0}:\{1}".format(volume_name,files))
    except NotADirectoryError:
        #print("not a directory")
        continue
    except PermissionError:
        continue
    except FileNotFoundError:
        continue
print("Empty folders deleted or no empty folders exist")
print("*****************************************")


#deletes empty directories function
def deleteEmptyDirectories():
    #give a name of directory to delete
    print("You will enter folder name below")
    folder_name = input("Enter folder name : ")
    print(folder_name + " will be deleted")
    if (path.exists(r"I:\{0}".format(folder_name))):
        print("*************************")
        print("directory exists")
        print("Checking if {0} directory is empty".format(folder_name))
        print("*************************")
        #checking if directory is empty
        if not os.listdir(r"I:\{0}".format(folder_name)):
            print("directory is emty !!Deleting!! ")
            print("*************************")
            shutil.rmtree(r"I:\{0}".format(folder_name))
            print("{} directory deleted".format(folder_name))
        else:
            print("directory not empty can not delete")

    else:
         print("***************************************")
         print("{0} directory does not exist!!".format(folder_name))
         print("***************************************")


#calling delete empty directory function
#deleteEmptyDirectories()





        
