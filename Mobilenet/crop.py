#import cv2
import json
import csv
final = "/media/srinath/Major Project/Major/00/"
personsavepath = "/media/srinath/Major Project/Major/newdata/person/"
carsavepath = "/media/srinath/Major Project/Major/newdata/car/"
trucksavepath = "/media/srinath/Major Project/Major/newdata/truck/"
vansavepath = "/media/srinath/Major Project/Major/newdata/van/"
autosavepath = "/media/srinath/Major Project/Major/newdata/auto/"
twowheelersavepath = "/media/srinath/Major Project/Major/newdata/twowheeler/"
dontcaresavepath = "/media/srinath/Major Project/Major/newdata/dontcare/"
#img = cv2.imread("/media/srinath/Major Project/Major/00/0000.png")
#cv2.imshow("1",img)
F = open('/media/srinath/Major Project/Major/voc.txt','w+')
with open('00.json','r') as f:
	dictonary = json.load(f)
	#print(dictonary[0]['External ID'])

	for i in range(1195):
		image = (dictonary[i]['External ID'])
		label = dictonary[i]['Label']
		keys = label.keys()
		print(len(keys))
		print(keys[0])
		personnumber = 0
		Carnumber = 0
		Trucknumber = 0
		Vannumber = 0
		autonumber = 0
		twowheelernumber = 0
		dcnumber = 0
		k = 0
		j = 0
		width = 0
		height = 0
		for j in range(len(keys)):	
			if (keys[j] == 'Person'):
				personnumber = len(label['Person'])
				for k in range (personnumber):
					coordinates = label['Person'][k]['geometry']
					#print(coordinates)
					height = abs(label['Person'][k]['geometry'][0]['x'] - label['Person'][k]['geometry'][2]['x'])
					width = abs(label['Person'][k]['geometry'][0]['y'] - label['Person'][k]['geometry'][2]['y'])
					print(width, height)
					if(label['Person'][k]['geometry'][0]['x'] < label['Person'][k]['geometry'][2]['x']):
						x = (label['Person'][k]['geometry'][0]['x'])
					else:
						x = (label['Person'][k]['geometry'][2]['x'])
					if(label['Person'][k]['geometry'][0]['y'] < label['Person'][k]['geometry'][2]['y']):
						y = label['Person'][k]['geometry'][0]['y']
						print(type(y))
					else:
						y = label['Person'][k]['geometry'][2]['y']
						print(type(y))
					final_image = final + image
					print(final_image)
					# img = cv2.imread(final_image)
					# cro_img = img[y:y+width, x:x+height]
					# cv2.imwrite(personsavepath + str(image[0:4]) + "_" +  "%06i.jpg"%k , cro_img)
					#print(final_image, x, x+height, y, y+height, 0)
					F.write(final_image)
					F.write(" ")
					F.write(str(x))
					F.write(" ")
					F.write(str(x+height))
					F.write(" ")
					F.write(str(y))
					F.write(" ")
					F.write(str(y+height))
					F.write(" ")
					F.write('0')
					F.write('\n')
					#cv2.imshow("temp",cro_img)
					#cv2.waitKey(0)
				continue


			if (keys[j] == 'Car'):
				Carnumber = len(label['Car'])
				for k in range (Carnumber):
					coordinates = label['Car'][k]['geometry']
					#print(coordinates)
					height = abs(label['Car'][k]['geometry'][0]['x'] - label['Car'][k]['geometry'][2]['x'])
					width = abs(label['Car'][k]['geometry'][0]['y'] - label['Car'][k]['geometry'][2]['y'])
					print(width, height)
					if(label['Car'][k]['geometry'][0]['x'] < label['Car'][k]['geometry'][2]['x']):
						x = (label['Car'][k]['geometry'][0]['x'])
					else:
						x = (label['Car'][k]['geometry'][2]['x'])
					if(label['Car'][k]['geometry'][0]['y'] < label['Car'][k]['geometry'][2]['y']):
						y = label['Car'][k]['geometry'][0]['y']
						print(type(y))
					else:
						y = label['Car'][k]['geometry'][2]['y']
						print(type(y))
					final_image = final + image
					print(final_image)
					F.write(final_image)
					F.write(" ")
					F.write(str(x))
					F.write(" ")
					F.write(str(x+height))
					F.write(" ")
					F.write(str(y))
					F.write(" ")
					F.write(str(y+height))
					F.write(" ")
					F.write('1')
					F.write('\n')
					# img = cv2.imread(final_image)
					# cro_img = img[y:y+width, x:x+height]
					# cv2.imwrite(carsavepath + str(image[0:4]) + "_" +  "%06i.jpg"%k , cro_img)
					#cv2.imshow("temp",cro_img)
					#cv2.waitKey(0)
				continue


			if (keys[j] == 'Truck'):
				Trucknumber = len(label['Truck'])
				for k in range (Trucknumber):
					coordinates = label['Truck'][k]['geometry']
					#print(coordinates)
					height = abs(label['Truck'][k]['geometry'][0]['x'] - label['Truck'][k]['geometry'][2]['x'])
					width = abs(label['Truck'][k]['geometry'][0]['y'] - label['Truck'][k]['geometry'][2]['y'])
					print(width, height)
					if(label['Truck'][k]['geometry'][0]['x'] < label['Truck'][k]['geometry'][2]['x']):
						x = (label['Truck'][k]['geometry'][0]['x'])
					else:
						x = (label['Truck'][k]['geometry'][2]['x'])
					if(label['Truck'][k]['geometry'][0]['y'] < label['Truck'][k]['geometry'][2]['y']):
						y = label['Truck'][k]['geometry'][0]['y']
						print(type(y))
					else:
						y = label['Truck'][k]['geometry'][2]['y']
						print(type(y))
					final_image = final + image
					print(final_image)
					F.write(final_image)
					F.write(" ")
					F.write(str(x))
					F.write(" ")
					F.write(str(x+height))
					F.write(" ")
					F.write(str(y))
					F.write(" ")
					F.write(str(y+height))
					F.write(" ")
					F.write('2')
					F.write('\n')
					# img = cv2.imread(final_image)
					# cro_img = img[y:y+width, x:x+height]
					# cv2.imwrite(trucksavepath + str(image[0:4]) + "_" +  "%06i.jpg"%k , cro_img)
				continue


			if (keys[j] == 'Van'):
				Vannumber = len(label['Van'])
				for k in range (Vannumber):
					coordinates = label['Van'][k]['geometry']
					#print(coordinates)
					height = abs(label['Van'][k]['geometry'][0]['x'] - label['Van'][k]['geometry'][2]['x'])
					width = abs(label['Van'][k]['geometry'][0]['y'] - label['Van'][k]['geometry'][2]['y'])
					print(width, height)
					if(label['Van'][k]['geometry'][0]['x'] < label['Van'][k]['geometry'][2]['x']):
						x = (label['Van'][k]['geometry'][0]['x'])
					else:
						x = (label['Van'][k]['geometry'][2]['x'])
					if(label['Van'][k]['geometry'][0]['y'] < label['Van'][k]['geometry'][2]['y']):
						y = label['Van'][k]['geometry'][0]['y']
						print(type(y))
					else:
						y = label['Van'][k]['geometry'][2]['y']
						print(type(y))
					final_image = final + image
					print(final_image)
					F.write(final_image)
					F.write(" ")
					F.write(str(x))
					F.write(" ")
					F.write(str(x+height))
					F.write(" ")
					F.write(str(y))
					F.write(" ")
					F.write(str(y+height))
					F.write(" ")
					F.write('3')
					F.write('\n')
					# img = cv2.imread(final_image)
					# cro_img = img[y:y+width, x:x+height]
					# cv2.imwrite(vansavepath + str(image[0:4]) + "_" +  "%06i.jpg"%k , cro_img)
				continue


			if (keys[j] == 'Auto rickshaw'):
				autonumber = len(label['Auto rickshaw'])
				for k in range (autonumber):
					coordinates = label['Auto rickshaw'][k]['geometry']
					#print(coordinates)
					height = abs(label['Auto rickshaw'][k]['geometry'][0]['x'] - label['Auto rickshaw'][k]['geometry'][2]['x'])
					width = abs(label['Auto rickshaw'][k]['geometry'][0]['y'] - label['Auto rickshaw'][k]['geometry'][2]['y'])
					print(width, height)
					if(label['Auto rickshaw'][k]['geometry'][0]['x'] < label['Auto rickshaw'][k]['geometry'][2]['x']):
						x = (label['Auto rickshaw'][k]['geometry'][0]['x'])
					else:
						x = (label['Auto rickshaw'][k]['geometry'][2]['x'])
					if(label['Auto rickshaw'][k]['geometry'][0]['y'] < label['Auto rickshaw'][k]['geometry'][2]['y']):
						y = label['Auto rickshaw'][k]['geometry'][0]['y']
						print(type(y))
					else:
						y = label['Auto rickshaw'][k]['geometry'][2]['y']
						print(type(y))
					final_image = final + image
					print(final_image)
					F.write(final_image)
					F.write(" ")
					F.write(str(x))
					F.write(" ")
					F.write(str(x+height))
					F.write(" ")
					F.write(str(y))
					F.write(" ")
					F.write(str(y+height))
					F.write(" ")
					F.write('4')
					F.write('\n')
					# img = cv2.imread(final_image)
					# cro_img = img[y:y+width, x:x+height]
					# cv2.imwrite(autosavepath + str(image[0:4]) + "_" +  "%06i.jpg"%k , cro_img)
				continue


			if (keys[j] == 'Two wheeler'):
				twowheelernumber = len(label['Two wheeler'])
				for k in range (twowheelernumber):
					coordinates = label['Two wheeler'][k]['geometry']
					#print(coordinates)
					height = abs(label['Two wheeler'][k]['geometry'][0]['x'] - label['Two wheeler'][k]['geometry'][2]['x'])
					width = abs(label['Two wheeler'][k]['geometry'][0]['y'] - label['Two wheeler'][k]['geometry'][2]['y'])
					print(width, height)
					if(label['Two wheeler'][k]['geometry'][0]['x'] < label['Two wheeler'][k]['geometry'][2]['x']):
						x = (label['Two wheeler'][k]['geometry'][0]['x'])
					else:
						x = (label['Two wheeler'][k]['geometry'][2]['x'])
					if(label['Two wheeler'][k]['geometry'][0]['y'] < label['Two wheeler'][k]['geometry'][2]['y']):
						y = label['Two wheeler'][k]['geometry'][0]['y']
						print(type(y))
					else:
						y = label['Two wheeler'][k]['geometry'][2]['y']
						print(type(y))
					final_image = final + image
					print(final_image)
					F.write(final_image)
					F.write(" ")
					F.write(str(x))
					F.write(" ")
					F.write(str(x+height))
					F.write(" ")
					F.write(str(y))
					F.write(" ")
					F.write(str(y+height))
					F.write(" ")
					F.write('5')
					F.write('\n')
					# img = cv2.imread(final_image)
					# cro_img = img[y:y+width, x:x+height]
					# cv2.imwrite(twowheelersavepath + str(image[0:4]) + "_" +  "%06i.jpg"%k , cro_img)
				continue


			# if (keys[j] == 'Dont care'):
			# 	dcnumber = len(label['Dont care'])
			# 	for k in range (dcnumber):
			# 		coordinates = label['Dont care'][k]['geometry']
			# 		#print(coordinates)
			# 		height = abs(label['Dont care'][k]['geometry'][0]['x'] - label['Dont care'][k]['geometry'][2]['x'])
			# 		width = abs(label['Dont care'][k]['geometry'][0]['y'] - label['Dont care'][k]['geometry'][2]['y'])
			# 		print(width, height)
			# 		if(label['Dont care'][k]['geometry'][0]['x'] < label['Dont care'][k]['geometry'][2]['x']):
			# 			x = (label['Dont care'][k]['geometry'][0]['x'])
			# 		else:
			# 			x = (label['Dont care'][k]['geometry'][2]['x'])
			# 		if(label['Dont care'][k]['geometry'][0]['y'] < label['Dont care'][k]['geometry'][2]['y']):
			# 			y = label['Dont care'][k]['geometry'][0]['y']
			# 			print(type(y))
			# 		else:
			# 			y = label['Dont care'][k]['geometry'][2]['y']
			# 			print(type(y))
			# 		final_image = final + image
			# 		print(final_image)
			# 		F.write(final_image)
			# 		F.write(" ")
			# 		F.write(str(x))
			# 		F.write(" ")
			# 		F.write(str(x+height))
			# 		F.write(" ")
			# 		F.write(str(y))
			# 		F.write(" ")
			# 		F.write(str(y+height))
			# 		F.write(" ")
			# 		F.write('6')
			# 		F.write('\n')
			# 		# img = cv2.imread(final_image)
			# 		# cro_img = img[y:y+width, x:x+height]
			# 		# cv2.imwrite(dontcaresavepath + str(image[0:4]) + "_" +  "%06i.jpg"%k , cro_img)
			# 	continue
		print(personnumber,Carnumber,Trucknumber,dcnumber,Vannumber,twowheelernumber,autonumber,image)
	
F.close()













		#personnumber = len(label['Person'])

		 
		#print(label['Person'][0]['geometry'])
		# if(label['Person']):
		# 	print("person")
		# 	print(i)
		# else:
		# 	continue
		# elif(label['Car']):
		# 	print("car")
		# 	print(i)
		# elif(label['Two wheeler']):
		# 	print("tw")
		# 	print(i)
		# elif(label['Auto rickshaw']):
		# 	print("ar",i)
		# elif(label['Van']):
		# 	print("van",i)
		# elif(label['Truck']):
		# 	print("truck",i)
		# elif(label['Dont care']):
		# 	print("dc",i)
		

		#print(label)
		#final_image = final + image
		#print(final_image)
		#img = cv2.imread(final_image)

		#cv2.imshow("temp",img)
		#cv2.waitKey(0)




























# for dic in dictonary:
# 	print(dic['External ID'])
# 	imagelist =  dic['External ID']
	



#print(imagelist[0:8])

	# converted = str(dic['External ID'])
	# print(type(converted))
	# print(type(dic['External ID']))
	# for image in dic['External ID']:
	# 	print(image)
	# 	final_image = final + image
	# 	print(final_image)
	# 	img = cv2.imread(final_image)
	# 	cv2.imshow("temp",img)
	# 	cv2.waitKey(0)








# img = cv2.imread("1.jpeg")
# crop_img = img[0:0+50, 0:100]
# cv2.imshow("cropped", crop_img)
# cv2.imwrite("edited.jpeg",crop_img)
# cv2.waitKey(0)

































#with open('1.csv') as csv_file:
# 	csv_reader = csv.DictReader(csv_file, delimiter = ',')
# 	print(csv_reader.join(row))