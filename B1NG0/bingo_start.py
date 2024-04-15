
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import font
import os

import cardcreation
import bingosim
import bingoanalysis
import bingoprint

                
################################################################################################
#Root Class of Tkinter Window
class MainMenu:
    def __init__(self, master):
        
        self.cards_holder = None
        self.user_image = None
        
        self.master = master
        self.master.geometry("500x250")
        
        self.master.title("Main Menu")
        self.master.resizable(width=False, height=False) # inserted to avoid user resizing and disturbing orientation
        
        #Change window icon
        folder_dir = os.path.dirname(__file__)
        self.icon_path = os.path.join(folder_dir, "Images\icon.ico")
        self.master.iconbitmap(self.icon_path)
        
        #Window Decorations and Buttons
        self.greet = tk.Label(master, text="Welcome to B1NG0, to start a new bingo instance, please select \"Card Creation Menu\".")
        self.greet.pack(anchor=tk.N)

        self.ccm_button = tk.Button(self.master, text="Card Creation Menu", command=self.openBCM,padx = 20, pady = 10) #Button for Card Creation Menu
        self.ccm_button.place(relx = 0.35, rely = 0.40, anchor = tk.CENTER)

        self.sbutton = tk.Button(self.master, text="Simulation Menu", command=self.openSIM, padx = 20, pady = 10) #Button for Simulation menu
        self.sbutton.place(relx = 0.65, rely = 0.40, anchor = tk.CENTER)
        
        self.pbutton = tk.Button(self.master, text = "Print Bingo Cards To PDF", command = self.ask_user, padx = 20, pady = 10) #Button for Print to PDF
        self.pbutton.place(relx = 0.50, rely = 0.60, anchor = tk.CENTER)
        
        self.qbutton = tk.Button(self.master, text="Quit", command=self.quit) #Quit Button
        self.qbutton.place(relx=0.5, rely=1, anchor=tk.S)
        
    def quit(self): #function for ending the program
        self.master.destroy()
        
        
    def openBCM(self):
        self.bcm = tk.Toplevel(root)
        self.bcm.title("Card Creation Menu")
        self.bcm.geometry("500x250")
        self.bcm.iconbitmap(self.icon_path)
        self.bcm.resizable(width=False, height=False)
        
        #Choose Number of Cards Selection
        
        self.bcm.l1 = tk.Label(self.bcm, text = "Number of Cards:")
        self.bcm.l1.place(relx = 0.50, rely = 0.10, anchor = tk.N)
        
        
        self.bcm.s1 = tk.Scale(self.bcm, from_=1, to=50, orient = tk.HORIZONTAL)
        self.bcm.s1.set(5)
        self.bcm.s1.place(relx = 0.50, rely = 0.20, anchor = tk.N)
        
        
        #Choose Dimensions of Cards Selection
        
        #Rows Slider
        
        self.bcm.l2 = tk.Label(self.bcm, text = "Number of Rows:")
        self.bcm.l2.place(relx = 0.20, rely = 0.10, anchor = tk.N)
        
        self.bcm.s2 = tk.Scale(self.bcm, from_=3, to=50, orient = tk.HORIZONTAL, command = self.idsc)
        self.bcm.s2.set(5)
        self.bcm.s2.place(relx = 0.20, rely = 0.20, anchor = tk.N)
        
        #Cols Slider
        
        self.bcm.l3 = tk.Label(self.bcm, text = "Number of Columns:")
        self.bcm.l3.place(relx = 0.20, rely = 0.40, anchor = tk.N)
        
        self.bcm.s3 = tk.Scale(self.bcm, from_=3, to=50, orient = tk.HORIZONTAL, command = self.idsc)
        self.bcm.s3.set(5)
        self.bcm.s3.place(relx = 0.20, rely = 0.50, anchor = tk.N)
        
        #Choose Range of Numbers Selection Slider
        
        self.bcm.l4 = tk.Label(self.bcm, text = "Range of Numbers to be Called:")
        self.bcm.l4.place(relx = 0.80, rely = 0.10, anchor = tk.N)
        
        self.bcm.s4 = tk.Scale(self.bcm, from_=75, to = 5*75, orient = tk.HORIZONTAL, resolution = 75)
        self.bcm.s4.set(75)
        self.bcm.s4.place(relx = 0.80, rely = 0.20, anchor = tk.N)
        
        #Choose Number of Free Cells Slider
        
        self.bcm.l5 = tk.Label(self.bcm, text = "Number of Free Cells:")
        self.bcm.l5.place(relx = 0.50, rely = 0.40, anchor = tk.N)
        
        self.bcm.s5 = tk.Scale(self.bcm, from_= 0, to= 5*5, orient = tk.HORIZONTAL)
        self.bcm.s5.set(0)
        self.bcm.s5.place(relx = 0.50, rely = 0.50, anchor = tk.N)
        
        #Choose Free Cell Distribution Type Dropdown
        
        self.bcm.l5 = tk.Label(self.bcm, text = "Select Free Cell Distribution Type:")
        self.bcm.l5.place(relx = 0.80, rely = 0.40, anchor = tk.N)
        
        choices = ['Diamond', 'Random'] #diamond and random explained in cardcreation
        self.variable = tk.StringVar(self.bcm)
        self.variable.set('Diamond')
        
        self.bcm.w1 = tk.OptionMenu(self.bcm, self.variable, *choices)
        self.bcm.w1.place(relx = 0.80, rely = 0.55, anchor = tk.N)
        
        #Exit Button
        
        self.bcm.qbutton = tk.Button(self.bcm, text="Exit", command=self.exit_bcm_window)
        self.bcm.qbutton.place(relx=0.10, rely=1, anchor=tk.S)
        
        #Confirm Button = creates card using current slider settings
        
        self.bcm.cbutton = tk.Button(self.bcm, text = "Confirm", command = self.create_cards)
        self.bcm.cbutton.place(relx = 0.90, rely = 1, anchor = tk.S)
    
    def idsc(self,value): #idsc is designed to dynamically change the range of the numbers called to soft lock the user from creating improper combinations
        colin = self.bcm.s3.get()
        rowin = self.bcm.s2.get()
        
        self.bcm.s4.configure(from_=colin*rowin, to= 5*(colin*rowin), resolution = colin*rowin)
        self.bcm.s5.configure(from_= 0, to= (colin*rowin))
        
    def openSIM(self): #Simulation tkinter instance
        if self.cards_holder is not None:
            self.sim = tk.Toplevel(root) 
            self.sim.title("Simualtion Menu")
            self.sim.resizable(width=False, height=False)
            
            #Number of simulations Slider
            
            self.sim.l1 = tk.Label(self.sim, text = "Number of Simulations:")
            self.sim.l1.place(relx = 0.50, rely = 0.10, anchor = tk.N)
        
            self.sim.s1 = tk.Scale(self.sim, from_=1, to=150, orient = tk.HORIZONTAL)
            self.sim.s1.set(10)
            self.sim.s1.place(relx = 0.50, rely = 0.20, anchor = tk.N)
            
            #Exit Button
            self.sim.qbutton = tk.Button(self.sim, text="Exit", command=self.exit_sim_window)
            self.sim.qbutton.place(relx=0.20, rely=1, anchor=tk.S)
            
            #Confirm Button
            self.sim.cbutton = tk.Button(self.sim, text = "Confirm", command = self.do_simulation)
            self.sim.cbutton.place(relx = 0.80, rely = 1, anchor = tk.S)
            
        else:
            self.msg_window("Please create bingo cards before beginning the Simulation.")
        
    
    def printpdf(self): #function handeling printing bingo cards to pdf
        
        pdf = bingoprint.PDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        if self.user_image is not None:
            bingoprint.draw_bingo_cards(pdf, self.cards_holder, self.user_image)
                
        else:
            bingoprint.draw_bingo_cards(pdf, self.cards_holder)

        pdf.output("bingo_cards.pdf")
        self.msg_window("Bingo Cards Printed To Folder.")
            
    def msg_window(self,msg): #simple message window taken from lecture slides in order to provide the user with a message
        child1 = tk.Toplevel(self.master)
        child1.resizable(width=False, height=False)
        label = tk.Label(child1, text = msg )
        label.pack()
        
    def ask_user(self): #Pop up window used to find if the user wants to use a custom image if they put free spaces into the bingo card
        if self.cards_holder is not None:
            if self.freenumbers > 0:
                self.child2 = tk.Toplevel(self.master)
                self.child2.resizable(width=False, height=False)
                label = tk.Label(self.child2, text = "Would you like to insert an image into the free cells?")
                label.pack(side = tk.TOP)
                
                approve = tk.Button(self.child2, text = "Yes", command = self.set_user_image)
                approve.pack(side = tk.LEFT, expand = True)
                
                disapprove = tk.Button(self.child2, text = "No", command = self.exit_ask_user)
                disapprove.pack(side = tk.LEFT, expand = True)
            else:
                self.printpdf()    
            
        else:
            self.msg_window("Please create bingo cards before printing them to PDF.")
        
    def set_user_image(self): #function to path to if a user wants to add an image to the free spaces
        self.user_image = filedialog.askopenfilename(title="Select a file", filetypes=(("PNG Files", "*.png"),("All Files", "*.*"))) #opens a file directory window used to find PNG files
        print(self.user_image)
        try:
            self.printpdf()
            self.child2.withdraw()
        except:
            self.msg_window("Please select an appropriate image")
        
    def exit_ask_user(self): #function to path to if a user does not want to add an image to the free spaces
        self.printpdf()
        self.child2.withdraw()
        
    def exit_bcm_window(self): 
        self.bcm.withdraw()
        
    def exit_sim_window(self):
        self.sim.withdraw()
        
    def create_cards(self): #command to get slider values and create bingo cards using these values
        cardnum = self.bcm.s1.get()
        rownum = self.bcm.s2.get()
        colnum = self.bcm.s3.get()
        numrange = self.bcm.s4.get()
        freenum = self.bcm.s5.get()
        disttype = self.variable.get()
    
        self.cards_holder = cardcreation.create_bingo_cards(cardnum, rownum, colnum, numrange, freenum, disttype)
        self.poolie = numrange #saved for futher use in simulations part
        self.freenumbers = freenum #saved for further use in printing to pdf
        
        if colnum > 30 or rownum > 30 or numrange > 3*(colnum*rownum):
            self.msg_window("WARNING!!! Exceptionally Large Bingo Card Combinations May Increase Simulation Processing Times")
        
        self.exit_bcm_window()
        
    def do_simulation(self): #command to get simulator slider and call simulation function
        simnum = self.sim.s1.get()
        
        self.bingo_results, self.full_results = bingosim.bingo_simulation(self.cards_holder,simnum, self.poolie)
        centrality_figs = bingoanalysis.plot_combined_analysis(self.bingo_results, self.full_results) #produces graphs and then returns centrality statistics
        
        #create a window to display centrality figures outside of the terminal
        disp1 = tk.Toplevel(self.master)
        disp1.title("Centrality Results")
        
        table_font = font.nametofont("TkFixedFont")
        
        text_widget = scrolledtext.ScrolledText(disp1, width = 260, height = 62, font = table_font)
        text_widget.insert(tk.END, centrality_figs.to_string(index = False))
        text_widget.pack()
        
        screen_width = disp1.winfo_screenwidth()
        screen_height = disp1.winfo_screenheight()
        disp1.geometry(f"{screen_width}x{screen_height}")
        disp1.resizable(width=False, height=False)
        
        self.exit_sim_window()
        
        
        
root = tk.Tk()
MainMenu(root)
root.mainloop()
