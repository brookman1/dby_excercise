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


def json_output_optimal_order(input_s):
  """
  input_s: proper JSONstring, the comman that was on line 7 won't pass.
  """
  input_list = json.loads(input_s)
  return json.dumps(optimal_order_output2(input_list))
  
if __name__ == '__main__':
  print(json_output_optimal_order(input_s).replace('}, ', '},\n'))
  #pprint.pprint(optimal_order_output2(input_list)) 