def count_i_in_content(character, filepath):
    with open(filepath, "r") as qwe:
        content = qwe.read()
    count_i = content.count(character)
    return count_i


print(count_i_in_content("z", "bear2.txt"))


def test_count():
    assert count_i_in_content("z", "bear2.txt") == 3
