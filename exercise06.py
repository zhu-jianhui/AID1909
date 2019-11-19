"""
    练习:古代的秤一斤16两,
        在终端中获取两,  100
        输出几斤零几两.
"""
liang_weight = int(input("请输入两:"))
jin = liang_weight // 16
liang = liang_weight % 16
# 在字符串中插入数据
print(str(jin) + "斤零" + str(liang) + "两")
