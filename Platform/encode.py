import zlib, base64


def en():

	text = input(': ') 

	byte = text.encode('utf-8')

	algorithm_encode =  base64.b64encode(zlib.compress(byte,9))


	print ('\n'+str(algorithm_encode))

	wait = input()
