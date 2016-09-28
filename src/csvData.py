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
            studentID = "00000000"
            for j in range(len(dataList[i])):
                key = self.columnNames[j]
                dataPair[key] = dataList[i][j]
                if key == "Student ID":
                    studentID = dataPair[key]
            self.studentGrades[studentID] = dataPair

    def getStudentGrades(self):
        return self.studentGrades

    def getColumnNames(self):
        return self.columnNames
