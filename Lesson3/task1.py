# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов
def duplicates_elem(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 'a', 'a', 'b']
print(duplicates_elem(my_list))