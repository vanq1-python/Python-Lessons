def calculate_structure_sum(data_structure):
  total_sum = 0
  for item in data_structure:
      if isinstance(item, (list, tuple, set)):
          total_sum += calculate_structure_sum(item)
      elif isinstance(item, dict):
          for key, value in item.items():
              if isinstance(key, str):
                  total_sum += len(key)
              else:
                  total_sum += key
              if isinstance(value, str):
                  total_sum += len(value)
              else:
                  total_sum += value
      else:
          if isinstance(item, str):
              total_sum += len(item)
          else:
              total_sum += item

  return total_sum
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
