#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
tkinterを使った8-QueenのGUI
'''

from PIL import Image, ImageTk
import tkinter  as tk
import NQueen as q
from tkinter import * 

Q_front = ('Times', 14)

def qdiff(a1, a0):
    ls = []
    for i in range(8):
        if not a0[i] == a1[i]:
            ls.append((i, a0[i], False))
            ls.append((i, a1[i], True))
    return ls

class Queen(tk.Frame):
    def init_title(self):
        self.master.title('8 Queens')
        self.f_title = tk.Frame(self)
        #self.i_title = tk.PhotoImage(file = '8qsubtitle.ppm')
        self.l_title = tk.Label(self.f_title)
        self.l_title.pack()
        self.f_title.pack(side=tk.TOP, padx=10, pady=10)

    def init_board(self):
        self.f_board = tk.Frame(self, relief=tk.GROOVE, bd=3)
        self.f_board.pack(side=tk.TOP, padx=10, pady=10)
        #self.cell_images = [tk.PhotoImage(file=ppm) for ppm in ('bw.ppm', 'bg.ppm', 'qw.ppm', 'qg.ppm')]
        #answer = self.q_answers[0]
        for i in range(8):
            for j in range(8):
                tk.Label(self.f_board).grid(row=1, column=j)

    def init_footer(self):
        self.f_footer = tk.Frame(self)
        self.f_footer.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.s_counter = tk.StringVar()
        self.s_counter.set('%d/12' % (1+self.q_counter))
        self.f_label = tk.Label(self.f_footer, textvariable = self.s_counter, font=Q_font, width=8)
        self.f_label.pack(side=tk.RIGHT, padx=10)
        self.b_button = tk.Button(self.f_footer, text='back', font=Q_font, command = self.show_prev)
        self.b_button.pack(side=tk.RIGHT, padx=1, pady=1)
        self.a_button = tk.Button(self.f_footer, text='next', font=Q_font, command = self.show_next)
        self.a_button.pack(side=tk.RIGHT, padx=1, pady=1)

    def __init__(self, set_answer):
        self.q_counter = 0
        self.q_answer = list(set_answer)
        tk.Frame.__init__(self, None)
        self.pack()
        self.init_title()
        self.init_board()
        self.init_footer()

    def refresh(self, forward):
        i_now = self.q_counter
        self.q_counter += 1 if forward else -1
        self.s_counter.set('%d/12' % (1+self.q_counter))
        for i, j, is_add in qdiff(self.q_answers[self.q_counter], self.q_answers[i_now]):
            tk.Label(self.f_board, image=self.cell_images[qmod(i,j)+(2 if is_add else 0)]).grid(row=i, column=j)

    def show_next(self):
        if(self.q_counter < 11):
            self.refresh(True)

    def show_prev(self):
        if(self.q_counter > 0):
            self.refresh(False)

if __name__ == "__main__":
    que = Queen(q.nqueen(8))
    que.pack()
    que.mainloop()

'''
http://www.shido.info/py/queen_py3.html
'''

'''
8qsubtitle.ppm
適当に画像を用意すれば良い

上のコードはまだ未完成
'''




