value = input("Атомный номер: ")

if value:
    
    num = int(value)
    
    if num == 2:
        print("Li - литий")
        
    elif num ==25:
        print("Mn - марганец")

    elif num == 80:
        print("Hg - ртуть")
        
    elif num == 17:
        print("Cl - хлор")
        
    else:
        print("Элемент отсутсвует")
else:
    print("Нет значения")
