def total_salary(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            lines=[el.strip().split(',') for el in file.readlines()]
            if not file:
                return 0,0
            salaries=[float(salary) for _,salary in lines]
            total=sum(salaries)
            averange=total/len(salaries)
            return total, averange
    except FileNotFoundError:
        print(f'файл {path} не існує, або не знайдено')
        return None, None
    except Exception as e:
        print(f'сталась помилка {e}')  
total, average = total_salary('salary_file.txt')
print(f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}")         