import os.path
import subprocess
import sys

import library as lib

def test_70():
	''' 70% threshold test '''

	try:
		assert os.path.exists('assign.py')
	except AssertionError:
		print('assign.py does not exist')
		sys.exit(1)

	temp_command = '70'

	test_input = '.grader/in.0'
	test_output = 'out0.70.png'
	test_correct = '.grader/out0.70.png'
	subprocess.run(['python3 assign.py %s %s %s' % (test_input, test_output, temp_command)], shell=True, capture_output=True, text=True)
	assert lib.imgcompare(test_output, test_correct)

	test_input = '.grader/in.1'
	test_output = 'out1.70.png'
	test_correct = '.grader/out1.70.png'
	subprocess.run(['python3 assign.py %s %s %s' % (test_input, test_output, temp_command)], shell=True, capture_output=True, text=True)
	assert lib.imgcompare(test_output, test_correct)
