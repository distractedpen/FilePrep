import tkinter as tk
import create_doc as doc
from datetime import datetime, date, timedelta

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):

        width = 50

        def makeDoc():
            #doc.create_document(start date, activityList, homeworkList)
            activitylist = [a1.get(), a2.get(), a3.get(), a4.get(), a5.get()]
            homeworklist = [h1.get(), h2.get(), h3.get(), h4.get(), h5.get()]
            section = str(v.get())
            start_date = datetime(year=int(year.get()), month=int(month.get()), day=int(day.get()))
            file_name =doc.create_document(start_date, section, activitylist, homeworklist)
            
            top = tk.Toplevel(self)
            top.title("Result...")
            msg = tk.Message(top, text="File saved as " + file_name)
            msg.pack()
            button = tk.Button(top, text="Close Program", command=self.master.destroy)
            button.pack()


        #Start Top Frame
        f_top = tk.Frame(self)
        f_top.pack(side=tk.TOP)

        #Start Date Spin Boxes
        tk.Label(f_top, text="Start Date: ").pack(side=tk.LEFT)
        month = tk.Spinbox(f_top, from_=1, to=12)
        month.pack(side=tk.LEFT)
        tk.Label(f_top, text="/").pack(side=tk.LEFT)
        day = tk.Spinbox(f_top, from_=1, to=31)
        day.pack(side=tk.LEFT)
        tk.Label(f_top, text="/").pack(side=tk.LEFT)
        year = tk.Spinbox(f_top, from_=2020, to= 2050)
        year.pack(side=tk.LEFT)
        tk.Label(f_top, text="/").pack(side=tk.LEFT)

        #Button: Create Document
        b = tk.Button(f_top, text="Create Document", command=makeDoc)
        b.pack()

        ##Make a Radio Button to Choose Algebra 1 or Algebra 2 Section
        v = tk.StringVar()
        v.set("Algebra 1")
        sections = [
            ("Algebra 1", "Algebra 1"),
            ("Algebra 2", "Algebra 2")
            ]
        for val, section in sections:
            tk.Radiobutton(f_top, text=section, padx=5, variable=v, value=val).pack(anchor=tk.W)
        #End Top Frame
        
        #Start Left Frame
        f_left = tk.Frame(self)
        f_left.pack(side=tk.LEFT)

        #Activity Entry List
        tk.Label(f_left, text="Monday").pack(side=tk.TOP)
        a1 = tk.Entry(f_left, width=width)
        a1.pack(side=tk.TOP)
        tk.Label(f_left, text="Tuesday").pack(side=tk.TOP)
        a2 = tk.Entry(f_left, width=width)
        a2.pack(side=tk.TOP)
        tk.Label(f_left, text="Wednesday").pack(side=tk.TOP)
        a3 = tk.Entry(f_left, width=width)
        a3.pack(side=tk.TOP)
        tk.Label(f_left, text="Thursday").pack(side=tk.TOP)
        a4 = tk.Entry(f_left, width=width)
        a4.pack(side=tk.TOP)
        tk.Label(f_left, text="Friday").pack(side=tk.TOP)
        a5 = tk.Entry(f_left, width=width)
        a5.pack(side=tk.TOP)
        #End Left Frame

        #Start Right Frame
        f_right = tk.Frame(self)
        f_right.pack(side=tk.RIGHT)
        #Homework Entry List
        tk.Label(f_right, text="Monday").pack(side=tk.TOP)
        h1 = tk.Entry(f_right, width=width)
        h1.pack(side=tk.TOP)
        tk.Label(f_right, text="Tuesday").pack(side=tk.TOP)
        h2 = tk.Entry(f_right, width=width)
        h2.pack(side=tk.TOP)
        tk.Label(f_right, text="Wednesday").pack(side=tk.TOP)
        h3 = tk.Entry(f_right, width=width)
        h3.pack(side=tk.TOP)
        tk.Label(f_right, text="Thursday").pack(side=tk.TOP)
        h4 = tk.Entry(f_right, width=width)
        h4.pack(side=tk.TOP)
        tk.Label(f_right, text="Friday").pack(side=tk.TOP)
        h5 = tk.Entry(f_right, width=width)
        h5.pack(side=tk.TOP)
        #End Right Frame

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
        
if __name__ == "__main__":
    main()


