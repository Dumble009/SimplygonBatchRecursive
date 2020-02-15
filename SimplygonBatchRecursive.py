from subprocess import Popen
import glob
import sys

if __name__ == "__main__":
    args = sys.argv

    inputRootPath = args[1]
    outputPath = args[2]
    rulePath = args[3]
    pathOfSimplygonBatch = "C:\\PROGRA~1\\Simplygon\\8\\Tools\\SimplygonBatch\\SimplygonBatch.exe"

    fbxPaths = glob.glob(inputRootPath + "/**/*.fbx", recursive = True)
    for inputPath in fbxPaths:

        command = pathOfSimplygonBatch + " --Input " + inputPath + " --Output " + outputPath + " --Spl " + rulePath + " --Verbose" + '\"'

        print(command)
        process = Popen(command, shell = True)
        process.wait()