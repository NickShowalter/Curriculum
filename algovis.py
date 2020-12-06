from algovis import searching

my_list = [i + 1 for i in range(50)]
bin_search = searching.BinarySearch(my_list)
bin_search.search(42, steps=True)

bin_search.evaluate(24, iterations=100)

bin_search.visualize(29, interval = 100)

bin_search.info()