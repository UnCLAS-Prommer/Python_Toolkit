import openpyxl
import copy

class Pos :
    def __init__(self):
        self.column = 0
        self.row = 0
class Cells :
    rowrange = 0
    columnrange = 0
    def __init__(self):
        self.start = Pos()
        self.end = Pos()

def get_merge_range(sheet):
    merged_ranges = []
    for i in sheet.merged_cells.ranges:
        mergecell = Cells()
        mergecell.start.column = i.min_col
        mergecell.start.row = i.min_row
        mergecell.end.column = i.max_col
        mergecell.end.row = i.max_row
        mergecell.rowrange = i.size['rows']
        mergecell.columnrange = i.size['columns']
        merged_ranges.append(mergecell)
        del mergecell.start
        del mergecell.end
    print(merged_ranges)
    return merged_ranges


def Main():
    filepath = input("File Path: ")
    output = open("output.html", "w",encoding = "utf8")
    document = openpyxl.load_workbook(filepath,data_only=True)
    worksheet = document.active
    maxcols = 0
    cols = 0
    output.write('<!DOCTYPE html>\n<html>\n<head></head>\n<body>\n')
    output.write('<table border = "1">\n')
    merged_ranges = get_merge_range(worksheet)
    for row in worksheet.iter_rows():
        output.write("<tr>\n")
        cols = 0
        for cell in row:
            print("Cell Row:", cell.row, "Cell Col:", cell.column)
            written = False
            for mergecell in merged_ranges:
                print("MergeCell Row:", mergecell.start.row, "MergeCell Col:", mergecell.start.column)
                if cell.column >= mergecell.start.column and cell.row >= mergecell.start.row and cell.row <= mergecell.end.row and cell.column <= mergecell.end.column:
                    if cell.column == mergecell.start.column and cell.row == mergecell.start.row:
                        output.write('<td rowspan = "' + str(mergecell.rowrange) + '" colspan = "' + str(mergecell.columnrange) + '">' + str(cell.value) + '</td>\n')
                        written = True
            if not written:
                output.write("<td>" + str(cell.value) + "</td>\n")
            cols += 1
        if cols > maxcols:
            maxcols = cols
        output.write("</tr>\n")
    output.write("<maxcols>" + str(maxcols) + "</maxcols>\n")
    output.write("</table>\n</body>\n</html>")

Main()