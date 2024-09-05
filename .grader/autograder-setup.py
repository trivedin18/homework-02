#!/usr/bin/python3

import glob

# Write yaml preamble to classroom.yaml file
preamble  = '''name: Autograding Tests
on:
  - push
  - workflow_dispatch
  - repository_dispatch
permissions:
  checks: write
  actions: read
  contents: read
jobs:
  run-autograding-tests:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4\n'''

f = open('classroom.yaml', 'w')
f.write(preamble)

# Get all test files in the directory
test_files = glob.glob('test*.py')

# Option for a single test script
if len(test_files) == 1:
    
    # Count number of tests
    test_script = open(test_files[0], 'r').readlines()
    num_tests = 0
    for line in test_script:
        if 'def test_' in line:
            num_tests += 1
    
    # Write single test
    f.write('      - name: Autograding test\n')
    f.write('        id: assign\n')
    f.write('        uses: classroom-resources/autograding-command-grader@v1\n')
    f.write('        with:\n')
    f.write('          test-name: \'All credit bundled\'\n')
    f.write('          setup-command: \'pip3 install -r .grader/requirements.txt\'\n')
    f.write('          command: \'pytest .grader/%s\'\n' % test_files[0])
    f.write('          timeout: 10\n')
    f.write('          max-score: %d\n' % num_tests)

    # Write single reporter
    f.write('      - name: Autograding Reporter\n')
    f.write('        uses: classroom-resources/autograding-grading-reporter@v1\n')
    f.write('        env:\n')
    f.write('          ASSIGN_RESULTS: "${{steps.assign.outputs.result}}"\n')
    f.write('        with:\n')
    f.write('          runners: assign\n')

# Option for multiple test scripts
else:

  # Get number of points for each test
  points = [int(t.split('.py')[0].split('-')[1]) for t in test_files]
  points.sort()

  # Write individual tests
  for i in range(len(points)):
      f.write('      - name: Autograding test %d\n' % (i))
      f.write('        id: assign%d\n' % points[i])
      f.write('        uses: classroom-resources/autograding-command-grader@v1\n')
      f.write('        with:\n')
      f.write('          test-name: \'%d%% credit\'\n' % points[i])
      f.write('          setup-command: \'pip3 install -r .grader/requirements.txt\'\n')
      f.write('          command: \'pytest .grader/test-%d.py\'\n' % points[i])
      f.write('          timeout: 10\n')
      f.write('          max-score: %d\n' % points[i])

  # Write reporter
  f.write('      - name: Autograding Reporter\n')
  f.write('        uses: classroom-resources/autograding-grading-reporter@v1\n')
  f.write('        env:\n')
  for i in range(len(points)):
      f.write('          ASSIGN%d_RESULTS: "${{steps.assign%d.outputs.result}}"\n' % (points[i], points[i]))
  f.write('        with:\n')
  f.write('          runners: %s\n' % ', '.join(['assign%d' % p for p in points]))

f.close()