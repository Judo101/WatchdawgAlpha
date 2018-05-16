# -*- coding: utf-8 -*-
####
# Figure out how to put settings in another window tab CHECK
# Try to move stuff around to make it look cooler CHECK (?)
# GET BETTER BUTTON PICTURES CHECK
####

from Tkinter import *
import ttk
import tkFileDialog as filedialog
import tkMessageBox as messagebox
import ScrolledText as tkst
import time

class watchdawg(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

    # init counter for the video feed
    watchdawg_window_counter = 0
    # init default video length
    video_length = 15
    video_length_set = 0
    # init default snapshot burst
    snapshot_burst = 2
    snapshot_burst_set = 0

    def setupGUI(self):
        self.pack(fill = BOTH, expand = 1)

        # setup the snapshot button to the right of the image along with label
        # wget is a Tkinter button
        # yeah
        watchdawg.snapshot_label = Label(self, text = "Snapshot:")
        watchdawg.snapshot_label.grid(row = 0, column = 1, sticky = W)
        watchdawg.snapshot_button = Button(self, bg = "white", command = self.snapshot)
        watchdawg.snapshot_button.grid(row = 0, rowspan = 1, column = 2, columnspan = 2, sticky = N+S+E+W)
        watchdawg.snapshotting = 0

        # setup another...button? The Record one, to the right of the snapshop button along with label
        # wget is a Tkinter button
        # yeah
        watchdawg.record_label = Label(self, text = "Record:")
        watchdawg.record_label.grid(row = 1, column = 1, sticky = W)
        watchdawg.record_button = Button(self, bg = "white", command = self.record)
        watchdawg.record_button.grid(row = 1, rowspan = 1, column = 2, columnspan = 2, sticky = N+S+E+W)
        watchdawg.recording = 0

        # setup email input to the right of the e-mail label
        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to Nothing right now. Will prob be for email
        # Put it to the right of the email label
        watchdawg.email_input = Entry(self, bg = "white")
        watchdawg.email_input.bind("<Return>", self.process_email)
        watchdawg.email_input.grid(row = 4, column = 2, columnspan = 2, sticky = W+E)

        # setup a label for an entry
        #wget is a Tkinter label
        watchdawg.email_label = Label(self, text = "E-mail:  ")
        watchdawg.email_label.grid(row = 4, column = 1, columnspan = 1, sticky = W)

        # set up a label for an entry
        # wget is a Tkinter Label
        watchdawg.save_dir_label = Label(self, text = "Save Dir:")
        watchdawg.save_dir_label.grid(row = 5, column = 1, sticky = W)
        
        # setup another input, this one for the save directory
        # wget is a Tkinter entry
        # set its background to white and bind the return key to Nothing right now. Will be for save directory
        # put it to the right of the directory label
        watchdawg.save_dir_button = Button(self, text = "Choose Directory...", fg = "red", command = self.open_askdirectory)
        watchdawg.save_dir_button.grid(row = 5, column = 2, columnspan = 2, sticky = W+E)

        # set up status section
        # there will be a GPIO connection light, and a Camera Connection light
        # two wget types, two labels and two lights (in pics)
        # Gotta sort these out...

        # Remote RPI
        # Label
        watchdawg.gpio_status_label = Label(self, text = "RPI Connection")
        watchdawg.gpio_status_label.grid(row = 8, column = 2, columnspan = 1, sticky = W)
        # Pic
        watchdawg.gpio_status_pic = Label(self, image = None)
        watchdawg.gpio_status_pic.grid(row = 8, column = 1, sticky = W+E)
        watchdawg.gpio_status_pic.pack_propagate(False)

        # Camera
        watchdawg.camera_status_label = Label(self, text = "Camera Connection")
        watchdawg.camera_status_label.grid(row = 9, column = 2, columnspan = 1, sticky = W)
        # Pic
        watchdawg.camera_status_pic = Label(self, image = None)
        watchdawg.camera_status_pic.grid(row = 9, column = 1, columnspan = 1, sticky = W+E)
        watchdawg.camera_status_pic.pack_propagate(False)

        # setup ip input label to the left of the input
        # wget is Tkinter Label
        # yeah
        watchdawg.ip_address_label = Label(self, text = "IP Addr.:")
        watchdawg.ip_address_label.grid(row = 10, column = 1, columnspan = 1, sticky = W)

        # setup ip input to the right of the ip address label
        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to Nothing right now. Will prob be for ip address
        # Put it to the right of the ip address label
        watchdawg.ip_address_input = Entry(self, bg = "white")
        watchdawg.ip_address_input.bind("<Return>", self.process_ip)
        watchdawg.ip_address_input.grid(row = 10, column = 2, columnspan = 2, sticky = W+E)

##        # video feed button
##        watchdawg.video_feed_button = Button(self, text = "Open Video Feed", command = self.create_feed_window)
##        watchdawg.video_feed_button.grid(row = 11, column = 1, columnspan = 3, sticky = W+E)

        # sets a combobox to a list of resolutions, these resolutions will dicate the size of the window
        # a label for the resolutions is there too
        watchdawg.res_selector = ttk.Combobox(self, state = "readonly")
        watchdawg.res_selector["values"] = ("1280x720", "1366x768", "1600x900", "1920x1080", "1920x1200", "2560x1440", "2560x1600", "2592x1944")
        watchdawg.res_selector.current(2)
        watchdawg.res_selector.grid(row = 11, column = 2, sticky = E+W)
        watchdawg.res_selector_current = watchdawg.res_selector.get()
        watchdawg.res_label = Label(self, text = "Res:")
        watchdawg.res_label.grid(row = 11, column = 1, sticky = W)

        # scrolled text box for the credits!
        watchdawg.credits_box = tkst.ScrolledText(self, wrap = "word", width = 25, height = 10, bg = "grey")
        watchdawg.credits_box.grid(row = 0, rowspan = 12, column = 4, sticky = N+S+E+W)
        watchdawg.credits_box.insert(INSERT, "Credits:\n\n GUI:                 Morgan King\n\n Controller/Programming: Tường Linh Nguyễn\n\n Motion Sensor:         Nick Williams\n\n Presentation/Frame: Dakota Hollis")
        watchdawg.credits_box.config(state = DISABLED)

        # set the gpio pic
        # issue a check to see if the var is ticked to determine which status light to show
    def gpio_status_pic_img_setter(self):
        if (gpio_status == 1):
            watchdawg.img2 = PhotoImage(file = "status_light_on.gif")
            watchdawg.gpio_status_pic.config(image = watchdawg.img2)
        else:
            watchdawg.img2 = PhotoImage(file = "status_light_off.gif")
            watchdawg.gpio_status_pic.config(image = watchdawg.img2)

        # set the Camera pic
        # issue a check to see if the var is ticked to determine which status light to show
    def camera_status_pic_img_setter(self):
        if (camera_status == 1):
            watchdawg.img3 = PhotoImage(file = "status_light_on.gif")
            watchdawg.camera_status_pic.config(image = watchdawg.img3)
        else:
            watchdawg.img3 = PhotoImage(file = "status_light_off.gif")
            watchdawg.camera_status_pic.config(image = watchdawg.img3)

        # set the snapshot button pic
    def snapshot_button_pic_setter(self):
        watchdawg.img4 = PhotoImage(file = "camera.gif")
        watchdawg.snapshot_button.config(image = watchdawg.img4, justify = CENTER, width = "32", height = "24")

        # set the record button pic
    def record_button_pic_setter(self):
        watchdawg.img5 = PhotoImage(file = "record.gif")
        watchdawg.record_button.config(image = watchdawg.img5, justify = CENTER, width = "32", height = "24")

        # starts recording
        # not my job rn
        # I'm making it change color when pressed
        # should make it check to make sure a directory is chosen
    def record(self):
##        try:
        if (watchdawg.directory != None and watchdawg.recording == 0):
            watchdawg.img5 = PhotoImage(file = "record_alt.gif")
            watchdawg.record_button.config(image = watchdawg.img5, width = "32", height = "24")
            watchdawg.recording = 1
            watchdawg.snapshot_button.config(state = DISABLED)
            
            # make it ask for length of video
            if (watchdawg.video_length_set == 0):
                # in this case, lets make a child window to handle labels
                # calls for it through the function
                self.create_child_window(0)
            else:
                # here is where the stuff gets passed to the controller program
                # put a holder here for now
                print "holder"                
            
            # handle pressing the button again
        elif (watchdawg.directory != None and watchdawg.recording == 1):
            watchdawg.img5 = PhotoImage(file = "record.gif")
            watchdawg.record_button.config(image = watchdawg.img5, width = "32", height = "24")
            watchdawg.recording = 0
            watchdawg.snapshot_button.config(state = NORMAL)
##        except:
##            messagebox.showerror("ERROR", "No Directory has been set! Use the 'Choose Directory...' button to choose a directory!")

    def snapshot(self):
        try:
            if (watchdawg.directory != None and watchdawg.snapshotting == 0):
                watchdawg.img4 = PhotoImage(file = "camera_alt.gif")
                watchdawg.snapshot_button.config(image = watchdawg.img4, width = "32", height = "24")
                watchdawg.snapshotting = 1
                watchdawg.record_button.config(state = DISABLED)

                # make it ask for number of pictures
                if (watchdawg.snapshot_burst_set == 0):
                    # in this case, lets make a child window to handle labels
                    # calls for it through the function
                    self.create_child_window(1)
                else:
                    # here is where the stuff gets passed to the controller program
                    # put a holder here for now
                    print "holder"  

                # handle pressing the button again
            elif (watchdawg.directory != None and watchdawg.snapshotting == 1):
                watchdawg.img4 = PhotoImage(file = "camera.gif")
                watchdawg.snapshot_button.config(image = watchdawg.img4, width = "32", height = "24")
                watchdawg.snapshotting = 0
                watchdawg.record_button.config(state = NORMAL)
        except:
            messagebox.showerror("ERROR", "No Directory has been set! Use the 'Choose Directory...' button to choose a directory!")

    def process_email(self, event):
        # take input
        email = watchdawg.email_input.get()
        # emails are not case sensistive, so let's just put it all in lowercase to make things easier!
        email = email.lower()
        # check the email address to make sure its real
        if ("@" not in email):
            watchdawg.email_input.delete(0, END)
            response = messagebox.showerror("Invalid E-mail", "That doesn't look like a valid e-mail address! Try again.")
        else:
            # now save the address
            watchdawg.email_address = email
            response = messagebox.showinfo("E-mail Saved!", "{} ".format(watchdawg.email_address) + "has been saved as current e-mail address.")

    def process_ip(self, event):
        # take input
        ip = watchdawg.ip_address_input.get()
        # just in case
        ip = ip.lower()
        # check the ip address to make sure its real (ipv4)
        if ((len(ip) < 11) or ("." not in ip)):
            watchdawg.ip_address_input.delete(0, END)
            response = messagebox.showerror("Invalid IP Address", "That doesn't look like a valid IP address! Try again.")
        else:
            # now save the address
            watchdawg.ip_address = ip
            response = messagebox.showinfo("IP Adress Saved!", "{} ".format(watchdawg.ip_address) + "has been saved as current IP address.")
    
        # command for the Save Dir. button. Using this so the dialog doesn't pop up immediately when WDA opens
    def open_askdirectory(self):
        # max 21 characters in button
        watchdawg.directory = "./"
        watchdawg.directory = filedialog.askdirectory()
        # check length
        if (len(watchdawg.directory) > 21):
            watchdawg.button_directory = ""
            # take the string length and cuts it off and adds ... to the end, but still saves the directory.
            sub = len(watchdawg.directory) - 11
            final = watchdawg.directory[:-sub]
            final = "".join(final)
            final += "..."
            watchdawg.button_directory = final
            # add a check to make sure there's actually a directory
            watchdawg.save_dir_button.config(text = watchdawg.button_directory)
            watchdawg.save_dir_button.pack_propagate(False)
                
        # USE watchdawg.directory FOR EVERYTHING ELSE EXCEPT THE BUTTON

        # function to handle closing for the child window button
    def on_closing(self):
        watchdawg.video_length = child_window.input_entry.get()
        watchdawg.video_length = int(watchdawg.video_length)
        child_window.destroy()
        
##
##        # function that creates the video feed window when the button is pressed
##        # works just like another window
##        # set the title and a placeholder pic
##        # tick a counter to change the state of the video feed button
##        # make it call a function when closed
##    def create_feed_window(self):
##        global video_feed
##        video_feed = Toplevel(self)
##        video_feed.wm_title("Watchdawg Video Feed")
##        video_feed.img = PhotoImage(file = "placeholder.gif")
##        video_feed.label = Label(video_feed, image = video_feed.img)
##        video_feed.label.grid(row = 1, column = 0, columnspan = 2, sticky = E+W)
##        self.watchdawg_window_counter += 1
##        watchdawg.video_feed_button.config(state = DISABLED)
##        video_feed.protocol("WM_DELETE_WINDOW", self.on_closing)
##        
##        # figure out how to add a selection piece to select the different resolutions of the camera CHECK
##        # part to select diff res CHEKC
##        # use StringVar to check if the value of the resolution changes, then call a function
##        # sets a combobox to a list of resolutions, these resolutions will dicate the size of the window
##        # a label for the resolutions is there too
##        video_feed.current_res = StringVar()
##        video_feed.res_selector = ttk.Combobox(video_feed, textvar = video_feed.current_res, state = "readonly")
##        video_feed.res_selector["values"] = ("1280x720", "1366x768", "1600x900", "1920x1080", "1920x1200", "2560x1440", "2560x1600", "2592x1944")
##        video_feed.res_selector.current(2)
##        video_feed.res_selector.grid(row = 0, column = 1, sticky = E+W)
##        video_feed.res_selector_current = video_feed.res_selector.get()
##        video_feed.res_label = Label(video_feed, text = "Resolutions:")
##        video_feed.res_label.grid(row = 0, column = 0, sticky = W)
##        video_feed.geometry("800x450")
##        video_feed.current_res.trace('w', self.change_video_feed_resolution)
##
##        # used to change the resolution of the video feed window
##    def change_video_feed_resolution(self, index, value, op):
##        video_feed.changing_res = video_feed.res_selector.get()
##        # split the resolution
##        video_feed.length_width = video_feed.changing_res.split("x")
##
##        # set the length and width (still strings) to a var, then convert to integers so the program can calc with them!
##        length_str = video_feed.length_width[0]
##        width_str = video_feed.length_width[1]
##        length_int = int(length_str)
##        width_int = int(width_str)
##
##        # now half the length and width so the menu isnt extremely huge, and set the geometry to that size
##        length_half = length_int / 2
##        width_half = width_int / 2
##
##        # convert back to string
##        length_half_str = str(length_half)
##        width_half_str = str(width_half)
##        
##        # slam the two strings back together
##        video_feed.changing_new_res = length_half_str + "x" + width_half_str
##
##        # finally set the geometry
##        video_feed.geometry(video_feed.changing_new_res)
##        # work to just scale down the video feed

        # child window creator
        # used for asking for input for recording and snapshotting
    def create_child_window(self, type):
        global child_window
        if (type == 0):
            # recording
            # we're going to assume the user wants to change the length of video recording
            # they will only be able to set this once
            child_window_default_ask = messagebox.askyesno("Default Video Length Detected", "Do you want to change the default video length? (Default = 15 seconds)")
            print child_window_default_ask

            # if they want the default
            if (child_window_default_ask == False):
                watchdawg.video_length_set = 1

            # if they want a different number
            else:
                child_window = Toplevel(self)
                child_window.wm_title("Watchdawg Alpha Settings")
                child_window.input_label = Label(child_window, text = "Please enter a video length:")
                child_window.input_label.grid(row = 0, column = 0, sticky = N+S+E+W)
                child_window.input_label2 = Label(child_window, text = "Close the window when done.")
                child_window.input_label2.grid(row = 1, column = 0, sticky = N+S+E+W)
                child_window.input_entry = Spinbox(child_window, from_ = 1, to = 30, width = 5, state = "readonly")
                child_window.input_entry.grid(row = 2, column = 0, sticky = N+S+E+W)
                child_window.protocol("WM_DELETE_WINDOW", self.on_closing)

                watchdawg.video_length_set = 1

        if (type == 1):
            # snapshotting
            # we're going to assume the user wants to change the number of snapshots taken
            # they will only be able to set this once
            child_window_default_ask = messagebox.askyesno("Default Snapshot Count Detected", "Do you want to change the default snapshot count? (Default = 2 Pictures)")
            print child_window_default_ask

            # if they want the default
            if (child_window_default_ask == False):
                watchdawg.snapshot_burst_set = 1

            # if they want a different number
            else:
                child_window = Toplevel(self)
                child_window.wm_title("Watchdawg Alpha Settings")
                child_window.input_label = Label(child_window, text = "Please enter a burst count:")
                child_window.input_label.grid(row = 0, column = 0, sticky = N+S+E+W)
                child_window.input_label2 = Label(child_window, text = "Close the window when done.")
                child_window.input_label2.grid(row = 1, column = 0, sticky = N+S+E+W)
                child_window.input_entry = Spinbox(child_window, from_ = 1, to = 10, width = 5, state = "readonly")
                child_window.input_entry.grid(row = 2, column = 0, sticky = N+S+E+W)
                child_window.protocol("WM_DELETE_WINDOW", self.on_closing)

                watchdawg.snapshot_burst_set = 1

    # check the status of the gpio.
    # use this to change the pic of the status barz
    # you can change the pic on the fly here, see waaaay above for the variables
    def check_gpio_status(self):
        window.after(1000, self.check_gpio_status)
        print "ping!"
        pass

    # check the status of the camera.
    # use this to change the pic of the status barz
    # you can change the pic on the fly here, see waaaay above for the variables
    def check_camera_status(self):
        window.after(1000, self.check_camera_status)
        print "pong!"
        pass
    
        # start the GUI
    def start(self):
        self.setupGUI()
        self.gpio_status_pic_img_setter()
        self.camera_status_pic_img_setter()
        self.snapshot_button_pic_setter()
        self.record_button_pic_setter()

### 
###
## Main Program ##

width = 800
height = 600
snapshot_during_recording_var = None
alert_when_start_recording_var = None
camera_status = 0
gpio_status = 0
watchdawg_window_counter = 0

window = Tk()

window.title("Watchdawg Alpha")

watchdawg = watchdawg(window)
watchdawg.start()

window.after(0, watchdawg.check_gpio_status)
window.after(0, watchdawg.check_camera_status)
window.mainloop()

