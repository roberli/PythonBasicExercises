word = str(input("Type a word or a sentence palindrome: "))
reversew = word[::-1]

if word == reversew:
    print("Great the word {0} typed, it's a palindrome".format(word))
else:
    print("Sorry, try again buddy !!!")

### Way to do same thing with loop for ###

def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')