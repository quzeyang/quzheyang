#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：屈泽阳
日期：2019/11/20
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
	if name=="石头":
		return 0
	if name=="史波克":
		return 1
	if name=="布":
		return 2
	if name=="蜥蜴":
		return 3
	if name=="剪刀":
		return 4
	if name!="石头" and name!="史波克" and name!="布" and name!="蜥蜴" and name!="剪刀":
		return 99

def number_to_name(number):
	if number==0:
	   return "石头"
	if number==1:
	   return "史波克"
	if number==2:
	   return "布"
	if number==3:
	   return "蜥蜴"
	if number==4:
	   return "剪刀"

def rpsls(player_choice):
	print("您的选择为:",player_choice)
	a=name_to_number(player_choice)	
	comp_number=random.randrange(0,5)
	b=number_to_name(comp_number)
	print("计算机的选择为:",b)
	c=a-comp_number	
	if c in range(-4,-2) or c in range(1,3):
		print("您赢了")	
	if c in range(-2,0) or c in range(3,5):
		print("机器赢了")
	if c==0:
		print("您和机器出的一样呢")
	if a==99:
		print("Error: No Correct Name")
	
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)

