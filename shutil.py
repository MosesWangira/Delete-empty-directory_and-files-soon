import shutil
import os
from os import path

#show list of all directories in labelled volume
print("************************************************************************")
directories = os.listdir(r"I:")
print("\n".join(directories))
print("************************************************************************")


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
deleteEmptyDirectories()





        
