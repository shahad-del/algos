known_letters = input().lower()
no_words_book = int(input())
results = []
isvalid = False
for i in range(no_words_book):
    words = input().lower()
    for letters in words:
        if letters in known_letters:
                # results.append('yes')
                isvalid = True
        else:
               
              isvalid = False
    if isvalid:
        results.append('yes')
    else:
        results.append('no')
for i in results:
    print(i)