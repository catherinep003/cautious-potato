from readCsv import CsvRead

class CsvData():

    def __init__(self):
        with CsvRead() as r:
            dataList = list(r)
        self.columnNames = dataList[0]
        self.setStudentGrades(dataList)

    def setStudentGrades(self, dataList):
        self.studentGrades = {}
        for i in range(1, len(dataList)):
            dataPair = {}
            studentID = ""
            for j in range(len(dataList[i])):
                key = self.columnNames[j]
                dataPair[key] = dataList[i][j]
                if "Student ID" in key:
                    if studentID == "":
                        studentID = dataPair[key]
                    else:
                        if dataPair[key] != "":
                            studentID += "_" + dataPair[key]
            if studentID != "":
                self.studentGrades[studentID] = dataPair

    def getStudentGrades(self):
        return self.studentGrades

    def getColumnNames(self):
        return self.columnNames
