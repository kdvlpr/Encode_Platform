import encode # local library(platform:/encode.py)
import decode # local library(platform:/decode.py)
#KDVLPR

print('Do you want compress or decode : ')

print ('1)Encode')
print('2)Decode')

print('\n')

user_d = str(input())


if user_d == '1':

	if __name__ == '__main__':
		encode.en()

elif user_d == '2':

	if __name__ == '__main__':
		decode.de()

else :
	print('')
