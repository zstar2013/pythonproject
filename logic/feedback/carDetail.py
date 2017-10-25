from tools import strtool as st
from logic.feedback.feedback import getRoute,getCar_id
#获取明细数据
def load_detail_data(table, item):
    nrows = table.nrows
    list = []
    indexR = item[0]
    carNoC = item[1]
    route = getRoute(table.name)
    for i in range(indexR, nrows):
        if table.cell(i, carNoC).value is "":
            continue
        if st.contains(str(table.cell(i, carNoC).value), "合计"):
            continue
        item = []
        car_id = getCar_id(table.cell(i, carNoC).value,table.name)
        item.append(car_id)  # 车辆id
        item.append(route)  # 车辆线路
        item.append(table.cell(i, carNoC + 4).value)  # 停驶天数
        item.append(table.cell(i, carNoC + 5).value)  # 工作天数
        item.append(table.cell(i, carNoC + 7).value)  # 营业公里
        item.append(table.cell(i, carNoC + 8).value)  # 包车公里
        item.append(table.cell(i, carNoC + 9).value)  # 公用公里
        item.append(table.cell(i, carNoC + 10).value)  # 调车公里
        item.append(table.cell(i, carNoC + 14).value)  # 故障次数
        item.append(table.cell(i, carNoC + 15).value)  # 故障分钟
        list.append(item)
    return list
#保存数据到xls表格
def save_date_to_xls(table,item):
    pass
#保存数据到数据库
def save_date_to_db(item):
    pass


