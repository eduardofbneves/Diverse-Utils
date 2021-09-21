# install eyed3 with tue command $ pip install eyed3
# must have python 3.6 or above

import tkinter as tk
import eyed3


class MFileGUI(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        fr = tk.Frame(self, height=200, width=400)
        fr.grid()

    def input_spaces(self, fr):
        info = tk.Label(self, text='Title: \nArtist: \nAlbum: \n Track Number:')
        info.pack(side=tk.LEFT)
        entry_fr = tk.Frame().pack(side=tk.LEFT)
        e_title = tk.Entry(entry_fr, width=40).pack()
        e_artist = tk.Entry(entry_fr, width=40).pack()
        e_album = tk.Entry(entry_fr, width=40).pack()
        e_track_num = tk.Entry(entry_fr, width=40).pack()
        return [e_title, e_artist, e_album, e_track_num]

    def save_button(self, audio, entry_list):
        audio.tag.title = entry_list[0].get()
        audio.tag.artist = entry_list[1].get()
        audio.tag.album = entry_list[2].get()
        audio.tag.track_num = int(entry_list[3].get())
        audio.tag.save()
        return None

if __name__ == '__main__':
    mu = MFileGUI()
    mu.mainloop()
