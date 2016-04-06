from mpl_toolkits.basemap import Basemap
import pandas as pd

def plot_accidentes_by_far_part(far121=True, far135=False):

    far_parts = []

    if far121:
        far_parts.append('121')
    if far135:
        far_parts.appeng('135')

    cond = aircraft['far_part'].isin(far_parts)
    ev_ids_for_desired_far = aircraft[cond]['ev_id'].drop_duplicates()

    aircraft_ = aircraft.loc[ev_ids_for_desired_far.index]

    mask = events['ev_id'].isin(ev_ids_for_desired_far.values)
    events_ = events[mask]

    lon_ = events['longitude_num'].values
    lat_ = events['latitude_num'].values

    m1 = Basemap('mill', lon_0=0, lat_0=0)
    m1.bluemarble()
    m1.drawcoastlines()
    m1.scatter(lon_, lat_, latlon=True, marker='.', color='r')

if __name__ == '__main__':
    pass