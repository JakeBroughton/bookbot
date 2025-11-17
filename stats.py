def word_count(text):
    count = len(text.split())
    return count


def character_hist(text):
    cleaned_text = text.lower()
    result_dict = {}

    for character in cleaned_text:
        result_dict[character] = result_dict.get(character, 0) + 1

    return result_dict


def sort_on_num(dict):
    return dict["num"]


def sort_character_dict(dict):
    list_of_dicts = [{"char": k, "num": v} for k, v in dict.items()]
    list_of_dicts.sort(reverse=True, key=sort_on_num)

    return list_of_dicts
