import zlib, base64


def de():

	compressed_text = input(': ')

	compressed_byte = compressed_text.encode('utf-8')

	algorithm_decode = zlib.decompress(base64.b64decode(compressed_byte))


	print ('\n'+str(algorithm_decode))

	wait2 = input()
