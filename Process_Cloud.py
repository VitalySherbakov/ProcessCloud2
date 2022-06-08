import os, sys, json
from google.colab import files

current_dir = os.getcwd()
current_dir = current_dir.replace("\\","//")
#print(f"D: {current_dir}")

class WIFI_Init(object):
	DirHomeHC22000=""
	DirHomeDicts=""
	DirGoogleDisk=""
	DirWIFI=[]
	Speed=1
	One=7
	Two=12
	GoogleDisk1=[]
	GoogleDisk2=[]
	GoogleDisk3=[]
	DictsProces=[]
	DataJson=""
	DataJson2=""
	def __init__(self, filesetting ,wifidecode , FlagRead=True, encode="utf-8"):
		super(WIFI_Init, self).__init__()
		if FlagRead:
			with open(wifidecode, "rt", encoding=encode) as f:
				self.DataJson=json.loads(f.read())
				self.DirHomeHC22000=self.DataJson['DirHomeHC22000']
				self.DirHomeDicts=self.DataJson['DirHomeDicts']
				self.DirGoogleDisk=self.DataJson['DirGoogleDisk']
				self.Speed=self.DataJson['Speed']
				for i in self.DataJson['DirWIFI']:
					self.DirWIFI.append(i)
			with open(filesetting, "rt", encoding=encode) as f2:
				self.DataJson2=json.loads(f2.read())
				self.One=self.DataJson2['One']
				self.Two=self.DataJson2['Two']
				for i in self.DataJson2['GoogleDisk1']:
					self.GoogleDisk1.append(i)
				for i in self.DataJson2['GoogleDisk2']:
					self.GoogleDisk2.append(i)
				for i in self.DataJson2['GoogleDisk3']:
					self.GoogleDisk3.append(i)
				for i in self.DataJson2['DictsProces']:
					self.DictsProces.append(i)
		else:
			self.DataJson=json.loads(wifidecode)
			self.DirHomeHC22000=self.DataJson['DirHomeHC22000']
			self.DirHomeDicts=self.DataJson['DirHomeDicts']
			self.DirGoogleDisk=self.DataJson['DirGoogleDisk']
			self.Speed=self.DataJson['Speed']
			self.DataJson2=json.loads(filesetting)
			self.One=self.DataJson2['One']
			self.Two=self.DataJson2['Two']
			for i in self.DataJson2['GoogleDisk1']:
				self.GoogleDisk1.append(i)
			for i in self.DataJson2['GoogleDisk2']:
				self.GoogleDisk2.append(i)
			for i in self.DataJson2['GoogleDisk3']:
				self.GoogleDisk3.append(i)
			for i in self.DataJson2['DictsProces']:
				self.DictsProces.append(i)					


class WIFI_MASK:
	FileHC22000=""
	Mask="?a?a?a?a?a?a?a?a"
	Speed=1
	Minimum=8
	Maximum=12
	FlagMinMax=False


class WIFI_Cloud:
	"""WIFI Cloud"""
	def LibInit(github="https://github.com/VitalySherbakov/hashcat.git"):
		"""Иницилизациия Библиотек"""
		com=f"install cmake build-essential -y && apt install checkinstall git -y && git clone {github} && cd hashcat && git submodule update --init && make && make install && pip install unrar"
		return com
	def DirInit(dir_hc):
		"""Иницилизация создание необходимых директорий"""
		dir_home=f"{current_dir}//{dir_hc.DirHomeHC22000}"
		dir_dicts=f"{current_dir}//{dir_hc.DirHomeDicts}"
		WIFI_Cloud.CreatDir(dir_home)
		WIFI_Cloud.CreatDir(dir_dicts)
		for li in dir_hc.DirWIFI:
 			dir_new=f"{current_dir}//{dir_hc.DirHomeHC22000}//{li}"
 			WIFI_Cloud.CreatDir(dir_new)
	def GoogleDisk1_ZIP_Extract(dir_hc):
		"""Распаковка Первого Пакета Словарей zip"""
		command=""
		for i,li in enumerate(dir_hc.GoogleDisk1):
			if(i==0):
				command+=f"{dir_hc.DirGoogleDisk}/{li}.zip -d {dir_hc.DirHomeDicts} && "
			if(i>0 and i<len(dir_hc.GoogleDisk1)-1):
				command+=f"unzip {dir_hc.DirGoogleDisk}/{li}.zip -d {dir_hc.DirHomeDicts} && "
			if(i==len(dir_hc.GoogleDisk1)-1):
				command+=f"unzip {dir_hc.DirGoogleDisk}/{li}.zip -d {dir_hc.DirHomeDicts}"
		return command
	def GoogleDisk2_ZIP_Extract(dir_hc):
		"""Распаковка Второй Пакета Словарей zip"""
		command=""
		for i,li in enumerate(dir_hc.GoogleDisk2):
			if(i==0):
				command+=f"{dir_hc.DirGoogleDisk}/{li}.zip -d {dir_hc.DirHomeDicts} && "
			if(i>0 and i<len(dir_hc.GoogleDisk2)-1):
				command+=f"unzip {dir_hc.DirGoogleDisk}/{li}.zip -d {dir_hc.DirHomeDicts} && "
			if(i==len(dir_hc.GoogleDisk2)-1):
				command+=f"unzip {dir_hc.DirGoogleDisk}/{li}.zip -d {dir_hc.DirHomeDicts}"
		return command
	def GoogleDisk3_ZIP_Extract(dir_hc):
		"""Распаковка Третий Пакета Словарей zip"""
		command=""
		for i,li in enumerate(dir_hc.GoogleDisk3):
			if(i==0):
				command+=f"{dir_hc.DirGoogleDisk}/{li}.zip -d {dir_hc.DirHomeDicts} && "
			if(i>0 and i<len(dir_hc.GoogleDisk3)-1):
				command+=f"unzip {dir_hc.DirGoogleDisk}/{li}.zip -d {dir_hc.DirHomeDicts} && "
			if(i==len(dir_hc.GoogleDisk3)-1):
				command+=f"unzip {dir_hc.DirGoogleDisk}/{li}.zip -d {dir_hc.DirHomeDicts}"
		return command
	def GoogleDisk1_RAR_Extract(dir_hc):
		"""Распаковка Первого Пакета Словарей rar"""
		command=""
		for i,li in enumerate(dir_hc.GoogleDisk1):
			if(i==0):
				command+=f"{dir_hc.DirGoogleDisk}/{li}.rar x {dir_hc.DirHomeDicts} && "
			if(i>0 and i<len(dir_hc.GoogleDisk1)-1):
				command+=f"unrar {dir_hc.DirGoogleDisk}/{li}.rar x {dir_hc.DirHomeDicts} && "
			if(i==len(dir_hc.GoogleDisk1)-1):
				command+=f"unrar {dir_hc.DirGoogleDisk}/{li}.rar x {dir_hc.DirHomeDicts}"
		return command
	def GoogleDisk2_RAR_Extract(dir_hc):
		"""Распаковка Второй Пакета Словарей rar"""
		command=""
		for i,li in enumerate(dir_hc.GoogleDisk2):
			if(i==0):
				command+=f"{dir_hc.DirGoogleDisk}/{li}.rar x {dir_hc.DirHomeDicts} && "
			if(i>0 and i<len(dir_hc.GoogleDisk2)-1):
				command+=f"unrar {dir_hc.DirGoogleDisk}/{li}.rar x {dir_hc.DirHomeDicts} && "
			if(i==len(dir_hc.GoogleDisk2)-1):
				command+=f"unrar {dir_hc.DirGoogleDisk}/{li}.rar x {dir_hc.DirHomeDicts}"
		return command
	def GoogleDisk3_RAR_Extract(dir_hc):
		"""Распаковка Третий Пакета Словарей rar"""
		command=""
		for i,li in enumerate(dir_hc.GoogleDisk3):
			if(i==0):
				command+=f"{dir_hc.DirGoogleDisk}/{li}.rar x {dir_hc.DirHomeDicts} && "
			if(i>0 and i<len(dir_hc.GoogleDisk3)-1):
				command+=f"unrar {dir_hc.DirGoogleDisk}/{li}.rar x {dir_hc.DirHomeDicts} && "
			if(i==len(dir_hc.GoogleDisk3)-1):
				command+=f"unrar {dir_hc.DirGoogleDisk}/{li}.rar x {dir_hc.DirHomeDicts}"
		return command
	def CreatDir(dirnew):
		"""Создать Директорию"""
		if os.path.exists(dirnew)==False:
			os.mkdir(dirnew)
	def GenerateHASH_ZIP(filehash, filename):
		"""Генератор Хеша !cat"""
		return f"{filehash} | grep -E -o '(\\$pkzip2\\$.*\\$/pkzip2\\$)|(\\$zip2\\$.*\\$/zip2\\$)' > {filename}.hash"
	def GenerateHASH_RAR(filehash, filename):
		"""Генератор Хеша !cat"""
		return f"{filehash} | grep -E -o '(\\$RAR3\\$[^:]+)|(\\$rar5\\$.*)' > {filename}.hash"
	def RunProcessZIP(filehash,mask,speed=1):
		"""Запуск на поиск пароля ZIP !hashcat"""
		return f"-w {speed} -m 13600 -a3 {filehash} {mask}"
	def RunProcessRAR(filehash,mask,speed=1):
		"""Запуск на поиск пароля RAR !hashcat"""
		return f"-w {speed} -m 13000 -a3 {filehash} {mask}"
	def FormatFile(filepath: str):
		"""Формат Файла"""
		formatfile=os.path.basename(filepath)
		formatfileres=os.path.splitext(formatfile)[1]
		formatfileres=formatfileres.replace(".","")
		return formatfileres
	def UploadedFile(dirhomeHC22000: str,wifidir: str):
		"""Загрузка Файла в Cloud"""
		uploaded = files.upload()
		for k, v in uploaded.items():
		  open(k, 'wb').write(v)
		filestr=list(uploaded.keys())[0]
		os.rename(filestr,f"{dirhomeHC22000}/{wifidir}/{filestr}")
		return filestr
	def HelpMask():
		"""Инфа по Маске"""
		text=""
		telin=["? | Charset",
		"===+=========",
		"l | abcdefghijklmnopqrstuvwxyz [a-z]",
		"u | ABCDEFGHIJKLMNOPQRSTUVWXYZ [A-Z]",
		"d | 0123456789                 [0-9]",
		"h | 0123456789abcdef           [0-9a-f]",
		"H | 0123456789ABCDEF           [0-9A-F]",
		"s |  !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",
		"a | ?l?u?d?s",
		"b | 0x00 - 0xff"]
		for li in telin:
			text+=f"{li}\n";
		print(text)
	def CreateProcessDict(filedict):
		"""Создание Словаря"""
		if(wifihc.FlagMinMax):
			return f"--stdout -a3 -i --increment-min={wifihc.Minimum} --increment-max={wifihc.Maximum} {wifihc.Mask} > {filedict}"
		else:
			return f"--stdout -a3 {wifihc.Mask} > {filedict}"
	def RunProcessMaskDict(filedict,wifihc):
		"""Запуск Процеса Перебора WIFI по Созданому Словарю"""
		return f"-m 22000 -a3 -w {wifihc.Speed} {wifihc.FileHC22000} {filedict}"
	def RunProcessMask(wifihc):
		"""Запуск Процеса Перебора WIFI с Маской !hashcat"""
		if(wifihc.FlagMinMax):
			return f"--stdout -a3 -i --increment-min={wifihc.Minimum} --increment-max={wifihc.Maximum} {wifihc.Mask} > tmp.txt && hashcat -m 22000 -a3 -w {wifihc.Speed} {wifihc.FileHC22000} tmp.txt && rm -rf tmp.txt"
		else:
			return f"--stdout -a3 {wifihc.Mask} > tmp.txt && hashcat -m 22000 -a3 -w {wifihc.Speed} {wifihc.FileHC22000} tmp.txt && rm -rf tmp.txt"
	def CatDirToDict(dir_cat, link_dicts):
	 """Склеивание Путей Директори"""
	 link_dicts_new=""
	 mass=link_dicts.split(' ')
	 for i,li in enumerate(mass):      
	    if(i<len(mass)):
		    link_dicts_new+=f"{dir_cat}/{li} "
	    if(i==len(mass)):
	      link_dicts_new+=f"{dir_cat}/{li}"
	 return link_dicts_new
	def RunProcess(dir_hc):
	 	"""Запуск Процеса Перебора WIFI !hashcat"""
	 	#-------------------Иницилизация---------------------
	 	selectfilespath,dir_wifi,one_string_dicts="","",""
	 	url_convert="https://hashcat.net/cap2hashcat/"
	 	#Словари Папка
	 	try:
	 		filesdicts = os.listdir(dir_hc.DirHomeDicts)
	 		print(f"--------Словари {dir_hc.DirHomeDicts}-------")
	 		for i,li in enumerate(filesdicts):
	 			print(f"Номер: {i}|Словарь: {li}")
	 		print(f"-------Захваты {dir_hc.DirHomeHC22000}--------")
	 		wifidir=input("WIFI: ")
	 		WIFI_Cloud.CreatDir(f"{current_dir}/{dir_hc.DirHomeHC22000}/{wifidir}")
	 		WIFI_Cloud.UploadedFile(f"{current_dir}/{dir_hc.DirHomeHC22000}", wifidir)
	 		dirs = os.listdir(dir_hc.DirHomeHC22000)
	 		for i,li in enumerate(dirs):
	 			print(f"Номер: {i}|Папка: {li}")
	 		print("---------------")
	 		#-------Этапы 3--------
	 		three_mass=["","",""]
	 		for i,di in enumerate(dir_hc.DictsProces):
	 			if(i<dir_hc.One):
	 				di=WIFI_Cloud.CatDirToDict(dir_hc.DirHomeDicts,di)
	 				three_mass[0]+=f"{di} "
	 			if(i==dir_hc.One):
	 				di=WIFI_Cloud.CatDirToDict(dir_hc.DirHomeDicts,di)
	 				three_mass[0]+=f"{di}"
	 			if(i>dir_hc.One and i<dir_hc.Two):
	 				di=WIFI_Cloud.CatDirToDict(dir_hc.DirHomeDicts,di)
	 				three_mass[1]+=f"{di} "
	 			if(i>dir_hc.One and i==dir_hc.Two):
	 				di=WIFI_Cloud.CatDirToDict(dir_hc.DirHomeDicts,di)
	 				three_mass[1]+=f"{di}"
	 			if(i>dir_hc.Two and i<len(dir_hc.DictsProces)-1):
	 				di=WIFI_Cloud.CatDirToDict(dir_hc.DirHomeDicts,di)
	 				three_mass[2]+=f"{di} "
	 			if(i==len(dir_hc.DictsProces)-1):
	 				di=WIFI_Cloud.CatDirToDict(dir_hc.DirHomeDicts,di)
	 				three_mass[2]+=f"{di}"
	 		#-------Этапы Единий-----
	 		for i,di in enumerate(dir_hc.DictsProces):
	 			if(i<len(dir_hc.DictsProces)-1):
	 				di=WIFI_Cloud.CatDirToDict(dir_hc.DirHomeDicts,di)
	 				one_string_dicts+=f"{di} "
	 			if(i==len(dir_hc.DictsProces)-1):
	 				di=WIFI_Cloud.CatDirToDict(dir_hc.DirHomeDicts,di)
	 				one_string_dicts+=f"{di}"
	 		#----------------------------------------------------
	 		indexspeed=dir_hc.Speed
	 		if (indexspeed>3):
	 			print(f"Вы выбрали Скорость {indexspeed} за приделы 1-3, по умолчанию выставлено 1")
	 			indexspeed=1
	 		selectdir=input("Укажы Номер Папки с Файлом *.hc22000: ")
	 		indexdir=int(selectdir)
	 		for i,li in enumerate(dirs):
	 			if(indexdir==i):
	 				dir_wifi=li
	 				pathdir=f"{dir_hc.DirHomeHC22000}/{li}"
	 				files=os.listdir(pathdir)
	 				if len(files)>0:
	 					selectfilespath=f"{pathdir}/{files[0]}"
	 				else:
	 					print(f"Нету Сконвентированого файла {url_convert} из формата *.cap в *.hc22000")
	 					sys.exit()
	 		print(f"Файл Перебора: {selectfilespath}")
	 		print(f"-----------------Выбор Метода 1-Полный 2-Тройной 3-Кусками-----------------")
	 		etap_select=input("Выбор Метода: ")
	 		index_etap_select=int(etap_select)
	 		if index_etap_select<4:
	 			if(index_etap_select==1):
	 				#Единый Процес в Одном
	 				print(f"---------------Единый Процес в Одном (Полный Этап)---------------")
	 				print(f"Скорость-{dir_hc.Speed}")
	 				print(f"Папка Сеть WIFI: {dir_wifi}")
	 				print(f"Файл WIFI: {selectfilespath}")
	 				input(f"Запустить Процес........................")
	 				return f"hashcat -m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {one_string_dicts}"
	 			if(index_etap_select==2):
	 				pod_etap_select=input("Выбрать 1-3 Этапов: ")
	 				index_pod_etap_select=int(pod_etap_select)
	 				if(index_pod_etap_select<4):
	 					print(f"---------------Этапов 3---------------")
	 					print(f"Скорость-{dir_hc.Speed}")
	 					print(f"Папка Сеть WIFI: {dir_wifi}")
	 					print(f"Файл WIFI: {selectfilespath}")
	 					if(index_pod_etap_select==1):
	 						input(f"Запустить Этап ({index_pod_etap_select}) Процес........................")
	 						return f"-m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {three_mass[0]}"
	 					if(index_pod_etap_select==2):
	 						input(f"Запустить Этап ({index_pod_etap_select}) Процес........................")
	 						return f"-m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {three_mass[1]}"
	 					if(index_pod_etap_select==3):
	 						input(f"Запустить Этап ({index_pod_etap_select}) Процес........................")
	 						return f"-m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {three_mass[2]}"
	 			if(index_etap_select==3):
	 				print(f"---------------Процес Кусками---------------")
	 				print(f"Скорость-{dir_hc.Speed}")
	 				print(f"Папка Сеть WIFI: {dir_wifi}")
	 				print(f"Файл WIFI: {selectfilespath}")
	 				for i3,li3 in enumerate(dir_hc.DictsProces):
	 					print(f"Номер {i3+1} Этапа | {li3}")
	 				pod_etap_select2=input(f"Выбрать 1-{len(dir_hc.DictsProces)} Этапов: ")
	 				index_pod_etap_select2=int(pod_etap_select2)
	 				if (index_pod_etap_select2<len(dir_hc.DictsProces)):
	 					for i2,li2 in enumerate(dir_hc.DictsProces):
	 						if ((i2+1)==index_pod_etap_select2):
	 							input(f"Запустить Этап ({index_pod_etap_select2}) Процес........................")
	 							return f"-m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {dir_hc.DirHomeDicts}/{dir_hc.DictsProces[i2]}"
	 				else:
	 					print(f"Вы выбрали {index_pod_etap_select2}, за границы доступности {len(dir_hc.DictsProces)}")
	 		else:
	 			print(f"Вы выбрали {index_etap_select} Метод вышло за приделы 1-3")
	 	except Exception as ex:
 			print(f"ERROR: {ex}!")




# 							input(f"Запустить Этап ({index_pod_etap_select}) Процес........................")
# 							return f"-m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {three_mass[2]}"
# 				if(index_etap_select==3):
# 					print(f"---------------Процес Кусками---------------")
# 					print(f"Скорость-{dir_hc.Speed}")
# 					print(f"Папка Сеть WIFI: {dir_wifi}")
# 					print(f"Файл WIFI: {selectfilespath}")
# 					for i3,li3 in enumerate(dir_hc.DictsProces):
# 						print(f"Номер {i3+1} Этапа | {li3}")
# 					pod_etap_select2=input(f"Выбрать 1-{len(dir_hc.DictsProces)} Этапов: ")
# 					index_pod_etap_select2=int(pod_etap_select2)
# 					if (index_pod_etap_select2<len(dir_hc.DictsProces)):
# 						for i2,li2 in enumerate(dir_hc.DictsProces):
# 							if ((i2+1)==index_pod_etap_select2):
# 								input(f"Запустить Этап ({index_pod_etap_select2}) Процес........................")
# 								return f"-m 22000 -a 0 -w {dir_hc.Speed} {selectfilespath} {dir_hc.DirHomeDicts}/{dir_hc.DictsProces[i2]}"
# 					else:
# 						print(f"Вы выбрали {index_pod_etap_select2}, за границы доступности {len(dir_hc.DictsProces)}")
# 			else:
# 				print(f"Вы выбрали {index_etap_select} Метод вышло за приделы 1-3")
# 		except Exception as ex:
# 			print(f"ERROR: {ex}!")