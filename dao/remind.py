#查询每辆车对应的指标
#SELECT bus_info.car_id ,oilwear_target.target_noac,oilwear_target.target_ac from bus_info JOIN oilwear_target WHERE bus_info.cartype=oilwear_target.cartype AND oilwear_target.`enable`=TRUE