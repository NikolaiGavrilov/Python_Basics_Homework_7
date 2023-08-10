import random
import json

dishes = ["яичница", "пицца", "суши", "блинчики", "сэндвич"]
disheslen = len(dishes)-1

def save():
    with open("dishes.json", "w", encoding = "utf-8") as cul_bot:
        cul_bot.write(json.dumps(dishes, ensure_ascii = False))
    print("Бот успешно сохранил вашу кулинарную библиотеку. Проверьте изменения в файле dishes.json")

def load():
    with open("dishes.json", "r", encoding = "utf-8") as cul_bot:
        dishes = json.load(cul_bot)
    print("Бот успешно загрузил измененную библиотеку в файл dishes.json")

while True:
    command = input("Введите команду:")
    if command == "/start":
        print("Процесс запущен. Вас приветствует кулинарный бот!")
    elif command == "/finish":
        save()
        print("Работа кулинарного бота завершена. До новых встреч!")
        break
    elif command == "/info":
        print("Кулинарный бот может посоветовать вам вкусняшку. Используйте следующие команды, чтобы воспользоваться им.")
        print("/start - для запуска бота,", end = " ")
        print("/stop - для прекращения работы бота,")
        print("/info - для получения информации о работе бота,", end = " ")
        print("/all - для ознакомления со всем списком блюд,")
        print("/add - для добавления новых блюд в кулинарную библиотеку,", end = " ")
        print("/remove - для удаления блюда из библиотеки,")
        print("/norepeats - для удаления повторяющихся блюд в кулинарной библиотеке,", end = " ")
        print("/save - для полного очищения библиотеки блюд,")
        print("/random - для рандомного выбора блюда на сегодня,", end = " ")
        print("/save - для сохранения вашей библиотеки в файл,")
        print("/load - для загрузки вашей библиотеки в файл", end = " ")
        print("")
    elif command == "/all":
        print("Ознакомьтесь с текущим списком кулинарных блюд:")
        print(dishes)
    elif command == "/add":
        new_dish = input("Введите название блюда, которое вы хотите добавить в свою кулинарную библиотеку: ")
        dishes.append(new_dish)
        print("Готово! Спасибо за дополнение!")
    elif command == "/remove":
        rmv_dish = input("Введите название блюда, которое вы хотите удалить из своей кулинарной библиотеки: ")
        try:
            dishes.remove(rmv_dish)
            print("Удаление выполнено. Этого блюда больше нет в вашей кулинарной библиотеке.")
        except: 
            print("Блюдо отсутсвует в вашей библиотеке. Проверьте правильность ввода.")
    elif command == "/norepeats":
        dishes = set(dishes)
        dishes = list(dishes)
        print("Бот навёл в вашей библиотеке порядок. Повторяющихся блюд теперь нет.")
    elif command == "/clear":
        dishes.clear()
        print("Библиотека очищена.")
    elif command == "/random":
        random_dish = dishes[random.randint(0, disheslen)]
        print(f"Великий рандом решил, что сегодня вам стоит приготовить блюдо '{random_dish}'")
    elif command == "/save":
        save()
    elif command == "/load":
        load()
    else:
        print("Бот вас не понял. Для ознакомления со списком команд бота используйте команду /info")
    


              
