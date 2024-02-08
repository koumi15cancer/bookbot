import re
path_to_file = "books/frankenstein.txt"

def main():
  str = read_file(path_to_file)
  cnt = return_count_words(str)
  dict = return_dic_char_cnt(str)
  list_dics = transform_dic_list_of_dics(dict)
  sorted_list = list_dics.sort(reverse=True, key= lambda x: x["value"])
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{cnt} words found in the document")
  #print(list_dics)
  #print(sorted_list)
  print_summary(list_dics)
  print("--- End report ---")

def transform_dic_list_of_dics(dict):
    list_of_dics = [{"key": key, "value": value} for key,value in dict.items() ]
    return list_of_dics

def return_count_words(text):
  return len(text.split())

def read_file(path_to_file):
 with open(path_to_file) as f:
     file_contents = f.read()
     return file_contents

def return_dic_char_cnt(text):
  dict = {}
  new_txt = re.sub(r"\s+","",text)
  for i in new_txt:
    char = i.lower()
    if char not in dict.keys():
        dict[char] = 0
    else:
        dict[char] += 1
  return dict

def print_summary(list):
   for i in list:
      print(f"The '{i["key"]}' character was found {i["value"]} times")

main()


