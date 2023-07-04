# moviepy for video exchange, tkinter for GUI
import moviepy.editor as mpe
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# audio filename storage
audio_filename = ''
foregroundColor = "#788475"
textBackgroundColor = "#453643"
applicationBackgroundColor = "#8DAA91"


def v2aconvert():
    global audio_filename

    filetypes = (("Audio files", "*.mp3 , *.waw , *.ogg"), ("All files", "*.*"))

    # get video
    video = mpe.VideoFileClip(audio_filename)
    # extract audio
    audio = video.audio
    # export result
    file = asksaveasfilename(filetypes=filetypes)
    audio.write_audiofile(f'{file}{format.get()}')

    # finish indicator
    label5 = Label(root, text="Process Finished", font=("Jetbrains Mono", 16), fg=foregroundColor)
    label5.config(bg=textBackgroundColor)
    label5.pack()
    label5.place(x=370, y=288)


def select():
    global audio_filename

    filetypes = (
        ('video files',
         '*.WEBM , *.MPG, *.MP2 , *.MPEG , *.MPE , *.MPV , *.MP4 , *.M4P ,'
         ' *.M4V , *.AVI , *.WMV , *.MOV , *.QT , *.FLV , *.SWF , *.AVCHD'),
        ('All files', '*.*')
    )

    audio_filename = askopenfilename(filetypes=filetypes)

    # selected indicator
    label3.config(text="Video Selected", fg="red")
    label3.config(bg=applicationBackgroundColor)

    # label for audio format
    label4 = Label(root, text="Select Audio format", font=("Jetbrains Mono", 16))
    label4.config(bg=applicationBackgroundColor)
    label4.pack()
    label4.place(x=125, y=240)

    # options for audio format
    options = [".mp3", ".wav"]
    format.set(".mp3")
    menu = OptionMenu(root, format, *options)
    menu.pack()
    menu.place(x=400, y=240)

    # convert button
    button3 = Button(root, text="Export", bg='light blue', font=("Jetbrains Mono", 10),
                     command=v2aconvert, width=12, height=1)
    button3.pack()
    button3.place(x=250, y=290)


# basic tkinter GUI
root = Tk()

# background color of the application
root.configure(bg=applicationBackgroundColor)

# application GUI size
root.geometry("700x450")
root.minsize(600, 350)
root.maxsize(600, 350)

# application title
root.title("V2A Converter")

# heading
label1 = Label(root, text="Extract It! Video2Audio", font=("Jetbrains Mono", 26))
label1.config(bg=applicationBackgroundColor)
label1.pack()
label1.place(x=56, y=30)

# label for video file selection
label2 = Label(root, text="Select Video To Convert", font=("Jetbrains Mono", 16))
label2.config(bg=applicationBackgroundColor)
label2.pack()
label2.place(x=150, y=90)

# button for video file selection
button1 = Button(root, text="Choose File", bg='light blue', font=("Jetbrains Mono", 10),
                 command=select, width=12, height=1)
button1.pack()
button1.place(x=250, y=190)

label3 = Label(root, font=("Jetbrains Mono", 18, "bold"))
label3.pack()
label3.place(x=200, y=135)
format = StringVar()

# application startup
root.mainloop()
