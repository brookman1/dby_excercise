import json
from optimal_order import optimal_order_output, optimal_order_output2
import pprint
"""
String below: comma(,) removed on line 6 to make JSON compliant 
"""
input_s = """[
  {
    "name": "Accessories",
    "id": 1,
    "parent_id": 20
  },
  {
    "name": "Watches",
    "id": 57,
    "parent_id": 1
  },
  {
    "name": "Men",
    "id": 20,
    "parent_id": null
  }
]"""


    
input_list = json.loads(input_s)
print('output ready:')
pprint.pprint(optimal_order_output2(input_list)) 