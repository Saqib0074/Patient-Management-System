"""Main Execution File"""
from sub_windows import *

root = Tk()
root.configure(background='light blue')
root.geometry('1920x1600')
root.title("Patient Management System")
# Header frame
header_frame = Frame(root, bg='grey', borderwidth=4, border=10, background='teal')  # constraint search frame
topLab = Label(header_frame, text='Patient Management System', font='Calibre 20')  # app name
topLab.grid(column=1, row=1, padx=5, pady=5)
header_frame.grid(column=2, row=1, pady=5)

# button Frame

button_frame = Frame(root, bg='blue', borderwidth=4, border=10, background='teal', )  # all buttons in this frame
# button frame header
button_frame_header = Label(button_frame, text="Main Menu", height=2, width=30, font='Times,Bold,21')
button_frame_header.grid(column=1, row=3, padx=5, pady=20)
# add record button

add_button = Button(button_frame, text='ADD New Patient', height=1, width=23, font='14',
                    command=addwindow)  # record addition button
add_button.grid(column=1, row=7, pady=5)
# delete record button
delete_button = Button(button_frame, text='Delete Patient Record', height=1, width=23, font='14',
                       command=delete)  # delete window button
delete_button.grid(column=1, row=8, pady=5)
# data display frame
data_display_Frame = Frame(root, bg='grey', borderwidth=4, border=2, background='light cyan', bd=2)
data_display_label = Label(data_display_Frame, text='Records', font='calibre 20', borderwidth=4, border=3,
                           background='white', bd=3, width=20)
data_display_label.grid(column=1, row=1, pady=4, padx=3)
data_display_Frame.grid(column=2, row=3, padx=0)
# data display top frame
data_display_Frame_top = Frame(data_display_Frame, bg='blue', borderwidth=4, border=2, bd=2, background='light blue')

# ----------------------------------------------Display data------------------------------------------------------------


update_button = Button(button_frame, text="Update Records", height=1, width=23, font='14',
                       command=update)  # update record button
update_button.grid(column=1, row=11, pady=5)
button_frame.grid(column=1, row=3, pady=15, padx=10)
# ======================================================================================================================
eventupdate_button = Button(button_frame, text="Update Event", height=1, width=23, font='14',
                            command=event_update)  # event update window button
eventupdate_button.grid(column=1, row=13, pady=5)
closeallwin_button = Button(button_frame, text="Close", height=1, width=23, font='14', command=closeallwin,
                            background='red', bg='red')
closeallwin_button.grid(column=1, row=16, pady=5)

# ----------------------------------------------Display data------------------------------------------------------------

# search record head
id_entry = Entry(data_display_Frame_top, width=15, font='Calibri 15 bold')
id_entry.grid(column=2, row=1, padx=2)
name_entry = Entry(data_display_Frame_top, width=15, font='Calibri 15 bold')
name_entry.grid(column=25, row=1, padx=2)


def viewdatafinal():  # view all data
    viewdata(data_display_Frame)


def viewdatabyidfinal():  # view record by id or name
    viewdatabyid(id_entry, data_display_Frame, name_entry)
    id_entry.delete(0, END)
    name_entry.delete(0, END)


view_button = Button(button_frame, text=" Refresh Records", height=1, width=23, font='14',
                     command=viewdatafinal)  # view all record button
view_button.grid(column=1, row=9, pady=5)
search_record_top_button = Button(data_display_Frame_top, text="Search Record By id", height=1, width=17,
                                  font='calibri,10,bold', borderwidth=2, border=3, bg='white',
                                  command=viewdatabyidfinal)  # search by id button
search_record_top_button.grid(column=1, row=1, padx=5, pady=2)
search_record_name_button = Button(data_display_Frame_top, text="Search Record By Name", height=1, width=20,
                                   font='calibri,10,bold', borderwidth=2, border=3, bg='white',
                                   command=viewdatabyidfinal)  # search by name button
search_record_name_button.grid(column=23, row=1, padx=5, pady=2)

data_display_Frame_top.grid(column=1, row=0, padx=3)
viewdata(data_display_Frame)

root.mainloop()
