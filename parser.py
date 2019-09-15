from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
English = ['beginning [start]',
'end',
'before',
'after',
'early',
'late',
'soon',
'now',
'during',
'whenever [when]',
'later',
'time',
'hour',
'minute',
'night [evening]',
'second',
'noon',
'midnight',
'during the morning [in the morning]',
'during the evening [at night]',
'during the afternoon [in the afternoon]',
'in the morning [am]',
'in  the evening [pm]',
'in the afternoon [pm]',
'quarter past',
'half past',
'appointment [date]',
'semester',
'schedule',
'clock [watch]',
'How often...? [With what frequency...?]',
'sometimes',
'never',
'often',
'rarely',
'every day',
'always',
'once in a while [sometimes]',
'no longer',
'Would you like to come with me to ...?',
'I invite you ...',
'Would you like ...?',
'I would like ...',
"Thanks, but I can't.",
'Yes, I would love to.',
'What a shame!',
'invitation',
'Maybe another day',
'(At) What time is ...?',
"it's one o'clock",
"it's ten minutes to one",
'(at) What time?',
"it's two o'clock",
'Right now!',
"at four o'clock",
"What time is it?",
"at one o'clock",
'backpack',
'chalkboard',
'pen',
'marker',
'scissors',
'pencil sharpener',
'folder',
'printer',
'screen',
'keyboard',
'algebra',
'geometry',
'music',
'physical education',
'computer science',
'French',
'Japanese',
'Chinese',
'Italian',
'novel',
'poem',
'poetry',
'magazine',
'newspaper',
'letter',
'manual',
'mail',
'email',
'piano',
'to play the piano',
'guitar',
'to play the guitar',
'drum set',
'saxophone',
'violin',
'flute',
'clarinet',
'cassette',
'radio-tape player',
'radio [apparatus]',
'compact disc',
'auditorium',
'office',
'cafeteria',
'gym',
'museum',
'park',
'theater',
'concert',
'store',
'airport',
'bank',
'bus station',
'pharmacy [drug store]',
'hotel',
'church',
'plaza [town square]',
'synagogue',
'(movie) theater',
'wide',
'old [ancient]',
'enormous',
'narrow [tight]',
'formal',
'informal [casual]',
'luxurious',
'modern',
'ordinary',
'simple',
'traditional',
'to ride a bike',
'to skateboard',
'to skate',
'to ride',
'to visit',
'to go for a walk',
'to drive [conduct]',
'to ride a horse',
'(The) United States',
'Spain',
'Mexico',
'Brazil',
'Canada',
'China',
'Ecuador',
'India',
'Japan',
'Peru',
'Paraguay',
'Uruguay',
'(The) Dominican Republic',
'rain',
'snow',
'sun',
'degree',
'ice',
'cloud',
'cloudy',
'wind',
'to snow',
'to rain',
'temperature',
'storm',
'outdoors',
'suntan lotion',
'sunglasses',
'umbrella',
'beach',
'to sunbathe',
'sea',
'sand',
'wave',
'vacation',
'to go scuba diving [to scuba dive]',
'water skiing',
'to go sailing',
'to swim',
'woods [forest]',
'desert',
'lake',
'mountain',
'river',
'ocean',
'tree',
'flower',
'plant',
'pollution [contamination]',
'season',
'winter',
'fall [autumn]',
'summer',
'spring [season]',
'it is hot',
'it is cool',
'it is cold',
'it is bad outside [the weather is bad]',
'it is sunny',
'it is windy',
'the weather is nice',
'it is sunny',
'it is windy',
"it's cloudy",
'What is the weather like?',
'cheap [inexpensive]',
'expensive',
'What size is it?',
'purchase',
'money',
'dollar',
'free [no cost]',
'price',
'discount [sale]',
'bargain',
'sale',
'purse [wallet]',
'bag',
'elevator',
'bathroom',
'fence',
'chimney',
'dining room',
'corridor',
'bedroom',
'stairway [stairs,staircase]',
'room',
'bedroom',
'living room',
'kitchen',
'patio',
'garden',
'cupboard',
'carpet [rug]',
'pillow',
'appliance [device, gadget]',
'wardrobe [closet]',
'vacuum cleaner',
'bathtub',
'coffee pot',
'heater',
'bed',
'brush',
'dresser',
'curtain',
'painting',
'shower',
'broom',
'mirror',
'shelf',
'stove',
'(kitchen) sink',
'cabinet',
'oven',
'microwave',
'toilet',
'basin [(bathroom) sink]',
'washer [washing machine]',
'dishwasher',
'table',
'hairdryer',
'clothes dryer',
'armchair',
'bush',
'court [field]',
'shopping center [mall]',
'department',
'owner [landlord]',
'statue',
'town [village]',
'tree',
'school',
'church',
'store',
'to sweep',
'to warm up',
'to mow the lawn [to cut the grass]',
'to feed',
'to dust',
'to vacuum',
'to water',
'to take out the trash',
'to make the bed',
'to rent',
'to support',
'to close',
'to share',
'to know [be familiar with]',
'to send',
'to turn on',
'to turn off',
'to turn on [to light (a match)]',
'someone [anyone]',
'principal',
'fun',
'employee',
'entrance',
'news',
'pair [couple]',
'price',
'sale',
'agreeable [nice, pleasant]',
'ample',
'furnished',
'cheap [inexpensive]',
'expensive',
'own',
'serious',
'useful'

]

Spanish = ['(el) comienzo',
'(el) fin',
'antes (de)',
'después (de)',
'temprano(a)',
'tarde',
'pronto',
'ahora',
'durante',
'cuando',
'luego',
'(el) tiempo',
'(la) hora',
'(el) minuto',
'(la) noche',
'(el) segundo',
'(el) mediodía',
'(la) medianoche',
'por la mañana',
'por la noche',
'por la tarde',
'de la mañana',
'de la noche',
'de la tarde',
'y cuarto',
'y media',
'(la) cita',
'(el) semestre',
'(el) horario',
'(el) reloj',
'¿Con qué frecuencia...?',
'a veces',
'nunca',
'mucho',
'rara vez',
'todos los días',
'siempre',
'de vez en cuando',
'ya no',
'¿Quieres acompañarme a ...?',
'Te invito ...',
'¿Te gustaría ...?',
'Me gustaría ...',
'Gracias, pero no puedo.',
'Sí, me encantaría.',
'¡Qué lástima!',
'(la) invitación',
'Tal vez otro día',
'¿A qué hora es ...?',
'es la una',
'es la una menos diez',
'¿A qué hora?',
'son las dos',
'¡Ahora mismo!',
'a las cuatro',
'¿Qué hora es?',
'a la una',
'(la) mochila',
'(el) pizarrón',
'(la) pluma',
'(el) marcador',
'(las) tijeras',
'(el) sacapuntas',
'(la) carpeta',
'(la) impresora',
'(la) pantalla',
'(el) teclado',
'(el) álgebra',
'(la) geometría',
'(la) música',
'(la) educación física',
'(la) computación',
'(el) francés',
'(el) japonés',
'(el) chino',
'(el) italiano',
'(la) novela',
'(el) poema',
'(la) poesía',
'(la) revista',
'(el) periódico',
'(la) carta',
'(el) manual',
'(el) correo',
'(el) correo electrónico',
'(el) piano',
'tocar el piano',
'(la) guitarra',
'tocar la guitarra',
'(la) batería',
'(el) saxofón',
'(el) violín',
'(la) flauta',
'(el) clarinete',
'(el) casete',
'(el) radiocasete',
'(el) radio',
'(el) disco compacto',
'(el) auditorio',
'(la) oficina',
'(la) cafetería',
'(el) gimnasio',
'(el) museo',
'(el) parque',
'(el) teatro',
'(el) concierto',
'(la) tienda',
'(el) aeropuerto',
'(el) banco',
'(la) estación de autobuses',
'(la) farmacia',
'(el) hotel',
'(la) iglesia',
'(la) plaza',
'(la) sinagoga',
'(el) cine',
'ancho(a)',
'antiguo(a)',
'enorme',
'estrecho(a)',
'formal',
'informal',
'lujoso(a)',
'moderno(a)',
'ordinario(a)',
'sencillo(a)',
'tradicional',
'andar en bicicleta',
'andar en patineta',
'patinar',
'montar',
'visitar',
'pasear',
'conducir',
'montar a caballo',
'(los) Estados Unidos',
'España',
'México',
'Brasil',
'Canadá',
'China',
'(el) Ecuador',
'India',
'(el) Japón',
'Perú',
'(el) Paraguay',
'(el) Uruguay',
'(la) República Dominicana',
'(la) lluvia',
'(la) nieve',
'(el) sol',
'(el) grado',
'(el) hielo',
'(la) nube',
'nublado(a)',
'(el) viento',
'nevar',
'llover',
'(la) temperatura',
'(la) tormenta',
'al aire libre',
'(el) bronceador',
'(las) gafas de sol',
'(el) paraguas',
'(la) playa',
'tomar el sol',
'(el) mar',
'(la) arena',
'(la) ola',
'(las) vacaciones',
'bucear',
'(el) esquí acuático',
'pasear en velero',
'nadar',
'(el) bosque',
'(el) desierto',
'(el) lago',
'(la) montaña',
'(el) río',
'(el) océano',
'(el) árbol',
'(la) flor',
'(la) planta',
'(la) contaminación',
'(la) estación',
'(el) invierno',
'(el) otoño',
'(el) verano',
'(la) primavera',
'hace calor',
'hace fresco',
'hace frío',
'hace mal tiempo',
'hace sol',
'hace viento',
'hace buen tiempo',
'hay sol',
'hay viento',
'está nublado',
'¿Qué tiempo hace?',
'barato(a)',
'caro(a)',
'¿Qué talla es?',
'(la) compra',
'(el) dinero',
'(el) dólar',
'gratis',
'(el) precio',
'(la) rebaja',
'(la) ganga',
'(la) venta',
'(la) cartera',
'(la) bolsa',
'(el) ascensor',
'(el) baño',
'(la) cerca',
'(la) chimenea',
'(el) comedor',
'(el) corredor',
'(el) dormitorio',
'(la) escalera',
'(la) habitación',
'(la) recámara',
'(la) sala',
'(la) cocina',
'(el) patio',
'(el) jardín',
'(la) alacena',
'(la) alfombra',
'(la) almohada',
'(el) aparato',
'(el) armario',
'(la) aspiradora',
'(la) bañera',
'(la) cafetera',
'(el) calentador',
'(la) cama',
'(el) cepillo',
'(la) cómoda',
'(la) cortina',
'(el) cuadro',
'(la) ducha',
'(la) escoba',
'(el) espejo',
'(el) estante',
'(la) estufa',
'(el) fregadero',
'(el) gabinete',
'(el) horno',
'(el) microondas',
'(el) inodoro',
'(el) lavabo',
'(la) lavadora',
'(el) lavaplatos',
'(la) mesa',
'(el) secador de pelo',
'(la) secadora',
'(el) sillón',
'(el) arbusto',
'(la) cancha',
'(el) centro comercial',
'(el) departamento',
'(el/la) dueño(a)',
'(la) estatua',
'(el) pueblo',
'(el) árbol',
'(la) escuela',
'(la) iglesia',
'(la) tienda',
'barrer',
'calentarse',
'cortar el césped',
'dar de comer',
'desempolvar',
'pasar la aspiradora',
'regar',
'sacar la basura',
'tender la cama',
'alquilar',
'apoyar',
'cerrar',
'compartir',
'conocer',
'enviar',
'prender',
'apagar',
'encender',
'alguien',
'(el/la) director(a)',
'(la) diversión',
'(el/la) empleado(a)',
'(la) entrada',
'(las) noticias',
'(la) pareja',
'(el) precio',
'(la) venta',
'agradable',
'amplio(a)',
'amueblado(a)',
'barato(a)',
'caro(a)',
'propio(a)',
'serio(a)',
'útil'
]

print("""
_________________________________

Wordplay Macro Program
_________________________________

	""")
print('path:')
path = input() # ex: C:\chromedriver_win32\chromedriver.exe
driver=webdriver.Chrome(path)
print('\n\nusername:')
username = input()
print('\npassword:')
password = input()

# gets on to the login site
driver.get('https://wordplay.com/login')

driver.find_element_by_id('username').send_keys(username)

driver.find_element_by_id('password').send_keys(password)

driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[1]/form/button').click()

driver.implicitly_wait(30)

numofwords = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/h5')
num_of_word= numofwords.get_attribute("textContent")
numofwords2 = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[3]/h5')
num_of_word2= numofwords2.get_attribute("textContent")
fin_num_of_words = int(num_of_word) + int(num_of_word2)

# gets on to the dashboard & clicks review now

driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div[2]/div[2]/a').click()

print('\n\n\ntotal words: ')
print(fin_num_of_words)
print('\n')

# ad

print('''

-----------------------------

	wait 60 seconds...

-----------------------------

	''')

driver.implicitly_wait(60)


key=''


def conver(test_str):			#conversion function
	    ret = ''
	    skip1c = 0
	    skip2c = 0
	    for i in test_str:
	        if i == '[':
	            skip1c += 1
	        elif i == '(':
	            skip2c += 1
	        elif i == ']' and skip1c > 0:
	            skip1c -= 1
	        elif i == ')'and skip2c > 0:
	            skip2c -= 1
	        elif skip1c == 0 and skip2c == 0:
	            ret += i
	    return ret



i2 = 0 # num of words

#retention

while i2<fin_num_of_words:

	


	shownword = driver.find_element_by_xpath('//*[@id="review-content"]/div[2]/div[2]/div[1]/div/h3')
	shown_word= shownword.get_attribute("textContent")

	i = 0 #words

	while i < len(Spanish):

		if (conver(shown_word).replace(" ","")) == (conver(Spanish[i]).replace(" ","")):
			
			key = conver(English[i])

			driver.find_element_by_xpath('//*[@id="type-input"]').send_keys(key)
			

			driver.find_element_by_css_selector('#done-btn').send_keys("\n")
			time.sleep(1)
			driver.find_element_by_xpath('//*[@id="type-input"]').send_keys(30 * Keys.BACKSPACE)        
			time.sleep(2.5)

			element = driver.find_element_by_xpath('//*[@id="altModal"]')
			hidden_box = element.get_attribute('class')
	


			element2 = driver.find_element_by_xpath('//*[@id="wrongEx"]')
			incorrect_mark = element2.get_attribute('style')
	


			if hidden_box=="modal fade in":
				driver.find_element_by_xpath('//*[@id="altModal"]/div/div/div[3]/button').click()
				i = i+1
				continue
			elif "inline" in incorrect_mark:
				i = i+1
				continue
			else:
				break

			
		elif (conver(shown_word).replace(" ","")) == (conver(English[i]).replace(" ","")):
		

			key = conver(Spanish[i])
			driver.find_element_by_xpath('//*[@id="type-input"]').send_keys(key)
			

			driver.find_element_by_css_selector('#done-btn').send_keys("\n")
			time.sleep(1)

			driver.find_element_by_xpath('//*[@id="type-input"]').send_keys(30 * Keys.BACKSPACE)        
			time.sleep(2.5)

			element = driver.find_element_by_xpath('//*[@id="altModal"]')
			hidden_box = element.get_attribute('class')
	


			element2 = driver.find_element_by_xpath('//*[@id="wrongEx"]')
			incorrect_mark = element2.get_attribute('style')

			if hidden_box=="modal fade in":
				driver.find_element_by_xpath('//*[@id="altModal"]/div/div/div[3]/button').click()
				i = i+1
				continue
			elif "inline" in incorrect_mark:
				i = i+1
				continue
			else:
				break
		else:
			i=i+1
			
		
	


	i2 = i2+1
	print('\n')
	print(fin_num_of_words-i2)
	print('words left...\n')



	

print("program ended")

