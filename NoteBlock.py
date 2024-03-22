import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk


class SetNote:
    # Window Form Init
    __root = Tk()

    # Initial Specs
    __thisWidth = 600
    __thisHeight = 400
    __thisTextArea = Text(__root, pady=10, padx=10,
                          wrap='word', font=('Consolas 12'))
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisViewMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):

        # Icon Set
        try:
            self.__root.wm_iconbitmap('NoteBlockIcon.ico')
        except:
            pass

        # Window Form Init - Title('Untitled - NoteBlock')
        try:
            self.__root.title('Untitled - NoteBlock')
        except KeyError:
            pass

        # Window Form Init - Size(300x300)
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # Text Area Padding
        paddingLeft = (screenWidth / 2) - (self.__thisWidth / 2)
        paddingTop = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry(
            '%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, paddingLeft, paddingTop))

        # Text Area Def
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__thisTextArea.grid(sticky=N + E + S + W)

# ------------------------------------------------------------------------------------------------------------------------------------------

        # Menu Bar Initializing
        self.__root.config(menu=self.__thisMenuBar)
        # Scroll Bar Setting
        self.__thisScrollBar.pack(side=RIGHT, fill=Y,)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(
            yscrollcommand=self.__thisScrollBar.set, wrap='word')

        # File Menu Commands
        # Create New File
        self.__thisFileMenu.add_command(
            label='New', command=self.__newFile)
        # Open File
        self.__thisFileMenu.add_command(
            label='Open', command=self.__openFile)
        # Save File
        self.__thisFileMenu.add_command(
            label='Save', command=self.__saveFile)
        # Separator
        self.__thisFileMenu.add_separator()
        # Exit
        self.__thisFileMenu.add_command(
            label='Exit', command=self.__quitApplication)
        # Adding Menu Bar - File Commands
        self.__thisMenuBar.add_cascade(
            label='File', menu=self.__thisFileMenu)

        # Edit Menu Commands
        # Copy Command
        self.__thisEditMenu.add_command(
            label='Copy', command=self.__copy)
        # Cut Command
        self.__thisEditMenu.add_command(
            label='Cut', command=self.__cut)
        # Paste Command
        self.__thisEditMenu.add_command(
            label='Paste', command=self.__paste)
        # Adding Menu Bar - Edit Commands
        self.__thisMenuBar.add_cascade(
            label='Edit', menu=self.__thisEditMenu)

        # Help Menu Commands
        # About Command
        self.__thisHelpMenu.add_command(
            label='About', command=self.__showAbout)
        # Adding Menu Bar - Help Commands
        self.__thisMenuBar.add_cascade(
            label='Help', menu=self.__thisHelpMenu)

    # File Functions
    # New File Function

    def __newFile(self):
        self.__root.title('Untitled - NoteBlock')
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    # Open File Function
    def __openFile(self):
        self.__file = askopenfilename(
            defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])

        if self.__file == '':
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + ' - NoteBlock')
            self.__thisTextArea.delete(1.0, END)
            file = open(self.__file, 'r')
            self.__thisTextArea.insert(1.0, file.read())
            file.close()

    # Save File Function
    def __saveFile(self):
        if self.__file == None:
            self.__file = asksaveasfilename(
                initialfile='Untitled', defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
            if self.__file == '':
                self.__file = None
            else:
                file = open(self.__file, 'w')
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + ' NoteBlock')
        else:
            file = open(self.__file, 'w')
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    # Quit Application Function
    def __quitApplication(self):
        self.__root.destroy()

    # Edit Functions
    # Copy Function
    def __copy(self):
        self.__thisTextArea.event_generate('<<Copy>>')

    # Cut Function
    def __cut(self):
        self.__thisTextArea.event_generate('<<Cut>>')

    # Paste Function
    def __paste(self):
        self.__thisTextArea.event_generate('<<Paste>>')

    # Help Functions
    # About Function
    def __showAbout(self):
        showinfo(
            'NoteBlock - About', 'Versão: 0.0.1\nLicença: Grátis\nDev: https://github.com/FuchsbauP')

    def run(self):
        self.__root.mainloop()


note = SetNote()
note.run()
