def indefinite_number_of_strings(*args) -> list[str]:
    strings_in_list = [str.upper(i) for i in args if isinstance(i, str)]
    return strings_in_list


print(sorted(indefinite_number_of_strings("hello", 6, "byebye", 'a', 'c')))
