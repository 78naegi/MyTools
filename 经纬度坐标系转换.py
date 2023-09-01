import requests
from pyproj import Proj, transform

def get_gcj02_coordinates():
    url = ''
    response = requests.get(url)
    data = response.json()
    return data['longitude'], data['latitude']

def is_in_china(longitude, latitude):
    p = Proj(init='epsg:4326')  # 使用WGS-84坐标系
    return 73.66 <= longitude <= 135.05 and 3.86 <= latitude <= 53.55

def gcj02_to_wgs84(longitude, latitude):
    p1 = Proj(init='epsg:4326')  # 使用WGS-84坐标系
    p2 = Proj(init='epsg:3857')  # 使用火星坐标系
    return transform(p2, p1, longitude, latitude)

lo,la=gcj02_to_wgs84(139.702070,35.685494)
print(lo,'\n',la)

from math import pi, atan, exp, sin, cos, sqrt, atan2

def gcj_to_wgs(gcj_lng, gcj_lat):
    a = 6378245.0
    ee = 0.00669342162296594323
    d_lng = transform_lng(gcj_lng - 105.0, gcj_lat - 35.0)
    d_lat = transform_lat(gcj_lng - 105.0, gcj_lat - 35.0)
    rad_lat = gcj_lat / 180.0 * pi
    magic = sin(rad_lat)
    magic = 1 - ee * magic * magic
    sqrt_magic = sqrt(magic)
    d_lng = (d_lng * 180.0) / (a / sqrt_magic * cos(rad_lat) * pi)
    d_lat = (d_lat * 180.0) / ((a * (1 - ee)) / (magic * sqrt_magic) * pi)
    wgs_lng = gcj_lng - d_lng
    wgs_lat = gcj_lat - d_lat
    return wgs_lng, wgs_lat

def transform_lng(x, y):
    return 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * sqrt(abs(x))

def transform_lat(x, y):
    return  -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * sqrt(abs(x))

def wgs_to_bd(wgs_lng, wgs_lat):
    x_pi = 3.14159265358979324 * 3000.0 / 180.0
    z = sqrt(wgs_lng * wgs_lng + wgs_lat * wgs_lat) + 0.00002 * sin(wgs_lat * x_pi)
    theta = atan2(wgs_lat, wgs_lng) + 0.000003 * cos(wgs_lng * x_pi)
    bd_lng = z * cos(theta) + 0.0065
    bd_lat = z * sin(theta) + 0.006
    return bd_lng, bd_lat



# 输入火星坐标系下的经纬度坐标
gcj_lng, gcj_lat = 139.702070, 35.685494

print("GCJ-02经度：", gcj_lng)
print("GCJ-02纬度：", gcj_lat)

# 将火星坐标系下的坐标转换为WGS-84坐标系下的坐标
wgs_lng, wgs_lat = gcj_to_wgs(gcj_lng, gcj_lat)

print("WGS-84经度：", wgs_lng)
print("WGS-84纬度：", wgs_lat)

# 将WGS-84坐标系下的坐标转换为百度坐标系（BD-09）下的坐标
bd_lng, bd_lat = wgs_to_bd(wgs_lng, wgs_lat)

print("百度坐标系经度：", bd_lng)
print("百度坐标系纬度：", bd_lat)


