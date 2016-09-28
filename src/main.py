from csvData import CsvData
from assignmentPath import AssignmentPath
import output

csvData = CsvData()
columnNames = csvData.getColumnNames()
studentGrades = csvData.getStudentGrades()

assignmentPath = AssignmentPath()
for studentID, dataPair in studentGrades.items():
    writePath = assignmentPath.findLatestAssignmentPathOfStudent(studentID)
    content = output.determineFileContent(columnNames, dataPair)
    output.writeToFile(writePath, "mark.txt", content)
