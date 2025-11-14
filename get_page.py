get_total_page = lambda m, n : m // n if m % n == 0 else m // n + 1
print(get_total_page(30, 10))