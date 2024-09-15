calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    l = len(string)
    string_u = string.upper()
    strint_l = string.lower()
    return l, string_u, strint_l


def is_contains(string, list_to_search):
    count_calls()
    flag = False
    for i in  list_to_search:
        if string.lower() in i.lower():
            flag = True
            break
    return flag


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(is_contains('dx', ['lskjfdx' 'sdflj']))
print(calls)
