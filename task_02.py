from pathlib import Path

def get_cats_info(path):
    path = Path(path)
    with open('Cats_info.txt', 'r', encoding='utf-8') as file:
        try:
            cats_info = []
            for line in file:
                id,name,age = line.strip().split(',')
                cat_dict = {'id':id, 'name':name, 'age':age}
                cats_info.append(cat_dict)
            return cats_info
         
        except OSError:
            print('Error while reading file')

cats_info = get_cats_info('Cats_info.txt')
print(*cats_info, sep='\n')
