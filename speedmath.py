import random, time, datetime, calendar, locale

locale.setlocale(locale.LC_ALL, '')

while 1:

	print '''

        1. 3 x 3 multiplication (practice Vedic/Trachtenberg methods)  

        2. calendar dates (practice Zeller's Rule to calculate the day of the week) 

        3. quit

        choose 1, 2, or 3'''

	answer = raw_input('\n')
	
	if answer == '1':

		class Math:
			def __init__(self):
				self.x = random.randint(100,999)
				self.y = random.randint(100,999)

		t1m = time.localtime().tm_min
		t1s = time.localtime().tm_sec
		t1 = t1m + t1s/100.0
		n = 0
		x = 0

		while n < 10:
			calc = Math()
			print '\n  ',calc.x,'x', calc.y,'=',				
			answer = raw_input()		
			if answer in [str(calc.x*calc.y), locale.format('%d', calc.x*calc.y, grouping=True)]:
				print 'correct'
				pass
			else:
				x += 1
				print locale.format('%d', calc.x*calc.y, grouping=True)
			n += 1

		t2m = time.localtime().tm_min
		t2s = time.localtime().tm_sec
		t2 = t2m + t2s/100.0
		td = t2 - t1		
		
		print '\n',x,'out of 10 wrong\navg time/question:',td/10,'\ntotal time:',td

	if answer == '2':

		class Date:
			def __init__(self):
				self.c = random.randint(16,30) # first two digits in a year
				self.y = random.randint(0,99)  # last two digits in a year
				self.month = random.randint(1,12) 
				self.year = self.c*100 + self.y 
		
				apr = [4,6,9,11] 
				feb = [2] 
				notleap = [1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600, 2700, 2900, 3000]
					
				if self.month in feb:          # assigns days given the month
					if self.year%4 == 0:
						if self.year in notleap:
							self.k = random.randint(1,28)
						else:
							self.k = random.randint(1,29)
					else:
						self.k = random.randint(1,28)
				elif self.month in apr:
					self.k = random.randint(1,30)
				else:
					self.k = random.randint(1,31)
	
				if self.month in [1,2]:        # months in zeller's rule are subtracted by 2 
					if self.y == 0:        # need to acct for jan/feb year change
						d = 99
						m = self.month + 10
					else:
						d = self.y - 1
						m = self.month + 10
				else:
					d = self.y
					m = self.month - 2
				
				self.z = self.k + (13*m-1)/5 + d + d/4 + self.c/4 - 2*self.c  # Zeller's formula

				self.r = self.z%7     # the remainder of z/7 determines the day of the week
	
				week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
				self.day = week[self.r]		
		
		t1m = time.localtime().tm_min
		t1s = time.localtime().tm_sec
		t1 = t1m + t1s/100.0
		n = 0
		x = 0

		while n < 10:
			newdate = Date()				
			print '\n  ',calendar.month_name[newdate.month], str(newdate.k) + ',',newdate.year,'=',
			answer = raw_input()
			if answer.capitalize() == newdate.day:
				print 'correct'
			        pass
			else:
				x += 1	
				print newdate.day
			n += 1
	
		t2m = time.localtime().tm_min
		t2s = time.localtime().tm_sec
		t2 = t2m + t2s/100.0
		td = t2 - t1		
		
		print '\n',x,'out of 10 wrong\navg time/question:',td/10,'\ntotal time:',td

        if answer == '3': break
