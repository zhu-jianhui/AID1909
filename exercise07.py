# 匀加速直线运动的位移与时间公式:
# 距离 = 初速度 * 时间 + 加速度 * 时间平方 * 0.5
# 在终端中获取:距离,时间,初速度
# 输出加速度

# (距离 - 初速度 * 时间) * 2 / 时间平方 =  加速度
distance = float(input("请输入距离:"))
initial_velocity = float(input("请输入初速度:"))
time = float(input("请输入时间:"))
accelerated_velocity = (distance - initial_velocity * time) * 2 / time ** 2
print("加速度是:"+str(accelerated_velocity))








