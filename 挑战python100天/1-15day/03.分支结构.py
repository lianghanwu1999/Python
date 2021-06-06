#TODO 分支结构

#用户身份验证
"""
username = input('输入用户名')
password = input('输入口令')

#用户名是admin 且密码是123456 则身份验证成功，否则身份验证失败
if username =='admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')

"""
"""
分段函数求值
        3x - 5  (x>1)
f(x) =  x+2 (-1 <= x < = 1)
        5x +3   (x<-1)
"""
"""
x = float(input('x= '))
if x > 1:
    y = 3 *x -5
elif x >=-1:
    y = x + 2
else:
    y = 5*x+3
print('f(%.2f)= %.2f' %(x,y ))
"""


"""
英制单位英寸和公制单位厘米互换
"""
"""
value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')
"""

"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
"""
a = float(input('a= '))
b = float(input('b ='))
c = float(input('c = '))
if a+b > c and a+c > b and b+c > a:
    print('周长：%f' %(a+b+c))
    p = (a+b+c )/2
    area = (p*(p-a)*(p-c))**0.5
    print("面积：%f" %(area))
else:
    print('不能构成三角形')
