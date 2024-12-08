# -*- coding: utf-8 -*-
import sys
import codecs

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)


from modules.Simulation import Simulation
from modules.Constants_morning import *


type_name = "wall01"
sim_name = "朝ラ�?シュ@" + type_name

# シミュレーションの設�?
sim = Simulation(WIDTH, HEIGHT, sim_name, type_name)

# sim.add_wall(400, 340, 410, 350)
# 壁�?�追�?

sim.add_wall(0, 0, 30, 500) # 左
sim.add_wall(430, 360, 500, 500) # 右
sim.add_wall(0, 450, 290, 500) # �?
sim.add_wall(290, 480, 500, 500) # �?
sim.add_wall(0, 0, 500, 150) # �?
sim.add_wall(0, 0, 300, 300) # 左�?
sim.add_wall(300, 150, 500, 180)
sim.add_wall(150, 300, 185, 350)

sim.add_wall(110, 420, 140, 450) # エレベ�?�ター
sim.add_wall(375, 180, 400, 210) # 精算�?

sim.add_wall(185, 300, 195, 340)
sim.add_wall(195, 300, 205, 330)
sim.add_wall(205, 300, 215, 320)
sim.add_wall(215, 300, 225, 310)

sim.add_wall(250, 370, 290, 450)
sim.add_wall(240, 380, 250, 450)
sim.add_wall(230, 390, 250, 450)
sim.add_wall(220, 400, 230, 450)
sim.add_wall(210, 410, 220, 450)
sim.add_wall(200, 420, 210, 450)
sim.add_wall(190, 430, 200, 450)
sim.add_wall(50, 300, 150, 350)
sim.add_wall(495, 0, 500, 500)

# 追�?障害物
sim.add_wall(395, 350, 405, 360)

# フェイク�?
# sim.add_fake_wall(475, 0, 500, 500)
sim.add_fake_wall(30,300, 50, 450)
sim.add_fake_wall(290, 370, 300, 450)
sim.add_fake_wall(290, 450, 500, 480) # �?

# スタート位置の追�?
### add_start_position(x, y, weight, futinobe, middle, middle_2)
# --- futinobe person ---
sim.add_start_position(490, 200, 1, True, False)
sim.add_start_position(490, 220, 1, True, False)
sim.add_start_position(490, 240, 1, True, False)

# --- futinobe worker ---
# 階段(奥)
sim.add_start_position(55, 440, 3, False, True)
sim.add_start_position(55, 430, 3, False, True)
sim.add_start_position(55, 420, 3, False, True) 
sim.add_start_position(55, 410, 3, False, True)

# エスカレーター(上り)
sim.add_start_position(310, 440, 3, False) 
sim.add_start_position(310, 420, 3, False) 

# 階段(手前)
sim.add_start_position(420, 440, 1, False, middle_2=True)
sim.add_start_position(420, 430, 2, False, middle_2=True)
sim.add_start_position(420, 420, 2, False, middle_2=True) 
sim.add_start_position(420, 410, 2, False, middle_2=True) 
sim.add_start_position(420, 400, 2, False, middle_2=True) 
sim.add_start_position(420, 390, 2, False, middle_2=True) 
sim.add_start_position(420, 380, 1, False, middle_2=True) 

# ------------------------------
### add_goal(x, y, weight, futinobe, middle, middle_2)
# 目�?地(確�?あり?�?
sim.add_goal(490, 260, 1, False)
sim.add_goal(490, 280, 1, False)
sim.add_goal(490, 300, 1, False)
sim.add_goal(490, 320, 1, False)
sim.add_goal(490, 340, 1, False) # 12/5 tuika

# 階段(右)
sim.add_goal(420, 440, 1, True, False, True)
# sim.add_goal(420, 430, 1, True, False, True)
# sim.add_goal(420, 420, 1, True, False, True)
# sim.add_goal(420, 410, 1, True, False, True) 
# sim.add_goal(420, 400, 1, True, False, True) 
# sim.add_goal(420, 390, 1, True, False, True) 
# sim.add_goal(420, 380, 1, True, False, True) 

# 階段(奥)
sim.add_goal(55, 400, 2, True, True) 
sim.add_goal(55, 390, 2, True, True)
sim.add_goal(55, 380, 2, True, True)
sim.add_goal(55, 370, 2, True, True)

# エスカレーター(下り)
sim.add_goal(310, 400, 2, True) 
sim.add_goal(310, 380, 2, True) 

# ------------------------------
# 中間地点
## add_middle_position(x, y, Right=False)
sim.add_middle_position(300, 310)
sim.add_middle_position(300, 320)
sim.add_middle_position(300, 330)
sim.add_middle_position(300, 340)
sim.add_middle_position(300, 350)
# sim.add_middle_position(300, 360)


# sim.add_middle_position(420, 350, True)
# sim.add_middle_position(415, 350, True)
sim.add_middle_position(410, 350, True)
# 消し�?
# sim.add_middle_position(405, 350, True)
# sim.add_middle_position(400, 350, True)
# sim.add_middle_position(395, 350, True)
sim.add_middle_position(390, 350, True)
sim.add_middle_position(385, 350, True)

# 初期エージェント�?�生�??
for _ in range(START_HUMAN_COUNT):
    sim.born_agent()

# アニメーションの実�?
sim.animate(FRAME_COUNT)

