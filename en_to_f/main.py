# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.image import Image
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from translate2 import translation
# from kivy.lang import Builder
#

# class En_to_f(App):
#     def build(self):
#         #returns a window object with all it's widgets
#
#         self.window = GridLayout()
#         self.window.cols = 1
#         self.window.size_hint = (0.6, 0.7)
#         self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
#
#         # image widget
#         self.window.add_widget(Image(source="logo.jpg"))
#
#         # label widget
#         self.greeting = Label(
#                         text= "Please enter the English language to be translated :",
#                         font_size= 18,
#                         color= '#00FFCE'
#                         )
#         self.window.add_widget(self.greeting)
#
#         # self.lq = Label(text='input', font_size='40sp',color= '#00FFCE')
#         # self.window.add_widget(self.lq)
#         # text input widget
#         self.use1 = TextInput(
#                     multiline= True,
#                     padding_y= (20,20),
#                     size_hint= (1, 0.5)
#                     )
#
#         self.window.add_widget(self.use1)
#         # self.out = Label(text='result', font_size='40sp', color='#00FFCE')
#         # self.window.add_widget(self.out)
#         self.use2 = TextInput(
#             multiline=True,
#             padding_y=(20, 20),
#             size_hint=(1, 0.5)
#         )
#
#         self.window.add_widget(self.use2)
#
#         # button widget
#         self.button = Button(
#                       text= "START",
#                       size_hint= (1,0.5),
#                       bold= True,
#                       background_color ='#00FFCE',
#                       #remove darker overlay of background colour
#                       # background_normal = ""
#                       )
#         self.button.bind(on_press=self.callback)
#         self.window.add_widget(self.button)
#         self.mod = "config1"
#
#         return self.window
#
#     def callback(self, instance):
#         self.use2.text  = "Answer: \n" + translation(src_text=self.use1.text, mod=self.mod)
#         #print(self.user.text)
#
#
#
# if __name__ == "__main__":
#     En_to_f().run()
# #
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from translate2 import translation

Builder.load_string("""
#:import Clipboard kivy.core.clipboard.Clipboard
#:import Factory kivy.factory.Factory
<MyPopup@Popup>:
    auto_dismiss:False
    title:'确定退出应用吗？'

    size_hint:.4,.4

    BoxLayout:
        anchor_x:'center'
        anchor_y:'bottom'
        Button:
            text:'否'
            size_hint:None,None
            size:147,60
            on_release:root.dismiss()
        Button:
            text:'是'
            size_hint:None,None
            size:147,60
            on_release:app.stop()
<MyPopup2@Popup>:
    auto_dismiss:False
    title:'请输入有效文本！'

    size_hint:.4,.4

    BoxLayout:
        anchor_x:'center'
        anchor_y:'bottom'
        Button:
            text:'好的'
            size_hint:None,None
            size:147,60

            on_release:root.dismiss()

<MyButton@Button>:
    background_color:"red"
    color:"orange"
    font_size:25
    bold:True

<MyGrid>:
    inp:input
    outp:output
    canvas:
        Color:
            rgba:[0.1,0.5,0.5,0.5]
        Rectangle:
            pos:self.pos
            size:self.size
    cols: 1
    BoxLayout:
        size_hint:0.5,0.2
        MyButton:
            text: '复制'
            bold:True
            # size_hint:.2,.15
            # pos:65,400
            on_release:
                Clipboard.copy(output.text)
        MyButton:
            text: '粘贴'
            # size_hint:.2,.15
            # pos:265,400
            on_release:
                input.text = Clipboard.paste()
        MyButton:
            text: '清除'
            # size_hint:.2,.15
            # pos:515,400
            on_release:
                input.text = ''
                output.text = ''

        MyButton:
            text: '退出'
            # size_hint:.2,.15
            # pos:515,400
            on_release: Factory.MyPopup().open()


    BoxLayout:
        size_hint:0.5,0.2
        MyButton:
            text: '英译法'
            bold:True
            # size_hint:.2,.15
            # pos:65,400
            on_release:
                root.mod="config1"
        MyButton:
            text: '法译英'
            # size_hint:.2,.15
            # pos:265,400
            on_release:
                root.mod="config2"
        MyButton:
            text: '翻译'
            # size_hint:.2,.15
            # pos:515,400
            on_release:
                Factory.MyPopup2().open() if input.text =='' else root.callback()





    GridLayout:
        cols:2
        Label:
            size_hint_x:0.25


            text: "输入: "
            font_size: 18
            bold:True
            color:"green"


        TextInput:
            # pos_hint: {"x":0.5, "top":0.8}
            size_hint_x:0.75
            id: input
            multiline: True
            font_size: 18
            foreground_color:[0.9,0.1,0,1]
            background_color:[1,1,1,1]

        Label:
            size_hint_x:0.25

            text: "输出: "
            font_size: 20
            bold:True
            color:"green"


        TextInput:
            # pos_hint: {"x":0.5, "top":0.8}
            size_hint_x:0.75
            id: output
            multiline: True
            font_size: 20
    # TextInput:
    #     id: txtinput
    #     font_size:50
    #     background_color:rgba(22,156,156,140)
    #     foreground_color:"orange"
    #     cursor_color:"green"
    #     multiline:True


""")


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.mod = "config1"


    def callback(self):

        self.outp.text = translation(src_text=self.inp.text, mod=self.mod)




class En_to_FApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    En_to_FApp().run()