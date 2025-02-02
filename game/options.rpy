﻿## Цей файл містить параметри, які можна змінити, щоб налаштувати гру.
##
## Рядки, що починаються з двох позначок «#», є коментарями, і ви не повинні
## розкоментувати їх. Рядки, що починаються з одного знака «#», є закоментованим
## кодом, і ви можете за потреби розкоментувати їх.


## Основи ######################################################################

## Зрозуміла назва гри. Це використовується для встановлення заголовка вікна за
## замовчуванням і відображається в інтерфейсі та звітах про помилки.
##
## _() навколо рядка позначає його як придатний для перекладу.

define config.name = _("""\
The history of the life
of Folket from Marseille""")


## Визначає, чи заголовок, наведений вище, відображається на екрані головного
## меню. Встановіть значення False, щоб приховати назву.

define gui.show_name = True


## Версія гри.

define config.version = "0.7.4"


## Текст, який розміщується на екрані інформації про гру. Поставте текст між
## потрійними лапками, а між абзацами залиште порожній рядок.

image telegram_icon:
    "images/icons/telegram.svg"
    fit "contain"

image mail_icon:
    "images/icons/mail.svg"
    fit "contain"

init python:
    def telegram_link(tag, argument):
        assert '/' not in argument
        return [
            (renpy.TEXT_TAG, "image=telegram_icon"),
            (renpy.TEXT_TAG, f"a=https://t.me/{argument}"),
            (renpy.TEXT_TEXT, argument),
            (renpy.TEXT_TAG, "/a"),
        ]
    
    def mail_link(tag, argument):
        assert '@' in argument
        return [
            (renpy.TEXT_TAG, "image=mail_icon"),
            (renpy.TEXT_TAG, f"a=mailto:{argument}"),
            (renpy.TEXT_TEXT, argument),
            (renpy.TEXT_TAG, "/a"),
        ]

    config.self_closing_custom_text_tags["telegram"] = telegram_link
    config.self_closing_custom_text_tags["mail"] = mail_link

define gui.about = """\
Team:

Heorhii Novikov - 2D artist 
{mail=heorhi.novikov@gmail.com}, {telegram=lasosesom}

Ira Sobchak - Game designer, 2D artist 
{telegram=RinkaRiko}, {mail=ira.sobchak.ss@gmail.com}

Michael Korabelskyi - Game-designer, writer
{mail=densetup@gmail.com}, {telegram=Michael_Kharkov}

Michael Ulianich - developer
{a=https://belkka.itch.io}belkka.itch.io{/a}, {telegram=belkka}
"""


## Коротка назва гри, яка використовується для виконуваних файлів і каталогів
## у вбудованому дистрибутиві. Це має бути лише ASCII і не повинно містити
## пробілів, двокрапки чи крапки з комою.

define build.name = "folket"


## Звуки і музика ##############################################################

## Ці три змінні керують, серед іншого, тим, які міксери відображаються гравцеві
## за замовчуванням. Встановлення для одного з них значення False приховає
## відповідний мікшер.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## Щоб дозволити користувачеві відтворювати тестовий звук на звуковому або
## голосовому каналі, розкоментуйте рядок нижче та використовуйте його, щоб
## установити зразок звуку для відтворення.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Розкоментуйте наступний рядок, щоб налаштувати аудіофайл, який
## відтворюватиметься, коли плеєр перебуває в головному меню. Цей файл
## продовжуватиме відтворюватися в грі, доки його не буде зупинено або не буде
## відтворено інший файл.
define config.main_menu_music = "audio/melancholic-piano-ballad.wav"

init python:
    def text_sound(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/pencil-drawing-on-paper.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

define config.all_character_callbacks = [text_sound]

## Переходи ####################################################################
##
## Ці змінні встановлюють переходи, які використовуються, коли відбуваються
## певні події. Кожна змінна має бути встановлена на перехід або None, щоб
## вказати, що перехід не слід використовувати.

## Вхід або вихід з меню гри.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Між екранами меню гри

define config.intra_transition = dissolve


## Перехід, що використовується після завантаження гри.

define config.after_load_transition = None


## Використовується під час входу в головне меню після завершення гри.

define config.end_game_transition = None


## Змінна для встановлення переходу, що використовується під час запуску гри, не
## існує. Натомість використовуйте а з заявою після показу початкової сцени.


## Керування вікнами ###########################################################
##
## Цей параметр визначає час відображення діалогового вікна. Якщо "show", він
## завжди відображається. Якщо "hide", воно відображається лише за наявності
## діалогу. Якщо "auto", вікно буде приховано перед операторами сцени та
## показано знову, коли відобразиться діалог.
##
## Після початку гри це можна змінити за допомогою операторів "window show",
## "window hide" і "window auto".

define config.window = "auto"


## Переходи, які використовуються для показу та приховування діалогового вікна

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Параметри за замовчуванням ##################################################

## Керує швидкістю тексту за замовчуванням. За замовчуванням, 0, є нескінченним,
## тоді як будь-яке інше число означає кількість символів за секунду, які
## потрібно ввести.

default preferences.text_cps = 50


## Затримка автоматичного пересилання за умовчанням. Більші числа призводять до
## довшого очікування, при цьому допустимим діапазоном є від 0 до 30.

default preferences.afm_time = 15


## Зберегти каталог ############################################################
##
## Контролює місце, де Ren'Py буде розміщувати файли збереження для цієї гри.
## Файли збереження будуть розміщені в:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Як правило, це не слід змінювати, і якщо це так, завжди має бути літеральний
## рядок, а не вираз.

define config.save_directory = "folket-1675218117"


## Значок ######################################################################
##
## Значок, що відображається на панелі завдань або док-станції.

define config.window_icon = "gui/window_icon.png"


## Конфігурація збірки #########################################################
##
## Цей розділ керує тим, як Ren'Py перетворює ваш проект у файли розповсюдження.

init python:

    ## Наступні функції приймають шаблони файлів. Шаблони файлів не чутливі до
    ## регістру та зіставляються зі шляхом відносно основного каталогу, з / без
    ## нього на початку. Якщо збігається декілька шаблонів, використовується
    ## перший.
    ##
    ## У шаблоні:
    ##
    ## / є роздільником каталогу.
    ##
    ## * відповідає всім символам, крім роздільника каталогу.
    ##
    ## ** відповідає всім символам, включаючи роздільник каталогу.
    ##
    ## Наприклад, "*.txt" відповідає файлам txt у базовому каталозі, "game/
    ## **.ogg" відповідає файлам ogg у каталозі гри або будь-якому з його
    ## підкаталогів, а "**.psd " відповідає файлам psd будь-де в проекті.

    ## Класифікуйте файли як None, щоб виключити їх із вбудованих дистрибутивів.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Щоб архівувати файли, класифікуйте їх як 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Файли, що відповідають шаблонам документації, дублюються у збірці
    ## програми Mac, тому вони з’являються як у програмі, так і в zip-файлі.

    build.documentation('*.html')
    build.documentation('*.txt')


## Для завантаження файлів розширення та здійснення покупок у програмі потрібен
## ліцензійний ключ Google Play. Його можна знайти на сторінці "Services & APIs"
## консолі розробника Google Play.

# define build.google_play_key = "..."


## Ім’я користувача та назва проекту, пов’язані з проектом itch.io, розділені
## скісною рискою.

# define build.itch_project = "renpytom/test-project"


define game.transition_pause = 1.5

