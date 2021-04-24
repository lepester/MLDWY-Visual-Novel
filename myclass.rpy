init python:
    #Описание характеристик персонажей
    class MyHero:
        def __init__(self, name, age, hobby, character):
            self.name = "Имя: Мирай"
            self.age = "возраст: 17"
            self.hobby = "хобби: музыкант"
            self.character = "характер: флегматик"

    class Rei(MyHero): #Наследование и полиморфизм
        def __str__(self, name, age, hobby, character):
            self.name = "Имя: Рэй"
            self.age = "возраст: 17"
            self.hobby = "хобби: косплей"
            self.character = "характер: меланхолик"

    class Noi(MyHero):
        def __init__(self, name, age, hobby, character):
            self.name = "Имя: Ной"
            self.age = "возраст: 16"
            self.hobby = "хобби: музыкант"
            self.character = "характер: холерик"

    class Kirari(MyHero):
        def __str__(self, name, age, hobby, character):
            self.name = "Имя: Кирари"
            self.age = "возраст: 18"
            self.hobby = "хобби: активистка"
            self.character = "характер: холерик"

    class MrKei(MyHero):
        def __init__(self, name, age, hobby, character):
            self.name = "Имя: Мистер Кей"
            self.age = "возраст: 43"
            self.hobby = "хобби: часовщик"
            self.character = "характер: сангвиник"

    class Meri(MyHero):
        def __str__(self, name, age, hobby, character):
            self.name = "Имя: Мэри"
            self.age = "возраст: 35"
            self.hobby = "хобби: готовка"
            self.character = "характер: меланхолик"
