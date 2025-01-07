import os
import shutil
import sys

GAME_DIR_PATTERN = "game"

def findAllGamePaths(source):
    gamePaths = []

    for roots, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                gamePaths.append(path)
        break
    return gamePaths

def getPathName(paths, toStrip):
    newNames = []
    for path in paths:
        _, dirName = os.path.split(path) #just scraps out the final part of the directory name
        newDirectoryName = dirName.replace(toStrip, "")
        newNames.append(newDirectoryName)

    return newNames

def copyAndOverwrite(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    shutil.copytree(source, destination)

def createDirectory(path):
    if not os.path.exists(path):
        os.mkdir(path)

def main(source, target):
    cwd = os.getcwd()
    sourcePath = os.path.join(cwd, source) #here string concatenation should not be used as an alternative as different OS have different type of naming style
    targetPath = os.path.join(cwd, target)

    gamePath = findAllGamePaths(sourcePath)

    createDirectory(targetPath)
    newGameDirectory = getPathName(gamePath, "game")

    for src, dest in zip(gamePath, newGameDirectory):
        destinationPath = os.path.join(targetPath, dest)
        copyAndOverwrite(src, destinationPath)

if __name__ == "__main__": #runs the file directly without any importing or exporting
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and a target directory respectively")

    source, target = args[1:] #1: removes the file name which is get_game_data in this case
    main(source, target)