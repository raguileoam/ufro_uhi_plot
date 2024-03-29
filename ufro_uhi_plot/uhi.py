# AUTOGENERATED! DO NOT EDIT! File to edit: 01_uhi.ipynb (unless otherwise specified).

__all__ = ['Uhi', 'OtherDf', 'Util']

# Cell
from .map import Map
from .map import UHIOptions
from .map import MapOptions
import pandas as pd
import numpy as np
import os
import gc
from datetime import datetime, timedelta

# Cell
class Uhi:
    """Represents an image(s) of urban heat island(s)

    Attributes:
      path_file: string
      station_label: string
      datetime_label: string
      temperature_label: string
      latitude_label: string
      longitude_label: string
    """
    def __init__(self,path_file,station_label,datetime_label,temperature_label,latitude_label,longitude_label):
      self.path_file = path_file
      self.station_label = station_label
      self.datetime_label = datetime_label
      self.temperature_label = temperature_label
      self.latitude_label = latitude_label
      self.longitude_label = longitude_label
      self.df=pd.read_csv(self.path_file,decimal=",",parse_dates=True,index_col=datetime_label,usecols=[station_label,datetime_label,temperature_label,latitude_label,longitude_label])
      self.dfToFloat()

    def dfToFloat(self):
      self.df=self.df.dropna(subset=[self.temperature_label])
      self.df[self.longitude_label] = self.df[self.longitude_label].astype(np.float)
      self.df[self.latitude_label] = self.df[self.latitude_label].astype(np.float)
      self.df[self.temperature_label] = self.df[self.temperature_label].astype(np.float)

    def plotImagesPerDay(self,dfDay,outputFolder,extent,hasBorders=None,hasLimits=False,transects=[],
                         Z_UNIT="°C",otherDf_id=None,otherDf_name=None,mapbox_username="",mapbox_token="",
                         prefixFile="",hasImage=True, hasScaleBar=True, hasCompassRose=True,hasLegend=True, hasColorbar=True,
                         transparency=.7, showPoints=False,contour="contourLine",drawMinMaxT=False):
      hours=dfDay.groupby(dfDay.index)
      dfListDay=[]
      for hour in hours.groups.keys():
        df_hour=hours.get_group(str(hour))
        if len(df_hour)>4:
          print(hour)
          dfListDay.append(df_hour)
          otherDf = None
          if otherDf_name is not None and otherDf_id is not None:
            otherDf_df = df_hour[df_hour[self.station_label]==otherDf_id]
            otherDf = OtherDf(otherDf_df,otherDf_id,otherDf_name)
            df_hour = df_hour[df_hour[self.station_label]!=otherDf_id]
          varMap = Map(df_hour,transects=transects,otherDf=otherDf,mapbox_username=mapbox_username,mapbox_token=mapbox_token)
          vMin=None
          vMax=None
          if hasLimits:
            vMin=dfDay[self.temperature_label].min()
            vMax=dfDay[self.temperature_label].max()

          uhiOptions = UHIOptions(hasBorders=hasBorders, vMin=vMin, vMax=vMax,
                                  transparency=transparency, showPoints=showPoints,contour=contour,drawMinMaxT=drawMinMaxT,
                                  LON_LABEL=self.longitude_label, LAT_LABEL=self.latitude_label,Z_LABEL=self.temperature_label, Z_UNIT=Z_UNIT)

          mapOptions = MapOptions(show=False, file=outputFolder+"/{} {}".format(prefixFile,hour), hasImage=hasImage,
                                  hasScaleBar=hasScaleBar, hasCompassRose=hasCompassRose,hasLegend=hasLegend, hasColorbar=hasColorbar)

          varMap.plot(extent,uhiOptions=uhiOptions,mapOptions=mapOptions)
        print("Limpiando...")
        df_hour=None
        varMap=None
        gc.collect()

      return dfListDay

    def plotImagesPerDaysArray(self,outputFolder,daysArray,extent,hasBorders=None,hasLimits=False,
                               Z_UNIT="°C",otherDf_id=None,otherDf_name=None,mapbox_username="",mapbox_token="",
                               prefixFile="",hasImage=True,hasScaleBar=True, hasCompassRose=True,hasLegend=True, hasColorbar=True,
                               transparency=.7, showPoints=False,contour="contourLine",drawMinMaxT=False):
      """

      Input:
      outputFolder: string of folder where the images of urban heat islands are saved.
      daysArray: array of strings of days to plot the urban heat islands.
      extent: array of 4 coordinates of the extent of the map.
      hasBorders: geojson to border the urban heat island in a map. (default:None)
      hasLimits: if has temperature's day range or temperature's hour range (default:False)
      Z_UNIT: unit of measure to be displayed in colobar. (default: '°C')
      otherDf_id: id of the temperature station that will not be included in the UHI's triangulation but will be displayed. (default: None)
      otherDf_name: name of the temperature station that will not be included in the UHI's triangulation but will be displayed. (default: None)
      mapbox_username: mapbox's username to plot background map. (default: '')
      mapbox_token: mapbox's token to plot background map. (default: '')
      prefixFile: string of the output prefix filename. (default:'')
      hasImage: boolean that decides if the image needs a Mapbox Map or not.
      hasScaleBar: boolean that decides if the image needs a Scaler Bar or not.
      hasCompassRose: boolean that decides if the image needs a Compass Rose or not.
      hasLegend: boolean that decides if the image neede a Legend or not.
      hasColorbar: boolean that decides if the image needs a color bar or not.
      transparency: trasparency of the UHI's triangulation.
      showPoints: boolean that decides if the image needs show station points.
      contour: show contourLine or only triangulation (default:'contourLine')
      drawMinMaxT: show station points with minimun and maximum temperature.
      Output: None
      """
      if not os.path.exists(outputFolder):
        try:
            os.makedirs(outputFolder)
        except OSError:
            print ("Creation of the directory %s failed" % outputFolder)
        else:
            print ("Successfully created the directory %s" % outputFolder)

      for day in daysArray:
        print("Plotting UHI Map of ",day)
        df1=self.df.loc[np.in1d(self.df.index.date, pd.to_datetime([day]).date)]
        print("...")
        self.plotImagesPerDay(df1,outputFolder,extent,hasBorders=hasBorders,hasLimits=hasLimits,transects=[],
                              Z_UNIT=Z_UNIT,otherDf_id=otherDf_id,otherDf_name=otherDf_name,mapbox_username=mapbox_username,mapbox_token=mapbox_token,
                              prefixFile=prefixFile,hasImage=hasImage,hasScaleBar=hasScaleBar, hasCompassRose=hasCompassRose,hasLegend=hasLegend, hasColorbar=hasColorbar,
                              transparency=transparency, showPoints=showPoints,contour=contour,drawMinMaxT=drawMinMaxT)
        print("Plot completed",day)
class OtherDf:
  def __init__(self,df,id,name):
    self.df = df
    self.id = id
    self.name = name

class Util:
  def getDaysFromRange(start,end):
    dates = [start, end]
    start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]
    return [(start + timedelta(x)).strftime(r"%Y-%m-%d") for x in range((end - start).days)]