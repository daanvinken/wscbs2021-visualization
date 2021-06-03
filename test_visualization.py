
from brane_visualization import groupbyplot

# set input variables
kind = "piechart"
csv_path = "data/test1000.csv"
output_path = "data/histimg.png"
column_name = "Census_PowerPlatformRoleName"
threshold_others = float(10)
title = "PlatformTypes"
drop_nan = True

#local testing
def test_visualizatino():
  assert visualization(kind, csv_path, output_path, column_name, threshold_others, title, drop_nan) == "data/histimg.png"
