import tkinter as tk
from pypbe.core import PBE
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Initialize widgets
        optionList = ('pf', '3e', '5e')
        self.v = tk.StringVar()
        self.v.set(optionList[0])      
        self.system = tk.OptionMenu(self, self.v, *optionList)
        self.dice_num = tk.Scale(label='# of Dice', from_=1, to=18, orient=tk.HORIZONTAL)
        self.dice_keep = tk.Scale(label='# Dice to Keep', from_=1, to=18, orient=tk.HORIZONTAL)
        self.dice_type = tk.Scale(label='Dice Type', from_=1, to=18, orient=tk.HORIZONTAL)
        self.dice_add = tk.Scale(label='Add', from_=0, to=18, orient=tk.HORIZONTAL)
        self.att_num = tk.Scale(label='# of Attrs', from_=1, to=18, orient=tk.HORIZONTAL)
        self.att_keep = tk.Scale(label='# Attr to Keep', from_=1, to=18, orient=tk.HORIZONTAL)
        self.arr_num = tk.Scale(label='# of Arrays', from_=1, to=18, orient=tk.HORIZONTAL)
        self.rerolls = tk.Scale(label='Rerolls', from_=0, to=18, orient=tk.HORIZONTAL)
        self.sim = tk.Button(text="Simulate", command=self.my_callback)      
        # Set defaults
        self.dice_num.set(3)
        self.dice_keep.set(3)
        self.dice_type.set(6)
        self.dice_add.set(0)
        self.att_num.set(6)
        self.att_keep.set(6)
        self.arr_num.set(1)
        self.rerolls.set(0)
        # Pack widgets
        for widget in [self.system, self.dice_num, self.dice_keep, self.dice_add,
                       self.att_num, self.att_keep, self.arr_num, self.rerolls,
                       self.sim]:
            widget.pack()
        # Matplotlib canvas
        self.f = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvasTkAgg(self.f, master=root)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.RIGHT, expand=1)

    def my_callback(self):
        alg = PBE(self.dice_num.get(), self.dice_type.get(), self.dice_add.get(), 
                  self.att_num.get(), self.arr_num.get(), self.rerolls.get(), 
                  self.dice_keep.get(), self.att_keep.get(), self.v.get())
        self.f = alg.roll_mc(int(1e5)).plot_histogram()

root = tk.Tk()
root.wm_title("PBE Simulator")
app = Application(master=root)
app.mainloop()


#    system = toga.Selection(items=['pf','3e','5e'])
#    dice_num = tk.Scale(from__value=1, to=18)
#    
        