def get_book_data():
	book = input("Book title: ")
	author = input("Author name: ")
	rating = int(input("Rating 1-10: "))
	return (book, author, rating)
book_ratings = {}
book = ''
author = ''
rating = 0

for i in range(3):
	book, author, rating = get_book_data()
	book_ratings[book] = (author, rating)

max_title = ''
max = 0
for key, value in book_ratings.items():
	print(f'{key} by {value[-2]} rated {value[-1]} out of 10')
	if value[-1] > max:
		max_title  = key
		max = value[-1]

print(f"{max_title} is the highest rated")	
