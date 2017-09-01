from core import PBE
import pandas as pd

# This script is meant to generate results from over 500 possible combinations
# of pypbe inputs. It will be used to create the recommendations array for
# pypbe-rec.

# See the Excel sheet for how this array was generated. In order:
# num_dice
# keep_dice
# dice_type
# add_val
# num_attribute
# keep_attribute
# num_arrays
# reroll
inputs=[[3,3,6,0,6,6,1,0,],
[3,3,6,0,6,6,1,1,],
[3,3,6,0,6,6,1,2,],
[4,3,6,0,6,6,1,0,],
[4,3,6,0,6,6,1,1,],
[4,3,6,0,6,6,1,2,],
[5,3,6,0,6,6,1,0,],
[5,3,6,0,6,6,1,1,],
[5,3,6,0,6,6,1,2,],
[3,3,6,0,7,6,1,0,],
[3,3,6,0,7,6,1,1,],
[3,3,6,0,7,6,1,2,],
[4,3,6,0,7,6,1,0,],
[4,3,6,0,7,6,1,1,],
[4,3,6,0,7,6,1,2,],
[5,3,6,0,7,6,1,0,],
[5,3,6,0,7,6,1,1,],
[5,3,6,0,7,6,1,2,],
[3,3,6,0,10,6,1,0,],
[3,3,6,0,10,6,1,1,],
[3,3,6,0,10,6,1,2,],
[4,3,6,0,10,6,1,0,],
[4,3,6,0,10,6,1,1,],
[4,3,6,0,10,6,1,2,],
[5,3,6,0,10,6,1,0,],
[5,3,6,0,10,6,1,1,],
[5,3,6,0,10,6,1,2,],
[3,3,6,0,12,6,1,0,],
[3,3,6,0,12,6,1,1,],
[3,3,6,0,12,6,1,2,],
[4,3,6,0,12,6,1,0,],
[4,3,6,0,12,6,1,1,],
[4,3,6,0,12,6,1,2,],
[5,3,6,0,12,6,1,0,],
[5,3,6,0,12,6,1,1,],
[5,3,6,0,12,6,1,2,],
[3,3,6,0,6,6,3,0,],
[3,3,6,0,6,6,3,1,],
[3,3,6,0,6,6,3,2,],
[4,3,6,0,6,6,3,0,],
[4,3,6,0,6,6,3,1,],
[4,3,6,0,6,6,3,2,],
[5,3,6,0,6,6,3,0,],
[5,3,6,0,6,6,3,1,],
[5,3,6,0,6,6,3,2,],
[3,3,6,0,7,6,3,0,],
[3,3,6,0,7,6,3,1,],
[3,3,6,0,7,6,3,2,],
[4,3,6,0,7,6,3,0,],
[4,3,6,0,7,6,3,1,],
[4,3,6,0,7,6,3,2,],
[5,3,6,0,7,6,3,0,],
[5,3,6,0,7,6,3,1,],
[5,3,6,0,7,6,3,2,],
[3,3,6,0,10,6,3,0,],
[3,3,6,0,10,6,3,1,],
[3,3,6,0,10,6,3,2,],
[4,3,6,0,10,6,3,0,],
[4,3,6,0,10,6,3,1,],
[4,3,6,0,10,6,3,2,],
[5,3,6,0,10,6,3,0,],
[5,3,6,0,10,6,3,1,],
[5,3,6,0,10,6,3,2,],
[3,3,6,0,12,6,3,0,],
[3,3,6,0,12,6,3,1,],
[3,3,6,0,12,6,3,2,],
[4,3,6,0,12,6,3,0,],
[4,3,6,0,12,6,3,1,],
[4,3,6,0,12,6,3,2,],
[5,3,6,0,12,6,3,0,],
[5,3,6,0,12,6,3,1,],
[5,3,6,0,12,6,3,2,],
[3,3,6,0,6,6,6,0,],
[3,3,6,0,6,6,6,1,],
[3,3,6,0,6,6,6,2,],
[4,3,6,0,6,6,6,0,],
[4,3,6,0,6,6,6,1,],
[4,3,6,0,6,6,6,2,],
[5,3,6,0,6,6,6,0,],
[5,3,6,0,6,6,6,1,],
[5,3,6,0,6,6,6,2,],
[3,3,6,0,7,6,6,0,],
[3,3,6,0,7,6,6,1,],
[3,3,6,0,7,6,6,2,],
[4,3,6,0,7,6,6,0,],
[4,3,6,0,7,6,6,1,],
[4,3,6,0,7,6,6,2,],
[5,3,6,0,7,6,6,0,],
[5,3,6,0,7,6,6,1,],
[5,3,6,0,7,6,6,2,],
[3,3,6,0,10,6,6,0,],
[3,3,6,0,10,6,6,1,],
[3,3,6,0,10,6,6,2,],
[4,3,6,0,10,6,6,0,],
[4,3,6,0,10,6,6,1,],
[4,3,6,0,10,6,6,2,],
[5,3,6,0,10,6,6,0,],
[5,3,6,0,10,6,6,1,],
[5,3,6,0,10,6,6,2,],
[3,3,6,0,12,6,6,0,],
[3,3,6,0,12,6,6,1,],
[3,3,6,0,12,6,6,2,],
[4,3,6,0,12,6,6,0,],
[4,3,6,0,12,6,6,1,],
[4,3,6,0,12,6,6,2,],
[5,3,6,0,12,6,6,0,],
[5,3,6,0,12,6,6,1,],
[5,3,6,0,12,6,6,2,],
[2,2,6,6,6,6,1,0,],
[2,2,6,6,6,6,1,1,],
[2,2,6,6,6,6,1,2,],
[3,2,6,6,6,6,1,0,],
[3,2,6,6,6,6,1,1,],
[3,2,6,6,6,6,1,2,],
[2,2,6,6,7,6,1,0,],
[2,2,6,6,7,6,1,1,],
[2,2,6,6,7,6,1,2,],
[3,2,6,6,7,6,1,0,],
[3,2,6,6,7,6,1,1,],
[3,2,6,6,7,6,1,2,],
[2,2,6,6,10,6,1,0,],
[2,2,6,6,10,6,1,1,],
[2,2,6,6,10,6,1,2,],
[3,2,6,6,10,6,1,0,],
[3,2,6,6,10,6,1,1,],
[3,2,6,6,10,6,1,2,],
[2,2,6,6,12,6,1,0,],
[2,2,6,6,12,6,1,1,],
[2,2,6,6,12,6,1,2,],
[3,2,6,6,12,6,1,0,],
[3,2,6,6,12,6,1,1,],
[3,2,6,6,12,6,1,2,],
[2,2,6,6,6,6,3,0,],
[2,2,6,6,6,6,3,1,],
[2,2,6,6,6,6,3,2,],
[3,2,6,6,6,6,3,0,],
[3,2,6,6,6,6,3,1,],
[3,2,6,6,6,6,3,2,],
[2,2,6,6,7,6,3,0,],
[2,2,6,6,7,6,3,1,],
[2,2,6,6,7,6,3,2,],
[3,2,6,6,7,6,3,0,],
[3,2,6,6,7,6,3,1,],
[3,2,6,6,7,6,3,2,],
[2,2,6,6,10,6,3,0,],
[2,2,6,6,10,6,3,1,],
[2,2,6,6,10,6,3,2,],
[3,2,6,6,10,6,3,0,],
[3,2,6,6,10,6,3,1,],
[3,2,6,6,10,6,3,2,],
[2,2,6,6,12,6,3,0,],
[2,2,6,6,12,6,3,1,],
[2,2,6,6,12,6,3,2,],
[3,2,6,6,12,6,3,0,],
[3,2,6,6,12,6,3,1,],
[3,2,6,6,12,6,3,2,],
[2,2,6,6,6,6,6,0,],
[2,2,6,6,6,6,6,1,],
[2,2,6,6,6,6,6,2,],
[3,2,6,6,6,6,6,0,],
[3,2,6,6,6,6,6,1,],
[3,2,6,6,6,6,6,2,],
[2,2,6,6,7,6,6,0,],
[2,2,6,6,7,6,6,1,],
[2,2,6,6,7,6,6,2,],
[3,2,6,6,7,6,6,0,],
[3,2,6,6,7,6,6,1,],
[3,2,6,6,7,6,6,2,],
[2,2,6,6,10,6,6,0,],
[2,2,6,6,10,6,6,1,],
[2,2,6,6,10,6,6,2,],
[3,2,6,6,10,6,6,0,],
[3,2,6,6,10,6,6,1,],
[3,2,6,6,10,6,6,2,],
[2,2,6,6,12,6,6,0,],
[2,2,6,6,12,6,6,1,],
[2,2,6,6,12,6,6,2,],
[3,2,6,6,12,6,6,0,],
[3,2,6,6,12,6,6,1,],
[3,2,6,6,12,6,6,2,],
[4,4,4,2,6,6,1,0,],
[4,4,4,2,6,6,1,1,],
[5,4,4,2,6,6,1,0,],
[5,4,4,2,6,6,1,1,],
[6,4,4,2,6,6,1,0,],
[6,4,4,2,6,6,1,1,],
[4,4,4,2,7,6,1,0,],
[4,4,4,2,7,6,1,1,],
[5,4,4,2,7,6,1,0,],
[5,4,4,2,7,6,1,1,],
[6,4,4,2,7,6,1,0,],
[6,4,4,2,7,6,1,1,],
[4,4,4,2,10,6,1,0,],
[4,4,4,2,10,6,1,1,],
[5,4,4,2,10,6,1,0,],
[5,4,4,2,10,6,1,1,],
[6,4,4,2,10,6,1,0,],
[6,4,4,2,10,6,1,1,],
[4,4,4,2,12,6,1,0,],
[4,4,4,2,12,6,1,1,],
[5,4,4,2,12,6,1,0,],
[5,4,4,2,12,6,1,1,],
[6,4,4,2,12,6,1,0,],
[6,4,4,2,12,6,1,1,],
[4,4,4,2,6,6,3,0,],
[4,4,4,2,6,6,3,1,],
[5,4,4,2,6,6,3,0,],
[5,4,4,2,6,6,3,1,],
[6,4,4,2,6,6,3,0,],
[6,4,4,2,6,6,3,1,],
[4,4,4,2,7,6,3,0,],
[4,4,4,2,7,6,3,1,],
[5,4,4,2,7,6,3,0,],
[5,4,4,2,7,6,3,1,],
[6,4,4,2,7,6,3,0,],
[6,4,4,2,7,6,3,1,],
[4,4,4,2,10,6,3,0,],
[4,4,4,2,10,6,3,1,],
[5,4,4,2,10,6,3,0,],
[5,4,4,2,10,6,3,1,],
[6,4,4,2,10,6,3,0,],
[6,4,4,2,10,6,3,1,],
[4,4,4,2,12,6,3,0,],
[4,4,4,2,12,6,3,1,],
[5,4,4,2,12,6,3,0,],
[5,4,4,2,12,6,3,1,],
[6,4,4,2,12,6,3,0,],
[6,4,4,2,12,6,3,1,],
[4,4,4,2,6,6,6,0,],
[4,4,4,2,6,6,6,1,],
[5,4,4,2,6,6,6,0,],
[5,4,4,2,6,6,6,1,],
[6,4,4,2,6,6,6,0,],
[6,4,4,2,6,6,6,1,],
[4,4,4,2,7,6,6,0,],
[4,4,4,2,7,6,6,1,],
[5,4,4,2,7,6,6,0,],
[5,4,4,2,7,6,6,1,],
[6,4,4,2,7,6,6,0,],
[6,4,4,2,7,6,6,1,],
[4,4,4,2,10,6,6,0,],
[4,4,4,2,10,6,6,1,],
[5,4,4,2,10,6,6,0,],
[5,4,4,2,10,6,6,1,],
[6,4,4,2,10,6,6,0,],
[6,4,4,2,10,6,6,1,],
[4,4,4,2,12,6,6,0,],
[4,4,4,2,12,6,6,1,],
[5,4,4,2,12,6,6,0,],
[5,4,4,2,12,6,6,1,],
[6,4,4,2,12,6,6,0,],
[6,4,4,2,12,6,6,1,],
[2,2,8,2,6,6,1,0,],
[2,2,8,2,6,6,1,1,],
[2,2,8,2,6,6,1,2,],
[2,2,8,2,6,6,1,3,],
[3,2,8,2,6,6,1,0,],
[3,2,8,2,6,6,1,1,],
[3,2,8,2,6,6,1,2,],
[3,2,8,2,6,6,1,3,],
[2,2,8,2,7,6,1,0,],
[2,2,8,2,7,6,1,1,],
[2,2,8,2,7,6,1,2,],
[2,2,8,2,7,6,1,3,],
[3,2,8,2,7,6,1,0,],
[3,2,8,2,7,6,1,1,],
[3,2,8,2,7,6,1,2,],
[3,2,8,2,7,6,1,3,],
[2,2,8,2,10,6,1,0,],
[2,2,8,2,10,6,1,1,],
[2,2,8,2,10,6,1,2,],
[2,2,8,2,10,6,1,3,],
[3,2,8,2,10,6,1,0,],
[3,2,8,2,10,6,1,1,],
[3,2,8,2,10,6,1,2,],
[3,2,8,2,10,6,1,3,],
[2,2,8,2,12,6,1,0,],
[2,2,8,2,12,6,1,1,],
[2,2,8,2,12,6,1,2,],
[2,2,8,2,12,6,1,3,],
[3,2,8,2,12,6,1,0,],
[3,2,8,2,12,6,1,1,],
[3,2,8,2,12,6,1,2,],
[3,2,8,2,12,6,1,3,],
[2,2,8,2,6,6,3,0,],
[2,2,8,2,6,6,3,1,],
[2,2,8,2,6,6,3,2,],
[2,2,8,2,6,6,3,3,],
[3,2,8,2,6,6,3,0,],
[3,2,8,2,6,6,3,1,],
[3,2,8,2,6,6,3,2,],
[3,2,8,2,6,6,3,3,],
[2,2,8,2,7,6,3,0,],
[2,2,8,2,7,6,3,1,],
[2,2,8,2,7,6,3,2,],
[2,2,8,2,7,6,3,3,],
[3,2,8,2,7,6,3,0,],
[3,2,8,2,7,6,3,1,],
[3,2,8,2,7,6,3,2,],
[3,2,8,2,7,6,3,3,],
[2,2,8,2,10,6,3,0,],
[2,2,8,2,10,6,3,1,],
[2,2,8,2,10,6,3,2,],
[2,2,8,2,10,6,3,3,],
[3,2,8,2,10,6,3,0,],
[3,2,8,2,10,6,3,1,],
[3,2,8,2,10,6,3,2,],
[3,2,8,2,10,6,3,3,],
[2,2,8,2,12,6,3,0,],
[2,2,8,2,12,6,3,1,],
[2,2,8,2,12,6,3,2,],
[2,2,8,2,12,6,3,3,],
[3,2,8,2,12,6,3,0,],
[3,2,8,2,12,6,3,1,],
[3,2,8,2,12,6,3,2,],
[3,2,8,2,12,6,3,3,],
[2,2,8,2,6,6,6,0,],
[2,2,8,2,6,6,6,1,],
[2,2,8,2,6,6,6,2,],
[2,2,8,2,6,6,6,3,],
[3,2,8,2,6,6,6,0,],
[3,2,8,2,6,6,6,1,],
[3,2,8,2,6,6,6,2,],
[3,2,8,2,6,6,6,3,],
[2,2,8,2,7,6,6,0,],
[2,2,8,2,7,6,6,1,],
[2,2,8,2,7,6,6,2,],
[2,2,8,2,7,6,6,3,],
[3,2,8,2,7,6,6,0,],
[3,2,8,2,7,6,6,1,],
[3,2,8,2,7,6,6,2,],
[3,2,8,2,7,6,6,3,],
[2,2,8,2,10,6,6,0,],
[2,2,8,2,10,6,6,1,],
[2,2,8,2,10,6,6,2,],
[2,2,8,2,10,6,6,3,],
[3,2,8,2,10,6,6,0,],
[3,2,8,2,10,6,6,1,],
[3,2,8,2,10,6,6,2,],
[3,2,8,2,10,6,6,3,],
[2,2,8,2,12,6,6,0,],
[2,2,8,2,12,6,6,1,],
[2,2,8,2,12,6,6,2,],
[2,2,8,2,12,6,6,3,],
[3,2,8,2,12,6,6,0,],
[3,2,8,2,12,6,6,1,],
[3,2,8,2,12,6,6,2,],
[3,2,8,2,12,6,6,3,],
[1,1,10,8,6,6,1,0,],
[1,1,10,8,6,6,1,1,],
[1,1,10,8,6,6,1,2,],
[1,1,10,8,6,6,1,3,],
[1,1,10,8,6,6,1,4,],
[2,1,10,8,6,6,1,0,],
[2,1,10,8,6,6,1,1,],
[2,1,10,8,6,6,1,2,],
[2,1,10,8,6,6,1,3,],
[2,1,10,8,6,6,1,4,],
[1,1,10,8,7,6,1,0,],
[1,1,10,8,7,6,1,1,],
[1,1,10,8,7,6,1,2,],
[1,1,10,8,7,6,1,3,],
[1,1,10,8,7,6,1,4,],
[2,1,10,8,7,6,1,0,],
[2,1,10,8,7,6,1,1,],
[2,1,10,8,7,6,1,2,],
[2,1,10,8,7,6,1,3,],
[2,1,10,8,7,6,1,4,],
[1,1,10,8,10,6,1,0,],
[1,1,10,8,10,6,1,1,],
[1,1,10,8,10,6,1,2,],
[1,1,10,8,10,6,1,3,],
[1,1,10,8,10,6,1,4,],
[2,1,10,8,10,6,1,0,],
[2,1,10,8,10,6,1,1,],
[2,1,10,8,10,6,1,2,],
[2,1,10,8,10,6,1,3,],
[2,1,10,8,10,6,1,4,],
[1,1,10,8,12,6,1,0,],
[1,1,10,8,12,6,1,1,],
[1,1,10,8,12,6,1,2,],
[1,1,10,8,12,6,1,3,],
[1,1,10,8,12,6,1,4,],
[2,1,10,8,12,6,1,0,],
[2,1,10,8,12,6,1,1,],
[2,1,10,8,12,6,1,2,],
[2,1,10,8,12,6,1,3,],
[2,1,10,8,12,6,1,4,],
[1,1,10,8,6,6,3,0,],
[1,1,10,8,6,6,3,1,],
[1,1,10,8,6,6,3,2,],
[1,1,10,8,6,6,3,3,],
[1,1,10,8,6,6,3,4,],
[2,1,10,8,6,6,3,0,],
[2,1,10,8,6,6,3,1,],
[2,1,10,8,6,6,3,2,],
[2,1,10,8,6,6,3,3,],
[2,1,10,8,6,6,3,4,],
[1,1,10,8,7,6,3,0,],
[1,1,10,8,7,6,3,1,],
[1,1,10,8,7,6,3,2,],
[1,1,10,8,7,6,3,3,],
[1,1,10,8,7,6,3,4,],
[2,1,10,8,7,6,3,0,],
[2,1,10,8,7,6,3,1,],
[2,1,10,8,7,6,3,2,],
[2,1,10,8,7,6,3,3,],
[2,1,10,8,7,6,3,4,],
[1,1,10,8,10,6,3,0,],
[1,1,10,8,10,6,3,1,],
[1,1,10,8,10,6,3,2,],
[1,1,10,8,10,6,3,3,],
[1,1,10,8,10,6,3,4,],
[2,1,10,8,10,6,3,0,],
[2,1,10,8,10,6,3,1,],
[2,1,10,8,10,6,3,2,],
[2,1,10,8,10,6,3,3,],
[2,1,10,8,10,6,3,4,],
[1,1,10,8,12,6,3,0,],
[1,1,10,8,12,6,3,1,],
[1,1,10,8,12,6,3,2,],
[1,1,10,8,12,6,3,3,],
[1,1,10,8,12,6,3,4,],
[2,1,10,8,12,6,3,0,],
[2,1,10,8,12,6,3,1,],
[2,1,10,8,12,6,3,2,],
[2,1,10,8,12,6,3,3,],
[2,1,10,8,12,6,3,4,],
[1,1,10,8,6,6,6,0,],
[1,1,10,8,6,6,6,1,],
[1,1,10,8,6,6,6,2,],
[1,1,10,8,6,6,6,3,],
[1,1,10,8,6,6,6,4,],
[2,1,10,8,6,6,6,0,],
[2,1,10,8,6,6,6,1,],
[2,1,10,8,6,6,6,2,],
[2,1,10,8,6,6,6,3,],
[2,1,10,8,6,6,6,4,],
[1,1,10,8,7,6,6,0,],
[1,1,10,8,7,6,6,1,],
[1,1,10,8,7,6,6,2,],
[1,1,10,8,7,6,6,3,],
[1,1,10,8,7,6,6,4,],
[2,1,10,8,7,6,6,0,],
[2,1,10,8,7,6,6,1,],
[2,1,10,8,7,6,6,2,],
[2,1,10,8,7,6,6,3,],
[2,1,10,8,7,6,6,4,],
[1,1,10,8,10,6,6,0,],
[1,1,10,8,10,6,6,1,],
[1,1,10,8,10,6,6,2,],
[1,1,10,8,10,6,6,3,],
[1,1,10,8,10,6,6,4,],
[2,1,10,8,10,6,6,0,],
[2,1,10,8,10,6,6,1,],
[2,1,10,8,10,6,6,2,],
[2,1,10,8,10,6,6,3,],
[2,1,10,8,10,6,6,4,],
[1,1,10,8,12,6,6,0,],
[1,1,10,8,12,6,6,1,],
[1,1,10,8,12,6,6,2,],
[1,1,10,8,12,6,6,3,],
[1,1,10,8,12,6,6,4,],
[2,1,10,8,12,6,6,0,],
[2,1,10,8,12,6,6,1,],
[2,1,10,8,12,6,6,2,],
[2,1,10,8,12,6,6,3,],
[2,1,10,8,12,6,6,4,],
[1,1,12,6,6,6,1,0,],
[1,1,12,6,6,6,1,1,],
[1,1,12,6,6,6,1,2,],
[1,1,12,6,6,6,1,3,],
[1,1,12,6,6,6,1,4,],
[1,1,12,6,6,6,1,5,],
[2,1,12,6,6,6,1,0,],
[2,1,12,6,6,6,1,1,],
[2,1,12,6,6,6,1,2,],
[2,1,12,6,6,6,1,3,],
[2,1,12,6,6,6,1,4,],
[2,1,12,6,6,6,1,5,],
[1,1,12,6,7,6,1,0,],
[1,1,12,6,7,6,1,1,],
[1,1,12,6,7,6,1,2,],
[1,1,12,6,7,6,1,3,],
[1,1,12,6,7,6,1,4,],
[1,1,12,6,7,6,1,5,],
[2,1,12,6,7,6,1,0,],
[2,1,12,6,7,6,1,1,],
[2,1,12,6,7,6,1,2,],
[2,1,12,6,7,6,1,3,],
[2,1,12,6,7,6,1,4,],
[2,1,12,6,7,6,1,5,],
[1,1,12,6,10,6,1,0,],
[1,1,12,6,10,6,1,1,],
[1,1,12,6,10,6,1,2,],
[1,1,12,6,10,6,1,3,],
[1,1,12,6,10,6,1,4,],
[1,1,12,6,10,6,1,5,],
[2,1,12,6,10,6,1,0,],
[2,1,12,6,10,6,1,1,],
[2,1,12,6,10,6,1,2,],
[2,1,12,6,10,6,1,3,],
[2,1,12,6,10,6,1,4,],
[2,1,12,6,10,6,1,5,],
[1,1,12,6,12,6,1,0,],
[1,1,12,6,12,6,1,1,],
[1,1,12,6,12,6,1,2,],
[1,1,12,6,12,6,1,3,],
[1,1,12,6,12,6,1,4,],
[1,1,12,6,12,6,1,5,],
[2,1,12,6,12,6,1,0,],
[2,1,12,6,12,6,1,1,],
[2,1,12,6,12,6,1,2,],
[2,1,12,6,12,6,1,3,],
[2,1,12,6,12,6,1,4,],
[2,1,12,6,12,6,1,5,],
[1,1,12,6,6,6,3,0,],
[1,1,12,6,6,6,3,1,],
[1,1,12,6,6,6,3,2,],
[1,1,12,6,6,6,3,3,],
[1,1,12,6,6,6,3,4,],
[1,1,12,6,6,6,3,5,],
[2,1,12,6,6,6,3,0,],
[2,1,12,6,6,6,3,1,],
[2,1,12,6,6,6,3,2,],
[2,1,12,6,6,6,3,3,],
[2,1,12,6,6,6,3,4,],
[2,1,12,6,6,6,3,5,],
[1,1,12,6,7,6,3,0,],
[1,1,12,6,7,6,3,1,],
[1,1,12,6,7,6,3,2,],
[1,1,12,6,7,6,3,3,],
[1,1,12,6,7,6,3,4,],
[1,1,12,6,7,6,3,5,],
[2,1,12,6,7,6,3,0,],
[2,1,12,6,7,6,3,1,],
[2,1,12,6,7,6,3,2,],
[2,1,12,6,7,6,3,3,],
[2,1,12,6,7,6,3,4,],
[2,1,12,6,7,6,3,5,],
[1,1,12,6,10,6,3,0,],
[1,1,12,6,10,6,3,1,],
[1,1,12,6,10,6,3,2,],
[1,1,12,6,10,6,3,3,],
[1,1,12,6,10,6,3,4,],
[1,1,12,6,10,6,3,5,],
[2,1,12,6,10,6,3,0,],
[2,1,12,6,10,6,3,1,],
[2,1,12,6,10,6,3,2,],
[2,1,12,6,10,6,3,3,],
[2,1,12,6,10,6,3,4,],
[2,1,12,6,10,6,3,5,],
[1,1,12,6,12,6,3,0,],
[1,1,12,6,12,6,3,1,],
[1,1,12,6,12,6,3,2,],
[1,1,12,6,12,6,3,3,],
[1,1,12,6,12,6,3,4,],
[1,1,12,6,12,6,3,5,],
[2,1,12,6,12,6,3,0,],
[2,1,12,6,12,6,3,1,],
[2,1,12,6,12,6,3,2,],
[2,1,12,6,12,6,3,3,],
[2,1,12,6,12,6,3,4,],
[2,1,12,6,12,6,3,5,],
[1,1,12,6,6,6,6,0,],
[1,1,12,6,6,6,6,1,],
[1,1,12,6,6,6,6,2,],
[1,1,12,6,6,6,6,3,],
[1,1,12,6,6,6,6,4,],
[1,1,12,6,6,6,6,5,],
[2,1,12,6,6,6,6,0,],
[2,1,12,6,6,6,6,1,],
[2,1,12,6,6,6,6,2,],
[2,1,12,6,6,6,6,3,],
[2,1,12,6,6,6,6,4,],
[2,1,12,6,6,6,6,5,],
[1,1,12,6,7,6,6,0,],
[1,1,12,6,7,6,6,1,],
[1,1,12,6,7,6,6,2,],
[1,1,12,6,7,6,6,3,],
[1,1,12,6,7,6,6,4,],
[1,1,12,6,7,6,6,5,],
[2,1,12,6,7,6,6,0,],
[2,1,12,6,7,6,6,1,],
[2,1,12,6,7,6,6,2,],
[2,1,12,6,7,6,6,3,],
[2,1,12,6,7,6,6,4,],
[2,1,12,6,7,6,6,5,],
[1,1,12,6,10,6,6,0,],
[1,1,12,6,10,6,6,1,],
[1,1,12,6,10,6,6,2,],
[1,1,12,6,10,6,6,3,],
[1,1,12,6,10,6,6,4,],
[1,1,12,6,10,6,6,5,],
[2,1,12,6,10,6,6,0,],
[2,1,12,6,10,6,6,1,],
[2,1,12,6,10,6,6,2,],
[2,1,12,6,10,6,6,3,],
[2,1,12,6,10,6,6,4,],
[2,1,12,6,10,6,6,5,],
[1,1,12,6,12,6,6,0,],
[1,1,12,6,12,6,6,1,],
[1,1,12,6,12,6,6,2,],
[1,1,12,6,12,6,6,3,],
[1,1,12,6,12,6,6,4,],
[1,1,12,6,12,6,6,5,],
[2,1,12,6,12,6,6,0,],
[2,1,12,6,12,6,6,1,],
[2,1,12,6,12,6,6,2,],
[2,1,12,6,12,6,6,3,],
[2,1,12,6,12,6,6,4,],
[2,1,12,6,12,6,6,5,],
[2,2,6,4,6,6,1,0,],
[2,2,6,4,6,6,1,1,],
[2,2,6,4,7,6,1,0,],
[2,2,6,4,7,6,1,1,],
[2,2,6,4,10,6,1,0,],
[2,2,6,4,10,6,1,1,],
[2,2,6,2,6,6,1,0,],
[2,2,6,2,6,6,1,1,],
[2,2,6,2,7,6,1,0,],
[2,2,6,2,7,6,1,1,],
[2,2,6,2,10,6,1,0,],
[2,2,6,2,10,6,1,1,],
[3,2,6,2,6,6,1,0,],
[3,2,6,2,6,6,1,1,],
[3,2,6,2,7,6,1,0,],
[3,2,6,2,7,6,1,1,],
[3,2,6,2,10,6,1,0,],
[3,2,6,2,10,6,1,1,],
[3,3,4,6,6,6,1,0,],
[3,3,4,6,7,6,1,0,],
[3,3,4,6,10,6,1,0,],
[3,3,4,6,12,6,1,0,],
[3,3,4,6,6,6,3,0,],
[3,3,4,6,7,6,3,0,],
[3,3,4,6,10,6,3,0,],
[3,3,4,6,12,6,3,0,],
[3,3,4,6,6,6,6,0,],
[3,3,4,6,7,6,6,0,],
[3,3,4,6,10,6,6,0,],
[3,3,4,6,12,6,6,0,],
[3,3,4,4,6,6,1,0,],
[3,3,4,4,7,6,1,0,],
[3,3,4,4,10,6,1,0,],
[3,3,4,4,12,6,1,0,],
[3,3,4,4,6,6,3,0,],
[3,3,4,4,7,6,3,0,],
[3,3,4,4,10,6,3,0,],
[3,3,4,4,12,6,3,0,],
[3,3,4,2,6,6,1,0,],
[3,3,4,2,7,6,1,0,],
[3,3,4,2,10,6,1,0,],
[3,3,4,2,12,6,1,0,],
[3,3,4,2,6,6,3,0,],
[3,3,4,2,7,6,3,0,],
[3,3,4,2,10,6,3,0,],
[3,3,4,2,12,6,3,0,],
[2,2,8,1,6,6,1,0,],
[2,2,8,1,7,6,1,0,],
[2,2,8,1,10,6,1,0,],
[2,2,8,1,12,6,1,0,],
[2,2,8,1,6,6,3,0,],
[2,2,8,1,7,6,3,0,],
[2,2,8,1,10,6,3,0,],
[2,2,8,1,12,6,3,0,],
[1,1,10,6,6,6,1,0,],
[1,1,10,6,6,6,1,1,],
[1,1,10,6,7,6,1,0,],
[1,1,10,6,7,6,1,1,],
[1,1,10,6,10,6,1,0,],
[1,1,10,6,10,6,1,1,],
[1,1,10,6,12,6,1,0,],
[1,1,10,6,12,6,1,1,],
[1,1,10,6,6,6,3,0,],
[1,1,10,6,6,6,3,1,],
[1,1,10,6,7,6,3,0,],
[1,1,10,6,7,6,3,1,],
[1,1,10,6,10,6,3,0,],
[1,1,10,6,10,6,3,1,],
[1,1,10,6,12,6,3,0,],
[1,1,10,6,12,6,3,1,],
[1,1,10,4,6,6,1,0,],
[1,1,10,4,6,6,1,1,],
[1,1,10,4,7,6,1,0,],
[1,1,10,4,7,6,1,1,],
[1,1,10,4,10,6,1,0,],
[1,1,10,4,10,6,1,1,],
[1,1,10,4,12,6,1,0,],
[1,1,10,4,12,6,1,1,],
[1,1,10,4,6,6,3,0,],
[1,1,10,4,6,6,3,1,],
[1,1,10,4,7,6,3,0,],
[1,1,10,4,7,6,3,1,],
[1,1,10,4,10,6,3,0,],
[1,1,10,4,10,6,3,1,],
[1,1,10,4,12,6,3,0,],
[1,1,10,4,12,6,3,1,],
[1,1,10,2,6,6,1,0,],
[1,1,10,2,6,6,1,1,],
[1,1,10,2,7,6,1,0,],
[1,1,10,2,7,6,1,1,],
[1,1,10,2,10,6,1,0,],
[1,1,10,2,10,6,1,1,],
[1,1,10,2,12,6,1,0,],
[1,1,10,2,12,6,1,1,],
[1,1,10,2,6,6,3,0,],
[1,1,10,2,6,6,3,1,],
[1,1,10,2,7,6,3,0,],
[1,1,10,2,7,6,3,1,],
[1,1,10,2,10,6,3,0,],
[1,1,10,2,10,6,3,1,],
[1,1,10,2,12,6,3,0,],
[1,1,10,2,12,6,3,1,],
[1,1,8,8,6,6,1,0,],
[1,1,8,8,6,6,1,1,],
[1,1,8,8,7,6,1,0,],
[1,1,8,8,7,6,1,1,],
[1,1,8,8,10,6,1,0,],
[1,1,8,8,10,6,1,1,],
[1,1,8,8,12,6,1,0,],
[1,1,8,8,12,6,1,1,],
[1,1,8,8,6,6,3,0,],
[1,1,8,8,6,6,3,1,],
[1,1,8,8,7,6,3,0,],
[1,1,8,8,7,6,3,1,],
[1,1,8,8,10,6,3,0,],
[1,1,8,8,10,6,3,1,],
[1,1,8,8,12,6,3,0,],
[1,1,8,8,12,6,3,1,],
[1,1,8,6,6,6,1,0,],
[1,1,8,6,6,6,1,1,],
[1,1,8,6,7,6,1,0,],
[1,1,8,6,7,6,1,1,],
[1,1,8,6,10,6,1,0,],
[1,1,8,6,10,6,1,1,],
[1,1,8,6,12,6,1,0,],
[1,1,8,6,12,6,1,1,],
[1,1,8,6,6,6,3,0,],
[1,1,8,6,6,6,3,1,],
[1,1,8,6,7,6,3,0,],
[1,1,8,6,7,6,3,1,],
[1,1,8,6,10,6,3,0,],
[1,1,8,6,10,6,3,1,],
[1,1,8,6,12,6,3,0,],
[1,1,8,6,12,6,3,1,],
[1,1,8,4,6,6,1,0,],
[1,1,8,4,6,6,1,1,],
[1,1,8,4,7,6,1,0,],
[1,1,8,4,7,6,1,1,],
[1,1,8,4,10,6,1,0,],
[1,1,8,4,10,6,1,1,],
[1,1,8,4,12,6,1,0,],
[1,1,8,4,12,6,1,1,],
[1,1,8,4,6,6,3,0,],
[1,1,8,4,6,6,3,1,],
[1,1,8,4,7,6,3,0,],
[1,1,8,4,7,6,3,1,],
[1,1,8,4,10,6,3,0,],
[1,1,8,4,10,6,3,1,],
[1,1,8,4,12,6,3,0,],
[1,1,8,4,12,6,3,1,],
[2,2,4,8,6,6,1,0,],
[2,2,4,8,7,6,1,0,],
[2,2,4,8,10,6,1,0,],
[2,2,4,8,12,6,1,0,],
[2,2,4,8,6,6,3,0,],
[2,2,4,8,7,6,3,0,],
[2,2,4,8,10,6,3,0,],
[2,2,4,8,12,6,3,0,],
[2,2,4,8,6,6,6,0,],
[2,2,4,8,7,6,6,0,],
[2,2,4,8,10,6,6,0,],
[2,2,4,8,12,6,6,0,],
[2,2,4,6,6,6,1,0,],
[2,2,4,6,7,6,1,0,],
[2,2,4,6,10,6,1,0,],
[2,2,4,6,12,6,1,0,],
[2,2,4,6,6,6,3,0,],
[2,2,4,6,7,6,3,0,],
[2,2,4,6,10,6,3,0,],
[2,2,4,6,12,6,3,0,],
[2,2,4,6,6,6,6,0,],
[2,2,4,6,7,6,6,0,],
[2,2,4,6,10,6,6,0,],
[2,2,4,6,12,6,6,0,],
[2,2,4,4,6,6,1,0,],
[2,2,4,4,7,6,1,0,],
[2,2,4,4,10,6,1,0,],
[2,2,4,4,12,6,1,0,],
[2,2,4,4,6,6,3,0,],
[2,2,4,4,7,6,3,0,],
[2,2,4,4,10,6,3,0,],
[2,2,4,4,12,6,3,0,],
[2,2,4,4,6,6,6,0,],
[2,2,4,4,7,6,6,0,],
[2,2,4,4,10,6,6,0,],
[2,2,4,4,12,6,6,0,],
[4,3,4,6,6,6,1,0,],
[4,3,4,6,7,6,1,0,],
[4,3,4,6,10,6,1,0,],
[4,3,4,6,12,6,1,0,],
[4,3,4,6,6,6,3,0,],
[4,3,4,6,7,6,3,0,],
[4,3,4,6,10,6,3,0,],
[4,3,4,6,12,6,3,0,],
[4,3,4,6,6,6,6,0,],
[4,3,4,6,7,6,6,0,],
[4,3,4,6,10,6,6,0,],
[4,3,4,6,12,6,6,0,],
[4,3,4,4,6,6,1,0,],
[4,3,4,4,7,6,1,0,],
[4,3,4,4,10,6,1,0,],
[4,3,4,4,12,6,1,0,],
[4,3,4,4,6,6,3,0,],
[4,3,4,4,7,6,3,0,],
[4,3,4,4,10,6,3,0,],
[4,3,4,4,12,6,3,0,],
[4,3,4,2,6,6,1,0,],
[4,3,4,2,7,6,1,0,],
[4,3,4,2,10,6,1,0,],
[4,3,4,2,12,6,1,0,],
[4,3,4,2,6,6,3,0,],
[4,3,4,2,7,6,3,0,],
[4,3,4,2,10,6,3,0,],
[4,3,4,2,12,6,3,0,],
[5,3,4,6,6,6,1,0,],
[5,3,4,6,7,6,1,0,],
[5,3,4,6,10,6,1,0,],
[5,3,4,6,12,6,1,0,],
[5,3,4,6,6,6,3,0,],
[5,3,4,6,7,6,3,0,],
[5,3,4,6,10,6,3,0,],
[5,3,4,6,12,6,3,0,],
[5,3,4,6,6,6,6,0,],
[5,3,4,6,7,6,6,0,],
[5,3,4,6,10,6,6,0,],
[5,3,4,6,12,6,6,0,],
[5,3,4,4,6,6,1,0,],
[5,3,4,4,7,6,1,0,],
[5,3,4,4,10,6,1,0,],
[5,3,4,4,12,6,1,0,],
[5,3,4,4,6,6,3,0,],
[5,3,4,4,7,6,3,0,],
[5,3,4,4,10,6,3,0,],
[5,3,4,4,12,6,3,0,],
[5,3,4,2,6,6,1,0,],
[5,3,4,2,7,6,1,0,],
[5,3,4,2,10,6,1,0,],
[5,3,4,2,12,6,1,0,],
[5,3,4,2,6,6,3,0,],
[5,3,4,2,7,6,3,0,],
[5,3,4,2,10,6,3,0,],
[5,3,4,2,12,6,3,0,],
[4,2,6,4,6,6,1,0,],
[4,2,6,4,6,6,1,1,],
[4,2,6,4,7,6,1,0,],
[4,2,6,4,7,6,1,1,],
[4,2,6,4,10,6,1,0,],
[4,2,6,4,10,6,1,1,],
[4,2,6,2,6,6,1,0,],
[4,2,6,2,6,6,1,1,],
[4,2,6,2,7,6,1,0,],
[4,2,6,2,7,6,1,1,],
[4,2,6,2,10,6,1,0,],
[4,2,6,2,10,6,1,1,],
[3,2,4,8,6,6,1,0,],
[3,2,4,8,7,6,1,0,],
[3,2,4,8,10,6,1,0,],
[3,2,4,8,12,6,1,0,],
[3,2,4,8,6,6,3,0,],
[3,2,4,8,7,6,3,0,],
[3,2,4,8,10,6,3,0,],
[3,2,4,8,12,6,3,0,],
[3,2,4,8,6,6,6,0,],
[3,2,4,8,7,6,6,0,],
[3,2,4,8,10,6,6,0,],
[3,2,4,8,12,6,6,0,],
[3,2,4,6,6,6,1,0,],
[3,2,4,6,7,6,1,0,],
[3,2,4,6,10,6,1,0,],
[3,2,4,6,12,6,1,0,],
[3,2,4,6,6,6,3,0,],
[3,2,4,6,7,6,3,0,],
[3,2,4,6,10,6,3,0,],
[3,2,4,6,12,6,3,0,],
[3,2,4,6,6,6,6,0,],
[3,2,4,6,7,6,6,0,],
[3,2,4,6,10,6,6,0,],
[3,2,4,6,12,6,6,0,],
[3,2,4,4,6,6,1,0,],
[3,2,4,4,7,6,1,0,],
[3,2,4,4,10,6,1,0,],
[3,2,4,4,12,6,1,0,],
[3,2,4,4,6,6,3,0,],
[3,2,4,4,7,6,3,0,],
[3,2,4,4,10,6,3,0,],
[3,2,4,4,12,6,3,0,],
[3,2,4,4,6,6,6,0,],
[3,2,4,4,7,6,6,0,],
[3,2,4,4,10,6,6,0,],
[3,2,4,4,12,6,6,0,],
[4,2,4,8,6,6,1,0,],
[4,2,4,8,7,6,1,0,],
[4,2,4,8,10,6,1,0,],
[4,2,4,8,12,6,1,0,],
[4,2,4,8,6,6,3,0,],
[4,2,4,8,7,6,3,0,],
[4,2,4,8,10,6,3,0,],
[4,2,4,8,12,6,3,0,],
[4,2,4,8,6,6,6,0,],
[4,2,4,8,7,6,6,0,],
[4,2,4,8,10,6,6,0,],
[4,2,4,8,12,6,6,0,],
[4,2,4,6,6,6,1,0,],
[4,2,4,6,7,6,1,0,],
[4,2,4,6,10,6,1,0,],
[4,2,4,6,12,6,1,0,],
[4,2,4,6,6,6,3,0,],
[4,2,4,6,7,6,3,0,],
[4,2,4,6,10,6,3,0,],
[4,2,4,6,12,6,3,0,],
[4,2,4,6,6,6,6,0,],
[4,2,4,6,7,6,6,0,],
[4,2,4,6,10,6,6,0,],
[4,2,4,6,12,6,6,0,],
[4,2,4,4,6,6,1,0,],
[4,2,4,4,7,6,1,0,],
[4,2,4,4,10,6,1,0,],
[4,2,4,4,12,6,1,0,],
[4,2,4,4,6,6,3,0,],
[4,2,4,4,7,6,3,0,],
[4,2,4,4,10,6,3,0,],
[4,2,4,4,12,6,3,0,],
[4,2,4,4,6,6,6,0,],
[4,2,4,4,7,6,6,0,],
[4,2,4,4,10,6,6,0,],
[4,2,4,4,12,6,6,0,],
[2,1,10,6,6,6,1,0,],
[2,1,10,6,6,6,1,1,],
[2,1,10,6,7,6,1,0,],
[2,1,10,6,7,6,1,1,],
[2,1,10,6,10,6,1,0,],
[2,1,10,6,10,6,1,1,],
[2,1,10,6,12,6,1,0,],
[2,1,10,6,12,6,1,1,],
[2,1,10,6,6,6,3,0,],
[2,1,10,6,6,6,3,1,],
[2,1,10,6,7,6,3,0,],
[2,1,10,6,7,6,3,1,],
[2,1,10,6,10,6,3,0,],
[2,1,10,6,10,6,3,1,],
[2,1,10,6,12,6,3,0,],
[2,1,10,6,12,6,3,1,],
[2,1,10,4,6,6,1,0,],
[2,1,10,4,6,6,1,1,],
[2,1,10,4,7,6,1,0,],
[2,1,10,4,7,6,1,1,],
[2,1,10,4,10,6,1,0,],
[2,1,10,4,10,6,1,1,],
[2,1,10,4,12,6,1,0,],
[2,1,10,4,12,6,1,1,],
[2,1,10,4,6,6,3,0,],
[2,1,10,4,6,6,3,1,],
[2,1,10,4,7,6,3,0,],
[2,1,10,4,7,6,3,1,],
[2,1,10,4,10,6,3,0,],
[2,1,10,4,10,6,3,1,],
[2,1,10,4,12,6,3,0,],
[2,1,10,4,12,6,3,1,],
[2,1,10,2,6,6,1,0,],
[2,1,10,2,6,6,1,1,],
[2,1,10,2,7,6,1,0,],
[2,1,10,2,7,6,1,1,],
[2,1,10,2,10,6,1,0,],
[2,1,10,2,10,6,1,1,],
[2,1,10,2,12,6,1,0,],
[2,1,10,2,12,6,1,1,],
[2,1,10,2,6,6,3,0,],
[2,1,10,2,6,6,3,1,],
[2,1,10,2,7,6,3,0,],
[2,1,10,2,7,6,3,1,],
[2,1,10,2,10,6,3,0,],
[2,1,10,2,10,6,3,1,],
[2,1,10,2,12,6,3,0,],
[2,1,10,2,12,6,3,1,],
[2,1,8,8,6,6,1,0,],
[2,1,8,8,6,6,1,1,],
[2,1,8,8,7,6,1,0,],
[2,1,8,8,7,6,1,1,],
[2,1,8,8,10,6,1,0,],
[2,1,8,8,10,6,1,1,],
[2,1,8,8,12,6,1,0,],
[2,1,8,8,12,6,1,1,],
[2,1,8,8,6,6,3,0,],
[2,1,8,8,6,6,3,1,],
[2,1,8,8,7,6,3,0,],
[2,1,8,8,7,6,3,1,],
[2,1,8,8,10,6,3,0,],
[2,1,8,8,10,6,3,1,],
[2,1,8,8,12,6,3,0,],
[2,1,8,8,12,6,3,1,],
[2,1,8,6,6,6,1,0,],
[2,1,8,6,6,6,1,1,],
[2,1,8,6,7,6,1,0,],
[2,1,8,6,7,6,1,1,],
[2,1,8,6,10,6,1,0,],
[2,1,8,6,10,6,1,1,],
[2,1,8,6,12,6,1,0,],
[2,1,8,6,12,6,1,1,],
[2,1,8,6,6,6,3,0,],
[2,1,8,6,6,6,3,1,],
[2,1,8,6,7,6,3,0,],
[2,1,8,6,7,6,3,1,],
[2,1,8,6,10,6,3,0,],
[2,1,8,6,10,6,3,1,],
[2,1,8,6,12,6,3,0,],
[2,1,8,6,12,6,3,1,],
[2,1,8,4,6,6,1,0,],
[2,1,8,4,6,6,1,1,],
[2,1,8,4,7,6,1,0,],
[2,1,8,4,7,6,1,1,],
[2,1,8,4,10,6,1,0,],
[2,1,8,4,10,6,1,1,],
[2,1,8,4,12,6,1,0,],
[2,1,8,4,12,6,1,1,],
[2,1,8,4,6,6,3,0,],
[2,1,8,4,6,6,3,1,],
[2,1,8,4,7,6,3,0,],
[2,1,8,4,7,6,3,1,],
[2,1,8,4,10,6,3,0,],
[2,1,8,4,10,6,3,1,],
[2,1,8,4,12,6,3,0,],
[2,1,8,4,12,6,3,1,]]

# num_dice
# keep_dice
# dice_type
# add_val
# num_attribute
# keep_attribute
# num_arrays
# reroll

for system in ["pf", "3e", "4e"]:
    big_res = []
    for roll_low_limit in [None, 5, 8]:
        for ii, comb in enumerate(inputs):
            try:
                pbe_gen = PBE(comb[0], comb[2], comb[3], comb[4], comb[6], comb[7],
                              comb[1], comb[5], pbe_map=system, 
                              roll_low_limit=roll_low_limit)
                pbe_gen.roll_mc(10**5)
                res = pbe_gen.get_results()
                res.append(comb)
                res.append(roll_low_limit)
                res.append("")
                big_res.append(res) 
                print(ii)
            except Exception as e:
                print(e)
                pass
    for pbe_low_limit in [None, 0, 10, 15, 20]:
        for ii, comb in enumerate(inputs):
            try:
                pbe_gen = PBE(comb[0], comb[2], comb[3], comb[4], comb[6], comb[7],
                              comb[1], comb[5], pbe_map=system, 
                              pbe_low_limit=pbe_low_limit)
                pbe_gen.roll_mc(10**5)
                res = pbe_gen.get_results()
                res.append(comb)
                res.append("")
                res.append(pbe_low_limit)
                big_res.append(res)    
                print(ii)
            except Exception as e:
                print(e)
                pass
    df = pd.DataFrame(big_res)
    df.columns = ["Description", "Typical Array", "Mean", "Standard Deviation", 
                  "5%", "95%", "Input", "Roll Low Limit", "PBE Low Limit"]
    df.to_csv('pypbe-rec_results_' + system + '.csv')