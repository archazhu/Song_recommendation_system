'''
To display window (gui) of the project
Author: Ashutosh
'''


from spotify_dataset_process import *
import tkinter
from tkinter.filedialog import askopenfilename
import random


#################################################################
#################################################################
def start_window():
    window = tkinter.Tk()
    window.geometry("425x500")
#window.minsize(350, 350)
    window.configure(bg='black')
    l1 = tkinter.Label(window, text="Song Recommendation System", anchor=tkinter.CENTER, font=("Arial Bold", 18),
                   padx=20, pady= 5,bg='black', fg='white', borderwidth=2, relief="groove")
    l1.grid(row=0)

    def click():
        global filename
        filename = ''
        filename = askopenfilename()
        while filename == () or filename == '':
            filename = askopenfilename()
    
        l3 = tkinter.Label(window, text="File chosen:" + filename, bg='black', fg='tomato', wraplength=400)
        l3.grid(row=3)
        
    #exception handling to be implemented if file is not a csv file
        bn = tkinter.Button(window, text="Continue", bg='black', fg='white', command=final)
        bn.grid(row=4)

    def final():
    #to modify it for further input and link it to the next function
        window.destroy()
        mid_window(filename)
    
    b1 = tkinter.Button(window,text="Choose a file", font=("Arial", 12), command=click, bg='black', fg='white')
    b1.grid(row=2,padx=20, pady=30)

    window.mainloop()






###############################################################33
#################################################################3
def mid_window(filename):
    def get():
        if 0 >= int(e2.get()) or 100 < int(e2.get()):
            lm1 = tkinter.Label(mid, text="Enter an age between 0 and 100 and press CONTINUE", fg='coral', bg='black')
            lm1.grid(row=3, column=1)
        else:
            try:
                age = int(e2.get())
            except ValueError:
                lmx = tkinter.Label(mid, text="Enter an integer value as age", fg='coral', bg='black')
                lmx.grid(mid, row=3, column=1)
                
            mid.destroy()
            if 'hindi' in filename:
                final_window(age, filename, 0)
            else:
                final_window(age, filename, 1)
                
    
    mid = tkinter.Tk()
    mid.configure(bg='black')
    la1 = tkinter.Label(mid, text='Hi there, please enter some details! ', bg='black', fg='white',
                       font=("Arial Bold", 15), borderwidth=2, pady=5)
    la1.grid(row=0)
    la2 = tkinter.Label(mid, text="Enter your name: ", fg='white', bg='black', )
    la2.grid(row=1, column =0)
    e1 = tkinter.Entry(mid, bd =2)
    e1.grid(row=1, column=1)
    la3 = tkinter.Label(mid, text="Enter your age: ", fg='white', bg='black')
    la3.grid(row=2, column =0)
    e2 = tkinter.Entry(mid, bd =2)
    e2.grid(row=2, column=1)
    ba1 = tkinter.Button(mid, text='Continue', command=get, fg='white', bg='black')
    ba1.grid(row=4)
    
    mid.mainloop()




###################################################################
###################################################################
def final_window(age, filename, lang):
    fileprocessing(filename)
    Ashu = User()
        
    def help():
        def exit():
            helpwindow.destroy()
            
        helpwindow = tkinter.Tk()
        helpwindow.minsize(375, 370)

        helpwindow.configure(bg='black')
        lla = tkinter.Label(helpwindow, bg='black', fg='white', text='HELP', font=("Arial Bold", 15)).grid(row=0)
        lla1 = tkinter.Label(helpwindow, bg='black', fg='light yellow', padx = 5, pady= 5,
                             text='1. Select a song from the drop-down menu' ).grid(row=1)
        lla2 = tkinter.Label(helpwindow, bg='black', fg='white',  padx = 5, pady = 5,
                             text='2. Add the song to your collection using ADD button').grid(row=2)
        lla3 = tkinter.Label(helpwindow, bg='black', fg='white',  padx = 5, pady =5,
                             text='3. Refresh the list using REFRESH button' ).grid(row=3)
        lla4 = tkinter.Label(helpwindow, bg='black', fg='white', padx = 5, pady = 5,
                             text="4. Click on 'Recommendation Section' for recommendations." ).grid(row=4)
        lla5 = tkinter.Label(helpwindow, bg='black', fg='white', padx = 5, pady = 10,
                             text='ENJOY :)' ).grid(row=5)
        bba1 = tkinter.Button(helpwindow, text='EXIT', command=exit, padx=5, pady=12).grid(row=6)
        

    root = tkinter.Tk()
    root.configure(bg='black')
    ll1 = tkinter.Label(root, text="Choose your favorite songs from the list",
                    anchor=tkinter.CENTER, font=("Arial Bold", 18), padx=20, bg='black', fg='white')
    ll1.grid(row=0, column=0)
    
    ll11 = tkinter.Button(root, text='HELP?', font=("Arial Bold", 18), padx=20, 
                          bg='black', fg='SeaGreen2', borderwidth=2, relief="groove", 
                          command=help).grid(row=0, column=2)

    ll2 = tkinter.Label(root, text="",bg='black', fg='white')
    ll2.grid(row=1, column=0)
    
    global lst
    lst = Ashu.show_entries(age)
    Option = lst.keys()
          
# Creating a Listbox and 
# attaching it to root window 

#refresh is working :)
    def refresh():
        global lab
        if lab != None:
            lab.destroy()
        lab = None
        global lst
        lst = Ashu.show_entries(age)
        #print(lst.keys())
        Option = lst.keys()
        var.set('None')
        opt = tkinter.OptionMenu(root, var, *list(Option))
        #opt.config(width=50)
        opt.config(bg = "white")
        opt.grid(row=2,columnspan=3)
    
    global lab
    lab = None
    var = tkinter.StringVar(root)
    var.set('None')

    opt = tkinter.OptionMenu(root, var, *list(Option))
    #opt.config(width=50)
    opt.config(bg = "white")
    opt.grid(row=2,columnspan=3)


    def continue_now():
        if var.get() == 'None':
            global lab
            lab = tkinter.Label(text="Please select a song from the drop-down menu", 
                                bg='black', fg='coral', pady = 5)
            lab.grid(row=4)
        #print("lst now", lst)
        #print('hey there', var.get() ,lst.get(var.get()))
        else:
            if lab != None:
                lab.destroy()
                lab = None
            Ashu.insert_song(lst.get(var.get())[0])
            lb1 = tkinter.Label(text="Song succesfully added to Your Collection", bg='black',
                               fg='SeaGreen1', pady = 5)
            lb1.grid(row=4)
            lb1.after(1000, lb1.destroy)

    def recommend():
        if lab != None:
            lab.destroy()
        root.destroy()
        root2 = tkinter.Tk()
        eng_label_db = {0:'Positive vibes', 1:'Raps', 2:'Melodies', 3:'Songs to pump you up',
                       4:'Explicit', 5:'Chill songs', 6:'Sad n Slow songs'}
        
        hindi_label_db = {0: 'Fast paced songs', 1:'Soothing', 2:'Chill',
                         3:'Positive vibes', 4:'Energetic songs', 5:'Happy Melodies', 6:'Most popular songs'}
        
        color = ['SeaGreen1' ,'mint cream' ,'light salmon', 'bisque', 'thistle1', 'RosyBrown1', 'turquoise1','tomato', 'ivory2','orchid1']
        root2.configure(bg='black')
        ll1 = tkinter.Label(root2, text="Here are some recommendations for you", borderwidth=2, relief="groove",
                    anchor=tkinter.CENTER, font=("Arial Bold", 18), padx=20, bg='black', fg='white')
        ll1.pack()

        for i in range(7):
            temp2 = Ashu.return_songs(i)
            if (not temp2.equals(pd.DataFrame([[]]))):
                if lang == 0:
                    lla = tkinter.Label(root2, text=hindi_label_db[i], font=("Arial Bold", 14), bg='black', fg=random.choice(color), pady=7).pack()
                else:
                    lla = tkinter.Label(root2, text=eng_label_db[i], font=("Arial Bold", 14), bg='black', fg=random.choice(color), pady=7).pack()
                
                now = list(temp2.values)
                print(now)
                for k in now:
                    lly = tkinter.Label(root2, text=k[0] + " by " + k[1], bg='black', fg='white')
                    lly.pack()
            #print(temp)

#continue is working :)

    def show_db():
        
        def exit_now():
            db_window.destroy()
        
        db_window = tkinter.Tk()
        db_window.geometry("425x500")
        db_window.configure(bg='black')

        x = Ashu.return_listen_history()
        llabel = tkinter.Label(db_window, text= "Your History !", bg='black', fg='white', font=("Arial Bold", 14), pady=10).pack()
        for i in x.keys():
            lla = tkinter.Label(db_window, text=str(i), bg='black', fg='white')
            lla.pack()
            #print(i, " -- ", x.get(i))
        bba1 = tkinter.Button(db_window, text="EXIT", command=exit_now, bg='black', fg='white', pady=10)
        bba1.pack()
        db_window.mainloop()
    #print(temp)

    bb0 = tkinter.Button(root, text="MY LIST", command=show_db, bg='black', fg='white')
    bb0.grid(row=3, column=0)

    bb1 = tkinter.Button(root, text="ADD song", command=continue_now, bg='black', fg='white')
    bb1.grid(row=3, column=1)

    bb2 = tkinter.Button(root, text="REFRESH THE LIST", command=refresh, bg='black', fg='white')
    bb2.grid(row=3, column=2)

    bb3 = tkinter.Button(root, text="RECOMMENDATIONS", command=recommend, bg='black', fg='white')
    bb3.grid(row=3, column=3)

    root.mainloop()

if __name__ == '__main__':
    start_window()
