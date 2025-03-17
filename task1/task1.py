from pathlib import Path

def total_salary(path: str) -> tuple[int, int]:
    file_path = Path(path).absolute()
    total = 0
    average = 0

    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            lines = [line.strip().split(', ') for line in file.readlines()]
            for line in lines:
                salary = int(line[0].split(',')[1])
                total += salary
            average = int(total / len(lines))
        return (total, average)
    except FileNotFoundError:
        print(f"File '{path}' not found")
        return (total, average)
    except Exception as e:
        print(f"Error: {e}")
        return (total, average)

if __name__ == '__main__':
    total, average = total_salary('employees.txt')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")