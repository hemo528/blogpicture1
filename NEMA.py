import pynmea2


def parse_gga(data):
    try:
        gga = pynmea2.parse(data)
        if isinstance(gga, pynmea2.types.talker.GGA):
            print(f"时间: {gga.timestamp}")
            print(f"纬度: {gga.latitude} {gga.lat_dir}")
            print(f"经度: {gga.longitude} {gga.lon_dir}")
            print(f"GPS质量: {gga.gps_qual}")
            print(f"卫星数量: {gga.num_sats}")
            print(f"水平精度因子: {gga.horizontal_dil}")
            print(f"海拔高度: {gga.altitude} 米")

            # Check if diff_age is available
            if hasattr(gga, 'diff_age') and gga.diff_age is not None:
                print(f"差分时间: {gga.diff_age} 秒")
            else:
                print("差分时间: 不可用")

            print(f"差分参考站ID: {gga.ref_station_id}")
    except pynmea2.ParseError as e:
        print(f'解析错误: {e}')


# Sample GGA data
gga_data = [
    "$GBGGA,035616.000,3204.162398,N,11854.159119,E,1,08,2.94,78.145,M,0.00,M,,*4E"
]

for line in gga_data:
    parse_gga(line)