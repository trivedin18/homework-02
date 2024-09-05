#!/usr/bin/python3

import glob

# Get all test files in the directory
test_files = glob.glob('test-*.py')

# Get number of points for each test
points = [int(t.split('.py')[0].split('-')[1]) for t in test_files]
points.sort()

# Write tests to classroom.yaml file
tab_steps = '  '
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

# Write individual tests
for i in range(len(points)):
    f.write('      - name: Autograding test %d\n' % (i))
    f.write('        id: assign%d\n' % points[i])
    f.write('        uses: classroom-resources/autograding-python-grader@v1\n')
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