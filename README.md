# Largest remainder calculator

Allows for a **dictionary** or **list** to be passed into their respective methods along with a **scale** to calculate their whole number representation using the largest remainder methodology. 

## What this solves
Rounding all of the following percentages to the nearest whole number:
```
  33.34 -> 33%
  33.33 -> 33%
  33.33 -> 33%
```
Doesn't quite add up to 100. With `n` number of decimals in this list, this number could be greater than 100 or less than 100.

Another Example is:
```
  18.562874251497007 -> 19
  20.958083832335326 -> 21
  18.562874251497007 -> 19
  19.161676646706585 -> 19
  22.75449101796407  -> 23
```
Which all add up to 101. 

## Basic Usage
This project was designed to work with a list of numbers as well as a dictionary.

### Dictionary Usage
```python
data = {
  "promoter": 33.33,
  "passive": 33.33,
  "detractor": 33.33,
}

whole_number_dict = dict_largest_remainder(data)
print(whole_number_dict)

outputs:

{
  "promoter": 33,
  "passive": 33,
  "detractor": 34
}
```


### List Usage

```json
data = [ 3, 7, 4, 6, 1 ]

whole_number_list = list_largest_remainder(data)
print(whole_number_dict)

outputs: [14, 33, 19, 29, 5]
```


## Scale
Something you may notice about that last example are the output numbers. There is a scale feature in that allows you to pass in a value and it will scale a list of values to it. 

In the context of percentages, you would want the target to be 100 but there are cases where you don't want that to be the case. 100 is the default, but to change it, add a 2nd value as an argument.

### Example
```python 
data = {
  'Conservatives': 13636684,
  'Labour': 12877918,
  'SNP': 977568,
  'Liberal Democrats': 2371861,
  'Green': 525665,
  'Other': 746144
}

scaled_whole_numbers = dict_largest_remainder(dict_test, 650))

outputs:
{
  'Conservatives': 285,
  'Labour': 269,
  'SNP': 20,
  'Liberal Democrats': 49,
  'Green': 11,
  'Other': 16
}
```

Long story short, adding a `target` to your arugments will scale dictionary or list values to that number and give you only whole number that add up to the `target` value. **Remember**: Not adding a `target` will use `100` as the target.  

## Future Features
- Add a precision feature that allows rounding to an `nth` decimal place and will still add up to the whole number target.
- Allow `dict_largest_remaider` to take in dictionary keywords to allow users to chose what they want in their returned dictionary.
- Optionally allow all generated contents to be returned.