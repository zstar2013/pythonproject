# todo 常量文件

gConst = {"businfo":
              {"teams": ["1队", "2队", "3队", "4队", "5队", ""],
               "routes": [],  # todo  是否设置默认线路数组
               "powertpye": ["柴油", "混合", "纯电", ""],
               "header": ['车辆id', '线路', '车长', '核定载客', '登记时间', '车型', '是否报废', '所属车队', '备注', ''],
               "headerkeymap": ['car_id', 'route', 'length', 'busload', 'uptime', 'cartype', 'scrap', 'team',
                                'descript']},
          "oil": {
              "month": ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
              "attr": ["paytime", "cardnum", "printnum", "carid", "oiltype", "oilstation", "charge"]
          },
          "imagedialog": {
              "defaultHeight": "500",
              "defaultWidth": "820"
          },
          "defaultSettings": {
              "oil": {"outputpath": "F:\\报表\\油耗相关","inputpath":"G:\\油耗\\油料中心"},
              "database": {"db_port": "3306", "db_user": "root", "db_host": "127.0.0.1", "db_psw": ""}
          }, "settings": {"setfilepath": "D:\\设置\\settings.ini"}}
