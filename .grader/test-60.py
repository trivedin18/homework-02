import os.path
import subprocess
import sys

import library as lib

def test_60():
	''' 60% threshold test '''

	try:
		assert os.path.exists('assign.py')
	except AssertionError:
		print('assign.py does not exist')
		sys.exit(1)

	test_input = '.grader/in.0'
	test_output = 'out0.60.png'
	test_correct = '.grader/out0.60.png'
	subprocess.run(['python3 assign.py %s %s' % (test_input, test_output)], shell=True, capture_output=True, text=True)
	assert lib.imgcompare(test_output, test_correct)

	test_input = '.grader/in.1'
	test_output = 'out1.60.png'
	test_correct = '.grader/out1.60.png'
	subprocess.run(['python3 assign.py %s %s' % (test_input, test_output)], shell=True, capture_output=True, text=True)
	assert lib.imgcompare(test_output, test_correct)
