# ufro_uhi_plot
> Python proyect to plotting urban heat island.


## Install

`pip install ufro_uhi_plot`

## How to use

Import Uhi from the package

```
from ufro_uhi_plot.uhi import Uhi
```

Instantiate the Uhi Class

```
file_path = "examples/data_example.csv"
station_label = "Vivienda.ID"
datetime_label = "Fecha"
temperature_label = "Pm25"
latitude_label = "Latitud"
longitude_label = "Longitud"

uhi = Uhi(file_path,station_label,datetime_label,temperature_label,latitude_label,longitude_label)
```

Plot the images according your preferences

```

output_folder="examples/generated maps"

days_array = ["2019-05-26"]
extent = [-72.69,-72.53,-38.78,-38.68]
prefix_file = "contamination map"
unit = "ug/m³"
mapbox_username = #<insert your mapbox's username>
mapbox_token= #<insert your mapbox's token>

uhi.plotImagesPerDaysArray(output_folder,days_array,extent,prefixFile=prefix_file,hasLimits=True,Z_UNIT=unit,mapbox_username=mapbox_username,mapbox_token=mapbox_token)
```

    Successfully created the directory examples/generated maps
    Plotting UHI Map of  2019-05-26
    ...
    2019-05-26 00:59:35
    2019-05-26 01:59:35
    2019-05-26 02:59:35
    2019-05-26 03:59:35
    2019-05-26 04:59:35
    2019-05-26 05:59:35
    2019-05-26 06:59:35
    2019-05-26 07:59:35
    2019-05-26 08:59:35
    2019-05-26 09:59:35
    2019-05-26 10:59:35
    2019-05-26 11:59:35
    2019-05-26 12:59:35
    2019-05-26 13:59:35
    2019-05-26 14:59:36
    2019-05-26 15:59:35
    2019-05-26 16:59:35
    2019-05-26 17:59:35
    2019-05-26 18:59:35
    2019-05-26 19:59:35
    2019-05-26 20:59:35
    2019-05-26 21:59:36
    2019-05-26 22:59:35
    2019-05-26 23:59:35
    Plot completed 2019-05-26


### Google Colab use

If you have a problem with Google Colab you can install binary shapely in a jupyter notebox that fix this.

```
!pip uninstall shapely --yes
!pip install shapely --no-binary shapely
```
