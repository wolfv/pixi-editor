import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QMenuBar, QMenu, QFileDialog, QAction

class TextEditor(QMainWindow):
    def __init__(self, filename=None):
        super().__init__()
        self.initUI()
        if filename:
            self.openFile(filename)

    def initUI(self):
        self.setWindowTitle('Simple Text Editor')
        self.setGeometry(100, 100, 800, 600)

        # Create text edit widget
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Create menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # File menu actions
        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.openFileDialog)

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.saveFile)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

    def openFileDialog(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if filename:
            self.openFile(filename)

    def openFile(self, filename):
        try:
            with open(filename, 'r') as f:
                text = f.read()
                text += "\n" + "..".join(sys.argv)
                self.text_edit.setText(text)


            self.setWindowTitle(f'Simple Text Editor - {filename}')

        except Exception as e:
            print(f"Error opening file: {e}")

    def saveFile(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File')
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(self.text_edit.toPlainText())
            except Exception as e:
                print(f"Error saving file: {e}")

def main():
    app = QApplication(sys.argv)
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    editor = TextEditor(filename)
    editor.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
