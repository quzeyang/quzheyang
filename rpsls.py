#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2019/11/20
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	if name=="ʯͷ":
		return 0
	if name=="ʷ����":
		return 1
	if name=="��":
		return 2
	if name=="����":
		return 3
	if name=="����":
		return 4
	if name!="ʯͷ" and name!="ʷ����" and name!="��" and name!="����" and name!="����":
		return 99

def number_to_name(number):
	if number==0:
	   return "ʯͷ"
	if number==1:
	   return "ʷ����"
	if number==2:
	   return "��"
	if number==3:
	   return "����"
	if number==4:
	   return "����"

def rpsls(player_choice):
	print("����ѡ��Ϊ:",player_choice)
	a=name_to_number(player_choice)	
	comp_number=random.randrange(0,5)
	b=number_to_name(comp_number)
	print("�������ѡ��Ϊ:",b)
	c=a-comp_number	
	if c in range(-4,-2) or c in range(1,3):
		print("��Ӯ��")	
	if c in range(-2,0) or c in range(3,5):
		print("����Ӯ��")
	if c==0:
		print("���ͻ�������һ����")
	if a==99:
		print("Error: No Correct Name")
	
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)

