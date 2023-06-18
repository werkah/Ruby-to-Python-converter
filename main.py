from antlr4 import *
from grammar.RubyLexer import RubyLexer
from grammar.RubyParser import RubyParser
from grammar.RubyVisitor import RubyVisitor
import PySimpleGUI as sg


def main():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Text("Select a file to convert:", font='Helvetica 14')],
        [sg.Input(key="-FILE-"), sg.FileBrowse(font='Helvetica 14')],
        [sg.Button("Convert", key="-CONVERT-", font='Helvetica 14'), sg.Button("Quit", key="-QUIT-",font='Helvetica 14')],
        [sg.Output(size=(60, 20), key="-OUTPUT-")]
    ]
    window = sg.Window("Ruby to Python Converter", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "-QUIT-":
            break
        if event == "-CONVERT-":
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
                print("Select file to convert!")
    window.close()


if __name__ == '__main__':
    main()