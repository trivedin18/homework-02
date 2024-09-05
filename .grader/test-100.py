import os.path
import subprocess
import sys

import library as lib

def test_100():
	''' 100% threshold test '''

	try:
		assert os.path.exists('assign.py')
	except AssertionError:
		print('assign.py does not exist')
		sys.exit(1)

	test_input = '.grader/mc.0 .grader/mc.1 .grader/mc.2'
	test_output = 'out0.100.png'
	test_correct = '.grader/out0.100.png'
	subprocess.run(['python3 assign.py %s %s 100' % (test_input, test_output)], shell=True, capture_output=True, text=True)
	assert lib.imgcompare(test_output, test_correct, threshold=0.005)

	test_input = '.grader/mc2.0 .grader/mc2.1 .grader/mc2.2'
	test_output = 'out1.100.png'
	test_correct = '.grader/out1.100.png'
	subprocess.run(['python3 assign.py %s %s 100' % (test_input, test_output)], shell=True, capture_output=True, text=True)
	assert lib.imgcompare(test_output, test_correct, threshold=0.005)

	test_input = '.grader/in.0 .grader/in.1'
	test_output = 'out0.80.png'
	test_correct = '.grader/out0.80.png'
	subprocess.run(['python3 assign.py %s %s 100' % (test_input, test_output)], shell=True, capture_output=True, text=True)
	assert lib.imgcompare(test_output, test_correct, threshold=0.005)