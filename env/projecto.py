import telebot
import webbrowser
TOKEN = "7136688024:AAE5nwdkYmD04JWXcM9ja0drApBqvkar6eM"
bot = telebot.TeleBot(TOKEN)
#version 1.1


#sesion
sesion1 = """Сессия — это период времени в течение учебного года, когда студенты сдают экзамены и зачеты по всем предметам, которые они изучали в течение семестра. Результаты сессии влияют на общий успех студента в учебном году.
    Существуют различные виды сессий. Ниже перечислены основные виды очных сессий в ТулГу:
    Экзаменационная сессия — период, в течение которого проводятся зачеты и экзамены по всем предметам, изучаемым в течение семестра или учебного года. Обычно проводится две экзаменационные сессии в год: зимняя (в январе-феврале) и летняя (в июне-июле).
    Дополнительная сессия — это возможность для студентов, которые не смогли сдать экзамены или зачеты во время основной экзаменационной или зачетной сессии, исправить свои оценки. Информацию о сроках дополнительной сессии можно узнать в дирекции института."""

sesion2 = """Предметы по сдаче делятся на «Зачет» (зч), «Диф.зачет» или зачет с оценкой (ДЗ) и «Экзамен» (Экзамен).
    В Тульском государственном университете бальная система получения оценки. Чтобы получить «Зачет» студенту нужно набрать 40 баллов. Это касается только предметов из категории «Зачет». Чтобы получить оценку «Удовлетворительно» или простыми словами тройку нужно набрать 41 балл, оценку «Хорошо» или четверку – 61 балл, а оценку «Отлично» или пятерку – 81 балл.
    У каждого предмета индивидуальная система набора баллов, каждый преподаватель озвучивает её на лекциях или на практиках. В основном во время семестра можно получить 60 баллов – за посещение лекций, работы на практических занятиях, за лабораторные и контрольные работы. 
    Во время сессии студенту дается выбор – он может написать работу на 40 баллов или же полностью обнулить все свои баллы, заработанные во время семестра и написать работу на 100 баллов, но она будет намного сложнее и объемнее.
    Итоговая оценка, идущая в зачетную книжку, складывается за работу во время семестра (60 баллов максимально) и сдачи сессии (40 баллов максимально)."""
sesion3 = """При получении долга необходимо постараться сдать его во время дат сессии, в случае успеха вы сможете сохранить стипендию. При получении долга необходимо договориться с преподавателем о пересдаче и взять заявление о пересдаче предмета."""
#money
money1 = """Стипендия - регулярная финансовая помощь, которая может быть оплатой за обучение или ежемесячно выдаваемым пособием учащимся высших или средних профессиональных заведений, а также аспирантам и докторантам. 
    Стипендия выдается студентам, учащимся на оценки «Хорошо» или выше. Те, кто получили оценку «Удовлетворительно» стипендии лишаются до тех пор, пока они не закроют сессию на одни хорошие оценки."""
money2 = """Все оценки «Отлично» - 5130 руб.
    Оценок «Отлично» > оценок «Хорошо» («Отлично» > 50%) – 3695 руб.
    Оценок «Отлично» ≤ оценок «Хорошо» («Отлично» ≤ 50%) – 2980 руб.

    Стипендия выплачивается каждый месяц 25 числа."""

#money for beggar
beggar1 = """Студенты 1 курса бакалавриата/специалитета, обучающиеся на бюджетной основе, имеют право подать заявление на получение социальной стипендии.
    Всю информацию о социальной стипендии можно узнать здесь: \nhttps://vk.com/profcom_tsu?w=wall-403589_44271"""
beggar2 = "Всю информацию о ЕМП можно узнать здесь:\nhttps://vk.com/profcom_tsu?w=wall-403589_45552"
#СТУД.АКТИВ
std = ""


@bot.message_handler(commands=["start"])
def start(message):
    mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Сессия")
    item2 = telebot.types.KeyboardButton("Стипендия")
    item3 = telebot.types.KeyboardButton("Социальные выплаты")
    item4 = telebot.types.KeyboardButton("Cтуд.актив")
    item5 = telebot.types.KeyboardButton("Расписание")
    item6 = telebot.types.KeyboardButton("Карта студенческого городка")
    mark.add(item1, item2)
    mark.add(item3, item4)
    mark.add(item5)
    mark.add(item6)


    bot.send_message(message.chat.id, "Начало", reply_markup=mark)






@bot.message_handler(content_types=['text'])
def info(message):

#-------------------------------------Блок сеcсия------------------------------------------------'''

    if message.text == "Сессия":
        
        mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("Что такое сессия?")
        item2 = telebot.types.KeyboardButton("Какая система сессии в ТулГу") # sesion2
        item3 = telebot.types.KeyboardButton("Чем отличается ДЗ от Экзамена")
        item4 = telebot.types.KeyboardButton("Как мне узнать, когда у меня сдача предмета")
        item4 = telebot.types.KeyboardButton("Я получил долг по предмету. Что делать?")
        back = telebot.types.KeyboardButton("назад")
        mark.add(item1, item2)
        mark.add(item3)
        mark.add(item4)
        mark.add(back)
        bot.send_message(message.chat.id,"Сессия",reply_markup=mark)

#-------------------------------------Блок Стипендия---------------------------------------------'''

    elif message.text == "Стипендия":
        mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("Что такое стипендия?")
        item2 = telebot.types.KeyboardButton("Размер стипендии ТулГУ")
        back = telebot.types.KeyboardButton("назад")
        mark.add(item1, item2)
        mark.add(back)
        bot.send_message(message.chat.id, "Стипендия",reply_markup=mark)

#-------------------------------------Социальные выплаты---------------------------------------------'''
    elif message.text == "Социальные выплаты":
        mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("Что такое социальная стипендия?")
        item2 = telebot.types.KeyboardButton("Что такое Единовременная материальная помощь?")
        back = telebot.types.KeyboardButton("назад")
        mark.add(item1) 
        mark.add(item2) 
        mark.add(back)
        bot.send_message(message.chat.id, "Социальные выплаты",reply_markup=mark)

#-----------------------------------СТУД.АКТИВ--------------------------------------------
#-------------------------------------Другое---------------------------------------------'''
    elif message.text == "назад":
        mark = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("Сессия")
        item2 = telebot.types.KeyboardButton("Стипендия")
        item3 = telebot.types.KeyboardButton("Социальные выплаты")
        item4 = telebot.types.KeyboardButton("Карта студенческого городка")
        item5 = telebot.types.KeyboardButton("Расписание")
        item6 = telebot.types.KeyboardButton("Cтуд.актив")
        mark.add(item1, item2)
        mark.add(item3, item4)
        mark.add(item5)
        mark.add(item6)
        bot.send_message(message.chat.id, "Начало", reply_markup=mark)


    #Сессия
    if message.text == "Что такое сессия?":
        bot.send_message(message.chat.id,sesion1)
    elif message.text == "Какая система сессии в ТулГу":
        bot.send_message(message.chat.id,sesion2)
    elif message.text == "Чем отличается ДЗ от Экзамена":
        bot.send_message(message.chat.id,"Ничем")
    elif message.text == "Как мне узнать, когда у меня сдача предмета":
        bot.send_message(message.chat.id,"Ближе к сессии на сайте расписания ТулГУ будет опубликовано расписание всей сессии.\n https://tulsu.ru/schedule/")
    elif message.text == "Я получил долг по предмету. Что делать":
        bot.send_message(message.chat.id,sesion3)

    #СТИПЕНДИЯ
    if message.text == "Что такое стипендия?":
        bot.send_message(message.chat.id,money1)
    elif message.text == "Размер стипендии ТулГУ":
        bot.send_message(message.chat.id,money2)


    #money for beggar
    if message.text == "Что такое социальная стипендия?":
        bot.send_message(message.chat.id,beggar1)
    elif message.text == "Что такое Единовременная материальная помощь?":
        bot.send_message(message.chat.id,beggar2)

    if message.text == "Cтуд.актив":
        bot.send_message(message.chat.id,"Это для педиков")


    if message.text == "Расписание":
        bot.send_message(message.chat.id,'https://tulsu.ru/schedule/')
    if message.text == "Карта студенческого городка":
        bot.send_message(message.chat.id,'https://yandex.ru/maps/15/tula/?from=mapframe&ll=37.592002%2C54.170004&mode=usermaps&source=mapframe&um=constructor%3Ac37cdb018503b787b7be940ccda87f17d70bc3d86624c538abac1021c6d70511&utm_source=mapframe&z=14')
    

  

bot.polling(none_stop = False)