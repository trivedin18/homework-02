#!/usr/bin/env python3
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

if len(sys.argv) < 3:
    print("Usage: ./assign.py <input_file1> <input_file2> ... <output_file>")
    sys.exit(1)

# The last argument is the output file, all others are input files
input_files = sys.argv[1:-1]  # List of input files (all except the last argument)
output_file = sys.argv[-1]    # The last argument is the output file

# Function to read data from a file and return x_data, y_data, and label
def read_data(file_name):
    x_data = []
    y_data = []
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
        # First line is the label (header)
        data_name = lines[0].strip()  # This will be used as the label
        
        # Process each line of x, y data
        for line in lines[1:]:
            x, y = map(int, line.strip().split(','))
            x_data.append(x)
            y_data.append(y)
    
    return x_data, y_data, data_name

# List of markers and styles to cycle through for each plot
line_styles = ['-', '-', '-', '-']
markers = ['o', 'o', 'o', 'o', 'o', 'o']

# Plot each input file as a separate data series
for i, input_file in enumerate(input_files):
    x_data, y_data, label = read_data(input_file)
    
    # Cycle through styles and markers for each dataset
    line_style = line_styles[i % len(line_styles)]
    marker = markers[i % len(markers)]
    
    # Plot the data
    plt.plot(x_data, y_data, linestyle=line_style, marker=marker, label=label)

# Add labels and title
plt.xlabel('Time (min)')  # Label for the x-axis
plt.ylabel('Cell Count')  # Label for the y-axis


# Add a legend with the "best" location
plt.legend(loc='best')

# Save the plot to the output file
plt.savefig(output_file)
plt.show()  # Optional: Show the plot for debugging or viewing

print(f"Plot saved to {output_file}")