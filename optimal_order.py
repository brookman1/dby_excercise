'''
two solutions to excercise:
optimal_order_output
optimal_order_output2 -- memory efficient solution
'''

def optimal_order_output(input_list):
  """
  input is treated as immutable.  output is a list in optimal insert order.
  """
  pid_idx_dict = {}
  output_list = []
  out_ids = set()

  for idx, i in enumerate(input_list):
    _id, pid = i.get('id', None), i.get('parent_id', None)
    if not pid:
      output_list.append(i)
      out_ids.add(i['id'])
      continue

    child_list = pid_idx_dict.get(pid)
    if child_list:
      child_list.append(idx)
    else:
      pid_idx_dict[pid] = [
          idx,
      ]

  items = []
  while True:
    for i in out_ids:
      #print('children: ', i, pid_idx_dict.get(i, []))
      more_items = [input_list[a] for a in pid_idx_dict.get(i, [])]
      if more_items:
        items.extend(more_items)

    if items:
      output_list.extend(items)
    else:
      break
    out_ids = set([i.get('id') for i in items])
    items = []
  return output_list


def optimal_order_output2(input_list):
  """
  input is treated as mutable.  output is a list in optimal insert order.
  after this function returns input_list is empty.
  input_list: mutable list of named pairs with id and parent_id order.
  """
  pid_item_dict = {}

  output_list = []
  out_ids = set()

  while input_list:
    i = input_list[0]
    input_list.pop(0)
    _id, pid = i.get('id', None), i.get('parent_id', None)
    if not pid:
      output_list.append(i)
      out_ids.add(i['id'])
      continue

    child_list = pid_item_dict.get(pid)
    if child_list:
      child_list.append(i)
    else:
      pid_item_dict[pid] = [
          i,
      ]

  items = []
  while True:
    for i in out_ids:
      #print('children: ', i, pid_idx_dict.get(i, []))
      more_items = pid_item_dict.get(i, [])
      if more_items:
        pid_item_dict.pop(i)
        items.extend(more_items)

    if items:
      output_list.extend(items)
    else:
      break
    out_ids = set([i.get('id') for i in items])
    items = []
  return output_list
