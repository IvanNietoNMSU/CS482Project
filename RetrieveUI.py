import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import DatabaseMethods as dB


choices = ['Games', 'Players', 'Play', 'Teams']


def retrieval():
    retrieval_window = tk.Toplevel()
    retrieval_window.title('Load Given Table')
    retrieval_window.resizable(False, False)
    retrieval_window.configure(bg='#2d3436')

    frameLeft = tk.LabelFrame(retrieval_window, text='Select the name of the table you wish to retrieve', bg='#2d3436',
                              fg='#ff7675')
    frameLeft.pack(side=tk.LEFT)

    comboBox = ttk.Combobox(frameLeft, values=choices, state='readonly')
    comboBox.pack(side=tk.TOP, fill=tk.X, padx=50, pady=20)
    comboBox.current(0)

    frameRight = tk.LabelFrame(retrieval_window)
    frameRight.pack(side=tk.RIGHT)

    result = scrolledtext.ScrolledText(frameRight, height=10, width=100, wrap=tk.NONE, state=tk.DISABLED)
    result.pack(fill=tk.BOTH)

    def PrintResults():
        result.config(state=tk.NORMAL)
        result.delete(1.0, tk.END)
        st = dB.retrieve(comboBox.get().lower())
        result.insert(tk.END, st)
        result.config(state=tk.DISABLED)

    submitButton = tk.Button(frameLeft, text='Submit', command=PrintResults)
    submitButton.pack(side=tk.BOTTOM, fill=tk.X)

    retrieval_window.mainloop()

