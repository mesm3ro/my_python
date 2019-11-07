list_of_tasks = []

while True:
    try:
        print("простой todo:\n"
            "    1. Добавить задачу.\n"
            "    2. Вывести список задач.\n"
            "    3. Выход.\n")
        choice = input("Укажите число: ")

        if choice == '1':
            new_task_desc = input("Сформулируйте задачу: ")
            new_task_cat = input("Добавьте категорию к задаче: ")
            new_task_time = input("Добавьте время к задаче: ")
            list_of_tasks.append((new_task_desc, new_task_cat, new_task_time))

        if choice == '2':
            for task in list_of_tasks:
                print("Задача: ",task[0],"Категория: ",task[1],"Дата: ",task[2])

        if choice == '3':
            break

    except:
        continue
