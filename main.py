import tkinter as tk
import sv_ttk

class windows(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.master = master
		self.tk.init_window()

if __name__ == "__main__":
	root = tk.Tk()
	sv_ttk.set_theme("dark")
	root.state("zoomed")
	root.mainloop()
