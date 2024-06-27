letters_list = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']
letters_tuple = ('a', 'b', 'd', 'e', 'i', 'j', 'o', 'u')
letters_set = {'a', 'b', 'd', 'e', 'i', 'j', 'o', 'u'}


# Filter the vowels
# a,e,i,o,u

def vowel_given(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


filtered_words = filter(vowel_given, letters_list)
print(list(filtered_words))