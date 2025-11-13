#Important!!!!!
#Please confirm that you have already installed:
#numpy, scipy, matplotlib !!!
#if you haven't, please search for downloading packages from pip OR YOU CANNOT RUN THIS PROGRAM !!!!!





import numpy as np
from scipy import stats as sts
import webbrowser
from matplotlib import pyplot as plt
import sys
import time
import random
from scipy.stats import gaussian_kde
import json

def ini_func():# 打印初始化动画和界面的函数，包含版本号等。等这个播放完按enter该函数结束运行。		无输入参数和返回值	注：该版本不适配Sublime Text和IDLE!
	print('\033[1;32mLoading', end='')

	for i in range(9):
		time.sleep(0.5)
		print('.', end='')
	time.sleep(0.5)
	print('.')







	print('Statistic Homework Assistant Ver. 0.1.26.Alpha, Copyright © 2025 Zhang Yiwei, based on python, numpy, scipy and matplotlib.')

	time.sleep(0.5)


	print('     ______    ________    ____      ________    ____    ______    ________    ____    ________    ______')
	time.sleep(0.25)
	print('    / ____/   /__   __/   / __ |    /__   __/   /___/   / ____/   /__   __/   /___/   /  _____/   / ____/')
	time.sleep(0.25)
	print('   / /___       /  /     / /_| |      /  /     ____    / /___      /  /      ____    /  /        / /___')
	time.sleep(0.25)
	print('  /____ /      /  /     / ____ |     /  /     /   /   /____ /     /  /      /   /   /  /        /____ /')
	time.sleep(0.25)
	print('  ___/ /      /  /     / /   | |    /  /     /   /    ___/ /     /  /      /   /   /  /_____    ___/ /')
	time.sleep(0.25)
	print('/_____/      /__/     /_/    |_|   /__/     /___/   /_____/     /__/      /___/   /________/  /_____/ ')
	time.sleep(0.25)
	print('Press Enter to start: \033[0m')







	input()




def exit_func(): #退出动画，无输入参数和返回值
	print('\033[1;32mThanks for using Statistics Homework Assistant!')
	print('Copyright © 2025 Zhang Yiwei')
	print('If you are satisfied with the experience of using this program, ')
	print('you are welcome to support me on my personal social media account.')
	print('Your support is the motivation for me to continue developing programs.')

	print("Do you want to be redirected to my social media account? (y/n)\033[0m")


	last = input()

	if last == 'y' or last == 'Y':
		print('\033[1;32mThank you for your supporting very much!')

		print('Redirecting', end = '')

		for i in range(6):
			time.sleep(0.5)
			print('.', end='')

		print('Succeed!\033[0m')


		webbrowser.open("https://space.bilibili.com/1505913565?spm_id_from=333.1007.0.0")





	else:
		print('\033[1;32mThanks for using! Wish you a good day!\033[0m')


	sys.exit()





def input_func(): #该函数无输入参数，用于采集用户输入的数据集或生成随机数据集。 返回一个列表，其元素为一个或几个列表。 二级列表下的元素为浮点型




	variable_list = []




	while True:




		while True:

			print('Please enter values of a numerical variable, use space to split each value, enable random number generator(R) or linear generator(LN) to generate a dataset, load data(LD), or enter # to exit: ')
			input_string = input().upper()

			if input_string == '#':

				if len(variable_list) == 0:

					if ask_func("You haven't enter anything yet, confirm to exit?(y/n)",'Y','y','N','n'):

						return variable_list
					else:

						pass

				else:

					return variable_list


			elif input_string == 'R':



				input_string = random_generator()

			elif input_string == 'LD':


				while True:
					file_path = list(input('Please enter the path of the file: '))

					while '"' in file_path:
						del file_path[file_path.index('"')]

					file_path =  ''.join(file_path)

					try:
						input_string = json_reading(file_path)

					except OSError:

						print('Invalid path, please try again!')

					if not input_string == False:

						break


			elif input_string == 'LN':

				input_string = linear_lst()



			valid_characters = '1234567890. -Ee'
			if all(char in valid_characters for char in input_string) and input_string != '#':
				input_string_list = input_string.split(' ')
				try:
					input_values_list = [float(i) for i in input_string_list]
				except ValueError:
					print('Invalid input, please try again! ')
				else:
					break

			elif input_string == '#':

				pass


			else:
				print('Invalid input, please try again! ')

		print('Your input is: ')
		print(input_values_list)
		variable_list.append(input_values_list)



def histo_plotting(data): #生成直方图的函数，输入参数为一个元素为浮点型的列表，为需要画的数据集，无返回值
	

	print('How many bins do you want, or enter nothing to enable default settings.')

	while True:

		bin_num_str = input()

		if bin_num_str == '':
			bin_num_str = str(int(1 + np.log10(len(data)) / np.log10(2)))


		try:
			bin_number = int(bin_num_str)

		except ValueError:
			print('Invalid input, please try again! ')
		else:
			break


	

	dens_des = ask_func('Do you want to display density line? (y/n)', 'Y', 'y', 'N', 'n')



	plt.hist(data, bins=bin_number, edgecolor='black', density = dens_des)


	if dens_des:

		component = calc_density(data)

		plt.plot(component[0], component[1])


	title = input('Please type in the title of the histogram: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')


	x_label = default_label(x_label, 'Observation')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')



	if y_label == '' and (not dens_des):

		y_label = 'Frequency'


	elif y_label == '':

		y_label = 'Relative frequency(%)'


	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()

	plt.show()

	print('Succeed!')



def box_plotting(data): #生成箱线图的函数，输入参数为一个元素为列表的列表，二级列表的元素是浮点型，为总的数据集，无返回值
	print('Boxplot mode')

	data_needed = []

	data_index = []

	data_label_input = ''



	data_group_label = []

	while True:

		while True:

			data_index_working = ask_number_with_exit('Which data set would you like to plot, or enter # to finish?')

			

			if data_index_working == '#':

				break

			



			if data_index_working >= len(data) or data_index_working < (0 - len(data)):
				print(error_index_range(data))

			else:

				print('Please enter a label for this group: ')

				data_label_input = input()

				break

		if data_index_working == '#':

			break

		data_index.append(data_index_working)
		data_group_label.append(data_label_input)

	vert_idx = ask_func('Vertical (v) or horizontal(h) box?','v','V','h','H')

	mean_display = ask_func('Do you want do display mean in this plot? (y/n)','y','Y','n','N')

	for i in data_index:

		data_needed.append(data[i])






	plt.grid(True)
	plt.boxplot(data_needed, patch_artist = True, showmeans = mean_display, meanline = True, vert = vert_idx, tick_labels = data_group_label)

	title = input('Please type in the title of the box plot: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')

	x_label = default_label(x_label, 'Observation')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')

	y_label = default_label(y_label, 'Distribution')



	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)

	plt.show()

	print('Succeed!')



def ask_func(qst,tr_a,tr_b,fl_c,fl_d): #选择函数，接受五个输入参数，分别是一个问题，两个真条件触发值和两个假条件触发值，都是字符串类型。 返回布尔值，真假皆有。
	while True:
		print(qst)



		ans = input()
		if ans == tr_a or ans == tr_b:
			return True
		elif ans == fl_c or ans == fl_d:
			return False
		else:
			print('Invalid input, please try again.')







def calc_para(inp_dat): #计算统计学参数的函数，输入参数是一个元素为浮点型的列表，为待测数据集。 返回值为一个列表，对应： 0： 排序后的数据集（列表）， 1： 数据集长度（整数）
	#， 2： 均值（浮点）， 3： 中位数（浮点）， 4： 众数， 5：众数的出现次数，6： 下四分位数（浮点）， 7： 上四分位数（浮点）， 8： 极差（浮点）， 9： 四分位差（浮点）， 10： 离群值（列表），11: 方差（浮点）， 12： 标准差（浮点）13；百分数（列表），14：z-分数（列表）
	data = sorted(inp_dat)
	mean = np.mean(data)
	median = np.median(data)
	mode = sts.mode(data)
	q1 = sts.scoreatpercentile(data,25)
	q3 = sts.scoreatpercentile(data,75)
	range_data = np.ptp(data)
	iqr = q3 - q1
	outlier = []
	total_variance = np.var(data)
	total_std = np.std(data)




	for otl_check in data:

		if otl_check <= q1 - 1.5 * iqr or otl_check >= q3 + 1.5 * iqr:
			outlier.append(otl_check)





	print('Data after arrangement: ')
	print(data)
	print('Count: ')
	print(len(data))
	print('Mean: ')
	print(round(mean,3))
	print('Median: ')
	print(round(median,3))
	print('Mode: ')
	print(mode.mode)
	print('Count of mode: ')
	print(mode.count)
	print('Q1: ')
	print(round(q1,3))
	print('Q3: ')
	print(round(q3,3))
	print('Range: ')
	print(round(range_data,3))
	print('IQR: ')
	print(round(iqr,3))
	print('Outliers: ')
	print(outlier)
	print('Variance: ')
	print(round(total_variance,3))
	print('Standard deviation: ')
	print(round(total_std,3))



	advance_des = ask_func('Do you want to calculate advanced parameters?(y/n)','Y','y','N','n')


	if advance_des:

		advance_para = advance_para_calc(inp_dat, mean, total_std)

	else:
		advance_para = [[],[]]

	return [data, len(data), mean, median, mode.mode, mode.count, q1, q3, range_data, iqr, outlier, total_variance, total_std, advance_para[0], advance_para[1]]




def ask_number(qst, float_check=False): #问询数字函数，输入参数为一个字符串和一个布尔值，输出一个整数
	while True:
		print(qst)

		input_thing = input()





		try:

			if not float_check:
				input_num = int(input_thing)

			else:

				input_num = float(input_thing)



		except ValueError:
			print('Invalid input, please try again! ')



		else:
			return input_num







def ask_number_with_exit(qst): #带退出问询数字函数，输入参数为一个字符串，输出一个整数或 '#'。 用于触发某些退出条件
	while True:
		print(qst)

		input_thing = input()



		if input_thing == '#':
			return '#'
		try:
			input_num = int(input_thing)



		except ValueError:
			print('Invalid input, please try again! ')



		else:
			return input_num



def random_num(start, end, times): #随机数函数，输入参数为数据下限（整数），数据上限（整数），数据量（整数），输出一个只包含浮点数和空格的字符串
	list_ran = []

	

	for i in range(times):

		list_ran.append(str(random.randint(start, end)))
	
	string = ' '.join(list_ran)



	return string






def normal_dis_num(mean_dis, std_dis, size_dis): #正态分布函数，输入参数为均值（浮点数），标准差（浮点），数据量（整数），输出一个只包含浮点数和空格的字符串

	list_nrm = []


	normal_list = np.random.normal(loc = mean_dis, scale = std_dis, size = (1, size_dis))


	for normal_index in range(size_dis):

		list_nrm.append(str(normal_list[0][normal_index]))
	
	string = ' '.join(list_nrm)


	return string




def multi_histo_plotting(data): #多数据直方图函数，输入参数为数据总集（两层嵌套列表，二级列表元素为浮点），无返回值
	print('Multi-Histogram mode')

	data_needed = []

	data_index = []




	data_group_label = []

	data_label_input = ''

	while True:

		while True:

			data_index_working = ask_number_with_exit('Which data set would you like to plot, or enter # to finish?')

			

			if data_index_working == '#':

				break



			if data_index_working >= len(data) or data_index_working < (0 - len(data)):
				print(error_index_range(data))

			else:

				print('Please enter a label for this group: ')

				data_label_input = input()

				break

		if data_index_working == '#':

			break

		data_index.append(data_index_working)
		data_group_label.append(data_label_input)
	

	print('How many bins do you want, or enter nothing to enable default settings.')

	while True:

		bin_num_str = input()

		if bin_num_str == '':

			bin_num_str = str( int(1 + np.log10(len(data[data_index[random.randint(0, len(data_index) - 1)]])) / np.log10(2)))
		try:
			bin_number = int(bin_num_str)

		except ValueError:
			print('Invalid input, please try again! ')
		else:
			break


	for i in data_index:

		data_needed.append(data[i])


	label_index = 0



	for index_of_data in data_needed:

		plt.hist(index_of_data, bins=bin_number, edgecolor='black', alpha=0.5, label = data_group_label[label_index])




		label_index += 1



	title = input('Please type in the title of the histogram: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')

	x_label = default_label(x_label, 'Observation')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')

	y_label = default_label(y_label, 'Frequency')


	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()
	plt.legend()

	plt.show()

	print('Succeed!')





def cum_rel_frequency_g(data): #堆积百分比图，输入参数为数据总集（两层嵌套列表，二级列表元素为浮点），无返回值
	print('Cumulative relative frequency graph mode')



	while True:

		data_index_working = ask_number('Which data set would you like to plot?')


		if data_index_working >= len(data) or data_index_working < (0 - len(data)):
			print(error_index_range(data))

		else:

			break


	data_needed = sorted(data[data_index_working])


	plt.ecdf(data_needed)



	title = input('Please type in the title of the graph: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')

	x_label = default_label(x_label, 'Observation')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')

	y_label = default_label(y_label, 'Cumulative relative frequency')


	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()
	plt.show()

	print('Succeed!')


def dot(data): #点状图，输入参数为数据总集（两层嵌套列表，二级列表元素为浮点），无返回值
	print('Dotplot mode')



	while True:

		data_index_working = ask_number('Which data set would you like to plot?')


		if data_index_working >= len(data) or data_index_working < (0 - len(data)):
			print(error_index_range(data))

		else:

			break

	data_needed = sorted(data[data_index_working])

	data_height = count_list(data_needed)[1]
	x_axis = count_list(data_needed)[0]






	for index_of_data in range(len(x_axis)):

		for index_of_data_height in range(1, int(data_height[index_of_data])):

			data_height.append(index_of_data_height)
			x_axis.append(x_axis[index_of_data])




	plt.scatter(x_axis, data_height)

	title = input('Please type in the title of the graph: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')

	x_label = default_label(x_label, 'Observation')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')

	y_label = default_label(y_label, 'Frequency')

	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.ylim(0,None)

	plt.show()

	print('Succeed!')


def fre_sct(data):  # 频率散点图，输入参数为数据总集（两层嵌套列表，二级列表元素为浮点），无返回值
	print('Scatter(frequency) mode')



	while True:

		data_index_working = ask_number('Which data set would you like to plot?')

		if data_index_working >= len(data) or data_index_working < (0 - len(data)):
			print(error_index_range(data))

		else:

			break

	data_needed = sorted(data[data_index_working])




	x_axis = count_list(data_needed)[0]

	data_height = count_list(data_needed)[1]

	plt.scatter(x_axis, data_height)

	title = input('Please type in the title of the graph: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')

	x_label = default_label(x_label, 'Observation')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')

	y_label = default_label(y_label, 'Frequency')

	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)

	plt.grid()
	plt.ylim(0,None)


	plt.show()

	print('Succeed!')

def calc_density(data): #密度图，输入参数为数据集（列表，列表元素为浮点），返回值一个列表，两个元素(x值和y值)

	data_sorted = sorted(data)

	density = gaussian_kde(data)
	x = np.linspace(data_sorted[0], data_sorted[-1], len(data_sorted))
	y = density(x)

	return [x, y]

def count_list(data): #计算列表中元素的数量，输入参数为一个列表，返回值为一个双层列表，0是原来的元素，1是元素的数量


	dic_frequency = {}


	for item in data:
		if item not in dic_frequency:
			dic_frequency[item] = 1
		else:
			dic_frequency[item] += 1




	return [list(dic_frequency.keys()),list(dic_frequency.values())]




def scatter_plt(data): #散点图，输入参数为数据总集（两层嵌套列表，二级列表元素为浮点），无返回值
	print('Scatter mode')



	while True:

		while True:

			data_index_working = ask_number('Which data set would you like to plot as x-axis?')

			if data_index_working >= len(data) or data_index_working < (0 - len(data)):
				print(error_index_range(data))

			else:
				x_axis = data[data_index_working]
				break

		while True:

			data_index_working = ask_number('Which data set would you like to plot as y-axis?')

			if data_index_working >= len(data) or data_index_working < (0 - len(data)):
				print(error_index_range(data))

			else:
				y_axis = data[data_index_working]
				break


		if len(x_axis) == len(y_axis):

			break

		else:



			print('Error! Type: x-axis and y-axis have different length!')

	plt.scatter(x_axis, y_axis, label = 'Data')

	reg_des = ask_func('Do you want to display regression line in your scatter plot?(y/n)','Y','y','n','N')

	if reg_des:

		while True:
			type_des = input('Do you want a linear regression(L) or a polynomial regression(P)?\n').upper()

			match type_des:

				case 'L':

					try:
						result_reg = linear_reg(x_axis, y_axis)

						break

					except ValueError:

						result_reg = [0, 0, 0, 0]

						break

				case 'P':
					result_reg = [0, 0, 0, 0]
					try:

						n = float(input('Please enter the degree of the regression(n in R): '))

						ploy_reg(x_axis, y_axis, n)

						break

					except ValueError:

						print('Invalid input of degree!')

					break


				case _:

					print('Invalid input!')
	else:

		result_reg = [0, 0, 0, 0]

		type_des = None

	title = input('Please type in the title of the graph: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')

	x_label = default_label(x_label, 'Observation')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')

	y_label = default_label(y_label, 'Frequency')

	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)


	if reg_des:
		plt.legend()

		if type_des == 'L':

			print('s=' + str(round(result_reg[2],3)))
			print('r^2=' + str(round(result_reg[3],3)))


	plt.grid()

	plt.show()

	print('Succeed!')




def binomial_dis_num(): #二项分布函数，输入参数为试验次数（整数），成功概率（浮点，0-1），实验量（整数），输出一个只包含浮点数和空格的字符串

	list_bino = []


	n, p, size_dis = distri_ask_paras()


	bino_list = np.random.binomial(n=n, p=p, size=size_dis)


	for bino_index in range(size_dis):


		list_bino.append(str(bino_list[bino_index]))

	
	string = ' '.join(list_bino)


	return string




def test_range(tested_value, upper, lower, fault_message, include_up, include_low): #测试输入值是否在要求范围内
																					#参数：待测值（浮点/整数），上界（浮点/整数），下界（浮点/整数）。错误信息（字符串）
	if include_up and include_low:													#包括上界（布尔），包括下界（布尔）

		if tested_value > upper or tested_value < lower:
			print(fault_message)

			return False

		else:

			return True

	elif include_up and not include_low:

		if tested_value > upper or tested_value <= lower:
			print(fault_message)

			return False

		else:

			return True


	elif not include_up and include_low:

		if tested_value >= upper or tested_value < lower:
			print(fault_message)

			return False

		else:

			return True


	elif not include_up and not include_low:

		if tested_value >= upper or tested_value <= lower:
			print(fault_message)

			return False

		else:

			return True



def linear_reg(x_data,y_data): #线性拟合，输入为两个列表，元素为浮点，输出一个列表，0：斜率，1：y截距，2：残差标准差，3：r方

	if len(x_data) != len(y_data):

		raise ValueError('The length of x input and y input is not equal.')


	slope, intercept = np.polyfit(np.array(x_data), np.array(y_data), 1)



	plt.plot(np.array(x_data), np.array(x_data) * slope + intercept, color = 'red', label = str(round(slope,3)) + 'x + ' + str(round(intercept,3)))



	residual_all = 0

	y_y_bar = 0

	for index_for_res in x_data:

		residual_single = (slope * x_data[x_data.index(index_for_res)] + intercept) - y_data[x_data.index(index_for_res)]

		residual_all += residual_single ** 2

	for index_for_y_bar in y_data:

		y_y_bar_single = index_for_y_bar - float(np.mean(y_data))

		y_y_bar += y_y_bar_single ** 2


	s = (residual_all / (len(y_data) - 2)) ** 0.5


	r2 = 1 - (residual_all / y_y_bar)





	return [float(slope),float(intercept),s,r2]



def dst_plt(data):  #画密度曲线的函数，输入参数为数据总集，无返回值

	while True:

		index_dst = ask_number('Which data set would you like to plot?')

		if test_range(index_dst, len(data), 0 - len(data), error_index_range(data), True, True):

			data_needed = data[index_dst]

			break



	dst_crv = calc_density(data_needed)

	plt.plot(dst_crv[0], dst_crv[1])

	title = input('Please type in the title of the density curve: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')

	x_label = default_label(x_label, 'Observation')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')

	y_label = default_label(y_label, 'Relative frequency(%)')

	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()

	plt.show()

	print('Succeed!')



def default_label(label, default): #默认标签函数，输入两个字符串（输入标签，默认标签），返回一个字符串


	if label == '':

		return default

	else:
		return label

def advance_para_calc(data, mean, total_std): #计算高级统计学参数，输入参数为待算数据集，平均值，标准差（浮点），输出一个列表，0：百分数，1：z-分数


	percentile_all = []
	z_score_all = []
	percentile_all_print = []
	z_score_all_print = []

	for index_of_percentile_all in range(len(data)):

		percentile_current_val = index_of_percentile_all / len(data)

		percentile_all.append(percentile_current_val)
		percentile_all_print.append(str(round(100 * percentile_current_val,3)) + '%')

	for index_of_zscore_all in data:


		zscore = float((index_of_zscore_all - mean) / total_std)

		z_score_all.append(zscore)

		z_score_all_print.append(str(round(zscore,3)))

	print('Percentile: ')
	print(' '.join(percentile_all_print))
	print('Z-score: ')
	print(' '.join(z_score_all_print))


	return [percentile_all, z_score_all]




def poisson_dis(lam, size_dis):

	pois_nrm = []

	poi_list = np.random.poisson(lam, size_dis)

	for pois_index in range(size_dis):
		pois_nrm.append(str(poi_list[pois_index]))

	string = ' '.join(pois_nrm)

	return string



def random_generator():
	while True:

		print('Generate a Random distribution(R) , a Normal distribution(N), a Bernoulli distribution(BERN), a Binomial distribution(BINO), or a Poisson distribution(P)?')

		ans = input().upper()

		if ans == 'R':

			start_val = ask_number('Please enter the start value: ')

			end_val = ask_number('Please enter the end value: ')

			num_val = ask_number('Please enter the number of distribution:')

			out_string = (random_num(start_val, end_val, num_val))

			break


		elif ans == 'N':

			mean_val = ask_number('Please enter the mean of the distribution: ')

			std_val = ask_number('Please enter the standard deviation of the distribution: ')

			num_val = ask_number('Please enter the number of distribution:')

			out_string = normal_dis_num(mean_val, std_val, num_val)
			break

		elif ans == 'B':

			out_string = binomial_dis_num()

			break


		elif ans == 'P':

			lambda_pmt = ask_number('Please enter the parameter(lambda) of the distribution: ')

			size = ask_number('Please enter the size of the distribution: ')

			out_string = poisson_dis(lambda_pmt, size)
			break

		elif ans == 'BERN':

			out_string = bern_dis_num()

			break

		else:
			print('Invalid input, please try again.')

	return out_string



def bern_dis_num():
	bern_nrm = []

	n, prob, size_dis = distri_ask_paras(n_need = False)

	bern_list = np.random.binomial(n = n, p = prob, size = size_dis)

	for pois_index in range(size_dis):
		bern_nrm.append(str(bern_list[pois_index]))

	string = ' '.join(bern_nrm)

	return string


def distri_ask_paras(n_need = True):

	if n_need:

		while True:

			n = ask_number('Please input the number of independent experiment in a set(n): ')

			if n <= 0:
				print('Input out of range! Please try again! Available range: (0-infinity)')

			else:

				break

	else:

		n = 1

	while True:

		p = ask_number('Please input the probability of succeed(p): ', float_check=True)

		test_res = test_range(p, 1, 0, 'Input out of range! Please try again! Available range: [0-1]', True, True)


		if test_res:
			break

		else:

			pass

	while True:

		size_dis = ask_number('Please input the number of experiments sets: ')

		if size_dis <= 0:
			print('Input out of range! Please try again! Available range: (0-infinity)')

		else:

			return n, p, size_dis


def json_saving(data_original):

	data_list = []

	for index in data_original:

		data_list.append(str(index))

	data = ' '.join(data_list)

	json_data = json.dumps(data)

	file_name = input('File name: ')

	save_file = open(file_name + '.json', 'w')

	save_file.write(json_data)

	save_file.close()

def json_reading(path):

	try:

		with open(path, 'r') as file:
			data = list(file.read())

			while '"' in data:

				del data[data.index('"')]

			return ''.join(data)


	except FileNotFoundError:
		print("File does not exist at: " + path)

		return False


def select_dataset(universal_set):


	while True:

		index_dst = ask_number('Which data set would you save')

		if test_range(index_dst, len(universal_set), 0 - len(universal_set), error_index_range(universal_set), True, True):
			data_needed = universal_set[index_dst]

			break

	json_saving(data_needed)
	print('Succeed')

def view_data(datasets):

	while True:

		print('Number of dataset: ' + str(len(datasets)))

		index_of_data = int(input('Please enter the dataset you want to view: '))

		try:

			dataset_needed = datasets[index_of_data]

			print('Dataset: \n' + str(dataset_needed))

			break


		except IndexError:

			print(error_index_range(datasets))

			break



def ploy_reg(x_data,y_data,n): #

	if len(x_data) != len(y_data):

		raise ValueError('The length of x input and y input is not equal.')


	coef = np.polyfit(np.array(x_data), np.array(y_data), n)


	poly = np.poly1d(coef)

	plot_x = np.linspace(min(x_data),max(x_data),1000)

	plt.plot(plot_x,poly(plot_x), color = 'red', label = 'Line of best fit')

	print('Coefficients of regression function: \n' + str(coef))



def change_data(universal_set):

	while True:
		while True:
			try:
				data_change_index = int(input('Please enter the dataset you want to modify: '))

			except ValueError:

				print('Invalid input!')

			else:

				break

		if test_range(data_change_index, len(universal_set), 0 - len(universal_set), error_index_range(universal_set), True, True):

			break

	universal_set[data_change_index] = dataset_input(universal_set)
	print('Succeed!')
	return universal_set



def dataset_input(universal_set):
	while True:
		print('Please enter values of a numerical variable, use space to split each value, enable random number generator(R) or linear generator(LN) to generate a dataset, sort a dataset(S), load data(LD): ')
		input_string = input().upper()

		if input_string == 'R':

			input_string = random_generator()

		elif input_string == 'LD':

			while True:
				file_path = list(input('Please enter the path of the file: '))

				while '"' in file_path:
					del file_path[file_path.index('"')]

				file_path = ''.join(file_path)

				try:
					input_string = json_reading(file_path)

				except OSError:

					print('Invalid path, please try again!')

				if not input_string == False:
					break


		elif input_string == 'LN':

			input_string = linear_lst()

		elif input_string == 'S':

			input_string = sort_data_input(universal_set)


		valid_characters = '1234567890. -Ee'
		if all(char in valid_characters for char in input_string):
			input_string_list = input_string.split(' ')
			try:
				input_values_list = [float(i) for i in input_string_list]
			except ValueError:
				print('Invalid input, please try again! ')
			else:
				break
		else:
			print('Invalid input, please try again! ')


	print('Your input is: ')
	print(input_values_list)
	return input_values_list





def del_dataset(universal_set):

	while True:

		while True:
			while True:
				try:
					data_change_index = int(input('Please enter the dataset you want to delete: '))

				except ValueError:
					print('Invalid input!')

				else:

					break

			if test_range(data_change_index, len(universal_set), 0 - len(universal_set),error_index_range(universal_set), True, True):
				break
		del universal_set[data_change_index]

		print('Succeed!')

		return universal_set


def main_calc_para(universal_data):

	while True:

		try:

			data_set = calc_para(universal_data[ask_number('Which data set would you like to calculate parameters')])



		except IndexError:
			print(error_index_range(universal_data)) #防止索引超限，如果超限，提醒并重新输入

		else:

			return  data_set #成功生成就跳出




def main_add_dataset(universal_data):

	new_data = dataset_input(universal_data)

	universal_data.append(new_data)
	print('Succeed')
	return universal_data



def main_single_histo_plotting(original_data):
	print('Histogram mode')

	while True:

		index_histo = ask_number('Which data set would you like to plot?')  # 直方图函数须先确定画哪个数据集

		if index_histo >= len(original_data) or index_histo < (0 - len(original_data)):
			print(error_index_range(original_data))

		else:

			histo_plotting(original_data[index_histo])

			break





def prob_coin(universal_data):

	print('Tossing coins')

	result_coin = []

	while True:

		print_res = ''

		times = prob_ask_times('tossing coins')

		if not times:
			return prob_result_out(result_coin, universal_data)


		for index_tossing in range(times):

			result_sig = random.choice([0,1])
			result_coin.append(result_sig)


		for index_printing in result_coin:

			if index_printing == 0:

				print_res += 'T'

			else:

				print_res += 'H'

		print('Result(T is tail, H is head)\n' + print_res)


def main_prob(universal_data):

	type_prob = input('Which problem do you want to simulate: \nTossing coins(TC), Rolling dice(RD), Birthday paradox(BP)\n').upper()

	match type_prob:

		case 'TC':

			result_prob = prob_coin(universal_data)

		case 'RD':

			result_prob = prob_dice(universal_data)

		case 'BP':

			result_prob = prob_birthday(universal_data)


		case _:

			result_prob = universal_data

			print('Invalid input!')

	return result_prob




def prob_dice(universal_data):
	print('Rolling dice')

	result_dice = []

	while True:


		times = prob_ask_times('rolling dice')


		if not times:
			return prob_result_out(result_dice, universal_data)

		for index_tossing in range(times):
			result_sig = random.randint(1,6)
			result_dice.append(result_sig)

		print('Result: \n' + str(result_dice))






def prob_ask_times(name_program):
	while True:

		times_str = input('You can enter "+" for ' + name_program + ', enter times of ' + name_program + ' or enter "#" to exit: ')

		try:

			times = int(times_str)

			return times

		except ValueError:

			if times_str == '+':

				times = 1

				return times

			elif times_str == '#':

				return False

			else:

				print('Invalid input!')




def prob_result_out(prob_result, universal_data):
	universal_data.append(prob_result)

	print('Result has been saved at index: ' + str(universal_data.index(prob_result)))

	return universal_data




def line_plot(x, y):

	if len(x) != len(y):

		raise ValueError

	else:

		label = input('Please enter a label for this group: \n')

		plt.plot(x, y, label = label)




def main_line_graph(universal_set):
	print('Line graph mode')

	while True:
		while True:

			while True:
				x_index = input('Please enter the index of independent dataset, or enter "#" to exit: ')

				if x_index == '#':
					x_index = True

					break

				try:
					x_index = int(x_index)

				except ValueError:

					print('Invalid input!')

				else:

					break

			if x_index and x_index != 1:

				x_data = None

				break

			try:

				x_data = universal_set[x_index]

			except IndexError:

				print(error_index_range(universal_set))

			else:

				break

		if x_index:

			break


		while True:

			while True:

				y_index = input('Please enter the index of dependent dataset: ')

				try:
					y_index = int(y_index)

				except ValueError:

					print('Invalid input!')

				else:

					break

			try:

				y_data = universal_set[y_index]

			except IndexError:

				print(error_index_range(universal_set))

			else:

				break

		try:

			line_plot(x_data,y_data)


		except ValueError:

			print('Error!')



	title = input('Please type in the title of the line graph: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')

	x_label = default_label(x_label, 'X-axis')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')

	y_label = default_label(y_label, 'Y-axis')

	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()
	plt.legend()

	plt.show()

	print('Succeed!')



def stem_plot(universal_set):

	print('Stem plot mode')

	while True:

		while True:

			x_index = input('Please enter the index of x data: ')

			try:

				x_index = int(x_index)
				x_data = universal_set[x_index]

			except ValueError:

				print('Invalid input: input is not a number!')

			except IndexError:

				print(error_index_range(universal_set))

			else:

				break

		while True:

			y_index = input('Please enter the index of y data: ')

			try:

				y_index = int(y_index)
				y_data = universal_set[y_index]

			except ValueError:

				print('Invalid input: input is not a number!')

			except IndexError:

				print(error_index_range(universal_set))

			else:

				break

		if len(x_data) != len(y_data):

			print('Error: length of x and y is not equal!')

		else:

			break

	plt.stem(x_data,y_data)

	title = input('Please type in the title of the stem plot: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')

	x_label = default_label(x_label, 'X-axis')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')

	y_label = default_label(y_label, 'Y-axis')

	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()


	plt.show()

	print('Succeed!')



def histo_2d(universal_set):
	print('2D Histogram mode')

	while True:

		while True:

			x_index = input('Please enter the index of x data: ')

			try:

				x_index = int(x_index)
				x_data = universal_set[x_index]

			except ValueError:

				print('Invalid input: input is not a number!')

			except IndexError:

				print(error_index_range(universal_set))

			else:

				break

		while True:

			y_index = input('Please enter the index of y data: ')

			try:

				y_index = int(y_index)
				y_data = universal_set[y_index]

			except ValueError:

				print('Invalid input: input is not a number!')

			except IndexError:

				print(error_index_range(universal_set))

			else:

				break

		if len(x_data) != len(y_data):

			print('Error: length of x and y is not equal!')

		else:

			break

	print('How many bins do you want, or enter nothing to enable default settings.')

	while True:

		bin_num_str = input()

		if bin_num_str == '':
			bin_num_str = str( int(1 + np.log10((len(x_data) + len(y_data)) / 2) / np.log10(2)))
		try:
			bin_number = int(bin_num_str)

		except ValueError:
			print('Invalid input, please try again! ')
		else:
			break

	plt.hist2d(x_data, y_data, bins = bin_number)

	title = input('Please type in the title of the histogram: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')

	x_label = default_label(x_label, 'X-axis')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')

	y_label = default_label(y_label, 'Y-axis')

	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()
	plt.colorbar()
	plt.show()

	print('Succeed!')




def stairs_plot(universal_set):

	print('Stair plot mode')

	while True:

		y_index = input('Please enter the index of data: ')

		try:

			y_index = int(y_index)
			y_data = universal_set[y_index]

		except ValueError:

			print('Invalid input: input is not a number!')

		except IndexError:

			print(error_index_range(universal_set))

		else:

			break


	plt.stairs(y_data)

	title = input('Please type in the title of the stairs plot: ')

	x_label = input('Please type in the label of x-axis(Enter nothing to enable default label): ')

	x_label = default_label(x_label, 'X-axis')

	y_label = input('Please type in the label of y-axis(Enter nothing to enable default label): ')

	y_label = default_label(y_label, 'Y-axis')

	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()

	plt.show()

	print('Succeed!')




def error_index_range(universal_set):

	return 'Index out of range! Please try again! Available range: (' + str(0 - len(universal_set)) + ' to ' + str(len(universal_set) - 1) + ')'


def linear_lst():

	start_val = ask_number('Please enter the start value: ', float_check=True)

	end_val = ask_number('Please enter the end value: ', float_check=True)

	step = ask_number('Please enter the number of items: ')

	line_list = list(np.linspace(start=start_val, stop=end_val, num=step))

	return_string = ''

	for index_transfer in line_list:

		return_string += (str(index_transfer) + ' ')

	return_string = return_string[:-1]

	return return_string

def prob_birthday(universal_set):

	print('Birthday paradox')

	result_brh = []

	while True:

		times = prob_ask_times('add friend')

		if not times:
			return prob_result_out(result_brh, universal_set)

		for index_day in range(times):
			result_sig = random.randint(1, 365)
			result_brh.append(result_sig)

		check_same_day = {}

		for index_check in range(1,366):

			num_same_day = result_brh.count(index_check)

			if num_same_day >= 2:

				check_same_day[index_check] = num_same_day


		if len(check_same_day) == 0:

			print('No one has same birthday with others.')

		else:


			printing_string = ''

			for index_print in check_same_day.keys():

				printing_string += ' ' + str(check_same_day[index_print]) + ' of your friends have birthday at day ' + str(index_print) + ','

			printing_string = printing_string[1:-1]


			print(printing_string)

			print('Here are the details: \n' +str(result_brh) + '\nNumber of your friends: ' + str(len(result_brh)))



def sort_data_input(universal_set):



	while True:
		while True:
			try:
				data_sort_index = int(input('Please enter the dataset you want to sort: '))

			except ValueError:
				print('Invalid input!')

			else:

				break

		if test_range(data_sort_index, len(universal_set), 0 - len(universal_set),error_index_range(universal_set), True, True):
			break


	new_data = universal_set[data_sort_index]

	new_data.sort()


	output_string = ''

	for index_str in new_data:

		output_string += str(index_str) + ' '

	return output_string[:-1]



def main():




	ini_func() #初始化


	plt.rcParams['figure.figsize'] = [10, 8]

	original_data = input_func() #输入数据




	while True: #主程序




		print('Do you want: \nCalculate parameters(P)\nBivariate Chart: a Scatter plot(SC), a Multi-data histogram(M), a Box-plot(B), a Line graph(L), a Stem plot(ST), a 2D-histogram(2DH)\nUni-variate: Chart a Dot plot(D), a scatter plot(Frequency)(F), Histogram(H), a Cumulative relative frequency graph(C), a density curve(DC) or a Stairs plot(STP)? \nOr you can enter "ADD" to add a dataset, "DATA" to view a dataset,"MOD" to modify dataset,"DEL" to delete a dataset or "SAV" to save a dataset.\nEnter "Prob" to enable probability simulator\nEnter "#" to exit.')

		type_of_chart = input().upper()


		match type_of_chart:




			case 'H': #直方图

				main_single_histo_plotting(original_data)
			

			case 'SC': #散点图

				scatter_plt(original_data)


			case 'B': #箱线图


				box_plotting(original_data)

			case 'M': #多数据集直方图

				multi_histo_plotting(original_data)


			case 'C': #堆积百分比图

				cum_rel_frequency_g(original_data)


			case 'F': #频率散点图

				fre_sct(original_data)


			case 'D': #点状图

				dot(original_data)


			case 'DC': #密度图

				dst_plt(original_data)


			case 'SAV':

				select_dataset(original_data)


			case 'DATA':

				view_data(original_data)


			case 'MOD':

				original_data = change_data(original_data)


			case 'DEL':

				original_data = del_dataset(original_data)


			case 'P':

				main_calc_para(original_data)


			case 'ADD':

				original_data = main_add_dataset(original_data)

			case 'PROB':

				original_data = main_prob(original_data)


			case 'L':

				main_line_graph(original_data)

			case 'ST':

				stem_plot(original_data)

			case 'STP':

				stairs_plot(original_data)

			case '2DH':

				histo_2d(original_data)



			case '#': #触发退出


				exit_func()


			case _:
				print('Invalid input, please try again.') #要用While True: 主要考量是防止输错参数直接退出





main()




#数据可以在最后一行临时暂存：[]
