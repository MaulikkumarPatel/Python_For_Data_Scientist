import numpy as np
import pandas as pd
from datetime import datetime
import time

# Define the ASCII art for the Indian flag
indian_flag = """
                      __________________________________________
                     |                                          |
                     |      Happy 77th Independence Day!         |
     white           |                                          |
   _________________  |                                          |
   || * * * * * * *|| |                                          |
   ||* * * * * * * || |                                          |
   ||______________|| |                                          |
   |________________| |                                          |
    /###############/ /                                          |
   /###############/ /                                           |
  /###############/ /                                            |
 /###############/ /                  / \\                      / \\   
 -----------------                  /   \\____________________/   \\
   \\###############\\                \\    \\####################/    /
    \\###############\\                \\    \\##################/    /
     \\###############\\                \\    \\################/    /
      ++++++++++++++++                 /    /                \\    \\
                                       /    /                  \\    \\
                                      /    /                    \\    \\
                                     /    /                      \\    \\
                                    /    /                        \\    \\
                                   /    /                          \\    \\
                                  /    /                            \\    \\
                                 /    /____________________________\\    \\
                                /                                     \\    \\
                               /_______________________________________\\
"""

# Calculate the number of years since independence
independence_year = 1947
current_year = datetime.now().year
years_since_independence = current_year - independence_year

# Generate a random happiness index
np.random.seed(77)
happiness_index = np.random.uniform(0.7, 1.0)

# Create a DataFrame to store the message
data = {
    'Event': ['India\'s 77th Independence Day'],
    'Year': [current_year],
    'Years Since Independence': [years_since_independence],
    'Happiness Index': [happiness_index]
}
df = pd.DataFrame(data)

# Display the flag animation and the message
for line in indian_flag.splitlines():
    print(line)
    time.sleep(0.1)

print("\n")
print(df.to_string(index=False))
print("\nWishing all Indians a data-filled and prosperous journey ahead!")
