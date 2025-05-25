import pandas, sys

InputCSV = sys.argv[1]
data = pandas.read_csv(InputCSV)
IndentNum = 1
LatCol = data["Latitude"]
LonCol = data["Longitude"]
IdnCol = []
EmptyCol = []
TypeCol = []
for line in LatCol:
    IdnCol.append(IndentNum)
    EmptyCol.append("")
    TypeCol.append("Pin")
    IndentNum += 1
with open("Output.csv", "w", encoding="utf-8") as f:
    Frame = pandas.DataFrame(
        {
            "Type": TypeCol,
            "Empty2": EmptyCol,
            "Ident": IdnCol,
            "Lat": LatCol,
            "Lon": LonCol,
        }
    )
    Frame.to_csv(f, index=False, header=False)
    f.close()
