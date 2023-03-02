import openpyxl

class Pos :
    column = 0
    row = 0
class Cells :
    start = Pos()
    end = Pos()
    rowrange = 0
    columnrange = 0

def get_merge_range(sheet):
    merged_ranges = []
    mergecell = Cells()
    for i in sheet.merged_cells.ranges:
        tmp = str(i).split(":")
        mergecell.start.column = sheet[tmp[0]].column
        mergecell.start.row = sheet[tmp[0]].row
        mergecell.end.column = sheet[tmp[1]].column
        mergecell.end.column.row = sheet[tmp[1]].row
        merged_ranges.append(mergecell)
    return merged_ranges


def Main():
    filepath = input("File Path: ")
    output = open("output.html", "w",encoding = "utf8")
    document = openpyxl.load_workbook(filepath,data_only=True)
    worksheet = document.active
    maxcols = 0
    cols = 0
    output.write('<!DOCTYPE html>\n')
    output.write("<table>\n")
    merged_ranges = get_merge_range(worksheet)
    for row in worksheet.iter_rows():
        output.write("<row>\n")
        cols = 0
        for cell in row:
            for mergecell in merged_ranges:
                if cell.column >= mergecell.start.column and cell.row >= mergecell.start.row and cell.row <= mergecell.end.row and cell.column <= mergecell.end.column:
                    if cell.column == mergecell.start.column and cell.row == mergecell.start.column:
                        output.write("<cells></cells>")
                else:
                    output.write("<cells>" + str(cell.value) + "</cells>\n")
            cols += 1
        if cols > maxcols:
            maxcols = cols
        output.write("</row>\n")
    output.write("<maxcols>" + str(maxcols) + "</maxcols>")
    output.write("</table>")
Main()