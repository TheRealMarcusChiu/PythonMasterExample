import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
# see: https://stackoverflow.com/questions/42299352/installing-basemap-on-mac-python/53171723#53171723
# > brew install geos
# > pip3 install https://github.com/matplotlib/basemap/archive/master.zip

m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
m.bluemarble(scale=0.5)
