import os
import io

def determineFileContent(columnNames, dataPair):
    fileContent = []
    for index in range(len(columnNames)):
        key = columnNames[index]
        if key != "Notes":
            fileContent.append(key + ": " + dataPair[key] + "\n")
    return "".join(fileContent)

def writeToFile(fileFolderPath, filename, fileContent):
    filePath = os.path.join(fileFolderPath, filename)
    with io.FileIO(filePath, "w") as file:
        file.write(fileContent)
