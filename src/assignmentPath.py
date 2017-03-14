import os
import glob
import userAction
import time
import datetime

class AssignmentPath():
    def __init__(self):
        currentPath = os.path.dirname(os.path.realpath(__file__))
        self.setAssignmentPath(currentPath)

    def setAssignmentPath(self, currentPath):
        tryagain = False
        while not tryagain:
            studentFilesDir = userAction.promptInput("Enter assignment folder name: ")
            tempPath = os.path.normpath(os.path.join(currentPath+"/../resources", studentFilesDir))
            tryagain = True if userAction.promptInput("Is the folder path '" + tempPath + "' correct? (y/n) ") == "y" else False
        self.assignmentPath = tempPath

    def findAssignmentPathOfStudent(self, studentID):
        studentAssignmentPath = ""
        if "_" in studentID:
            studentID = studentID.split("_")[0]
        for root, dirs, files in os.walk(self.assignmentPath):
            for name in dirs:
                if studentID in name:
                    studentAssignmentPath = os.path.join(root, name)
        return studentAssignmentPath

    def convertFolderTimeStringToTimestamp(self, folderPath):
        timeStr = os.path.basename(folderPath)
        return time.mktime(datetime.datetime.strptime(timeStr, "%Y-%b-%d-%Hh%Mm%Ss%fms").timetuple())

    def findLatestTimestampedFolder(self, possibleFolderPaths):
        latestFolderPath = possibleFolderPaths[0]
        latestTimestamp = self.convertFolderTimeStringToTimestamp(latestFolderPath)

        for folderPath in possibleFolderPaths:
            timestamp = self.convertFolderTimeStringToTimestamp(folderPath)
            if latestTimestamp < timestamp:
                latestFolderPath = folderPath
        return latestFolderPath

    def findLatestAssignmentPathOfStudent(self, studentID):
        studentAssignmentPath = self.findAssignmentPathOfStudent(studentID)
        possibleFolderPaths = filter(lambda f: os.path.isdir(f), glob.glob(studentAssignmentPath + "/*/*"))
        return self.findLatestTimestampedFolder(possibleFolderPaths)
