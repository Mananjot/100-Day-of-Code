"""

Question: Hunt a new Apartment

You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment that you could move into. In order to pick your apartment, you want to optimize its location. 
You also have a list of requirements: a list of buildings that are important to you. For instance, you might value having a school and a gym near your apartment.
The list of blocks that you have contains information at every block about all of the buildings that are present and absent at the block in question.
For instance, for every block, you might know whether a school, a pool, an office, and a gym are present.
In order to optimize your life, you want to minimize the farthest distance you'd have to walk from your apartment to reach any of your required buildings.
Write a function that takes in a list of blocks and a list of your required buildings and that returns the location (the index) of the block that's most optimal for you.


Sample Input 1
blocks = [
 {"gym": false, "school": true, "store": false},
 {"gym": true, "school": false, "store": false},
 {"gym": true, "school": true, "store": false},
 {"gym": false, "school": true, "store": false},
 {"gym": false, "school": true, "store": true}
]
reqs = ["gym", "school", "store"]

Sample Output 1
3 

Explanation 1
At index 3, the farthest you'd have to walk to reach a gym, school, or a store is 1 block; at any other index, you'd have to walk farther

"""

import numpy as numpy
import pandas as pd

def apartmentHunting(blocks, reqs):
    # Write your code here.
    req_dist = float('inf')
    result = float('inf')
    distances =[]
    no_of_blocks = len(blocks)
    for i in range(no_of_blocks):
      for req in reqs:
        if blocks[i][req] == False:
          for j in range(no_of_blocks):
            if blocks[j][req] == True:
              if req_dist > abs(i-j):
                req_dist = abs(i-j)
          distances.append(req_dist)
          req_dist =  float('inf')
        # else:
        #   distances.append(0)
      if max(distances) < result:
        result = max(distances)
        result_idx = i
      distances = []  
    return result_idx
    # df = pd.DataFrame(blocks)
    # print(df)
          
blocks = [
 {"gym": False, "school": True, "store": False},
 {"gym": True, "school": False, "store": False},
 {"gym": True, "school": True, "store": False},
 {"gym": False, "school": True, "store": False},
 {"gym": False, "school": True, "store": True}
]
reqs = ["gym", "school", "store"]
print(apartmentHunting(blocks, reqs))


