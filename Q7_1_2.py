def list_average(f):
    try:
        return sum(f)/len(f)
    except:
        print('length:', len(f))
        return None

print(list_average([3.9, 4.5, 2,3]))
print(list_average([]))
