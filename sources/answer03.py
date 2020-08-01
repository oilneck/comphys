'''03 長方形の外周の長さと面積を求めるプログラム'''

height = 3.25 #(cm)
width = 5.72 #(cm)

perimeter = 2 * height + 2 * width
perimeter = round(perimeter,3) # 小数点3桁で四捨五入
area = height * width

params = '[(height,width)=({},{})]'.format(height,width)
print("The perimeter of a rectangle" + params + "is", perimeter)
print("The area of a rectangle" + params + "is", area)
