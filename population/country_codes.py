from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """返回给定country的Pygal二位国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 若未找到对应的country, 则返回None.
    return None
