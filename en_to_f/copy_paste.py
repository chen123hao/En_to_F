from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
#:import Clipboard kivy.core.clipboard.Clipboard
#:import Factory kivy.factory.Factory
<MyPopup@Popup>:  
    auto_dismiss:False   
    title:'Are you sure to exit?'   
    # on_dismiss:print('on_dismiss is running')   
    # on_open:print('on_open is running')  
    size_hint:.4,.4
 
    BoxLayout:  
        anchor_x:'center'   
        anchor_y:'bottom'  
        Button:    
            text:'No'  
            size_hint:None,None   
            size:147,60   
            on_release:root.dismiss()  
        Button:    
            text:'Yes'  
            size_hint:None,None   
            size:147,60   
            on_release:app.stop()

<MyButton@Button>: 
    background_color:"red"
    color:"orange"
    font_size:25
    bold:True
<MyGrid>:
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
            text: 'Copy'
            bold:True
            # size_hint:.2,.15
            # pos:65,400 
            on_release:
                Clipboard.copy(output.text)
        MyButton:
            text: 'Paste'
            # size_hint:.2,.15
            # pos:265,400 
            on_release:
                input.text = Clipboard.paste()
        MyButton:
            text: 'Clear'
            # size_hint:.2,.15
            # pos:515,400 
            on_release:
                input.text = ''
                output.text = ''
        
        MyButton:
            text: 'Exit'
            # size_hint:.2,.15
            # pos:515,400 
            on_release: Factory.MyPopup().open()
                        

    BoxLayout:
        size_hint:0.5,0.2
        MyButton:
            text: 'En_to_F'
            bold:True
            # size_hint:.2,.15
            # pos:65,400 
            on_release:
                Clipboard.copy(output.text)
        MyButton:
            text: 'F_to_En'
            # size_hint:.2,.15
            # pos:265,400 
            on_release:
                input.text = Clipboard.paste()
        MyButton:
            text: 'Start'
            # size_hint:.2,.15
            # pos:515,400 
            on_release:
                input.text = ''
                output.text = ''
        MyButton:
            text: 'Set_up'
            # size_hint:.2,.15
            # pos:515,400 
            on_release:
                input.text = ''
                output.text = ''
          
    
    GridLayout:
        cols:2
        Label:
            size_hint_x:0.25
            
            
            text: "INPUT: "
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
            
            text: "OUTPUT: "
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
    def show_popup():
        show = Popups()

        popupWindow = Popup(title="Are you sure to exit?", content=show,
                            size_hint=(None, None), size=(200, 200))

        popupWindow.open()



class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()