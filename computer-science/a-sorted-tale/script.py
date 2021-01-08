import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

def by_title_ascending(book_a, book_b):
  return book_a["title_lower"] > book_b["title_lower"]

def by_author_ascending(book_a, book_b):
  return book_a["author_lower"] > book_b["author_lower"]

def by_total_length(book_a, book_b):
  return len(book_a["title"]) + len(book_a["author"]) > len(book_b["title"]) + len(book_b["author"])

bookshelf_v1 = bookshelf[:]
bookshelf_v2 = bookshelf[:]

# sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
# for book in sort_1:
#   print(book["title"])

# sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
# for book in sort_2:
#   print(book["author"])

# sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
# for book in bookshelf_v2:
#   print(book["author"])

long_bookshelf = utils.load_books("books_large.csv")
# sorted_long_bookshelf = sorts.bubble_sort(long_bookshelf, by_total_length)
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
