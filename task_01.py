from pathlib import Path


def total_salary(path):
    path = Path(path)
    with open('salary_list.txt', 'r', encoding='utf-8') as file:
        try:
            salary = list()
            for line in file:
                salary.append(line.split(',')[1])
            total=0
            for i in salary:
                total += int(i) 
            average = (total / len(salary))
            return total, average
        except OSError:
            print('Error while reading file')

total, average = total_salary('salary_list.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")