def merge(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

def merge_sort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x)/2)
        a = merge_sort(x[:middle])
        b = merge_sort(x[middle:])
        return merge(a,b)

if __name__ == '__main__':
    print(merge_sort([1, 50, 30, 10, 60, 80]))
