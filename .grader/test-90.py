import os.path
import subprocess
import sys

import library as lib

def test_90():
	''' 90% threshold test '''

	try:
		assert os.path.exists('assign.py')
	except AssertionError:
		print('assign.py does not exist')
		sys.exit(1)

	test_input = '.grader/in.0 .grader/in.1 .grader/in.2'
	test_output = 'out0.90.png'
	test_correct = '.grader/out0.90.png'
	subprocess.run(['python3 assign.py %s %s 90' % (test_input, test_output)], shell=True, capture_output=True, text=True)
	assert lib.imgcompare(test_output, test_correct, threshold=0.005)

	test_input = '.grader/in.0'
	test_output = 'out1.90.png'
	test_correct = '.grader/out1.90.png'
	subprocess.run(['python3 assign.py %s %s 90' % (test_input, test_output)], shell=True, capture_output=True, text=True)
	assert lib.imgcompare(test_output, test_correct, threshold=0.005)

	test_input = '.grader/in.0 .grader/in.1'
	test_output = 'out2.90.png'
	test_correct = '.grader/out2.90.png'
	subprocess.run(['python3 assign.py %s %s 90' % (test_input, test_output)], shell=True, capture_output=True, text=True)
	assert lib.imgcompare(test_output, test_correct, threshold=0.005)
