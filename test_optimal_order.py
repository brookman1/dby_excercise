import unittest

import optimal_order

class TestOptimalOrderOutput(unittest.TestCase):
  def setUp(self):
    self.test_input = input = [
            {
              "name": "Accessories",
              "id": 1,
              "parent_id": 20
            }
          ,
            {
              "name": "Watches",
              "id": 57,
              "parent_id": 1
            }
          ,
            {
              "name": "Men",
              "id": 20,
              "parent_id": None
            }
          ,
          ]
          
    self.saved_input = self.test_input[:]
  def tearDown(self):
    self.test_input = self.saved_input[:]
  
  def test_provided_testcaste(self):
    expected = [{'id': 20, 'name': 'Men', 'parent_id': None}
               , {'id': 1, 'name': 'Accessories', 'parent_id': 20}
               , {'id': 57, 'name': 'Watches', 'parent_id': 1}
               , ]
    actual = optimal_order.optimal_order_output(self.test_input)
    self.assertEquals(actual, expected)

  def test_two_roots(self):
    expected = [{'id': 20, 'name': 'Men', 'parent_id': None}
              , {'id': 4, 'name': 'Boys', 'parent_id': None}
              , {'id': 1, 'name': 'Accessories', 'parent_id': 20}
              , {'id': 57, 'name': 'Watches', 'parent_id': 1}
              , ]
    self.test_input.append({'id':4, 'name': 'Boys', 'parent_id': None, })
    actual = optimal_order.optimal_order_output(self.test_input)
    self.assertEquals(actual, expected)
    #'''
    
  def test_two_from_root_node(self):
    expected = [{'id': 20, 'name': 'Men', 'parent_id': None}
              , {'id': 1, 'name': 'Accessories', 'parent_id': 20}
              , {'id': 4, 'name': 'Boys', 'parent_id': 20}
              , {'id': 57, 'name': 'Watches', 'parent_id': 1}

              , ]
    self.test_input.append({'id':4, 'name': 'Boys', 'parent_id': 20, })
    actual = optimal_order.optimal_order_output(self.test_input)
    self.assertEquals(actual, expected)
    
  def test_add_another_from_split(self):    
    expected = [{'id': 20, 'name': 'Men', 'parent_id': None}
              , {'id': 1, 'name': 'Accessories', 'parent_id': 20}
              , {'id': 4, 'name': 'Boys', 'parent_id': 20}
              , {'id': 57, 'name': 'Watches', 'parent_id': 1}
              , {'id':5, 'name': 'Boys to Men', 'parent_id': 4,}
              , ]
    self.test_input.append({'id':4, 'name': 'Boys', 'parent_id': 20, })
    self.test_input.append({'id':5, 'name': 'Boys to Men', 'parent_id': 4,})
    actual = optimal_order.optimal_order_output(self.test_input)
    self.assertEquals(actual, expected)


class TestOptimalOrderOutput2(unittest.TestCase):
  def setUp(self):
    self.test_input = input = [
            {
              "name": "Accessories",
              "id": 1,
              "parent_id": 20
            }
          ,
            {
              "name": "Watches",
              "id": 57,
              "parent_id": 1
            }
          ,
            {
              "name": "Men",
              "id": 20,
              "parent_id": None
            }
          ,
          ]
          
    self.saved_input = self.test_input[:]
  def tearDown(self):
    self.test_input = self.saved_input[:]
  
  def test_provided_testcaste(self):
    expected = [{'id': 20, 'name': 'Men', 'parent_id': None}
               , {'id': 1, 'name': 'Accessories', 'parent_id': 20}
               , {'id': 57, 'name': 'Watches', 'parent_id': 1}
               , ]
    actual = optimal_order.optimal_order_output2(self.test_input)
    self.assertEquals(actual, expected)

  def test_two_roots(self):
    expected = [{'id': 20, 'name': 'Men', 'parent_id': None}
              , {'id': 4, 'name': 'Boys', 'parent_id': None}
              , {'id': 1, 'name': 'Accessories', 'parent_id': 20}
              , {'id': 57, 'name': 'Watches', 'parent_id': 1}
              , ]
    self.test_input.append({'id':4, 'name': 'Boys', 'parent_id': None, })
    actual = optimal_order.optimal_order_output2(self.test_input)
    self.assertEquals(actual, expected)
    #'''
    
  def test_two_from_root_node(self):
    expected = [{'id': 20, 'name': 'Men', 'parent_id': None}
              , {'id': 1, 'name': 'Accessories', 'parent_id': 20}
              , {'id': 4, 'name': 'Boys', 'parent_id': 20}
              , {'id': 57, 'name': 'Watches', 'parent_id': 1}

              , ]
    self.test_input.append({'id':4, 'name': 'Boys', 'parent_id': 20, })
    actual = optimal_order.optimal_order_output2(self.test_input)
    self.assertEquals(actual, expected)
    
  def test_add_another_from_split(self):    
    expected = [{'id': 20, 'name': 'Men', 'parent_id': None}
              , {'id': 1, 'name': 'Accessories', 'parent_id': 20}
              , {'id': 4, 'name': 'Boys', 'parent_id': 20}
              , {'id': 57, 'name': 'Watches', 'parent_id': 1}
              , {'id':5, 'name': 'Boys to Men', 'parent_id': 4,}
              , ]
    self.test_input.append({'id':4, 'name': 'Boys', 'parent_id': 20, })
    self.test_input.append({'id':5, 'name': 'Boys to Men', 'parent_id': 4,})
    actual = optimal_order.optimal_order_output2(self.test_input)
    self.assertEquals(actual, expected)

    
if __name__ == '__main__':
  unittest.main()