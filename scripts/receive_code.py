epsg_codes = {
    "pseudo_mercator": 3857,
    "world_geodetic_system": 4326,
    "poland_cs1992": 2180
}


def receive_code(code):
    try:
        if (code == 1): code = epsg_codes["pseudo_mercator"]
        elif (code == 2): code = epsg_codes["world_geodetic_system"]
        elif (code == 3): code = epsg_codes["poland_cs1992"]
        else: raise ValueError
        return code
    except:
        return 0
