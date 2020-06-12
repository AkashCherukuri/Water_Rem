import winsound
import datetime

def plus_one(minute):
	if minute == 59:
		return 0
	else:
		return (minute + 1)

def timer (minutes):
	spent = 0
	while spent != minutes:
		now = datetime.datetime.now()
		while True:
			if(datetime.datetime.now().minute == plus_one(now.minute)):
				break
		spent+=1
	return True

while True:
	delay = input("Enter how frequently (in minutes) you'd like to be reminded: ")
	if not delay.isdigit():
		print("Enter a valid number bruh")
	else:
		delay = int(delay)
		break

print(f"Timer set for {delay} minutes\n")
num = 0
while True:
    timer(delay)
    winsound.PlaySound("Rick.wav", winsound.SND_ASYNC)
    num+=1
    conf = input(f"{num}) Enter Y/y after you're done drinking water(!): ")
    if conf == 'Y' or conf == 'y':
      	winsound.PlaySound(None, winsound.SND_ASYNC) 