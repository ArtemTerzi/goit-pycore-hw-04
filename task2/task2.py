from pathlib import Path

def get_cats_info(path: str)->list[dict[str, str, int]]:
    file_path = Path(path).absolute()
    cats = []

    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            lines = [line.strip() for line in file.readlines()]
            for i in range(len(lines)):
                cat_data = lines[i].split(',')
                cat = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats.append(cat)
        return cats
    except FileNotFoundError:
        print(f"File '{path}' not found")
        return cats
    except Exception as e:
        print(f"Error: {e}")
        return cats
    
    
if __name__ == '__main__':
    print(get_cats_info('cats.txt'))