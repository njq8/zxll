
############################################ lib
import os, sys, time, socket
############################################ colors
W = "\033[0m"
G = '\033[32;1m'
Y = '\033[33;1m'
R = '\033[31;1m'
############################################ I DON'T KNOW
list = []


try :
	import mechanize
except IOError as msg :
	print R + '[!] Error import : ' + G + 'Please install libraries !!!' + W
	print Y + '[LIBRARIES]' + W + ' mechanize '
	time.sleep(0.3)
	sys.exit()

web_br = mechanize.Browser()

def net():
	try :
		site = socket.gethostbyname("www.google.com")
		do = socket.create_connection((site, 80), 2)
		return True
	except socket.error :
		pass
	return False

def onemail():
	try :
		print Y + 'zxll ' + R + '/' + Y + ' mail >> ' + W 
		key = raw_input( Y + 'Enter the mail : ' + W )
		web_br.addheaders = [('Urse-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')]
		web_br.set_handle_robots(False)
		web_br.open("https://verifyemailaddress.com/")
		web_br.select_form(nr=0)
		web_br["email"] = key
		check = web_br.submit()
		if "is valid" in check.get_data():
		        print G + '+ - -- | ' + Y + key + G + '   ACTIVE :::: Good for e-marketing' + W
			time.sleep(0.2)
		else :
			print G + '+ - -- | ' + Y + key + R + '   NOT ACTIVE ' + W
			time.sleep(0.2)
		print ' '
		print G + '[^] DONE' + W
		print ' '
		finished()
	except IOError :
		pass

def finished():
	print '   [ 1 ] ENTER ANOTHER MAIL'
	print '   [ 2 ] BACK TO MAIN'
	print '   [ 3 ] EXIT'
	print ' '
	what = raw_input( Y + 'zxll ' + R + '/' + Y + ' mail >> ' + W )
	if what == '1' :
		onemail()
	if what == '2' :
		os.system('clear')
		main()
	if what == '3' :
		print Y + '[^] GOODBYES' + W
		time.sleep(0.3)
		sys.exit()
	else :
		print ' '
		print R + 'SORRY AM NOT SURE WHAT DO YOU MEAN ?!' + W
		print ' '
		finished()

def main():
        if net() != True :
                print R + '[?] Please check your connection !!' + W + ' And try again'
                time.sleep(0.3)
                sys.exit()
        try :
                print Y + '''
                + - -- [ Telegram : Kadaone ]
                + - -- [ Telegram channel : @hellosone ]
                + - -- [ Facebook : www.facebook.com/zxlll ]
                + - -- [ Facebook inbox : m.me/zxlll ]
	        + - -- [ github : zxllkada ]
                + - -- [ v 1.0  /  v 2.0 inbox me on Telegram ]
                + - -- [ Devloper : Kada ]

		* if you find any error please text me
		______________________________________
''' + W
                print ' '
                print '   [ 1 ] : check one mail '
                print '   [ 2 ] : check list ' + Y + ' [ PLEASE WAIT NEXT UPDATE ] ' + W
		print '   [ 0 ] : Exit '
                print ' '
                get = raw_input( Y + 'zxll ' + W + '>> ' )
                if get == '1' :
                        os.system('clear')
			time.sleep(0.4)
                        onemail()
		if get == '2' :
			os.system('clear')
			print '[ ' + Y + 'PLEASE WAIT NEXT UPDATE' + W + ' ]'
			main()
		if get == '0' :
			print '[^] ' + Y + 'GOODBYES' + W
			time.sleep(0.9)
			sys.exit()
		else :
			print 'THE COMMAND NOT FOUND   [' + R  + get + W +  ']   ??!!'
			time.sleep(1.5)
			os.system('clear')
			main()
	except IOError :
		print R + 'ERROR' + W
		sys.exit()
	except KeyboardInterrupt :
		sys.exit()

main()

