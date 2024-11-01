def all_variants_v1(text):
    for x in range(len(text)):
        for y in range(len(text)):
            if y >= x:
                yield text[x:y+1:]

a = all_variants_v1("abcs")
for i in a:
    print(i)
print('-'*25)

def all_variants_v2(text):
    y = 0
    while y < len(text):
        for x in range(len(text)):
            if x+y+1 <= len(text):
                yield text[x:x+1+y:]
        y += 1

a = all_variants_v2("abckm")
for i in a:
    print(i)