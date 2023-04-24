import sys
import os
import shutil


print('Welcome to the python-file-manager\n')

# Stores every drive connected on PC in a list.
# Finds all the available drives on the system
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]


# Lists each folder and file present in the current working directory
def listDirectories():
    # Get a list of all directories in the current working directory
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x)


while True:
    print("1.Open files/folders \n2.Rename \n3.Move and Paste \n4.Copy and Paste \n5.Delete\n")
    result = input("Choose one of the following: ")

    if result == '1':
        # Home Screen
        print('\nQuick Acess:\n1. Documents\n2. Videos\n3. Pictures\n4. Downloads\n')

        print('Drives: ')
        # Print the list of available drives
        for x in range(len(drives)):
            print(str(5 + x) + '. ' + drives[x])

        while True:
            inp = input("\nEnter your Choice: ")

            if inp == '1':
                path = 'C:\\Users\\$USERNAME\\Documents'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '2':
                path = 'C:\\Users\\$USERNAME\\Videos'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '3':
                path = 'C:\\Users\\$USERNAME\\Pictures'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '4':
                path = 'C:\\Users\\$USERNAME\\Downloads'
                os.chdir(os.path.expandvars(path))
                break

            elif inp in drives:
                os.chdir(inp + '\\')
                break

            else:
                print('Error\nEnter a correct input / drive name.\n')

        while True:
            listDirectories()

            print('\n\nType "exitManager" to exit from file manager.')
            print('Type "backManager" to go up one directory.')
            res = input('\nChoose a file/folder: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    os.system('"' + res + '"')
                else:
                    os.chdir(res)

            elif res == 'exitManager':  # Exit command to exit from loop
                sys.exit(0)

            elif res == 'backManager':  # Back command to go up one directory
                os.chdir('..')

            else:
                print('No file/folder exist of this name.')

    if result == '2':
        print("You chose to rename")
        print('Drives: ')
        # Print the list of available drives
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])

        while True:
            inp = input("\nEnter your Choice: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct drive name.\n')

        while True:
            listDirectories()

            print('\n\nType "exitManager" to exit from file manager.')
            print('Type "backManager" to go up one directory.')
            print('Type "renameManager" to rename this directory')

            res = input('\nChoose a file to rename: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if result == '5':
                    while True:
                        # Options to delete files/folders to permanently or otherwise
                        print('\n1. Permanently \n2. Recycle Bin')
                        query = input('Would you like to permanently delete or send to Recycle Bin?: ')

                        if query == '1':
                            print('You chose to permanently delete files/folders.\n')
                            print('Drives: ')
                            for x in range(len(drives)):
                                print(str(1 + x) + '. ' + drives[x])

                            while True:
                                inp = input("\nEnter your Choice: ")

                                if inp in drives:
                                    os.chdir(inp + '\\')
                                    break
                                else:
                                    print('Error\nEnter a correct drive name.\n')

                            while True:
                                listDirectories()
                                print('\n\nType "exitManager" to exit from file manager.')
                                print('Type "backManager" to go up one directory.')
                                print('Type "deleteManager" to permanently delete this directory')
                                res = input('\nChoose a file to delete: ')
                                print('\n')
                                if res in os.listdir(os.getcwd()):
                                    if os.path.isfile(res):
                                        # Warning to prevent unnecessary deletion
                                        print('Are you sure you want to permanently delete this file? (YES/NO)')
                                        ans = input('Yes or No: ')
                                        if ans.lower() == 'yes' or 'y':
                                            os.unlink(res)
                                        else:
                                            os.chdir(res)

                                    elif res == 'exitManager':  # Exit command to exit from loop
                                        sys.exit(0)

                                    elif res == 'backManager':  # Back command to go up one directory
                                        os.chdir('..')

                                    elif res == 'deleteManager':  # Delete command to delete one directory

                                        # Warning to prevent unnecessary deletion
                                        print('Are you sure you want to permanently delete this folder? (YES/NO)')
                                        ans = input('Yes or No: ')

                                        if ans.lower() == 'yes' or 'y':
                                            path = os.getcwd()
                                            os.chdir('..')
                                            shutil.rmtree(path)

                                else:
                                    print('No file/folder exist of this name.')

                        elif query == '2':
                            print('You chose to temporarily delete files/folders.')
                            print('Drives: ')
                            for x in range(len(drives)):
                                print(str(1 + x) + '. ' + drives[x])

                            while True:
                                inp = input("\nEnter your Choice: ")

                                if inp in drives:
                                    os.chdir(inp + '\\')
                                    break
                                else:
                                    print('Error\nEnter a correct drive name.\n')

                            while True:
                                listDirectories()

                                print('\n\nType "exitManager" to exit from file manager.')
                                print('Type "backManager" to go up one directory.')
                                print('Type "deleteManager" to send this directory to recycle bin')

                                res = input('\nChoose a file to delete: ')
                                print('\n')

                                if res in os.listdir(os.getcwd()):
                                    if os.path.isfile(res):

                                        # Warning to prevent unnecessary deletion
                                        print('Are you sure you want to send this folder to recycle bin? (YES/NO)')
                                        ans = input('Yes or No: ')
                                        if ans.lower() == 'yes' or 'y':
                                            send2trash.send2trash(res)
                                        else:
                                            os.chdir(res)

                                    elif res == 'exitManager':  # Exit command to exit from loop
                                        sys.exit(0)


                                    elif res == 'backManager':  # Back command to go up one directory

                                        os.chdir('..')

                                    else:

                                        print('No file/folder exists with this name.')

                                    if result == '5':

                                        while True:

                                            # Options to delete files/folders to permanently or otherwise

                                            print('\n1. Permanently \n2. Recycle Bin')

                                            query = input(
                                                'Would you like to permanently delete or send to Recycle Bin?: ')

                                            if query == '1':

                                                print('You chose to permanently delete files/folders.\n')

                                                print('Drives: ')

                                                for x in range(len(drives)):
                                                    print(str(1 + x) + '. ' + drives[x])

                                                while True:

                                                    inp = input("\nEnter your Choice: ")

                                                    if inp in drives:

                                                        os.chdir(inp + '\\')

                                                        break

                                                    else:

                                                        print('Error\nEnter a correct drive name.\n')

                                                while True:

                                                    listDirectories()

                                                    print('\n\nType "exitManager" to exit from file manager.')

                                                    print('Type "backManager" to go up one directory.')

                                                    print('Type "deleteManager" to permanently delete this directory')

                                                    res = input('\nChoose a file to delete: ')

                                                    print('\n')

                                                    if res in os.listdir(os.getcwd()):

                                                        if os.path.isfile(res):

                                                            # Warning to prevent unnecessary deletion

                                                            print(
                                                                'Are you sure you want to permanently delete this file? (YES/NO)')

                                                            ans = input('Yes or No: ')

                                                            if ans.lower() == 'yes' or 'y':

                                                                os.unlink(res)

                                                            else:

                                                                os.chdir(res)

                                                        elif res == 'exitManager':  # Exit command to exit from loop

                                                            sys.exit(0)

                                                        elif res == 'backManager':  # Back command to go up one directory

                                                            os.chdir('..')

                                                        elif res == 'deleteManager':  # Delete command to delete one directory

                                                            # Warning to prevent unnecessary deletion

                                                            print(
                                                                'Are you sure you want to permanently delete this folder? (YES/NO)')

                                                            ans = input('Yes or No: ')

                                                            if ans.lower() == 'yes' or 'y':

                                                                path = os.getcwd()

                                                                os.chdir('..')

                                                                shutil.rmtree(path)

                                                            else:

                                                                continue

                                                        else:

                                                            print('No file/folder exist with this name.')
                                            elif query == '2':
                                                print('You chose to temporarily delete files/folders.')
                                                print('Drives: ')
                                                for x in range(len(drives)):
                                                    print(str(1 + x) + '. ' + drives[x])

                                                while True:

                                                    inp = input("\nEnter your Choice: ")
                                                    if inp in drives:
                                                        os.chdir(inp + '\\')
                                                        break
                                                    else:
                                                        print('Error\nEnter a correct drive name.\n')

                                                while True:
                                                    listDirectories()
                                                    print('\n\nType "exitManager" to exit from file manager.')
                                                    print('Type "backManager" to go up one directory.')
                                                    print('Type "deleteManager" to send this directory to recycle bin')

                                                    res = input('\nChoose a file to delete: ')
                                                    print('\n')
                                                    if res in os.listdir(os.getcwd()):
                                                        if os.path.isfile(res):
                                                            # Warning to prevent unnecessary deletion
                                                            print(
                                                                'Are you sure you want to send this folder to recycle bin? (YES/NO)')
                                                            ans = input('Yes or No: ')

                                                            if os.path.isfile(res):
                                                                ans = input(
                                                                    f"\nAre you sure you want to send '{res}' to trash? (Y/N)").lower()
                                                                if ans == 'yes' or ans == 'y':
                                                                    send2trash.send2(res)
                                                                elif res == 'backManager':  # Back command to go up one directory
                                                                    os.chdir('..')
                                                            else:
                                                                print('No file/folder exists with this name.')

                                                            if result == '5':
                                                                while True:
                                                                    # Options to delete files/folders to permanently or otherwise
                                                                    print('\n1. Permanently \n2. Recycle Bin')
                                                                    query = input(
                                                                        'Would you like to permanently delete or send to Recycle Bin?: ')

    if query == '1':
        print('You chose to permanently delete files/folders.\n')
        print('Drives: ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])

        while True:
            inp = input("\nEnter your Choice: ")
            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct drive name.\n')

        while True:
            listDirectories()

            print('\n\nType "exitManager" to exit from file manager.')
            print('Type "backManager" to go up one directory.')
            print('Type "deleteManager" to permanently delete this directory')

            res = input('\nChoose a file to delete: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    # Warning to prevent unnecessary deletion
                    print('Are you sure you want to permanently delete this file? (YES/NO)')
                    ans = input('Yes or No: ')
                    if ans.lower() == 'yes' or 'y':
                        os.unlink(res)
                    else:
                        os.chdir(res)
                elif res == 'exitManager':  # Exit command to exit from loop
                    sys.exit(0)
                elif res == 'backManager':  # Back command to go up one directory
                    os.chdir('..')
                elif res == 'deleteManager':  # Delete command to delete one directory
                    # Warning to prevent unnecessary deletion
                    print('Are you sure you want to permanently delete this folder? (YES/NO)')
                    ans = input('Yes or No: ')
                    if ans.lower() == 'yes' or 'y':
                        path = os.getcwd()
                        os.chdir('..')
                        shutil.rmtree(path)
                    else:
                        continue
                else:
                    print('No file/folder exist with this name.')
    if query == '2':
        print('You chose to temporarily delete files/folders.')
        print('Drives: ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])
        while True:
            inp = input("\nEnter your Choice: ")
            if inp in drives:
                os.chdir(inp + '\\')
                break

            else:
                print('Error\nEnter a correct drive name.\n')
        while True:
            listDirectories()
            print('\n\nType "exitManager" to exit from file manager.')
            print('Type "backManager" to go up one directory.')
            print('Type "deleteManager" to send this directory to recycle bin')
            res = input('\nChoose a file to delete: ')
            print('\n')
            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    # Warning to prevent unnecessary deletion
                    print('Are you sure you want to send this folder to recycle bin? (YES/NO)')
                    ans = input('Yes or No: ')
                    if ans.lower() == 'yes' or 'y':
                        send2trash.send2trash(res)
                    else:
                        os.chdir(res)
                elif res == 'exitManager':  # Exit command to exit from loop
                    sys.exit(0)
                elif res == 'backManager':  # Back command to go up one directory
                    os.chdir('..')
                elif res == 'deleteManager':  # Delete command to delete one directory
                    # Warning to prevent unnecessary deletion
                    print('Are you sure you want to send this folder to recycle bin? (YES/NO)')
                    ans = input('Yes or No: ')
                    if ans.lower() == 'yes' or 'y':
                        path = os.getcwd()
                        os.chdir('..')
                        send2trash.send2trash(path)
                    else:
                        print('No file/folder exist of this name.')
            else:
                print('No file/folder exist of this name.')
        else:
            print('You chose wrong number')
