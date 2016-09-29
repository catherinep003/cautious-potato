from csvData import CsvData
from assignmentPath import AssignmentPath
import output

csvData = CsvData()
columnNames = csvData.getColumnNames()
studentGrades = csvData.getStudentGrades()

assignmentPath = AssignmentPath()
print("Mark file generated for the following students:")
count = 0
for studentID, dataPair in studentGrades.items():
    writePath = assignmentPath.findLatestAssignmentPathOfStudent(studentID)
    content = output.determineFileContent(columnNames, dataPair)
    output.writeToFile(writePath, "mark.txt", content)
    print(studentID)
    count += 1
print("Total of " + str(count) + " 'mark.txt' generated")
