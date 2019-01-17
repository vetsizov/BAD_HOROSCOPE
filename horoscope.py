import random
from datetime import datetime as dt

times = ["Завтра утром", "Завтра днем", "Завтра вечером", "Сегодня ночью", "В ближайшее время", "Совсем скоро"]
advices = ["ожидай", "остерегайся", "жди"]
promises = ["встречи с цыганкой, которая разведет тебя как последнего простофилю на круглую сумму денег", 
            "встречи со своим школьным приятелем, который гораздо успешнее тебя и прилюдно выставит тебя лузером",
            "того, что придется затариться Дошиком на месяц, другой еды не будет",
            "полицию и ФСБ которые арестуют тебя за тот пост ВКонтакте",
            "значения на весах +5кг к 'твоему нормальному весу'",
            "разбитой посылки из службы доставки",
            "встречи с агресивным соседом, который собрался делать ремонт по ночам",
            "прибытия инопланетян, которые похитят тебя для опытов",
            "твоего старого друга которому нужно занять 10 тысяч до зарплаты",
            "тещу, которая приедет в гости на пару недель",
            "охранника из Пятерочки который заподозрит тебя в краже ХубыБубы",
            "бомжа на улице, который попросит с ним бухнуть стекломоя"]


def generate_prophecies(total_num=5, num_sentences=3):
    prophecies = []

    for i in range(total_num):
        forecast = ""
        for j in range(num_sentences):
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = f"{t} {a} {p}."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence

        prophecies.append(forecast)

    return prophecies

def check_month():
    now = dt.now()
    if now.month == 1:
        return 'января'
    elif now.month == 2:
        return 'февраля'
    elif now.month == 3:
        return 'марта'
    elif now.month == 4:
        return 'апреля'
    elif now.month == 5:
        return 'мая'
    elif now.month == 6:
        return 'июня'
    elif now.month == 7:
        return 'июля'
    elif now.month == 8:
        return 'августа'
    elif now.month == 9:
        return 'сентября'
    elif now.month == 10:
        return 'октября'
    elif now.month == 11:
        return 'ноября'
    elif now.month == 12:
        return 'декабря'
    else:
        return 'какого-то месяца'

def pigga_said():
    phrases = ["Хватит, я пошутил!", 
    "Узбагойся, я сказал",
    "Ты сейчас весь мой жир растресешь!",
    "Тише, тише, мышь сломаешь",
    "Да ну нафиг, я сваливаю",
    "Я тебя щас по айпи вычислю!",
    "Екарный бабай, совсем попутал!",
    "Дикий, дерзкий, как пуля резкий?",
    "Ты выйди со мной раз на раз, а не щелкай в интернете!",
    "Не, ну это ваще, ты нормальный?"]
    return random.choice(phrases)

def pigga_said2():
    phrases = ["Ахаха! Я бы на это посмотрел!", 
    "Это просто жесть",
    "Вот это ты попал!",
    "Ой ой ой, это страшно представить",
    "Дааа, нормальный расклад",
    "Представляю твое лицо когда это случится",
    "Ахаха! Умора",
    "Мне даже тебя жалко",
    "ААААА. Но я думаю ты справишься"]
    return random.choice(phrases)