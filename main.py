# required libraries
import getImage
import recogniseDigits

from subprocess import call
import time 

print "Starting...."

cmd_beg= 'espeak '
cmd_end= ' | aplay Text.wav  2>/dev/null' 
cmd_out= '--stdout > Text.wav '

#text = input("Enter the Text: ")
#print(text)
print 'Hello, whats your name'

text='Hello, whats your name'
text = text.replace(' ', '_')
call([cmd_beg+cmd_out+text+cmd_end], shell=True)
time.sleep(5)

print "What do you want to learn"

text1="What do you want to learn"
text1 = text1.replace(' ', '_')
call([cmd_beg+cmd_out+text1+cmd_end], shell=True)
time.sleep(5)


# print "Write one for Numbers, Two for Alphabets"

# text2="Write one for Numbers, Two for Alphabets"
# text2 = text2.replace(' ', '_')
# call([cmd_beg+cmd_out+text2+cmd_end], shell=True)
# time.sleep(5)




# if (digits[0] == 1):

# 	print "Selected choice: ", digits[0]

print "Add two and two"

text3="Add two and two"
text3 = text3.replace(' ', '_')
call([cmd_beg+cmd_out+text3+cmd_end], shell=True)
time.sleep(10)

# **********************************************************

# **********************************************************


# ********************************** Image Part *****************************

# img_file = getImage.capture()
img_file = "../images/test_99.jpg"

digits = recogniseDigits.recog(img_file)
# Drop the first element (0)
digits = digits[1:]

print "digits: ", digits

if (digits[0] == 4):
	text4="Correct Answer"
	text4 = text4.replace(' ', '_')
	call([cmd_beg+cmd_out+text4+cmd_end], shell=True)
	time.sleep(5)

	print "Correct Answer"
else:
	text5="Incorrect, Try again"
	text5 = text5.replace(' ', '_')
	call([cmd_beg+cmd_out+text5+cmd_end], shell=True)
	time.sleep(5)

	print "Incorrect, Try again"

# !end