'''
  下面主要说明Python的基本运算的问题
  第一：加法运算
  第二：除法运算 单个除法的结果是浮点数
  第三：取模运算
'''
#print(3 + 7)
#print(10 / 7)
#print(10 % 7)

'''
  下面说明一下Python对负数除法的支持
'''
#print(10 / -7)

'''
负数在进行取模运算时，结果数的符号根据第二个操作数的符号决定
例如：  -10 % 7 =4
        10 % 7=-4
'''
#print(-10 % 7)
#print(10 % -7)

#float 浮点类型
#print(10.0 / 5)

'''
  这里有一个优先级的问题，在进行组合运算的时候，首先计算等号右边的值。然后在进行组合计算
'''
b = 10
b *= 10+2
print(b)