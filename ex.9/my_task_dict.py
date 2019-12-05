list_of_tasks = []

while True:
    try:
        print("простой todo:\n"
              "    1. Добавить задачу.\n"
              "    2. Вывести список задач.\n"
              "    3. Выход.\n")
        choice = input("Укажите число: ")

        if choice == '1':
            new_task_name = input("Сформулируйте задачу: ")
            new_task_cat = input("Добавьте категорию к задаче: ")
            new_task_time = input("Добавьте время к задаче: ")
            if new_task_name and new_task_cat and new_task_time:
                list_of_tasks.append({"name": new_task_name,
                                      "category": new_task_cat,
                                      "time": new_task_time})

        if choice == '2':
            for task in list_of_tasks:
                print("Задача: ", task["name"],
                      "| Категория: ", task["category"],
                      "| Дата: ", task["time"])

        if choice == '3':
            break
    except:
        continue
