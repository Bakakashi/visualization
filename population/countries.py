from pygal_maps_world.i18n import COUNTRIES

# 统计country_code
    
with open('country_code.txt', 'w') as f:
    for country_code in sorted(COUNTRIES.keys()):
        # 打印国家与其对应的国家码
        print(country_code, COUNTRIES[country_code])
        # 写入文件
        result = country_code + '\t' + COUNTRIES[country_code] + '\n'
        f.write(result)
