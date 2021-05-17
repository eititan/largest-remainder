import largest_remainder

class TestClass:
  def test_sum_list(self):
    list_test = [ 3, 7, 4, 6, 1 ]
    target = 100

    list = largest_remainder.list_largest_remainder(list_test, target)
    assert sum(list) == target

  def test_diff_list(self):
    list_test = [ 3, 7, 4, 6, 1 ]
    target = 100

    list = largest_remainder.list_largest_remainder(list_test, target)
    assert list_test.sort != list.sort()

  def test_sum_list_2(self):
    list_test = [
      18.562874251497007,
      20.958083832335326,
      18.562874251497007,
      19.161676646706585,
      22.75449101796407,
    ]
    target = 100

    list = largest_remainder.list_largest_remainder(list_test, target)
    assert sum(list) == target


  def test_sum_dict(self):
    dict_test = {
      "promoter": 33.33,
      "passive": 33.33,
      "detractor": 33.33,
    }

    target = 100

    dict = largest_remainder.dict_largest_remainder(dict_test, target)
    assert sum([v for k, v in dict.items()]) == target

  def test_sum_dict_2(self):
    dict_test = {
      'Conservatives': 13636684,
      'Labour': 12877918,
      'SNP': 977568,
      'Liberal Democrats': 2371861,
      'Green': 525665,
      'Other': 746144
    }

    target = 650

    dict = largest_remainder.dict_largest_remainder(dict_test, target)
    assert sum([v for k, v in dict.items()]) == target

