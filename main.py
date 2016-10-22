import sys
from random import randint
QUOTES_AMOUNT = 13
quote_id = randint(1,QUOTES_AMOUNT)
GREEN = '\033[92m'
BLUE = '\033[94m'
splash = open("000")
print(GREEN+splash.read())
splash.close()
print("\n\n")

quote = open("quotes/"+str(quote_id))
print(BLUE+quote.read())
quote.close()

print("1:	A loss")
print("2:	Inspiration")
print("3:	Feeling Down")
print("4:	Unconfident")
inp = input(":")
print(quote_id)
if(inp == "1"):
	nquote = open("quotes/01/"+str(quote_id))
	print(BLUE+nquote.read())
	nquote.close()
elif(inp == "2"):
	nquote = open("quotes/02/"+str(quote_id))
	print(BLUE+nquote.read())
	nquote.close()
elif(inp == "3"):
	nquote = open("quotes/03/"+str(quote_id))
	print(BLUE+nquote.read())
	nquote.close()
elif(inp == "4"):
	nquote = open("quotes/04/"+str(quote_id))
	print(BLUE+nquote.read())
	nquote.close()
else:
	print("Unknown category")
