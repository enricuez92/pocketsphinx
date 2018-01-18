from Tkinter import *
import Pmw
from Recognition_mic_copia import decode_sphinx
from pocketsphinx.pocketsphinx import *
from commands import command, notify
import pyaudio
import subprocess
import time


class Window(Frame):
    
    def __init__(self):
        
        fm = Frame(root)


        fm3 = Frame(fm)
        
        choice = None

        def choseEntry(entry):
            selezione= e4.get()
            print('You chose "%s"' % entry)
            print('You chose "%s"' % selezione)

        asply = ("parameter(1)","parameter(2)")

        combobox = Pmw.ComboBox(fm3, label_text='Parameter:', labelpos='w', listbox_width=24,
                                dropdown=1, selectioncommand=choseEntry, scrolledlist_items=asply)
        
        combobox.pack(side=LEFT,padx=5,pady=10)
        combobox.selectitem(asply[0])

        Label(fm3, text="Value:").pack(side=LEFT,padx=5)
        e4 = StringVar()
        Entry(fm3, textvariable=e4).pack(side=LEFT,padx=5)
        e4.set("...")

        fm3.pack()


        fm.pack(side=LEFT, fill=BOTH, expand=YES)

        fm2 = Frame(root)

        def sel():
            selection = var.get()
            text_selection = e.get()
            text_selection1 = e1.get()
            print(text_selection)
            print(text_selection1)

            threshold = selection
            kws_activation = '/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/activation.txt'
            kws_commands = '/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/commands.txt'

            activation_message = 'Started listening for activation...'
            commands_message = 'Started listening for commands...'
            reset_message = 'No commands heard. Back to Activation...'
            while True:

                audio_c = decode_sphinx(
                    kws_activation, activation_message, threshold, quitTimeS=10)

                if audio_c == "okscala" or audio_c == "ok scala":

                    audio_file = "/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/suoni-attivazione/Ding.wav"
                    notify('Chat-bot', 'Hey!')

                    return_code = subprocess.call(["afplay", audio_file])

                    audio = decode_sphinx(
                        kws_commands, commands_message, threshold, quitTimeS=10)

                    command(audio)
                    audio_file = "/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/suoni-attivazione/Ding2.wav"
                    return_code = subprocess.call(["afplay", audio_file])
                    break

        var = DoubleVar()
        scale = Scale(fm2, variable=var, tickinterval=50, from_=100, to=0)
        scale.pack(side=TOP, padx=5, pady=10)
        scale.set(50)

        button = Button(fm2, text="Start Recognition", command=sel)
        button.pack(side=TOP, padx=5, pady=10)
        label = Label(fm2)
        label.pack()

        Label(fm2, text="Dict:").pack(side=TOP, padx=5, pady=10)
        e = StringVar()
        Entry(fm2, width=35, textvariable=e).pack(side=TOP)
        e.set("Select dict...")

        Label(fm2, text="Keyword:").pack(side=TOP, padx=5, pady=10)
        e1 = StringVar()
        Entry(fm2, width=35, textvariable=e1).pack(side=TOP)
        e1.set("Select Keyword...")

        Label(fm2, text="Dict:").pack(side=TOP, padx=5, pady=10)
        e2 = StringVar()
        Entry(fm2, width=35, textvariable=e).pack(side=TOP)
        e2.set("Select dict...")

        Label(fm2, text="Keyword:").pack(side=TOP, padx=5, pady=10)
        e3 = StringVar()
        Entry(fm2, width=35, textvariable=e1).pack(side=TOP)
        e3.set("Select Keyword...") 

        
            
        fm2.pack(side=LEFT, padx=10)

        ####### menu #######

        # mBar = Frame(root, relief=RAISED, borderwidth=2)
        # mBar.pack(fill=X)
        # def makeCommandMenu():
        #     CmdBtn = Menubutton(mBar, text='Button Commands', underline=0)
        #     CmdBtn.pack(side=LEFT, padx="2m")
        #     CmdBtn.menu = Menu(CmdBtn)
        #     CmdBtn.menu.add_command(label="Undo")
        #     CmdBtn.menu.entryconfig(0, state=DISABLED)
        #     CmdBtn.menu.add_command(label='New...', underline=0)
        #     CmdBtn.menu.add_command(label='Open...', underline=0)
        #     CmdBtn.menu.add_command(label='Wild Font', underline=0,font=('Tempus Sans ITC', 14))
        #     CmdBtn.menu.add('separator')
        #     CmdBtn.menu.add_command(label='Quit', underline=0,background='white', activebackground='green')
        #     CmdBtn['menu'] = CmdBtn.menu
        #     return CmdBtn

        # def makeCascadeMenu():
        #     CasBtn = Menubutton(mBar, text='Cascading Menus', underline=0)
        #     CasBtn.pack(side=LEFT, padx="2m")
        #     CasBtn.menu = Menu(CasBtn)
        #     CasBtn.menu.choices = Menu(CasBtn.menu)
        #     CasBtn.menu.choices.wierdones = Menu(CasBtn.menu.choices)
        #     CasBtn.menu.choices.wierdones.add_command(label='Stockbroker')
        #     CasBtn.menu.choices.wierdones.add_command(label='Quantity Surveyor')
        #     CasBtn.menu.choices.wierdones.add_command(label='Church Warden')
        #     CasBtn.menu.choices.wierdones.add_command(label='BRM')
        #     CasBtn.menu.choices.add_command(label='Wooden Leg')
        #     CasBtn.menu.choices.add_command(label='Hire Purchase')
        #     CasBtn.menu.choices.add_command(label='Dead Crab')
        #     CasBtn.menu.choices.add_command(label='Tree Surgeon')
        #     CasBtn.menu.choices.add_command(label='Filing Cabinet')
        #     CasBtn.menu.choices.add_command(label='Goldfish')
        #     CasBtn.menu.choices.add_cascade(label='Is it a...', menu=CasBtn.menu.choices.wierdones)
        #     CasBtn.menu.add_cascade(label='Scipts', menu=CasBtn.menu.choices)
        #     CasBtn['menu'] = CasBtn.menu
        #     return CasBtn

        # CmdBtn = makeCascadeMenu()
        # CmdBtn = makeCommandMenu()

        ####### selection #######

        # selections = ["ciao","ciao"]

        # for index,selection in enumerate(selections):

        #     choice = None

        #     def choseEntry(entry):
        #         print('You chose "%s"' % entry)

        #     asply = (
        #         "The Mating of the Wersh",
        #         "Two Netlemeng of Verona",
        #         "Twelfth Thing",
        #         "The Chamrent of Venice",
        #         "Thamle",
        #         "Ring Kichard the Thrid")

        #     combobox = Pmw.ComboBox(root, label_text='Parameter:', labelpos='ws', listbox_width=24,
        #                             dropdown=1, selectioncommand=choseEntry, scrolledlist_items=asply)
        #     combobox.pack()
        #     combobox.selectitem(asply[0])

        #     Label(root, text="Value:").pack()
        #     e2 = StringVar()
        #     Entry(root, textvariable=e2).pack()
        #     e2.set("...")

        ####### baloon #######

        # balloon = Pmw.Balloon(root)
        # frame = Frame(root)
        # frame.pack(padx = 10, pady = 5)
        # field = Pmw.EntryField(frame, labelpos=W, label_text='Name:')
        # field.setentry('A.N. Other')
        # field.pack(side=LEFT, padx = 10)
        # balloon.bind(field, 'Your name', 'Enter your name')
        # check = Button(frame, text='Check')
        # check.pack(side=LEFT, padx=10)
        # balloon.bind(check, 'Look up', 'Check if name is in the database')
        # frame.pack()
        # messageBar = Pmw.MessageBar(root, entry_width=40,
        #                             entry_relief=GROOVE,
        #                             labelpos=W, label_text='Status:')
        # messageBar.pack(fill=X, expand=1, padx=10, pady=5)
        # balloon.configure(statuscommand = messageBar.helpmessage)

        ####### scale #######

        # def sel():
        #     selection = var.get()
        #     text_selection = e.get()
        #     text_selection1 = e1.get()
        #     print(text_selection)
        #     print(text_selection1)

        #     threshold = selection
        #     kws_activation = '/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/activation.txt'
        #     kws_commands = '/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/commands.txt'

        #     activation_message = 'Started listening for activation...'
        #     commands_message = 'Started listening for commands...'
        #     reset_message = 'No commands heard. Back to Activation...'
        #     while True:

        #         audio_c = decode_sphinx(
        #             kws_activation, activation_message, threshold, quitTimeS=10)

        #         if audio_c == "okscala" or audio_c == "ok scala":

        #             audio_file = "/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/suoni-attivazione/Ding.wav"
        #             notify('Chat-bot', 'Hey!')

        #             return_code = subprocess.call(["afplay", audio_file])

        #             audio = decode_sphinx(
        #                 kws_commands, commands_message, threshold, quitTimeS=10)

        #             command(audio)
        #             audio_file = "/Users/enricogiacalone/Desktop/Enry/chat-bot-pocketsphinx-python-master/suoni-attivazione/Ding2.wav"
        #             return_code = subprocess.call(["afplay", audio_file])
        #             break

        # var = DoubleVar()
        # scale = Scale(root, variable=var, tickinterval=50, from_=100, to=0)
        # scale.pack(side=TOP, padx=5, pady=10)

        # button = Button(root, text="Start Recognition", command=sel)
        # button.pack(side=TOP, padx=5, pady=10)
        # label = Label(root)
        # label.pack()

        ####### list #######

        # list = Listbox(root, height=6, width=15)
        # scroll = Scrollbar(root, command=list.yview)
        # list.configure(yscrollcommand=scroll.set)
        # list.pack(side=LEFT)
        # scroll.pack(side=RIGHT, fill=Y)
        # for item in range(30):
        #     list.insert(END, item)

        ####### textframe #######

        # Label(root, text="Dict:").pack(side=TOP, padx=5, pady=10)
        # e = StringVar()
        # Entry(root, width=35, textvariable=e).pack(side=TOP)
        # e.set("Select dict...")

        # Label(root, text="Keyword:").pack(side=TOP, padx=5, pady=10)
        # e1 = StringVar()
        # Entry(root, width=35, textvariable=e1).pack(side=TOP)
        # e1.set("Select Keyword...")

        # Label(root, text="Dict:").pack(side=TOP, padx=5, pady=10)
        # e2 = StringVar()
        # Entry(root, width=35, textvariable=e).pack(side=TOP)
        # e2.set("Select dict...")

        # Label(root, text="Keyword:").pack(side=TOP, padx=5, pady=10)
        # e3 = StringVar()
        # Entry(root, width=35, textvariable=e1).pack(side=TOP)
        # e3.set("Select Keyword...")

        ####### radiobuttons #######

        # var = IntVar()
        # for text, value in [('Passion fruit', 1), ('Loganberries', 2), ('Mangoes in syrup', 3), ('Oranges', 4),
        # ('Apples', 5),('Grapefruit', 6)]:
        #     Radiobutton(root, text=text, value=value, variable=var).pack(anchor=W)
        # var.set(3)

        ####### radiobuttons #######

        # def sel():
        #     selection = "You selected the option " + str(var.get())
        #     label.config(text = selection)

        # var = IntVar()
        # R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
        #           command=sel)
        # R1.pack( anchor = W )

        # R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
        #                 command=sel)
        # R2.pack( anchor = W )

        # R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
        #                 command=sel)
        # R3.pack( anchor = W)

        ####### checkbuttons #######

        # CheckVar1 = IntVar()
        # CheckVar2 = IntVar()
        # C1 = Checkbutton(root, text = "Music", variable = CheckVar1, \
        #                 onvalue = 1, offvalue = 0, height=5, \
        #                 width = 20)
        # C2 = Checkbutton(root, text = "Video", variable = CheckVar2, \
        #                 onvalue = 1, offvalue = 0, height=5, \
        #                 width = 20)
        # C1.pack()
        # C2.pack()

        ####### buttons #######

        # for bdw in range(5):

        #     of[bdw] = Frame(root, borderwidth=0)
        #     Label(of[bdw], text='borderwidth = %d ' % bdw).pack(side=LEFT)
        #     ifx = 0
        #     iff = []
        #     for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:

        #         iff.append(Frame(of[bdw], borderwidth=bdw, relief=relief))
        #         Label(iff[ifx], text=relief, width=10).pack(side=LEFT)
        #         iff[ifx].pack(side=LEFT, padx=7-bdw, pady=5+bdw)
        #         ifx = ifx+1
        #     of[bdw].pack()


root = Tk()
app = Window()
root.mainloop()
