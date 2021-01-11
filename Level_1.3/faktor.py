
articles, impact = input().split(" ")
articles_int = int(articles)
impact_int = int(impact)

num_science = (articles_int * impact_int) - articles_int + 1
print(num_science)