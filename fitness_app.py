from kivy.app import *
from kivy.uix.button import *
from kivy.uix.label import *
from kivy.uix.boxlayout import *
from kivy.uix.screenmanager import *
from kivy.animation import *
from kivy.uix.popup import *
from kivy.base import *
from kivy.lang import *
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import *
from kivy.uix.image import *
from kivy.animation import *
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader

size_hint1 = (.6, .90)
pos_hint1 ={'x':.20}
font_size1 = 30
font_size2 = 40
custom = [1,1,1,0.2]

curr = 0
maxm = 0
pause = 1
difficulty = "средний"
speed = "mid"

sound=SoundLoader.load('ending.mp3')
txt2_ab = Label(text="Сейчас выбран: " + difficulty, font_size = font_size2)

class FirstScr(Screen):                                                                         #ГЛАВНЫЙ ЭКРАН
    def __init__(self, name='first'): 
        super().__init__(name=name)
        with self.canvas.before:
            self.bg = Rectangle(pos=self.pos, size=self.size, source='background.jpg')
        layout1 = BoxLayout(orientation = 'vertical')
        btn1 = Button(text="Тренировки", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn2 = Button(text="Выбор уровня сложности", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn3 = Button(text="Выход", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        layout1.add_widget(btn1)
        layout1.add_widget(btn2)
        layout1.add_widget(btn3)
        btn1.on_press = self.next1
        btn2.on_press = self.next2
        btn3.on_press = self.next3
        self.add_widget(layout1)

    def next1(self):
        global maxm
        self.manager.transition.direction = 'left' 
        self.manager.current = 'second'
        if difficulty == "лёгкий":
            maxm = 10
        if difficulty == "средний":
            maxm = 15
        if difficulty == "сложный":
            maxm = 20
        txt4_a.text= str(curr) + "/" + str(maxm)

    def next2(self):
        self.manager.transition.direction = 'right' 
        self.manager.current = 'fourth'
    
    def next3(self):
        self.manager.transition.direction = 'up' 
        self.manager.current = 'third'

    def on_size(self, *args):
        self.bg.size = self.size

class SecondScr(Screen):
    def __init__(self, name='second'):                             #ВЫБОР УПРАЖНЕНИЯ
        super().__init__(name=name)
        with self.canvas.before:
            self.bg = Rectangle(pos=self.pos, size=self.size, source='background.jpg')
        layout1 = BoxLayout(orientation = 'vertical')
        layout2 = BoxLayout(orientation = 'horizontal')
        btn1 = Button(text="Отжимания", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn2 = Button(text="Приседания", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn3 = Button(text="Пресс", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn7 = Button(text="Назад", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        layout1.add_widget(btn1)
        layout1.add_widget(btn2)
        layout1.add_widget(btn3)
        layout1.add_widget(btn7)
        btn7.on_press = self.next1
        btn1.on_press = self.next2
        btn2.on_press = self.next3
        btn3.on_press = self.next4
        self.add_widget(layout1)

        
    def next1(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

    def next2(self):
        global txt2_a
        global maxm
        global speed_pushups
        self.manager.transition.direction = 'right'
        self.manager.current = 'pushups'
        txt2_a.text = "Уровень сложности: " + difficulty
        if speed == "low":
            speed_pushups = 3
        elif speed == "mid":
            speed_pushups = 2
        elif speed == "high":
            speed_pushups = 1

    def next3(self):
        global txt2_b
        global maxm
        global speed_squats
        self.manager.transition.direction = 'right'
        self.manager.current = 'squats'
        txt2_b.text = "Уровень сложности: " + difficulty
        if speed == "low":
            speed_squats = 3
        elif speed == "mid":
            speed_squats = 2
        elif speed == "high":
            speed_squats = 1

    def next4(self):
        global txt2_b
        global maxm
        global speed_squats
        self.manager.transition.direction = 'right'
        self.manager.current = 'abs'
        txt2_c.text = "Уровень сложности: " + difficulty
        if speed == "low":
            speed_squats = 3
        elif speed == "mid":
            speed_squats = 2
        elif speed == "high":
            speed_squats = 1

    def on_size(self, *args):
        self.bg.size = self.size

class ThirdScr(Screen):                                                           #ВЫХОД
    def __init__(self, name='third'):
        super().__init__(name=name)
        with self.canvas.before:
            self.bg = Rectangle(pos=self.pos, size=self.size, source='background.jpg')
        txt = Label(text="Вы уверены, что хотите выйти?", font_size = font_size2)
        btn1 = Button(text="Да",  font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn2 = Button(text="Нет", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn2.on_press = self.next1
        btn1.on_press = self.next2
        layout = BoxLayout(orientation = 'vertical')
        layout.add_widget(txt)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        self.add_widget(layout)
            
    def next1(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'first'
    def next2(self):
        stopTouchApp()
    
    def on_size(self, *args):
        self.bg.size = self.size

class FourthScr(Screen):                                                              #ВЫБОР СЛОЖНОСТИ                                                          
    def __init__(self, name='fourth'):
        super().__init__(name=name)
        with self.canvas.before:
            self.bg = Rectangle(pos=self.pos, size=self.size, source='background.jpg')
        global difficulty
        global txt2_ab
        txt1 = Label(text="Выбор уровня сложности", font_size = font_size2)
        btn1 = Button(text="Лёгкий",  font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn2 = Button(text="Средний",  font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn3 = Button(text="Сложный",  font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        txt2_ab = Label(text="Сейчас выбран: " + difficulty, font_size = font_size2)        
        btn4 = Button(text="Назад", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn4.on_press = self.next1
        btn1.on_press = self.next2
        btn2.on_press = self.next3
        btn3.on_press = self.next4
        layout1 = BoxLayout(orientation = 'vertical')
        layout2 = BoxLayout(orientation = 'horizontal')
        layout1.add_widget(txt1)
        layout1.add_widget(layout2)
        layout2.add_widget(btn1)
        layout2.add_widget(btn2)
        layout2.add_widget(btn3)
        layout1.add_widget(txt2_ab)
        layout1.add_widget(btn4)
        self.add_widget(layout1)

    def next1(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'
    
    def next2(self):
        global difficulty
        global txt2_ab
        global speed
        difficulty = "лёгкий"
        speed = "low"
        txt2_ab.text = "Сейчас выбран: " + difficulty

    def next3(self):
        global difficulty
        global txt2_ab
        global speed
        difficulty = "средний"
        speed = "mid"
        txt2_ab.text = "Сейчас выбран: " + difficulty

    def next4(self):
        global difficulty
        global txt2_ab
        global speed
        difficulty = "сложный"
        speed = "high"
        txt2_ab.text = "Сейчас выбран: " + difficulty
    
    def on_size(self, *args):
        self.bg.size = self.size

class PushUpsScr(Screen):                                                                       #ОТЖИМАНИЯ                                                 
    def __init__(self, name='pushups'):
        super().__init__(name=name)
        with self.canvas.before:
            self.bg = Rectangle(pos=self.pos, size=self.size, source='background.jpg')
        global layout1_a
        global txt1_a
        global txt2_a
        global txt4_a
        global btn1_a
        global btn2_a
        global btn3_a
        global img1_a
        global difficulty
        global maxm
        global curr
        global speed_pushups
        global speed
        img1_a = AsyncImage(source='pushups1.png')
        txt1_a = Label(text="Отжимания", font_size = font_size2, pos_hint = {'x':-0.35})
        txt2_a = Label(text="Уровень сложности: " + difficulty, font_size = font_size2)
        txt3_a = Label(text="Уровень сложности: " + difficulty, font_size = font_size2)
        txt4_a = Label(text= str(curr) + "/" + str(maxm), font_size = font_size2, pos_hint =  {'y':.20})
        btn2_a = Button(text="Старт", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn3_a = Button(text="Пауза", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn1_a = Button(text="Назад", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn1_a.on_press = self.next1
        btn2_a.on_press = self.next2
        btn3_a.on_press = self.next3
        layout1_a = BoxLayout(orientation = 'vertical')
        layout2 = BoxLayout(orientation = 'horizontal')
        layout1_a.add_widget(txt1_a)
        layout1_a.add_widget(img1_a)
        layout1_a.add_widget(txt2_a)
        layout1_a.add_widget(btn2_a)
        layout1_a.add_widget(btn1_a)
        self.add_widget(layout1_a)

        if difficulty == "лёгкий":
            maxm = 10
        elif difficulty == "средний":
            maxm = 15
        elif difficulty == "сложный":
            maxm = 20

    def next1(self):
        global layout1_a
        global txt1_a
        global txt2_a
        global btn1_a
        global btn2_a
        global btn3_a
        global img1_a
        global curr
        global event
        curr = 0
        txt4_a.text = str(curr) + "/" + str(maxm)
        try:
            event.cancel()
        except:
            pass
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'
        try:
            layout1_a.remove_widget(txt1_a)
            layout1_a.remove_widget(txt2_a)
            layout1_a.remove_widget(txt4_a)
            layout1_a.remove_widget(btn2_a)
            layout1_a.remove_widget(btn1_a)
            layout1_a.remove_widget(btn3_a)
            layout1_a.remove_widget(btn1_a)
            layout1_a.remove_widget(img1_a)

            layout1_a.add_widget(txt1_a)
            layout1_a.add_widget(img1_a)
            layout1_a.add_widget(txt2_a)
            layout1_a.add_widget(btn2_a)
            layout1_a.add_widget(btn1_a)
        except:
            pass

    def next2(self):
        global layout1_a
        global txt1_a
        global txt2_a
        global txt4_a
        global btn1_a
        global btn2_a
        global curr
        global maxm
        global event
        global speed_pushups
        global updt_pushups
        global sound
        updt_pushups = 0
        layout1_a.remove_widget(txt1_a)
        layout1_a.remove_widget(txt2_a)
        layout1_a.remove_widget(btn2_a)
        layout1_a.remove_widget(btn1_a)
        layout1_a.add_widget(txt4_a)
        layout1_a.add_widget(btn3_a)
        layout1_a.add_widget(btn1_a)
        img1_a.source='pushups2.png'

        def update_label(self):
            global curr
            global updt_pushups
            updt_pushups += 1
            if updt_pushups % 2 == 0:
                img1_a.source='pushups2.png'
            else:
                img1_a.source='pushups1.png'
                curr += 1
                txt4_a.text = str(curr) + "/" + str(maxm)
            if curr >= maxm:
                event.cancel()
                try:
                    layout1_a.remove_widget(img1_a)
                    layout1_a.remove_widget(btn2_a)
                    layout1_a.remove_widget(btn3_a)
                except:
                    pass   
                txt4_a.text = 'Ты молодец!'
                sound.play()
        event = Clock.schedule_interval(update_label, speed_pushups / 2)

    def next3(self):
        global pause
        global event
        pause += 1
        if pause % 2 == 0:
            btn3_a.text = "Продолжить"
            event.cancel()
        else:
            btn3_a.text = "Пауза"
            def update_label(self):
                global curr
                global updt_pushups
                updt_pushups += 1
                if updt_pushups % 2 == 0:
                    img1_a.source='pushups2.png'
                else:
                    img1_a.source='pushups1.png'
                    curr += 1
                    txt4_a.text = str(curr) + "/" + str(maxm)
                if curr >= maxm:
                    event.cancel()
                    try:
                        layout1_a.remove_widget(img1_a)
                        layout1_a.remove_widget(btn2_a)
                        layout1_a.remove_widget(btn3_a)
                    except:
                        pass   
                    txt4_a.text = 'Ты молодец!'
                    sound.play()
            event = Clock.schedule_interval(update_label, speed_pushups / 2)

    def on_size(self, *args):
        self.bg.size = self.size

class SquatsScr(Screen):                                                                       #ПРИСЕДАНИЯ                                              
    def __init__(self, name='squats'):
        super().__init__(name=name)
        with self.canvas.before:
            self.bg = Rectangle(pos=self.pos, size=self.size, source='background.jpg')
        global layout1_b
        global txt1_b
        global txt2_b
        global txt4_b
        global btn1_b
        global btn2_b
        global btn3_b
        global img1_b
        global img2_b
        global difficulty
        global maxm
        global curr
        global speed_squats
        global speed
        img1_b = AsyncImage(source='Squats2.png')
        txt1_b = Label(text="Приседания", font_size = font_size2, pos_hint = {'x':-0.35})
        txt2_b = Label(text="Уровень сложности: " + difficulty, font_size = font_size2)
        txt3_b = Label(text="Уровень сложности: " + difficulty, font_size = font_size2)
        txt4_b = Label(text= str(curr) + "/" + str(maxm), font_size = font_size2, pos = (100, 100))
        btn2_b = Button(text="Старт", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn3_b = Button(text="Пауза", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn1_b = Button(text="Назад", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn1_b.on_press = self.next1
        btn2_b.on_press = self.next2
        btn3_b.on_press = self.next3
        layout1_b = BoxLayout(orientation = 'vertical')
        layout2 = BoxLayout(orientation = 'horizontal')
        layout1_b.add_widget(txt1_b)
        layout1_b.add_widget(img1_b)
        layout1_b.add_widget(txt2_b)
        layout1_b.add_widget(btn2_b)
        layout1_b.add_widget(btn1_b)
        self.add_widget(layout1_b)

        if difficulty == "лёгкий":
            maxm = 10
        elif difficulty == "средний":
            maxm = 15
        elif difficulty == "сложный":
            maxm = 20

    def next1(self):
        global layout1_b
        global txt1_b
        global txt2_b
        global btn1_b
        global btn2_b
        global btn3_b
        global img1_b
        global img2_b
        global curr
        global event
        curr = 0
        txt4_b.text = str(curr) + "/" + str(maxm)
        try:
            event.cancel()
        except:
            pass
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'
        try:
            layout1_b.remove_widget(txt1_b)
            layout1_b.remove_widget(txt2_b)
            layout1_b.remove_widget(txt4_b)
            layout1_b.remove_widget(btn2_b)
            layout1_b.remove_widget(btn1_b)
            layout1_b.remove_widget(btn3_b)
            layout1_b.remove_widget(btn1_b)
            layout1_b.remove_widget(img1_b)

            layout1_b.add_widget(txt1_b)
            layout1_b.add_widget(img1_b)
            layout1_b.add_widget(txt2_b)
            layout1_b.add_widget(btn2_b)
            layout1_b.add_widget(btn1_b)
        except:
            pass

    def next2(self):
        global layout1_b
        global txt1_b
        global txt2_b
        global txt4_b
        global btn1_b
        global btn2_b
        global curr
        global maxm
        global event
        global speed_squats
        global updt_squats
        updt_squats = 0
        layout1_b.remove_widget(txt1_b)
        layout1_b.remove_widget(txt2_b)
        layout1_b.remove_widget(btn2_b)
        layout1_b.remove_widget(btn1_b)
        layout1_b.add_widget(txt4_b)
        layout1_b.add_widget(btn3_b)
        layout1_b.add_widget(btn1_b)
        img1_b.source='Squats1.png'
        txt4_b.text = str(curr) + "/" + str(maxm)

        def update_label(self):
            global curr
            global updt_squats
            global sound
            updt_squats += 1
            if updt_squats % 2 == 0:
                img1_b.source='Squats1.png'
            else:
                img1_b.source='Squats2.png'
                curr += 1
                txt4_b.text = str(curr) + "/" + str(maxm)
            if curr >= maxm:
                event.cancel()
                try:
                    layout1_b.remove_widget(img1_b)
                    layout1_b.remove_widget(btn2_b)
                    layout1_b.remove_widget(btn3_b)
                except:
                    pass   
                txt4_b.text = 'Ты молодец!'
                sound.play()

        event = Clock.schedule_interval(update_label, speed_squats / 2)

    def next3(self):
        global pause
        global event
        pause += 1
        if pause % 2 == 0:
            btn3_b.text = "Продолжить"
            event.cancel()
        else:
            btn3_b.text = "Пауза"
            def update_label(self):
                global curr
                global updt_squats
                global sound
                updt_squats += 1
                if updt_squats % 2 == 0:
                    img1_b.source='Squats1.png'
                else:
                    img1_b.source='Squats2.png'
                    curr += 1
                    txt4_b.text = str(curr) + "/" + str(maxm)
                if curr >= maxm:
                    event.cancel()
                    try:
                        layout1_b.remove_widget(img1_b)
                        layout1_b.remove_widget(btn2_b)
                        layout1_b.remove_widget(btn3_b)
                    except:
                        pass   
                    txt4_b.text = 'Ты молодец!'
                    sound.play()
            event = Clock.schedule_interval(update_label, speed_squats / 2)

    def on_size(self, *args):
        self.bg.size = self.size

class AbsScr(Screen):                                                                       #ПРЕСС                                             
    def __init__(self, name='abs'):
        super().__init__(name=name)
        with self.canvas.before:
            self.bg = Rectangle(pos=self.pos, size=self.size, source='background.jpg')
        global layout1_c
        global txt1_c
        global txt2_c
        global txt4_c
        global btn1_c
        global btn2_c
        global btn3_c
        global img1_c
        global img2_c
        global difficulty
        global maxm
        global curr
        global speed_squats
        global speed
        img1_c = AsyncImage(source='abs2.png')
        txt1_c = Label(text="Пресс
", font_size = font_size2, pos_hint = {'x':-0.35})
        txt2_c = Label(text="Уровень сложности: " + difficulty, font_size = font_size2)
        txt3_c = Label(text="Уровень сложности: " + difficulty, font_size = font_size2)
        txt4_c = Label(text= str(curr) + "/" + str(maxm), font_size = font_size2, pos = (100, 100))
        btn2_c = Button(text="Старт", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn3_c = Button(text="Пауза", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn1_c = Button(text="Назад", font_size = font_size1, size_hint = size_hint1, pos_hint = pos_hint1, background_color = custom)
        btn1_c.on_press = self.next1
        btn2_c.on_press = self.next2
        btn3_c.on_press = self.next3
        layout1_c = BoxLayout(orientation = 'vertical')
        layout2 = BoxLayout(orientation = 'horizontal')
        layout1_c.add_widget(txt1_c)
        layout1_c.add_widget(img1_c)
        layout1_c.add_widget(txt2_c)
        layout1_c.add_widget(btn2_c)
        layout1_c.add_widget(btn1_c)
        self.add_widget(layout1_c)

        if difficulty == "лёгкий":
            maxm = 10
        elif difficulty == "средний":
            maxm = 15
        elif difficulty == "сложный":
            maxm = 20

    def next1(self):
        global layout1_c
        global txt1_c
        global txt2_c
        global btn1_c
        global btn2_c
        global btn3_c
        global img1_c
        global img2_c
        global curr
        global event
        curr = 0
        txt4_c.text = str(curr) + "/" + str(maxm)
        try:
            event.cancel()
        except:
            pass
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'
        try:
            layout1_c.remove_widget(txt1_c)
            layout1_c.remove_widget(txt2_c)
            layout1_c.remove_widget(txt4_c)
            layout1_c.remove_widget(btn2_c)
            layout1_c.remove_widget(btn1_c)
            layout1_c.remove_widget(btn3_c)
            layout1_c.remove_widget(btn1_c)
            layout1_c.remove_widget(img1_c)

            layout1_c.add_widget(txt1_c)
            layout1_c.add_widget(img1_c)
            layout1_c.add_widget(txt2_c)
            layout1_c.add_widget(btn2_c)
            layout1_c.add_widget(btn1_c)
        except:
            pass

    def next2(self):
        global layout1_c
        global txt1_c
        global txt2_c
        global txt4_c
        global btn1_c
        global btn2_c
        global curr
        global maxm
        global event
        global speed_squats
        global updt_squats
        updt_squats = 0
        layout1_c.remove_widget(txt1_c)
        layout1_c.remove_widget(txt2_c)
        layout1_c.remove_widget(btn2_c)
        layout1_c.remove_widget(btn1_c)
        layout1_c.add_widget(txt4_c)
        layout1_c.add_widget(btn3_c)
        layout1_c.add_widget(btn1_c)
        img1_c.source='abs1.png'
        txt4_c.text = str(curr) + "/" + str(maxm)

        def update_label(self):
            global curr
            global updt_squats
            global sound
            updt_squats += 1
            if updt_squats % 2 == 0:
                img1_c.source='abs1.png'
            else:
                img1_c.source='abs2.png'
                curr += 1
                txt4_c.text = str(curr) + "/" + str(maxm)
            if curr >= maxm:
                event.cancel()
                try:
                    layout1_c.remove_widget(img1_c)
                    layout1_c.remove_widget(btn2_c)
                    layout1_c.remove_widget(btn3_c)
                except:
                    pass   
                txt4_c.text = 'Ты молодец!'
                sound.play()

        event = Clock.schedule_interval(update_label, speed_squats / 2)

    def next3(self):
        global pause
        global event
        pause += 1
        if pause % 2 == 0:
            btn3_c.text = "Продолжить"
            event.cancel()
        else:
            btn3_c.text = "Пауза"
            def update_label(self):
                global curr
                global updt_squats
                global sound
                updt_squats += 1
                if updt_squats % 2 == 0:
                    img1_c.source='abs1.png'
                else:
                    img1_c.source='abs2.png'
                    curr += 1
                    txt4_c.text = str(curr) + "/" + str(maxm)
                if curr >= maxm:
                    event.cancel()
                    try:
                        layout1_c.remove_widget(img1_c)
                        layout1_c.remove_widget(btn2_c)
                        layout1_c.remove_widget(btn3_c)
                    except:
                        pass   
                    txt4_c.text = 'Ты молодец!'
                    sound.play()
            event = Clock.schedule_interval(update_label, speed_squats / 2)
    
    def on_size(self, *args):
        self.bg.size = self.size

class MobileFitnessApp(App):
    def build(self):
        theRoot = FloatLayout()
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThirdScr())
        sm.add_widget(FourthScr())
        sm.add_widget(PushUpsScr())
        sm.add_widget(SquatsScr())
        sm.add_widget(AbsScr())
        return sm
app = MobileFitnessApp()
MobileFitnessApp().run()
