from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class MASApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#121212') # Темная тема
        self.data = {
        
    "салом": ["привет", "hello"],
    "китоб": ["книга", "book"],
    "мактаб": ["школа", "school"],
    "хон": ["комната", "room"],
    "об": ["вода", "water"],
    "нон": ["хлеб", "bread"],
    "модар": ["мать", "mother"],
    "падар": ["отец", "father"],
    "писар": ["сын", "son"],
    "духтар": ["дочь", "daughter"],
    "дӯст": ["друг", "friend"],
    "машқ": ["упражнение", "exercise"],
    "шаҳр": ["город", "city"],
    "деҳот": ["деревня", "village"],
    "автобус": ["автобус", "bus"],
    "машина": ["машина", "car"],
    "туш": ["сон", "dream"],
    "календар": ["календарь", "calendar"],
    "соат": ["часы", "clock"],
    "мизи": ["стол", "table"],
    "курс": ["курс", "course"],
    "дарс": ["урок", "lesson"],
    "даргоҳ": ["университет", "university"],
    "китобхона": ["библиотека", "library"],
    "фан": ["предмет", "subject"],
    "имтиҳон": ["экзамен", "exam"],
    "хат": ["письмо", "letter"],
    "телефон": ["телефон", "phone"],
    "компютер": ["компьютер", "computer"],
    "интернет": ["интернет", "internet"],
    "соҳиб": ["владелец", "owner"],
    "мағоза": ["магазин", "store"],
    "бозор": ["рынок", "market"],
    "таълим": ["образование", "education"],
    "дук": ["магазин", "shop"],
    "ресторан": ["ресторан", "restaurant"],
    "таом": ["еда", "food"],
    "фанн": ["наука", "science"],
    "миён": ["средний", "middle"],
    "бузург": ["большой", "big"],
    "хурд": ["маленький", "small"],
    "сурх": ["красный", "red"],
    "сабз": ["зелёный", "green"],
    "сиёҳ": ["чёрный", "black"],
    "сафед": ["белый", "white"],
    "шаб": ["ночь", "night"],
    "рӯз": ["день", "day"],
    "ҳафта": ["неделя", "week"],
    "моҳ": ["месяц", "month"],
    "соли": ["год", "year"],
    "ҳаво": ["погода", "weather"],
    "барф": ["снег", "snow"],
    "борон": ["дождь", "rain"],
    "офтоб": ["солнце", "sun"],
    "моҳтоб": ["луна", "moon"],
    "ситора": ["звезда", "star"],
    "гул": ["цветок", "flower"],
    "дарахт": ["дерево", "tree"],
    "барг": ["лист", "leaf"],
    "боғ": ["сад", "garden"],
    "сабзавот": ["овощ", "vegetable"],
    "мева": ["фрукт", "fruit"],
    "қалам": ["ручка", "pen"],
    "дафтар": ["тетрадь", "notebook"],
    "кӯрпача": ["подушка", "pillow"],
    "кат": ["кровать", "bed"],
    "кўрпача": ["одеяло", "blanket"],
    "пеши": ["стул", "chair"],
    "тобут": ["сундук", "chest"],
    "канд": ["печенье", "cookie"],
    "чой": ["чай", "tea"],
    "қаҳва": ["кофе", "coffee"],
    "шир": ["молоко", "milk"],
    "тушт": ["масло", "butter"],
    "тандур": ["печь", "oven"],
    "кухня": ["кухня", "kitchen"],
    "ҳоҷатхона": ["туалет", "toilet"],
    "ванна": ["ванна", "bath"],
    "душ": ["душ", "shower"],
    "мўй": ["волосы", "hair"],
    "чашм": ["глаз", "eye"],
    "даҳон": ["рот", "mouth"],
    "дандон": ["зуб", "tooth"],
    "гуфтор": ["язык", "tongue"],
    "кӯкр": ["шея", "neck"],
    "дона": ["рука", "hand"],
    "по": ["нога", "leg"],
    "пой": ["стопа", "foot"],
    "пешон": ["лоб", "forehead"],
    "қулоқ": ["ухо", "ear"],
    "бин": ["нос", "nose"],
    "сина": ["грудь", "chest"],
    "паҳлӯ": ["бок", "side"],
    "шикам": ["живот", "stomach"],
    "пеш": ["перед", "front"],
    "қафо": ["спина", "back"],
    "дӯстона": ["дружба", "friendship"],
    "мусиқӣ": ["музыка", "music"],
    "расм": ["картина", "picture"],
    "сурат": ["фото", "photo"],
    "китобча": ["буклет", "booklet"],
    "матн": ["текст", "text"],
    "хабар": ["новость", "news"],
    "рӯзнома": ["газета", "newspaper"],
    "журнал": ["журнал", "magazine"],
    "телевизор": ["телевизор", "television"],
    "радио": ["радио", "radio"],
    "кино": ["фильм", "movie"],
    "театр": ["театр", "theater"],
    "сахна": ["сцена", "stage"],
    "сана": ["дата", "date"],
    "соат": ["время", "time"],
    "дақиқа": ["минута", "minute"],
    "сония": ["секунда", "second"],
    "савдо": ["торговля", "trade"],
    "мағоза": ["магазин", "shop"],
    "бозор": ["рынок", "market"],
    "боғ": ["сад", "garden"],
    "кӯча": ["улица", "street"],
    "масҷид": ["мечеть", "mosque"],
    "чампон": ["церковь", "church"],
    "шиш": ["стекло", "glass"],
    "коғаз": ["бумага", "paper"],
    "қалам": ["карандаш", "pencil"],
    "дафтaр": ["тетрадь", "notebook"],
    "пардохт": ["оплата", "payment"],
    "ҳуқуқ": ["право", "law"],
    "адолат": ["справедливость", "justice"],
    "сабт": ["запись", "record"],
    "савол": ["вопрос", "question"],
    "ҷавоб": ["ответ", "answer"],
    "мавзӯъ": ["тема", "topic"],
    "мизоҷ": ["настроение", "mood"],
    "ҳолат": ["состояние", "condition"],
    "маълумот": ["информация", "information"],
    "таҳлил": ["анализ", "analysis"],
    "қарор": ["решение", "decision"],
    "амал": ["действие", "action"],
    "нақша": ["план", "plan"],
    "натиҷа": ["результат", "result"],
    "ҳаёт": ["жизнь", "life"],
    "мавҷудият": ["существование", "existence"],
    "охир": ["конец", "end"],
    "сарчашма": ["источник", "source"],
    "таърих": ["история", "history"],
    "давр": ["период", "period"],
    "замон": ["время", "era"],
    "макон": ["место", "place"],
    "сайёра": ["планета", "planet"],
    "замин": ["земля", "earth"],
    "обу ҳаво": ["климат", "climate"],
    "дарё": ["река", "river"],
    "кӯл": ["озеро", "lake"],
    "боҳр": ["море", "sea"],
    "тӯфон": ["буря", "storm"],
    "шамол": ["ветер", "wind"],
    "туман": ["туман", "fog"],
    "шоҳ": ["король", "king"],
    "шоҳзода": ["принц", "prince"],
    "шоҳзода": ["принцесса", "princess"],
    "подшоҳ": ["император", "emperor"],
    "вазир": ["министр", "minister"],
    "сарвазир": ["премьер-министр", "prime minister"],
    "ҳукумат": ["правительство", "government"],
    "қонун": ["закон", "law"],
    "сарҳад": ["граница", "border"],
    "сарзамин": ["территория", "territory"],
    "мард": ["мужчина", "man"],
    "зан": ["женщина", "woman"],
    "писар": ["сын", "son"],
    "духтар": ["дочь", "daughter"],
    "бобо": ["дедушка", "grandfather"],
    "модарбузург": ["бабушка", "grandmother"],
    "хоҳар": ["сестра", "sister"],
    "бародар": ["брат", "brother"],
    "дӯст": ["друг", "friend"],
    "ҳамкор": ["коллега", "colleague"],
    "муаллим": ["учитель", "teacher"],
    "шогирд": ["ученик", "student"],
    "донишҷӯ": ["студент", "student"],
    "таълим": ["образование", "education"],
    "донишгоҳ": ["университет", "university"],
    "синфхона": ["класс", "classroom"],
    "дарс": ["урок", "lesson"],
    "тафсилот": ["деталь", "detail"],
    "мақсад": ["цель", "goal"],
    "ҳадаф": ["задача", "objective"],
    "натича": ["результат", "result"],
    "таҷриба": ["опыт", "experience"],
    "маҳсулот": ["продукт", "product"],
    "хизмат": ["услуга", "service"],
    "ҷой": ["место", "place"],
    "шаҳр": ["город", "city"],
    "деҳа": ["деревня", "village"],
    "хиёбон": ["проспект", "avenue"],
    "кӯча": ["улица", "street"],
    "майдон": ["площадь", "square"],
    "боғ": ["сад", "garden"],
    "парк": ["парк", "park"],
    "маданӣ": ["культура", "culture"],
    "санъат": ["искусство", "art"],
    "расм": ["картина", "painting"],
    "сурат": ["фото", "photo"],
    "китобхона": ["библиотека", "library"]

}

        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Заголовок
        layout.add_widget(Label(
            text="MAS TRANSLATOR", 
            font_size='32sp', 
            bold=True, 
            color=get_color_from_hex('#4CAF50'),
            size_hint_y=None, height=100
        ))

        # Поле ввода
        self.input = TextInput(
            hint_text='Введите слово...',
            multiline=False, size_hint_y=None, height=120,
            font_size='24sp', padding=[20, 30],
            background_color=(0.2, 0.2, 0.2, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1)
        )
        self.input.bind(text=self.translate)
        layout.add_widget(self.input)

        # Результаты
        self.res_ru = Label(text="Русский: -", font_size='22sp', halign='left')
        self.res_en = Label(text="English: -", font_size='22sp', halign='left')
        
        layout.add_widget(self.res_ru)
        layout.add_widget(self.res_en)
        layout.add_widget(BoxLayout()) # Пустое место
        
        return layout

    def translate(self, instance, value):
        word = value.lower().strip()
        if word in self.data:
            self.res_ru.text = f"Русский: {self.data[word][0]}"
            self.res_en.text = f"English: {self.data[word][1]}"
        else:
            self.res_ru.text = "Не найдено"
            self.res_en.text = "-"

if __name__ == '__main__':
    MASApp().run()