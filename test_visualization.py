from brane_visualization import groupbyplot

# set input variables
kind = "piechart"
csv_path = "data/test1000.csv"
output_path = "data/histimg.png"
column_name = "Census_PowerPlatformRoleName"
threshold_others = float(10)
title = "PlatformTypes"
drop_nan = True

# local testing
def test_visualizatino():
    assert (
        groupbyplot(
            kind, csv_path, output_path, threshold_others, title, drop_nan, column_name
        )
        == "data/histimg.png"
    )
