import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView, FileChooserIconView
import PyPDF2

# Construct Label Class For Resizing
class MyLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = '50sp'
        self.size_hint = (1, None)
        self.height = self.texture_size[1]

# Construct File Chooser Class For Resizing
class MyFileChooser(FileChooserIconView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1.0, 0.6)
        self.path = '.'
        
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.path = '.'

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10

        file_chooser = MyFileChooser()
        self.add_widget(file_chooser)

        button = Button(text='Upload PDF File', size_hint_y=None, height=50, pos=(0, Window.height-100))
        button.bind(on_press=lambda x: self.upload_file(file_chooser.path))
        self.add_widget(button)
       

    def upload_file(self, path):
        print(f'Uploading file: {path}')
        # Use PyPDF to convert pdf to text
        pdfReader = PyPDF2.PdfReader(path)

        # printing number of pages in pdf file
        print(len(pdfReader.pages))

        # Create a string variable to store the text content
        text_content = ""

        # creating a page object
        for i in range(len(pdfReader.pages)):
            pageObj = pdfReader.pages[i]
            # extracting text from page
            text_content += pageObj.extract_text()

        print(text_content)
        

class MyApp(App):

    def build(self):
        Window.size = (400, 400)
        title = MyLabel(text= "PDF to Text App",pos=(0, Window.height-50))
        layout = MyBoxLayout()
        root = BoxLayout(orientation='vertical')
        root.add_widget(title)
        root.add_widget(layout)
        return root
       

    

    

if __name__ == '__main__':
    MyApp().run()