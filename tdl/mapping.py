swiss_topo = xyz.SwissFederalGeoportal

map_tiles = swiss_topo['NationalMapColor']

folium_map_kwargs = dict(
    tiles=map_tiles['url'],
    attr=map_tiles['html_attribution'],
    zoom_start=8,
    min_zoom=7,
    location=[0, 0],
    max_bounds=True,
    max_lat=0,
    max_lon=0,
    min_lat=0,
    min_lon=0,
    width=700,
    height=500)