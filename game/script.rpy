init python:
    mp = MultiPersistent("MLDWY")   #Инкапсуляция        #Этот класс позвляет сохранить данные из одного проекта
                                                         #посредством ключа "MLDWY". Это ключ можно использовать в другом проекте,
                                                         #который должен выступать продолжением или наследником.

                                                #Иными словами это подтверждение того, что пользователь закончил прохождение игры.

                                                #Во всех других случаях, если ключ не внедрен, то пользователь не прошел игру.

default said_true = False
label start:

    #Записываем тот факт, что пользователь прошел игру. (Напоминание - добавить в конец по завершению проекта__)
    $ mp.beat_part_1 = True
    $ mp.save()

    stop music
    #Предисловие
    #Умирать – мучительно горько, но идея умереть даже не живя – просто невыносима.
    #Имей в виду, что любой день может оказаться для тебя последним. Приятным будет   наступление часа, на который ты не надеялся.
    #Эрих Фромм и Гораций.

    #Начало игры. Сцена 1. Мирай находит Рэй без сознания. Ночью и на остановке. Идет дождь

    scene bg pred1 with dissolve
    pause 2
    scene bg pred2 with dissolve
    pause 2
    scene bg pred3 with dissolve
    pause 2
    scene bg pred4 with dissolve
    pause 3
    #scene bg black with dissolve
    #pause 2
    scene bg rain with dissolve

    play music "music/rain.mp3" fadein 1 fadeout 1

label scene1:

    """
    Были времена, когда всё было хорошо. Когда я не задумывался о тех счастливых днях, проведёных с ней.

    Мы были лучшими друзьями, которые были готовы заступиться друг за друга.

    Кто же мог представить, что такое может произойти?

    Хах...

    Хахахах...

    Из всех человеческих жизней на этой проклятой земле ты выбрал именно её жизнь.

    Что она тебе сделала?

    Чем она заслужила такую участь?

    Да кто ты вообще такой, чтобы отнимать у людей их счастье!?

    Слышишь меня?!

    ...

    И чего я пытаюсь этим добиться?

    Ты же всё равно ни черта не слышишь!

    Почему ей суждено погибнуть именно так?!

    Если... Если ты правда есть... Я-я прошу тебя, покажи мне способ спасти её.
    Я отдам что угодно взамен на это! Я отдам даже свою жизнь, если придётся! Только спаси её!
    """
    #Надпись на полный экран
    scene bg think with dissolve
    pause 3
    scene bg rain with dissolve
    """
    Вернуть бы то время назад...

    Только бы увидеть её улыбку еще раз... Хотя бы один раз...
    """
    scene bg black with dissolve
    play sound "music/siren.mp3" fadeout 0.5 fadein 0.5
    stop music

    scene bg black with dissolve
    m "А-ах..Рэй. Держись, они уже близко."
    #stop music
    #play music "music/rain.mp3" fadein 1 fadeout 0.2

    scene bg intro with dissolve
    pause 1


    stop music




    scene bg hos_1 with dissolve
    pause 1

    r "Ммм..."

    m "А?..."

    m "Рэй?... Рэй!"

    m "Оставайся в сознании! Еще пару минут! Всё будет в порядке!"
    scene bg hos_2 with dissolve
    pause 1

    show med front with dissolve

    med1 "Отойдите в сторону."


    "Как долго будет длиться этот кошмар?..."

    show med say with dissolve

    med2 "Кладите её на носилки. Объявите чрезвычайную ситуацию. "

    show med back with dissolve

    play sound "Music/close_door.mp3"

    med3 "Сделано! Разузнайте у того парня, что произошло."

    show med say with dissolve

    med1 "Расскажите, что произошло. Поможет любая информация."

    menu:
            "Что мне сделать?"

            "Ничего не говорить.":
                "\"Не думаю, что это хорошая идея.\""
                "\"Тем более, что они могут заподозрить меня в чем-то.\""
                "\"А, что, если они и правда сейчас думают об этом?\""
                "\"Стоит ли мне сбежать сейчас?\""
                "\"Или всё обойдется..?\""
                med1 "Так что случилось? Вы ответите на вопрос?"
                m "Я-я не знаю..."
                m "Абсолютно ничего не могу сказать... Простите..."
                med1 "Похоже у мальчишки нехилое количество стресса накопилось"
                m "Мне очень жаль... Правда."
                "\"Какое же я ничтожество!\""

            "Сказать правду.":
                $ said_true = True
                "\"Успокойся, Мирай! Возьми себя в руки. Сейчас не время для паники.\""
                m """
                Я сам мало что знаю.

                У этой девушки болезнь, которую невозможно излечить.

                Также я знаю, что эта болезнь досталась ей по наследству от отца.

                  """

            "Проснуться.":
                jump wake_up
label after_menu:
    med1 "Я вас понял. Успокойтесь, пожалуйста. На вас нет лица. И не переживайте по поводу болезни. Мы обязательно найдем способ спасти эту девушку."
    med1 "Но ответьте на один вопрос."




    stop music
    # Сцена 2. Мирай просыпается от плохого сна и собирается пойти в школу. По пути он раздумывает о том, что ему приснился ужасный сон.

#Конец сцены 1

label scene2:

    scene bg black with dissolve
    pause 3.5
    play sound "music/tick_tock_alarm.mp3" fadeout 1 fadein 1
    pause 3
    play sound "music/alarm_clock.mp3" fadeout 1 fadein 1
    scene bg home with dissolve


    m "Ммм…"
    "..."
    "...."
    "....."
    m "ДА СКОЛЬКО МОЖНО ЗВОНИТЬ!?"

    stop sound fadeout 1

    m """
    Который сейчас час?

    Что?! Уже 7:55?!

    Чёрт! Я же в школу опаздываю. Нужно поторопиться, иначе учитель опять весь мозг вынесет!
    """
    scene bg black with dissolve
    pause 2

    scene bg stairs with dissolve

    m "Так. Вроде бы всё взял. Вперёд."

    scene bg black
    with dissolve

    pause 1
    scene bg street with dissolve

    play music "music/happy song.mp3" fadeout 1 fadein 1

    "Такая рань, а он уже открыл свою лавочку."

    "Что же не так с этими взрослыми?.."

    "Доброе утро, Мистер Ки!"

    show k say with dissolve

    kei "Йо! Доброе утро, Мирай-кун! Опять проспал? Небось опять на гитаре всю ночь проиграл, я прав?"

    m "Ну что вы в самом деле, а? Пару раз всего было, а вы надо мной так каждый раз шутите."

    kei "Ахахахах! Да ладно тебе. Не буду я больше над тобой так шутить, но ты уж пораньше ложись, а то так и всю жизнь проспишь ведь. Ахахаха!"

    "\"Ну конечно...\""
    m "Я побежал. Хорошего вам дня!"
    show k smile with dissolve

    kei "Йо! И тебе удачи, Мирай-кун!"

    hide k with dissolve

    scene bg road with dissolve
    """
    Если вам интересно, кто это был, то я расскажу вам.

    Мистер Ки – это владелец двухэтажного дома, который я арендую.

    Я живу на 2-ом этаже, а на 1-ом этаже работает Мистер Ки. Он очень любит свою работу  и любит засиживаться в своём кабинете до последнего.

    Поэтому, иногда, когда я заигрываюсь с моим лучшим другом Ноем на наших музыкальных инструментах, то Мистер Ки всегда ворчит на нас.

    Когда мы начинаем ему действовать на нервы, он берет свою здоровенную швабру, и бьет по потолку, давая нам понять, чтобы мы перестали играть или сделали громкость вполовину тише.

    Славный старик.

    Как вы думаете, кем же он работает?

    Я вам отвечу: Мистер Ки – часовщик.

    Немалоизвестный факт – профессия часового мастера ювелирная, поэтому чаще всего часовщики любят тишину. Поэтому, наши затяжные выступления не очень нравятся Мистеру Кею.

    Но на самом деле Мистер Ки не ворчун и, если ему не действуют на нервы, то он очень даже добрый и отзывчивый старик.

    Каждый раз, когда я опаздываю в школу, он не упускает возможности пошутить про меня. Такой уж он старик...

    Что до меня, то меня зовут Мирай Ёсимура, мне 17. Я выпускник академии Курода, что находится в небольшой Японской деревеньке Кобаяси.

    Если вы взгляните на карту, то не сможете её там найти, потому что правительство Японии считает, что мы принадлежим к кварталу Акихабара. Что такое Акиба, я думаю, вы и сами прекрасно знаете.

    Ранее я говорил, что являюсь выпускником, и в этом году мне предстоит сдача вступительных экзаменов.

    Я со своим лучшим другом Ноем, хотим поступить в престижный музыкальный университет, чтобы вскоре основать музыкальную группу под названием Rebels.

    Сами по себе мы играем j-rock, но мы не против исполнить какой-нибудь трек в жанре heavy metal. Но это уже не так важно, как само поступление.

    Чтобы вы понимали, экзамен состоит только из практической части. И я несомненно этому рад! У меня всегда было плохо с теорией, но вот с практическими занятиями проблем никогда не возникало.

    Но зато когда мы с Ноем станем профессиональными музыкантами...

    Нас ждет совместная запись альбомов, миллионы фанов и взрывные концерты. Даааа...

    Эх... Мечты. Но реальность довольно суровая штука.

    Как на меня не посмотри, обычный школьник, поэтому можете смело присвоить мне звание типичного главного героя визуального романа.

    Но знаете… Кое-что меня беспокоит ещё с того момента как я проснулся.

    Мне приснился ужасный сон, я бы даже сказал кошмар.

    Если вкратце, то в нем я и мой друг детства Рэй были на улице ночью, тогда еще шёл дождь, помнится мне.

    Я держал её на своих руках, но она была без сознания и выглядела очень больной. Словно вот-вот умрёт. А потом—

    """
    show n say with dissolve

    n "Кого я вижу! Да это же Мирай! С добрым утром, соня!"

    menu:
        "Ответить.":
            m "И с каких это пор я соней стал?"
            $ reply = True

        "Игнорировать.":
            "..."
            n "Ты чего? Оглох что ли?"
            n "Приём! Земля вызывает Мирая! Приём!"
            m "Вот чего ты ко мне прицепился?"
            show n confuz with dissolve
            "Ну как же? Я не могу подколость своего лучшего друга?"
            jump end_tick

        "Секретный выбор" if said_true:
            "Поздравляем! Вы выбрали правильный вариант в прошлом выборе!"
label end_tick:
    n "Да ты себя видел?! У тебя на голове будто птичье гнездо!"

    m "А? Ну блин, опять..."



    show n surprise_opmou at Position(xalign = 1.0) with move

    show r smiler with dissolve

    r "Ахахаха..."

    m "О, Рэй-чан, привет!"

    show r shyr at Position(xalign = 0) with move

    r "..."

    m "Что-то не так?"

    r "Да, нет... Просто ты смешной, Мирай-кун."

    m "Ну, вот. И ты туда же."
    show r smiler at Position(xalign = 0) with Dissolve(0.3)

    r "Ахахаха… Но ведь правда смешно, прости, пожалуйста."

    m "Ладно, проехали. Пойдемте уже. Через пару минут урок начинается."
    scene bg black with dissolve
    pause 2
jump scene3
label wake_up:

    scene bg school_corr
    scene bg school
    with dissolve

    show t say

    teach """
    Для начала возьмите две точки и соедините их в пространстве.
    Далее, вам необходимо найти угол между ними.
    И, вот таким образом вы сможете построить этот график.
    """
    m "Ммм..."

    teach "И только после того, как вы выполните все эти действия, задание будет зачтено"
    """

    Ммм... Чёрт, опять уснул на уроке. Вот незадача.

    Сегодня точно лягу спать пораньше.

    Еще и сон какой-то приснился странный. Самый настоящий кошмар.

    """
    jump scene3_1

    hide Teacher

    #Конец сцены 2.

#Конец сцены 2


label scene3:
    scene bg school_corr with dissolve
    pause 1
    scene bg school
    show t say
    with dissolve

    teach """
    Для начала возьмите две точки и соедините их в пространстве.
    Далее, вам необходимо найти угол между ними.
    И, вот таким образом вы сможете построить этот график.
    """

    scene bg school_blur
    show t say_blur
    with Dissolve(0.5)
    """
    Сегодняшний сон был слишком реальным.

    Что-то не нравится мне всё это...

    Я что-то упускаю!

    ...Будто я упускаю что-то важное.

    Что-то очень важное.
    """
label scene3_1:
    show t angry with Dissolve(0.5)

    teach """
    Эй! Там за третьей партой! Мирай, да?
    Я смотрю, ты витаешь в облаках, а значит давным-давно всё понял.
    Так что давай к доске, скорее!
    """

    "\"Я постараюсь понять в чём дело.\""

    hide Teacher

    scene bg black with dissolve
    pause 1
    scene bg school with dissolve
    play sound "music/bell_sound.mp3" fadein 0.5 fadeout 0.5


    "Наконец-то."

    scene bg school_corrl with dissolve

    """
    А? Что это? Сообщение от Рэй. Что это с ней? Обычно она не пишет СМСки.

    Сейчас посмотрим...

    «Встретимся на нашем месте после школы. Буду ждать тебя как обычно. Рэй  (っ´ω｀)ﾉ.»

    На нашем месте, значит.

    Похоже, стоит сказать Ною, что репетиция задержится.

    Только вот, где его чёрт носит?

    Как только колокол звонит, то он тут как тут, а сегодня почему-то задерживается.
    """

    "\"ДА, ЧТОБ ТЕБЯ, НОЙ! ПАРШИВЕЦ! ВОТ Я ЕМУ НАДАЮ ПО БАШКЕ!!!\""

    show n say with dissolve

    n "А, вот и я."

    m "Я тебя ненавижу... Я говорил тебе об этом?!"


    n "Ахахах. Извини, я на пару минут задержался в кабинете студенческого совета."

    show n confuz with Dissolve(0.5)

    n "Они хотели сделать меня диджеем на школьном фестивале."

    show n dissapointed with Dissolve(0.5)

    n "Я пытался отказаться, но эта глава студсовета так на меня смотрела..."

    n """

    Так смотрела, словно от моего ответа зависело то, убьёт ли она меня или нет.

    """

    m """
    Жуткое зрелище... Согласен.

    Кирари Джун...

    Она является главой студсовета. Каждые 2 года в академии проходят выборы главы студенческого совета и, кто бы мог подумать, что её выберут пять раз подряд.

    Пять раз!

    Немыслимо!

    Мне кажется, что она держит в страхе даже директора академии.

    Иначе, мне не понятно почему её избирают такое количество раз.

    По академии ходит легенда. Как-то раз один из учеников отказался сотрудничать в подготовке к школьному фестивалю.

    После того дня его никто не видел.

    Одни считают, что она его убила, а другие, что наложила гипноз и отправила скитаться по миру.

    Аж мурашки по коже… Жуть какая!

    Я всё понимаю, приятель… У тебя не было выбора.
    """


    n "Спаси меня, Мирай! Я же не выдержу!"

    m """
    Не боись, я ведь тоже иду на школьный фестиваль как и ты.

    Так что всё будет в порядке.
    """


    n """
    Я на это надеюсь.
    Как вспомню ту легенду, так не по себе становится!
    Как... Как его звали, ты помнишь?
    """

    m """
    Не особо.

    Шуичи? Тюичи? Коичи?

    Точно! Коичи! Коичи Тидзуэ!
    """

    n "Да. Ты прав. Интересно, что  сейчас с ним? Он правда отправился обхдить весь земной шар? Это же невозможно, правда?"

    m """
    Как знать, как знать.
    Вот, блин, мне же уже идти пора!
    Ной, сегодня репетиция переносится на пару часов вперёд. Мне нужно встретиться с Рэй. Так что—
    """

    n "Я всё понимаю, мужик. Иди. Встретимся у тебя, я пока подготовлю инструменты и повторю наш репертуар."

    m "Ной… Спасибо! Увидимся!"

    hide Noi

#Конец сцены 3

label scene4:

    scene bg black

    """
    «Встретимся на нашем месте…» Чего же ты захотела вновь встретиться. Да еще и в этом месте.

    Давненько я не был там.

    Интересно, там всё еще так красиво, как я его помню?

    Место, к которому я иду — это холм у старого моря. Наше любимое место встречи с Рэй.

    Прекрасная густая трава растеляется на десятки километров.

    Чайки, кружащие над головами.

    И какие же чайки без моря?

    Конечно, там есть море, вид которого заставляет задуматься над тем, насколько же ты мал перед всем миром.

    Настолько оно красивое, море Абаккио.

    А названо оно в честь погибшего воина, защищающего дорогую для него девушку по имени Триш Уна.

    Но то, ради чего туда действительно стоит пойти, так это ради заката.

    Был бы я богат, то точно бы купил себе дом на этом холме и каждый вечер наблюдал бы за закатом.

    Ну, вот я и на месте.

    Где это Рэй?
    """

    show Rei

    m "Нашел—!"

    r "АААААА!"

    m "Ахахаха! Испугалась?"

    r "Дурак!"

    m "Чего это ты?"

    r "..."

    m """
    Видимо, она не в настроении.

	Ладно, ладно. Прости.
    """

    r "Ничего… Я не обижаюсь."

    m """
    Так зачем ты меня сюда позвала?

    Еще и СМСки отправляешь.

    Говорил же тебе — используй Teregran.

    Вечно она упрямится.
    """

    r "Мирай-кун..."

    m "А?"

    r """
    Помнишь, как мы играли здесь в детстве?

    Когда мне было грустно, ты звал меня на этот холм и вместе мы смотрели на закат, помнишь?

    Тогда мне было так одиноко... У меня не было друзей потому что другие дети считали меня странной. Но не ты.

    Ты был другим. И я была так счастлива.

    Так счастлива, что у меня наконец-то появился настоящий друг.
    """

    m "..."

    r "И тогда, ты сказал мне—"

    #Переход в прошлое

    m "Эй, ты! Чего ты такая грустная?"

    r "Со мной никто не хочет дружить..."

    m "Почему это?!"

    r "Они считают, что я странная."

    m "Странная?!"

    r "Да..."

    m """
    Слушай, что я скажу тебе.

    Все мы со своими причудами. Кто-то просто не в состоянии понять твои чувства и из-за этого они тебя боятся.
    """

    r "Но ведь..."

    m """
    Никаких «но ведь».

    Знаешь, я вот тоже странный! Я люблю кричать на каждом шагу, какой я крутой и никто мне не указ!
    """

    r "Хихихихи..."

    m "Ты чего смеешься?!"

    r "Да так... Просто ты немного смешной."

    m "Хехех... Пойдем со мной!"

    r "А? К-куда?"

    m "Я покажу тебе одно место."

    r "Н-но, ведь… Родители, они—"

    m "Никаких «но ведь». Я же тебе уже говорил об этом, а родители подождут, это недалеко."

    r "Л-ладно, только ненадолго."

    m "Тебе понравится, даю слово!"

    r "Ух ты... Какая красота..."

    m """
    Нравится, да?

    Я прихожу сюда всегда, когда мне становится грустно или одиноко.

    Когда я смотрю на этот закат, то мне становится совсем всё равно на остальной мир.

    Словно я и есть весь этот океан.

    Словно я один во всём мире.

    Как-то так...
    """

    r "Это правда невероятно красиво. С-спасибо… Э-эм… Я не знаю твоего имени, прости."

    m "Мирай."

    r "А...?"

    m "Меня зовут Мирай. Мирай Ёсимура."

    r "Спасибо тебе, Мирай-сенпай..."

    m "Зови меня просто Мирай."

    r "М-Мирай… Я очень тебе благодарна."

    m """
    Да не за что!

    Тебя-то как звать?
    """

    r "Я… Я Рэй. Рэй Юкари."

    m """
    Приятно познакомиться, Рэй-чан!

    Как ты смотришь на то, чтобы приходить сюда, иногда, вечером. Чтобы, э-эм… Смотреть на закат?
    """

    r "Хорошо, я согласна."

    m """
    Значит, договорились.

	Тогда—
    """
    r "Д-давай посидим вот так… Некоторое время."

    m "Н-ну, ладно..."

    #Конец прошлого

    r "Хорошее было время..."

    m "..."

    r """
    А теперь… Ты перестал приходить сюда и мне снова так одиноко…

    Настолько одиноко, что я чувствую как мое сердце охватывает невыносимая боль.

    Словно оно вот-вот разорвётся на куски.
    """

    m "..."

    r """
    Но, знаешь… Я привыкла к боли.

	Каждую ночь я чувствую как она разрушает меня изнутри.

	Каждое утро я просыпаюсь от того, что боль не прекращается.

	Она не даёт о себе забыть ни на минуту и, даже сейчас… Эта боль просто невыносима!

	Почему она просто не исчезнет!?

	Если мне и дальше придется терпеть её, то я лучше предпочту исчезнуть!
    """

    m """
    Хватит.

    Я что-нибудь придумаю.

    Я обязатель что-нибудь придумаю!

    Слышишь, Рэй!

    Я отдам, что угодно, ради твоего спасения.

    Даже собственную жизнь.
    """
    r """
    Мирай...

	Я не хочу больше страдать!

    Почему мне досталась эта болезнь.

    Как я смогу выздороветь, если даже врачи разводят руками!

    Знаешь, что они говорят?

    Они не имеют понятия, что это за болезнь!

    Говорят, что я единственная, кто имеет такой необъяснимый диагноз!

    За что мне всё это?! Я ведь не сделала ничего плохого!
    """
    m "Хватит!"

    r "..."

    m """
    Я ведь сказал тебе!

    Я ни за что не брошу тебя!

    Я ни за что не позволю тебе умереть!

    И пожертвую ради этого своей жизнью!
    """

    r """
    Мирай…

    Я не хочу умирать…
    """

    m """
    Мы выкарабкаемся из этой ситуации совместными усилиями.

	Уже темнеет. Я провожу тебя домой. Пойдём.
    """

    r "Ладно..."

    #Конец сцены

#Конец сцены 4

label scene5:

    m "Хорошо. Теперь мне пора домой."

    r "Будь осторожен по пути домой."

    m "Чего это ты за меня беспокоишься?"

    r "Да так..."

    m """
    ...

    ...Ладно, тогда я пойду.
    """

    r "Мирай..."

    m "М?"

    r """
    Спасибо...

	... За всё.
    """

    m """
    ...

	Увидимся в школе. До завтра.
    """














    return