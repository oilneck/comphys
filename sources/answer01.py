'''01 自分の名前を表示するプログラム'''

'''
pythonではシングルクォーテーション「'」3つで囲んだ部分がコメントアウトの扱いになる．
コメントアウトとはプログラム中にメモや注釈をコメントとして残すこと．
複数行でも可．一行のコメントアウトならシャープ「#」を先頭につければよい．
'''



# 解答1 [文字列はダブルクォーテーション「"」で囲む]
print("My name is  Pythonist.")

# 解答2  [シングルクォーテーション「'」で囲んでもよい]
print('My name is Pythonist')




'''------- 別解 -------'''

# 別解1 [変数nameに文字列を代入して表示]
name = "My name is Phthonist"
print(name)

# 別解2 [formatメソッドを用いて{}内を置換]
name = "Pythonist"
print("My name is {}".format(name))

# 別解3 [string(文字列)型の要素として表示]
print('My name is %s' % 'Pythonist')
