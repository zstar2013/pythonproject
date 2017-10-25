from tools import strtool as st
import logic.feedback as fb
#读取统计数据文件
def load_sum_data(table, item):
    print(table.name)
    nrows = table.nrows
    list = []
    indexR=item[0]
    carNoC=item[1]
    route=fb.getRoute(table.name)
    for i in range(indexR, nrows):
        if table.cell(i, carNoC).value is "":
            continue
        if st.contains(str(table.cell(i,carNoC).value),"小计"):
            continue
        item=[]
        car_id=fb.getCar_id(table.cell(i, carNoC).value,table.name)
        item.append(car_id)#车辆id
        item.append(route)#车辆线路
        item.append(table.cell(i,carNoC+1).value)#车公里
        item.append(table.cell(i,carNoC+2).value)#指标总量
        item.append(table.cell(i, carNoC + 3).value)  # 百公里指标target
        item.append(table.cell(i, carNoC + 4).value)  # 车辆油耗
        item.append(table.cell(i, carNoC + 6).value)  # 实际节约
        item.append(table.cell(i, carNoC + 7).value)  # 实际超耗
        item.append(table.cell(i, carNoC + 8).value)  # 二保
        item.append(table.cell(i, carNoC + 9).value)  # 跟车
        list.append(item)
    return list
