# game world module

# layer 0: Background Object
# layer 1: Foreground Object
objects = [[], [], []]

def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            print('REMOVE')
            del o
            return
    raise ValueError('Trying destroy non existing object')

def all_objects():
    for layer in objects:
        for o in layer:
            # 이 함수는 generater로 취급.
            yield o

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()