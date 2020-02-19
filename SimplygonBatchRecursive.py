from subprocess import Popen
import glob
import sys
import os

if __name__ == "__main__":
    args = sys.argv

    inputRootPath = args[1]
    outputPath = args[2]
    rulePath = args[3]
    pathOfSimplygonBatch = "C:\\PROGRA~1\\Simplygon\\8\\Tools\\SimplygonBatch\\SimplygonBatch.exe"

    modelPaths = []
    #modelPaths = glob.glob(inputRootPath + "/**/*.fbx", recursive = True)
    modelPaths.extend(glob.glob(inputRootPath + "/**/*.obj", recursive = True))
    for inputPath in modelPaths:

        command = pathOfSimplygonBatch + " --Input \"" + inputPath + "\" --Output \"" + outputPath + "\" --Spl \"" + rulePath + "\" --OutputFileFormat "+os.path.splitext(inputPath)[1]+" --Verbose" + '\"'

        print(command)
        process = Popen(command, shell = True)
        process.wait()