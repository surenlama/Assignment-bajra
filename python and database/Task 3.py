def bubble_sort(list_):
    for i in range(len(list_)):

        for j in range(len(list_) - i - 1):

            if list_[j] > list_[j + 1]:
                temp = list_[j]
                list_[j] = list_[j+1]
                list_[j+1] = temp
    
    return list_


def check_occurrence(string_):
    freq = {}
    for letter in set(string_):
        if letter in [",", "."]:
            continue
        freq[letter] = string_.count(letter)
    return freq


def pop_max(element):
    for index, value in enumerate(occurrence_list):
        if value == element:
            occurrence_list.pop(index)
            return


def build_dict():
    for i in result:
        max_element = max(occurrence_list)
        if result[i] == max_element and len(top5_occured_char)<5:
            top5_occured_char[i] = result[i] 
            pop_max(max_element)


def sort_keys():
    key_list = chest.keys()
    key_list_int = []
    for key in key_list:
        key_list_int.append(int(key))

    return bubble_sort(key_list_int)


def sort_dict_by_keys():
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict[key] = chest[str(key)]
    
    return sorted_dict


def get_values():
    first_key_value = sorted_dict[sorted_keys[0]]
    second_key_value = sorted_dict[sorted_keys[1]]
    last_key_value = sorted_dict[sorted_keys[len(sorted_keys)-1]]
    second_last_key_value = sorted_dict[sorted_keys[len(sorted_keys)-2]]

    return [first_key_value, second_key_value, last_key_value, second_last_key_value]


def concatenate_values():
    concatenated_statement = ""
    for index, statement in enumerate(required_values):
        if index<len(required_values)-1:
            concatenated_statement += statement + " "
        else:
            concatenated_statement += statement
    return concatenated_statement


def get_chars():
    words = concatenate_statements.split(" ")
    print(words)
    concatenated_str= ""
    for word in words:
        concatenated_str += word[0] + word[len(word)-1]
    return concatenated_str


chest = {
'42': 'It is the Answer to Life the Universe and Everything.',
'666': 'If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things.',
'8': 'It is wrong always, everywhere and for everyone, to believe anything upon insufficient evidence.',
'13': 'The Truth is in the Heart.',
'0': 'Freedom is secured not by the fulfilling of ones desires, but by the removal of desire.',
'9': 'The unexamined life is not worth living.',
'76': 'Life is a series of natural and spontaneous changes.',
'70': 'God is dead! He remains dead! And we have killed him.'
}

sorted_keys = sort_keys()
print(sorted_keys)

print('-----------------------------------------------------------------------------------------')

sorted_dict = sort_dict_by_keys()
print(sorted_dict)

print('-----------------------------------------------------------------------------------------')

required_values = get_values()
print(required_values)

print('-----------------------------------------------------------------------------------------')

concatenate_statements = concatenate_values()
print(concatenate_statements)

print('-----------------------------------------------------------------------------------------')

concatenated_str = get_chars()
print(concatenated_str)

print('-----------------------------------------------------------------------------------------')

result = check_occurrence(concatenated_str)
print(result)

print('-----------------------------------------------------------------------------------------')

occurrence_list = []
for i in result:
    occurrence_list.append(result[i])
print(occurrence_list)

print('-----------------------------------------------------------------------------------------')

top5_occured_char = {}

while len(top5_occured_char)<5:
    build_dict()
    
print(top5_occured_char)
print(len(top5_occured_char))

print('-----------------------------------------------------------------------------------------')

key_list = [52,51,61,71,58]

top5_occurrence_list = []
top5_occurrence_list = list(top5_occured_char.values())
print(top5_occurrence_list)

print('-----------------------------------------------------------------------------------------')

sum_list = []
for i in range(len(key_list)):
    sum_list.append(key_list[i] + top5_occurrence_list[i])
print(sum_list)

print('-----------------------------------------------------------------------------------------')

for i in sum_list:
    print(chr(i))