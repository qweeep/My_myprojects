import ipaddress #Подключение ВСТРОЕННОЙ библиотеки питон

ip = input("Введите IP-адрес: ") #Ввод IP адреса
mask = input("Введите маску сети: ") #Ввод Маски сети

def is_bin(mas_is_bin):  #Функция,проверяющая введено 10ичн значение или 2 ичн
	mas_is_bin = mas_is_bin.split('.')
	for i in mas_is_bin:
		if len(i) > 3:
			return 1
		else:
			return 0 

def to_dec(t0_dec): #Функция, которая переводит двоичное значение в десятичное 
	t0_dec = t0_dec.split('.')
	t0_dec[0] = int(str(t0_dec[0]), 2)
	t0_dec[1] = int(str(t0_dec[1]), 2)
	t0_dec[2] = int(str(t0_dec[2]), 2)
	t0_dec[3] = int(str(t0_dec[3]), 2)
	des = str(t0_dec[0]) + '.' + str(t0_dec[1]) + '.' + str(t0_dec[2]) + '.' + str(t0_dec[3])
	return des

if is_bin(ip) == 1: #проверка и перевод айпи адреса
	ip = to_dec(ip)

if is_bin(mask) == 1: #проверка и перевод маски сети
	mask = to_dec(mask)

network = ipaddress.IPv4Network(f'{ip}/{mask}', strict=False) #вычисление адреса сетис помощью методов встроенной библио
print('Адрес сети в 10 системе счисления', network.network_address)#вывод адреса сети в 10ичн виде

addr = ipaddress.IPv4Address(network.network_address)
addr = addr.packed 
addr_s = str(bin(addr[0]))[2:] + '.' + str(bin(addr[1]))[2:] + '.' + str(bin(addr[2]))[2:] + '.' + str(bin(addr[3]))[2:]
print('Адрес сети в 2 системе счисления', addr_s)
#в строках 32-35 производится преобразование адреса сети из 10ичн в 2ичн вид с помощью встроенной библиотеки
if addr[0] < 128:
	print('Сеть принадлежит Классу А')
elif 127 < addr[0] < 192:
	print('Сеть принадлежит Классу B')
elif 191 < addr[0] < 223:
	print('Сеть принадлежит Классу С')
elif 222 < addr[0] < 239:
	print('Сеть принадлежит Классу D')
elif 239 < addr[0] < 255:
	print('Сеть принадлежит Классу E')
#в строчках 37-42 происходит проверка и печать класса к которочу принадлежит адрес сети