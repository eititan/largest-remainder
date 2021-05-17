from typing import List

def main():

  list_test = [ 3, 7, 4, 6, 1 ]
  print(list_largest_remainder(list_test))
  

  test2 = [
    18.562874251497007,
    20.958083832335326,
    18.562874251497007,
    19.161676646706585,
    22.75449101796407,
  ]
  print(list_largest_remainder(test2))

  
  dict_test = {
    'Conservatives': 13636684,
    'Labour': 12877918,
    'SNP': 977568,
    'Liberal Democrats': 2371861,
    'Green': 525665,
    'Other': 746144
  }
  print(dict_largest_remainder(dict_test, 650))



def dict_largest_remainder(data: List, target: int = 100):
  remainder_list = [ {idx: { "original": data[d], "label": d, "position": idx} } for idx, d in enumerate(data) ]
  data = [v for k, v in data.items()]

  arr = process_largest_remainder( remainder_list, target )  
  return { v["label"]: v["scaled_total"] for i in arr for k, v in i.items() }



def list_largest_remainder(data: List, target: int = 100):
  dict_list = dict(enumerate(data))
  remainder_list = [ {idx: { "original": d, "label": d, "position": idx} } for idx, d in enumerate(data) ]
  data = [v for k, v in dict_list.items()]

  arr = process_largest_remainder(remainder_list, target) 
  return [ v["scaled_total"] for i in arr for k, v in i.items() ]
 



def process_largest_remainder(remainder_list: List, target: int = 100):
  sum_of_all = sum([round(v["original"]) for l in remainder_list for k, v, in l.items()])

  # gives me percentage of target
  for l in remainder_list:
    for k, v in l.items():
      v["scaled_percent"] = v["original"] / sum_of_all

  # get scaled total, in float
  for l in remainder_list:
    for k, v in l.items():
      v["scaled_total"] = v["scaled_percent"] * target

  scaled_sum = sum([round(v["scaled_total"]) for l in remainder_list for k, v, in l.items()])

  # calculate how far target number is off from scaled total sum
  spread = target - scaled_sum
  sorted_dict = _arr_sorter(remainder_list, spread)

  # add or subtract one from the appropriate number n times and make whole number
  for i in range(abs(spread)):
    for k, v in sorted_dict[i].items():
      val = round(sorted_dict[i][k]["scaled_total"]) + 1
      if spread < 0:
        val = round(sorted_dict[i][k]["scaled_total"]) - 1

      sorted_dict[i][k]["scaled_total"] = val 
 
  # round the rest of the numbers
  for i in range(len(sorted_dict)):
    for k, v in sorted_dict[i].items():
      sorted_dict[i][k]["scaled_total"] = round(sorted_dict[i][k]["scaled_total"])

  # to maintain order of items passed in from user, re-sort based on position 
  sorted_dict.sort(key=lambda k: [v["position"] for l, v in k.items()][0])
  return sorted_dict




def _positive_sort(d: float):
  return d % 1

def _negative_sort(d: float):
  return (_positive_sort(d) - .5 < 0, _positive_sort(d) - .5)

def _arr_sorter(data: List, split: int):
  data.sort(key=lambda k: _positive_sort([v["scaled_total"] for l, v in k.items()][0]), reverse=True)

  if split < 0:
    data.sort(key=lambda k: _negative_sort([v["scaled_total"] for l, v in k.items()][0]))

  return data



if __name__ == "__main__":
  main()