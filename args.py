from argparse import ArgumentParser

def make_args():
	parser = ArgumentParser(description='Retrive consolidated data related to stock trading.')

	# display and return values
	parser.add_argument('-listSize', dest='listSize', default='15', type=int)

	# api optimization
	parser.add_argument('-batchSize', dest='batchSize', default='100', type=int)

	args = parser.parse_args()
	return args