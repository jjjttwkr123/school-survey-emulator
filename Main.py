import time

#,end=""
#重要
debug = 'false'
#预定义
good = 'A'
ban = '回答错误,已改为'+good
S = 'C'
#Debug
if debug == 'true':
	schoolname = 'school'
	act = 'student'
	manager = 'teacher'
else:
	schoolname = 'school'
	act = 'student'
	manager = 'teacher'
#程序函数
def check( block ):
	 if S == block:
	     print(manager+':'+ban)
	     print('选项:'+good)
	 else:
	     	print('继续答题')
	     	print('选项:'+S)
def printnl ( pnt ):
	print ( pnt ,end='')
#正式程序
print(schoolname+'内部问卷调查')
time.sleep(3)
print('请各位'+act+'如实回答')
time.sleep(2)
print('本部分共有5题')
print('1.你每天睡几个小时')
print('A.10个小时 B.9个小时 C.8个小时')
S = input('')
check ( block='C' )
time.sleep(2)
print('2.你每天写作业多长时间')
print('A.一个小时 B.两个小时 C.两个小时以上')
S = input('')
check( block='C' )
time.sleep(2)
print('3.老师有体罚行为吗')
print('A.无 B.有')
S = input('')
check ( block='B' )
time.sleep(2)
print('4.老师有向家长索要钱财吗')
print('A.无 B.有')
S = input('')
check ( block='B' )
time.sleep(2)
print('5.你对学校满意吗')
print('A.满意 B.不满意')
S = input('')
check ( block='B' )
print('本次问卷结束，感谢您的填写')
printnl(pnt='举报电话:+86 11451419198')
time.sleep(10)