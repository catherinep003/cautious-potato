import csv
import userAction

class CsvRead():

    def __init__(self):
        filename = userAction.promptInput("Enter the CSV file name: ")
        filename += "" if ".csv" in filename else ".csv"
        self.csvFile = open("../resources/" + filename)
        self.csvReader = csv.reader(self.csvFile)

    def __enter__(self):
        return self.csvReader

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.csvFile.close()
