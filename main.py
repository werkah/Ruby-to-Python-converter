from antlr4 import *
from grammar.RubyLexer import RubyLexer
from grammar.RubyParser import RubyParser
from grammar.RubyVisitor import RubyVisitor
import PySimpleGUI as sg


def main():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text("Wybierz przykładowy plik do konwersji:")],
        [sg.Input(key="-FILE-"), sg.FileBrowse()],
        [sg.Button("Konwertuj"), sg.Button("Wyjście")],
        [sg.Output(size=(60, 20), key="-OUTPUT-")]
    ]
    window = sg.Window("Ruby to Python Converter", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Wyjście":
            break
        if event == "Konwertuj":
            file_path = values["-FILE-"]
            if file_path:
                try:
                    inp = FileStream(file_path)
                    lexer = RubyLexer(inp)
                    stream = CommonTokenStream(lexer)
                    parser = RubyParser(stream)
                    tree = parser.program()
                    visitor = RubyVisitor()
                    res = visitor.visit(tree)
                    output = open("output.py", "w")
                    output.write(res)
                    output.close()
                    window["-OUTPUT-"].update(res)
                except Exception as e:
                    print(f"Error: {str(e)}")
            else:
                print("Wybierz plik do konwersji!")
    window.close()


if __name__ == '__main__':
    main()