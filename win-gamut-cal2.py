import colour
import numpy as np
from shapely.geometry import Polygon
# 1  colour-science函数画出CIE1976UCS色域图
colour.plotting.plot_chromaticity_diagram_CIE1931(standalone=False)
#A = SDS_ILLUMINANTS["A"]
#D65 = SDS_ILLUMINANTS["D65"]
#plot_sds_in_chromaticity_diagram_CIE1931UCS([A, D65])
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# input the coordinates of the RGB color
red = [0.6920, 0.3077]
green =[0.1557,0.7391]
blue = [0.1326,0.0589]

ax = plt.gca()       # 获取CIE1976UCS的坐标系
# 2  将CIE1931 xy坐标转换成CIE1976 u'v'坐标
# 坐标转换函数
# colour.xy_to_Luv_uv        convert  CIE 1931 xy to CIE 1976UCS u'v'
# colour.xy_to_UCS_uv       convert CIE 1931 xy to CIE 1960UCS uv            
#  xy: CIE 1931 xy;    UCS_uv: CIE 1960UCS uv;  Luv_uv: CIE 1976 u'v'
REC_709=([[.64, .33], [.3, .6], [.15, .06]])
Trangle_rec709 = Polygon([(0.64,0.33),(0.3,0.6),(0.15,0.06)])

REC_2020=([[.708, .292], [.170, .797], [.131, .046]])
Trangle_rec2020 = Polygon([(0.708,0.292),(0.170,0.797),(0.131,0.046)])

DCI_P3=([[.68, .32], [.265, .69], [.15, .06]])
Trangle_dci = Polygon([(0.68,0.32),(0.265,0.69),(0.15,0.06)])

Testing_lamp = ([red,green,blue])
#Trangle_tes = Polygon([(0.6857, 0.3107),(0.1413,0.7171),(0.1363,0.0682)])
Trangle_tes = Polygon(Testing_lamp)

Intersection_area_rec709 = Trangle_tes.intersection(Trangle_rec709).area
Intersection_area_rec2020 = Trangle_tes.intersection(Trangle_rec2020).area
Intersection_area_dci = Trangle_tes.intersection(Trangle_dci).area

Ratio_rec709 = Intersection_area_rec709/Trangle_rec709.area
Ratio_rec2020 = Intersection_area_rec2020/Trangle_rec2020.area
Ratio_dci = Intersection_area_dci/Trangle_dci.area

# 3 matplotlib绘制ITU-R BT.709，ITU-R BT.2020，DCI-P3色域空间多边形
gamut_709=patches.Polygon(REC_709, linewidth=2, color='green', fill=False)
gamut_2020=patches.Polygon(REC_2020, linewidth=2, color='yellow', fill=False)
gamut_DCI_P3=patches.Polygon(DCI_P3, linewidth=1, color='blue', fill=False)
gamut_Testing_lamp=patches.Polygon(Testing_lamp, linewidth=1, color='red', fill=False)
#gamut_pointer=patches.Polygon(pointer_bound_uv, linewidth=2, color='white', fill=False)
ax.add_patch(gamut_709)
ax.add_patch(gamut_2020)
ax.add_patch(gamut_DCI_P3)
ax.add_patch(gamut_Testing_lamp)
#ax.add_patch(gamut_pointer)
# 4 附加曲线标注，修改坐标范围
plt.legend([gamut_709,gamut_2020, gamut_DCI_P3,gamut_Testing_lamp],
    ['Rec709 of ' + str(Ratio_rec709),'Rec2020 of ' + str(Ratio_rec2020), 'DCI-P3 of ' + str(Ratio_dci),'Our_lamp'],
    loc='upper right')  # 对曲线的标注
plt.axis([-0.1, 0.9, -0.1, 0.9])    #改变坐标轴范围

# 5 显示
plt.show()
