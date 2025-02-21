from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.scrollview import ScrollView
from main import  lbl_scr1, lbl_scr2, age_scr1, result_scr2, ecran3_txt, lbl_scr4, result2_scr4, result_scr4, name_scr1
from kivy.core.window import Window
from ruffire import sums_rufye
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar

list_1 = list()


class MainScr(Screen):
  def __init__(self, **kwargs):
      super(MainScr, self).__init__(**kwargs)

      Window.size = (950, 700)

      blue = (0.34, 0.45, 0.89, 1)
      Window.clearcolor = blue

      vl = BoxLayout(orientation='horizontal')
      loyout_main = BoxLayout(orientation='vertical')
      loyout_main2 = BoxLayout(orientation='vertical')
      loyout_main3 = BoxLayout(orientation='horizontal')
      hl = BoxLayout(orientation='vertical')

      self.txt_btn2 = TextInput(hint_text="Ось тутка", size_hint = (1, 0.2), pos_hint = {"center_x": 0.5, "center_y": 0.2}, multiline = False)
      self.year_btn = TextInput(hint_text="Ось тут", size_hint = (1, 0.2), pos_hint = {"center_x": 0.5, "center_y": 0.2}, multiline = False)
      self.nxt_btn = Button(text="Next page", size_hint=(0.4, 0), pos_hint = {"center_x": 0.5, "center_y": 0.5})
      
      loyout_main.add_widget(lbl_scr1)
      loyout_main3.add_widget(name_scr1)
      loyout_main3.add_widget(self.year_btn)
      vl.add_widget(age_scr1)
      vl.add_widget(self.txt_btn2)
      loyout_main2.add_widget(self.nxt_btn)

      hl.add_widget(loyout_main)
      hl.add_widget(loyout_main3)
      hl.add_widget(vl)
      hl.add_widget(loyout_main2)
      self.add_widget(hl)
      self.nxt_btn.bind(on_press=self.gosecondscr)
  def gosecondscr(self, instance):
     self.manager.current="first"
     global btn2_text, btn3_text
     btn2_text = self.txt_btn2.text     
     btn3_text = self.year_btn.text


class FirstScr(Screen):
  def __init__(self, **kwargs):
      super(FirstScr, self).__init__(**kwargs)
      vl = BoxLayout(orientation='vertical')
      hl = BoxLayout(orientation='horizontal')
      vl2 = BoxLayout(orientation='vertical')
      hl2 = BoxLayout(orientation='vertical')
      horithontal_5_1 = BoxLayout (orientation = "horizontal", size_hint = (1, None), height = 50)
      Window.size = (950, 700)
      #btn = Button(text='Назад', size_hint=(.5, .4), pos_hint={'down' : .5})
      self.button_5_1 = Button (text = "<-", size_hint = (None, None), size = (100, 50))
      self.btn_nxt = Button(text="Дальше", size_hint=(0.4, 0), pos_hint={"center_x": 0.5, "center_y": 0.5})
      self.txt_inp = TextInput(hint_text="Результат пишіть сюди", size_hint = (1, 0.2), pos_hint = {"center_x": 0.4, "center_y": 0.5}, multiline = False)
      self.btn_nxt.bind(on_press=self.gothirdscr)
      vl.add_widget(lbl_scr2)
      hl.add_widget(result_scr2)
      hl.add_widget(self.txt_inp)
      vl2.add_widget(self.btn_nxt)
      hl2.add_widget(vl)
      hl2.add_widget(hl)
      hl2.add_widget(vl2)
      horithontal_5_1.add_widget()
      hl2.add_widget(horithontal_5_1)
      self.add_widget(hl2)
  def gothirdscr(self, instance):
      self.manager.current = "second"
      global btn3_text3
      btn3_text3 = self.txt_inp.text 


class SecondScr(Screen):
  def __init__ (self, **kwargs):
      super (SecondScr, self).__init__ (**kwargs)
#Встановлюємо розмір вікна.
      Window.size = (950, 700)
#Створення направних ліній.
      widget_3 = BoxLayout (orientation = "vertical")
      vertical_3m = BoxLayout (orientation = "vertical", padding = 4, spacing = 4)
      horithontal_3_1 = BoxLayout (orientation = "horizontal", padding = 200)
      horithontal_3_2 = BoxLayout (orientation = "horizontal", padding = 20, spacing = 8)
      horithontal_3_3 = BoxLayout (orientation = "horizontal", spacing = 0)
      horithontal_3_4 =  BoxLayout (orientation = "horizontal", size_hint = (1, None), height = 50)
#Створення тексту таймера.
      self.krok_2_1 = Label (text = "45", font_size = "20sp")
      self.timer_label = Label (text = f"Залишилось часу: {self.krok_2_1.text} Секунд.", font_size = "20sp")
#Створення кнопок.
      self.button_3_1 = Button (text = "Продовжити", size_hint = (0.4, 0))
      self.button_3_1.disabled = True
      self.button_3_1.bind (on_press = self.go_to_scrin4)

      self.button_3_2 = Button (text = "Почати", size_hint = (0.4, 0))
      self.button_3_2.bind (on_release = self.start_progress)
      self.button_3_3 = Button (text = "<-", size_hint = (None, None), size = (100, 50))
      self.button_3_3.bind (on_press = self.go_to_scrin2)
#Створення прогресбару/рядка загрузеи.
      self.progress_bar = ProgressBar (max = 45, height = 50) #Встановлення максимального значення 45с-100%.
#Додавання до ліній інтерфейсу.
      horithontal_3_4.add_widget (self.button_3_3)
      horithontal_3_3.add_widget (self.timer_label)
      horithontal_3_1.add_widget (self.progress_bar)
      horithontal_3_2.add_widget (self.button_3_2)
      horithontal_3_2.add_widget (self.button_3_1)
#Додавання до віджету ліній.
      widget_3.add_widget (horithontal_3_4)
      widget_3.add_widget (vertical_3m)
      widget_3.add_widget (horithontal_3_3)
      widget_3.add_widget (horithontal_3_1)
      widget_3.add_widget (horithontal_3_2)

#Додавання до селфу віджету.
      self.add_widget (widget_3)
#Деф старту прогресбара.
  def start_progress(self, instance):
      self.button_3_2.disabled = True
#Становлення текст мітки таймера на 45.
      self.krok_2_1.text = ("45")
#Створення залишку часу.
      self.time_left = 45
#Створення значення прогрес бару.
      self.progress_bar.value = 0
#Запуск апдейтпрогрес кожну секунду/оновлювлення прогресбар та таймер.
      Clock.schedule_interval (self.update_progress, 1)
#Деф оновлення з часом прогрес бару.
  def update_progress (self, dt):
#Іф перевірки чи прогресбар не більший 45.
      if self.progress_bar.value < 45:
#Збільшуєм прогресбар.
          self.progress_bar.value += 1
#Зменшуєм час.
          self.time_left -= 1
#Оновлюємо текст.
          self.krok_2_1.text = str (self.time_left)
          self.timer_label.text = f"Залишилось часу: {self.time_left} Секунд."
      else:
#Зупинка апдейтпрогрес.
            Clock.unschedule (self.update_progress)
            self.button_3_1.disabled = False
#Деф переходу до скрін2.
  def go_to_scrin2 (self, instance):
      self.manager.transition = SlideTransition (direction = "right")
      self.manager.current = ("first")
#Деф переходу до скрін1.
  def go_to_scrin4 (self, instance):
      self.manager.transition = SlideTransition (direction = "left")
      self.manager.current = ("third")
class ThirdScr(Screen):
  def __init__(self,**kwargs):
      super(ThirdScr, self).__init__(**kwargs)

      Window.size = (950, 700)

      vl = BoxLayout(orientation='horizontal')
      hl = BoxLayout(orientation='vertical')
      vl2 = BoxLayout(orientation='vertical')
      hl2 = BoxLayout(orientation='horizontal')
      vl3 = BoxLayout(orientation='vertical')


      self.txt_btn3 = TextInput(hint_text="Результат пишіть сюди", size_hint = (1, 0.2), pos_hint = {"center_x": 0.2, "center_y": 0.5}, multiline = False)
      self.txt_btn4 = TextInput(hint_text="Результат пишіть сюди", size_hint = (1, 0.2), pos_hint = {"center_x": 0.2, "center_y": 0.5}, multiline = False)
      self.nxt_btn2 = Button(text="Next page", size_hint=(0.4, 0), pos_hint = {"center_x": 0.5, "center_y": 0.5})

      self.nxt_btn2.bind(on_press=self.gofourthscr)


      hl.add_widget(lbl_scr4)
      hl2.add_widget(result_scr4)
      hl2.add_widget(self.txt_btn3)
      vl.add_widget(result2_scr4)
      vl.add_widget(self.txt_btn4)
      vl2.add_widget(self.nxt_btn2)

      vl3.add_widget(hl)
      vl3.add_widget(hl2)
      vl3.add_widget(vl)
      vl3.add_widget(vl2)
      self.add_widget(vl3)

  def gofourthscr(self, istance):
      self.manager.current = "fourth"
      global btn3_text, btn4_text
      btn3_text = self.txt_btn3.text 
      btn4_text = self.txt_btn4.text


class FourthScr(Screen):
  def __init__(self, **kwargs):
      global txt_btn
      super(FourthScr, self).__init__(**kwargs)
      #vl = BoxLayout(orientation="horizontal")
      #hl = BoxLayout(orientation="vertical")

      Window.size = (950, 700)
#Створення направних ліній.
      widget_5 = BoxLayout (orientation = "vertical")
      vertical_5_1 = BoxLayout (orientation = "vertical", padding = 4, spacing = 4)
      horithontal_5_1 = BoxLayout (orientation = "horizontal", size_hint = (1, None), height = 50)
      horithontal_5_2 = BoxLayout (orientation = "horizontal", padding = 20, spacing = 8)
#Створення тексту індексаРуфє.
      global index_rufye
      index_rufye = Label (text = "")
#Створення кнопок.
      self.button_5_1 = Button (text = "<-", size_hint = (None, None), size = (100, 50))
      self.button_5_1.bind (on_press = self.go_to_scrin4)
      self.button_5_2 = Button (text = "Показати результат", size_hint = (0.2, 0))
      self.button_5_2.bind (on_release = self.show_result)
      #self.button_5_3 = Button (text = "Додати", size_hint = (0.2, 0))
      #self.button_5_3.bind (on_press = self.add_user_1)
#Додавання до ліній інтерфейсу.
      horithontal_5_1.add_widget (self.button_5_1)
      vertical_5_1.add_widget (index_rufye)
      horithontal_5_2.add_widget (self.button_5_2)
      #horithontal_5_2.add_widget (self.button_5_3)
#Додавання до віджету ліній.
      widget_5.add_widget (horithontal_5_1)
      widget_5.add_widget (vertical_5_1)
      widget_5.add_widget (horithontal_5_2)
#Додавання до селфу віджету.
      self.add_widget (widget_5)
#Деф передачі данних до самсРуфє (Самс).
  def show_result (self, instance):
      self.button_5_2.disabled = True
#Передача результатів до Деф в самсРуфє.
      index_rufye.text = sums_rufye (btn3_text, btn4_text, btn3_text3)
#Деф переходу до скрін4.
  def go_to_scrin4 (self, instance):
      self.manager.transition = SlideTransition (direction = "right")
      self.manager.current = ('third')
#Деф додавання користувачів1.
  def add_user_1 (self, instance):
#Додавання імя користувача до листа.
      user_name = list_1 [0]
#Отримання до скрінюзерс та додавання імя до скрінюзерс.
      self.manager.get_screen ("Збережені користувачі").add_user_2 (user_name) #Додавання імя до адюзерс2/скрінюзерс.

class MyApp(App):
  def build(self):
      sm = ScreenManager()
      sm.add_widget(MainScr(name='main'))
      sm.add_widget(FirstScr(name='first'))
      sm.add_widget(SecondScr(name='second'))
      sm.add_widget(ThirdScr(name='third'))
      sm.add_widget(FourthScr(name='fourth'))
      sm.current="main"
      return sm
  def __init__ (self, **kwargs):
    super (MyApp, self).__init__ (**kwargs)
# Встановлюємо ім'я вікна
    self.title = "Your Health"  
#Запуск програми.
if __name__ == "__main__":
  MyApp().run()


