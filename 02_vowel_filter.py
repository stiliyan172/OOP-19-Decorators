def vowel_filter(function):
    def wrapper():
        vowels = function()
        only_vowels = [el for el in vowels if el.lower() in "aeiouy"]
        return only_vowels

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
