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
                          wrap='word', font=('Consolas 12'), undo=True)
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
            label='New', command=self.__newFile, accelerator='Ctrl + N')
        # Open File
        self.__thisFileMenu.add_command(
            label='Open', command=self.__openFile, accelerator='Ctrl + O')
        # Save File
        self.__thisFileMenu.add_command(
            label='Save', command=self.__saveFile, accelerator='Ctrl + S')
        # Separator
        self.__thisFileMenu.add_separator()
        # Exit
        self.__thisFileMenu.add_command(
            label='Exit', command=self.__quitApplication, accelerator='Ctrl + Q')
        # Adding Menu Bar - File Commands
        self.__thisMenuBar.add_cascade(
            label='File', menu=self.__thisFileMenu)

        # Edit Menu Commands
        # Undo Command
        self.__thisEditMenu.add_command(
            label='Undo', command=self.__undo, accelerator='Ctrl + Z')
        # Separator
        self.__thisEditMenu.add_separator()
        # Copy Command
        self.__thisEditMenu.add_command(
            label='Copy', command=self.__copy, accelerator='Ctrl + C')
        # Cut Command
        self.__thisEditMenu.add_command(
            label='Cut', command=self.__cut, accelerator='Ctrl + X')
        # Paste Command
        self.__thisEditMenu.add_command(
            label='Paste', command=self.__paste, accelerator='Ctrl + V')
        # Delete Command
        self.__thisEditMenu.add_command(
            label='Delete', command=self.__delete, accelerator='Del')
        # Separator
        self.__thisEditMenu.add_separator()
        # Search Command
        self.__thisEditMenu.add_command(
            label='Search', command=self.__search, accelerator='Ctrl + F')
        # Adding Menu Bar - Edit Commands
        self.__thisMenuBar.add_cascade(
            label='Edit', menu=self.__thisEditMenu)

        # View Menu Commands
        # Dark Mode Command
        self.__thisViewMenu.add_checkbutton(
            label='Dark Mode', command=self.__darkMode)
        # Light Mode Command
        self.__thisViewMenu.add_checkbutton(
            label='Light Mode', command=self.__lightMode)
        # Adding Menu Bar - View Commands
        self.__thisMenuBar.add_cascade(
            label='View', menu=self.__thisViewMenu)

        # Help Menu Commands
        # About Command
        self.__thisHelpMenu.add_command(
            label='About', command=self.__showAbout)
        # Adding Menu Bar - Help Commands
        self.__thisMenuBar.add_cascade(
            label='Help', menu=self.__thisHelpMenu)

    # File Functions
    # New File Function
    def __newFile(self, event=None):
        self.__root.title('Untitled - NoteBlock')
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    # Open File Function
    def __openFile(self, event=None):
        self.__file = askopenfilename(
            defaultextension='.txt', filetypes=[('Text Documents', '*.txt'), ('All Files', '*.*')])

        if self.__file == '':
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + ' - NoteBlock')
            self.__thisTextArea.delete(1.0, END)
            file = open(self.__file, 'r')
            self.__thisTextArea.insert(1.0, file.read())
            file.close()

    # Save File Function
    def __saveFile(self, event=None):
        if self.__file == None:
            self.__file = asksaveasfilename(
                initialfile='Untitled', defaultextension='.txt', filetypes=[('Text Documents', '*.txt'), ('All Files', '*.*')])
            if self.__file == '':
                self.__file = None
            else:
                file = open(self.__file, 'w')
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                self.__root.title(os.path.basename(
                    self.__file) + ' NoteBlock')
        else:
            file = open(self.__file, 'w')
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    # Quit Application Function
    def __quitApplication(self, event=None):
        self.__root.destroy()

    # Edit Functions
    # Undo Function
    def __undo(self):
        if self.__thisTextArea.edit_undo():
            return True

    # Copy Function
    def __copy(self):
        self.__thisTextArea.event_generate('<<Copy>>')

    # Cut Function
    def __cut(self):
        self.__thisTextArea.event_generate('<<Cut>>')

    # Paste Function
    def __paste(self):
        self.__thisTextArea.event_generate('<<Paste>>')

    # Delete Function
    def __delete(self):
        self.__thisTextArea.delete(1.0, END)

    # Search Function
    def __search(self):
        ...

    # View Functions
    # Dark Mode Function
    def __darkMode(self):
        ...

    # Light Mode Function
    def __lightMode(self):
        ...

    # Help Functions
    # About Function
    def __showAbout(self):
        showinfo(
            'NoteBlock - About', 'Versão: 0.0.2\nLicença: Grátis\nDev: https://github.com/FuchsbauP')

    def run(self):
        self.__root.bind_all('<Control-N>', self.__newFile)
        self.__root.bind_all('<Control-n>', self.__newFile)
        self.__root.bind_all('<Control-O>', self.__openFile)
        self.__root.bind_all('<Control-o>', self.__openFile)
        self.__root.bind_all('<Control-S>', self.__saveFile)
        self.__root.bind_all('<Control-s>', self.__saveFile)
        self.__root.mainloop()


note = SetNote()
note.run()
