# WSCBS2021 Visualization

This is an example [Brane](https://docs.brane-framework.org/) package to explore data by visualization, using Matplotlib (Python package).
It can group columns of CSVs and show a bar plot / pie chart of the number of occurences.
Futhermore a threshold is available to place values below a specific count,
which will be merged in a group called "Others".
NaN values can be dropped by setting the corresponding boolean.

Import it as follows:

```shell
$ brane import daanvinken/wscbs2021-visualization
```

<img src="https://i.ibb.co/6B7jGgM/testimg.png"
     alt="example plot" />

The following environment variables can be set:

```shell
$ export INPUT='piechart' #or barplot
$ CSV_PATH=/data/test1000.csv
$ OUTPUT_PATH=/data/histimg.png
$ COLUMN_NAME=Census_PowerPlatformRoleName
$ THRESHOLD_OTHERS=10
$ PLOT_TITLE=Platform types
$ DROP_NAN=true
```

You also need to push the package to be able to import it in your remote session or jupyterlab notebook:
```shell
brane push visualization 1.0.0
```

For an overview of the parameters of the brane package, you can `test` the package
```shell
$ brane --debug test visualization --data data
# use parameters:
# - 
# - piechart
# - /data/data/test1000.csv
# - /data/piechart.png
# - 10.0
# - PlatformTypes
# - true
# - Census_PowerPlatformRoleName
```

The package can be build and published with `make build`.
After which the example notebook can be executed within the Jupyter IDE.
