"""sub windows functions"""
from tkinter import *

from Sqlcode import *


# -------------------------------------Add Function---------------------------------------------------------------------
# ====================================================================================================================

def snocheck(tbname, colname):  # checks serial no. / order integrity
    query = f"""select * from {tbname}"""
    data = read_query(connection, query)
    if data == []:
        print('Empty!')
    else:
        if len(data)>1:
            for i in range(len(data)):
                if data[i][0] != i + 1:
                    query = f"""update {tbname}
                        set {colname}={i + 1} where SNo ={data[i][0]}"""
                    execute_query(connection, query)


def snoalot(name):  # function for auto id/serial no. allocation
    snoval = ''
    try:
        que = f"""select * from {name}"""
        data = read_query(connection, que)
        print(data)
        if not data:
            snoval = 0
        else:
            snoval = data[-1][0]

    except Error as err:
        print('Error', err)
    snoval += 1
    return str(snoval)


# ====================================================================================================================
def addwindow():  # defines the whole record addition operation
    global addwindowdes

    def addwindowdes():
        addwindow.destroy()

    addwindow = Tk()
    addwindow.configure(background='light blue')
    addwindow.geometry('600x500')
    addwindow.title('Add New Patient')
    global addwindow_frame
    addwindow_frame = Frame(addwindow, borderwidth=4, bd=3, border=2, background='teal')

    addwindow_frame.grid(column=1, row=4, pady=7, padx=3)
    # window_name_frame
    window_name_frame = Frame(addwindow, bg='grey', borderwidth=4, border=10, background='teal')
    window_name_frame.grid(column=1, row=1, padx=20, pady=4)
    # window name
    window_name_label = Label(window_name_frame, text='Add New Patient', width=17, height=2, font='Times 15', bd=2)
    window_name_label.grid(column=1, row=1)
    # --------------------- entry widgets ----------------------------------------
    # patient_id set
    # name set
    name_label = Label(addwindow_frame, text='Enter Patient Name', font='Calibre 12 bold', width=15, height=1,
                       bd=3, borderwidth=3, border=3, bg='white')
    name_label.grid(column=3, row=3, padx=3, pady=5)
    name_entry = Entry(addwindow_frame, width=17, font='Calibre 13 bold')
    name_entry.grid(column=5, row=3, padx=2, pady=5)
    # doctor name
    doctor_label = Label(addwindow_frame, text="Enter Doctor's Name", font='Calibre 12 bold', width=15, height=1,
                         bd=3, borderwidth=3, border=3, bg='white')
    doctor_label.grid(column=3, row=4, padx=3, pady=5)
    doctor_entry = Entry(addwindow_frame, width=17, font='Calibre 13 bold')
    doctor_entry.grid(column=5, row=4, padx=2, pady=5)
    # condition
    condition_label = Label(addwindow_frame, text="Enter Diagnosis", font='Calibre 12 bold', width=15, height=1,
                            bd=3, borderwidth=3, border=3, bg='white')
    condition_label.grid(column=3, row=5, padx=3, pady=5)
    condition_entry = Entry(addwindow_frame, width=17, font='Calibre 13 bold')
    condition_entry.grid(column=5, row=5, padx=2, pady=5)

    # admit_date
    admit_date_label = Label(addwindow_frame, text='Enter Admit Date', font='Calibre 12 bold', width=15, height=1,
                             bd=3, borderwidth=3, border=3, bg='white')
    admit_date_label.grid(column=3, row=6, padx=3, pady=5)
    admit_date_entry = Entry(addwindow_frame, width=17, font='Calibre 13 bold')
    admit_date_entry.grid(column=5, row=6, padx=2, pady=5)

    def values():  # takes values and does final execution for add op
        patient_id = snoalot('patient_main')
        name = name_entry.get()
        doctor_name = doctor_entry.get()
        condition = condition_entry.get()
        admit_date = admit_date_entry.get()
        # discharge = discharge_entry.get()
        add(connection, patient_id, name, doctor_name, condition, admit_date)

    def clear():  # clears fields for next record (user-friendly feature)
        # patient_id_entry.delete(0, END)
        name_entry.delete(0, END)
        doctor_entry.delete(0, END)
        condition_entry.delete(0, END)
        admit_date_entry.delete(0, END)

    #   discharge_entry.delete(0, END)

    # ----------------submit button -------------
    submit_button = Button(addwindow_frame, command=values, width=10, height=1, text='Add Record')
    submit_button.grid(column=5, row=8, pady=5, padx=2)
    # ----------------Clear button -------------
    clear_button = Button(addwindow_frame, command=clear, width=10, height=1, text='Next Record')
    clear_button.grid(column=5, row=9, pady=5, padx=2)

    addwindow.mainloop()


def add(connection, patient_id, name, doctor_name, condition, admit_date):  # sql addition code
    query = f"""insert into patient_main values('{patient_id}','{name}','{doctor_name}','{condition}','{admit_date}',
    null) """
    patienttabque = f"create table {name + str(patient_id)}(SNo int not null,event varchar(200) default Null," \
                    f"event_date date default Null) "
    execute_query(connection, patienttabque)
    execute_query(connection, query)


# ======================================================================================================================

# --------------------------------------------------- Delete Function --------------------------------------------------
def delete():
    global delrotf

    def delrotf():
        delroot.destroy()

    delroot = Tk()
    delroot.configure(background='light blue')
    window_name_frame = Frame(delroot, bg='grey', borderwidth=4, border=10, background='teal')
    window_name_frame.grid(column=1, row=1, padx=20, pady=4)
    # window name
    window_name_label = Label(window_name_frame, text='Delete Record', width=17, height=2, font='Times 15', bd=2)
    window_name_label.grid(column=1, row=1)
    delroot.geometry('400x350')
    del_frame = Frame(delroot, bg='grey', borderwidth=4, border=10, background='teal')

    patient_id_entry = Entry(del_frame, width=17, font='Calibre 13 bold')
    patient_id_entry.grid(column=2, row=1)

    def deletefinal():
        patient_id = patient_id_entry.get()
        deleten(patient_id)

    def dellall():
        query = f"delete from patient_main"
        execute_query(connection, query)

    del_frame.grid(column=1, row=4, padx=10, pady=3)
    patient_id_Label = Label(del_frame, text='Enter Patient ID', font='Calibre 12 bold', width=15, height=1,
                             bd=3, borderwidth=3, border=3, bg='white')
    patient_id_Label.grid(column=1, row=1)
    del_button = Button(del_frame, text='Delete', font='Calibre 12 bold', width=15, height=1,
                        bd=3, borderwidth=3, border=3, bg='white', command=deletefinal)
    del_button.grid(column=2, row=4, padx=3, pady=5)
    del_button = Button(del_frame, text='Delete All Records', font='Calibre 12 bold', width=15, height=1,
                        bd=3, borderwidth=3, border=3, bg='white', command=dellall)
    del_button.grid(column=2, row=6, padx=3, pady=5)

    delroot.mainloop()


def deleten(patient_id):
    byid(patient_id)
    query = f"""delete from patient_main where patient_id ='{patient_id}'; """
    query2 = f"""drop table {byidl[0][1] + str(patient_id)}"""
    execute_query(connection, query)
    execute_query(connection, query2)


# ======================================================================================================================
# ---------------------------------------------------- Show Function ---------------------------------------------------
from_db = []


def showfunc():
    from_db.clear()

    query = "select * from patient_main"
    data = read_query(connection, query)

    for result in data:
        result = list(result)
        from_db.append(result)


showfunc()
byidl = []


def byid(patient_id):
    byidl.clear()
    query = f"""select * from patient_main where patient_id ='{patient_id}'"""
    dat = read_query(connection, query)
    for data in dat:
        byidl.append(data)


def byname(name):
    byidl.clear()
    query = f"""select * from patient_main where name ='{name}'"""
    data = read_query(connection, query)
    for data in data:
        byidl.append(data)


# ======================================================================================================================
def viewdata(frame):
    from tkinter import ttk
    showfunc()

    # Create an instance of tkinter frame
    # Create an object of Style widget
    style = ttk.Style(frame)
    style.configure('Treeview', rowheight=40)
    style.theme_use('clam')
    style.configure('.', font=(None, 14))
    # Add a Treeview widget
    tree = ttk.Treeview(frame,
                        column=("Patient Id", "Name", "Doctor", "Diagnosis", "Admit Date", "discharge"),
                        show='headings',
                        height=12)
    tree.column("# 1", anchor=CENTER, stretch=NO, width=65)
    tree.heading("# 1", text="Patient Id")
    tree.column("# 2", anchor=CENTER, stretch=NO, width=200)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER, stretch=NO, width=180)
    tree.heading("# 3", text="Doctor")
    tree.column("# 4", anchor=CENTER, stretch=True, width=430)
    tree.heading("# 4", text="Diagnosis")
    tree.column("# 5", anchor=CENTER, stretch=NO, width=120)
    tree.heading("# 5", text="Admit Date")
    tree.column("# 6", anchor=CENTER, stretch=NO, width=120)
    tree.heading("# 6", text="Discharge")
    # Insert the data in Treeview widget
    for rows in from_db:
        tree.insert('', 'end', text="1", values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5]))

    tree.grid(column=1, row=3, padx=5, pady=3)


# view all record button

def viewdatabyid(id, frame, name):
    from tkinter import ttk

    style = ttk.Style(frame)
    style.configure('Treeview', rowheight=30, columnwidth=7)
    style.theme_use('clam')
    style.configure('.', font=(None, 14))
    # Add a Treeview widget
    treebyid = ttk.Treeview(frame,
                            column=("Patient Id", "Name", "Doctor", "Diagnosis", "Admit Date", "Discharge Date"),
                            show='headings', height=3)
    treebyid.column("# 1", anchor=CENTER, stretch=NO, width=65)
    treebyid.heading("# 1", text="Patient Id")
    treebyid.column("# 2", anchor=CENTER, stretch=NO, width=200)
    treebyid.heading("# 2", text="Name")
    treebyid.column("# 3", anchor=CENTER, stretch=NO, width=180)
    treebyid.heading("# 3", text="Doctor")
    treebyid.column("# 4", anchor=CENTER, stretch=True, width=430)
    treebyid.heading("# 4", text="Diagnosis")
    treebyid.column("# 5", anchor=CENTER, stretch=NO, width=120)
    treebyid.heading("# 5", text="Admit Date")
    treebyid.column("# 6", anchor=CENTER, stretch=NO, width=120)
    treebyid.heading("# 6", text="Discharge")

    # Insert the data in Treeview widget
    def idfun():
        byid(id.get())
        for rows in byidl:
            treebyid.insert('', 'end', text="2", values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5]))

    def namefun():
        byname(name.get())
        for rows in byidl:
            treebyid.insert('', 'end', text="2", values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5]))

    if len(name.get()) > 0:
        namefun()
    else:
        idfun()

    treebyid.grid(column=1, row=8, padx=0, pady=5)


# ======================================================================================================================
# event func
def event_update():
    global delevenup

    def delevenup():
        root.destroy()

    root = Tk()
    root.geometry('1280x720')
    root.configure(background='light blue')
    root.title('Event Update')
    window_name_frame = Frame(root, bg='grey', borderwidth=4, border=10, background='teal')
    view_frame = Frame(root)
    name_frame_label = Label(window_name_frame, text="Event Update", font='Calibre 20')
    window_name_frame.grid(column=2, row=2, pady=5, padx=3)
    view_frame.grid(column=4, row=4, pady=5, padx=3)
    name_frame_label.grid(column=1, row=1)
    main_frame = Frame(root, background='grey', borderwidth=4, border=3, bg='teal')
    main_frame.grid(column=1, row=4, padx=4, pady=5, ipadx=4, ipady=4)
    id_label = Label(main_frame, text="Enter Patient ID", font='Calibre 12 bold', width=15, height=1,
                     bd=3,
                     borderwidth=3, border=3, bg='white')
    id_entry = Entry(main_frame, width=17, font='Calibre 13 bold')
    id_label.grid(column=1, row=1)
    id_entry.grid(column=3, row=1)
    event_label = Label(main_frame, text="Enter The Event", font='Calibre 12 bold', width=15, height=1,
                        bd=3,
                        borderwidth=3, border=3, bg='white')
    event_entry = Entry(main_frame, width=17, font='Calibre 13 bold')
    event_date = Label(main_frame, text="Enter Event Date", font='Calibre 12 bold', width=15, height=1,
                       bd=3,
                       borderwidth=3, border=3, bg='white')
    event_date_entry = Entry(main_frame, width=17, font='Calibre 13 bold')
    event_label.grid(column=1, row=2, pady=4, padx=2)
    event_entry.grid(column=3, row=2, pady=4, padx=2)
    event_date_entry.grid(column=3, row=3, pady=4, padx=2)
    event_date.grid(column=1, row=3, pady=4, padx=2)

    def clear():
        event_entry.delete(0, END)
        event_date_entry.delete(0, END)

    def sortord():
        byid(id_entry.get())
        name = byidl[0][1] + str(id_entry.get())
        snocheck(name, 'SNo')

    def event_update_final_add():
        try:
            submit_button1.destroy()
        except:
            pass
        try:
            submit_button2.destroy()
        except:
            pass
        try:
            delall_but.destroy()
        except:
            pass
        sortord()
        byid(id_entry.get())
        name = byidl[0][1] + str(id_entry.get())
        snoval = snoalot(name)

        print(snoval, name)

        query = f"""insert into {name} values({snoval},'{event_entry.get()}','{event_date_entry.get()}')"""
        execute_query(connection, query)

    def event_update_final_update():
        sortord()
        try:
            submit_button2.destroy()
        except:
            pass
        try:
            delall_but.destroy()
        except:
            pass
        byid(id_entry.get())
        name = byidl[0][1] + str(id_entry.get())
        sno_label = Label(main_frame, text='Enter Event No.', font='Calibre 12 bold', width=15, height=1,
                          bd=3,
                          borderwidth=3, border=3, bg='white')
        sno_entry = Entry(main_frame, width=17, font='Calibre 13 bold')
        sno_entry.grid(column=3, row=20, pady=4, padx=2)
        sno_label.grid(column=1, row=20, pady=4, padx=2)
        event = event_entry.get()
        event_dateval = event_date_entry.get()
        que = f"""select * from {name}"""
        data = read_query(connection, que)
        if event == '':
            event = data[0][1]
        if event_dateval == '':
            event_dateval = data[0][2]

        def run_update():
            query = f"""update {name}
                        set event = '{event}',event_date ='{event_dateval}'
                        where SNo={sno_entry.get()};"""
            execute_query(connection, query)

        global submit_button1
        submit_button1 = Button(main_frame, text='Process', width=10, height=1, command=run_update, font='calibri 12')
        submit_button1.grid(column=2, row=23, padx=3)

    def event_update_final_delete():
        try:
            submit_button1.destroy()
        except:
            pass
        byid(id_entry.get())
        name = byidl[0][1] + str(id_entry.get())
        sno_label = Label(main_frame, text='Enter Event No.', font='Calibre 12 bold', width=15, height=1,
                          bd=3,
                          borderwidth=3, border=3, bg='white')
        sno_entry = Entry(main_frame, width=17, font='Calibre 13 bold')
        sno_entry.grid(column=3, row=20, pady=4, padx=2)
        sno_label.grid(column=1, row=20, pady=4, padx=2)

        def run_delete():
            que = f"""delete from {name} where SNo = {sno_entry.get()}"""
            execute_query(connection, que)

        def delall():
            execute_query(connection, f'delete from {name} ')

        global submit_button2
        submit_button2 = Button(main_frame, text='Delete', width=10, height=1, command=run_delete, font='calibri 12')
        submit_button2.grid(column=2, row=24, padx=6, pady=4)
        global delall_but
        delall_but = Button(main_frame, text='Delete All records', command=delall)
        delall_but.grid(column=2, row=25, padx=6, pady=4)

    radio = IntVar()
    R1 = Radiobutton(main_frame, text="ADD   ", variable=radio, value=1, font=14, command=event_update_final_add)
    R1.grid(column=1, row=10, pady=4, padx=2)

    R2 = Radiobutton(main_frame, text="Delete ", variable=radio, value=2, font=14, command=event_update_final_delete)
    R2.grid(column=1, row=11, pady=4, padx=2)

    R3 = Radiobutton(main_frame, text="Update", variable=radio, value=3, font=14, command=event_update_final_update)
    R3.grid(column=1, row=12, pady=4, padx=3)

    # ----------------Submit button -------------

    # ----------------Clear button -------------
    clear_button = Button(main_frame, command=clear, width=10, height=1, text='Next Record', font='calibri 12')
    clear_button.grid(column=3, row=7, pady=5, padx=2)

    def viewdata(frame=view_frame):
        try:
            submit_button1.destroy()
        except:
            pass
        try:
            submit_button2.destroy()
        except:
            pass
        try:
            delall_but.destroy()
        except:
            pass
        sortord()
        byid(id_entry.get())
        name = byidl[0][1] + str(id_entry.get())
        from tkinter import ttk
        patient_event = []

        def byidviewup():
            patient_event.clear()
            query = f"""select * from {name}"""
            data = read_query(connection, query)
            for i in data:
                i = list(i)
                patient_event.append(i)

        byidviewup()

        # Create an instance of tkinter frame
        # Create an object of Style widget
        style = ttk.Style(root)
        style.configure('Treeview', rowheight=30)
        style.theme_use('clam')
        style.configure('.', font=("None", 14))
        # Add a Treeview widget
        tree2 = ttk.Treeview(frame,
                             column=("SNo", "Event Name", "Event Date"),
                             show='headings',
                             height=14)
        tree2.column("# 1", anchor=CENTER, stretch=NO, width=150)
        tree2.heading("# 1", text="SNo")
        tree2.column("# 2", anchor=CENTER, stretch=NO, width=300)
        tree2.heading("# 2", text="Event Name")
        tree2.column("# 3", anchor=CENTER, stretch=NO, width=180)
        tree2.heading("# 3", text="Event Date")
        # Insert the data in Treeview widget
        for rows in patient_event:
            tree2.insert('', 'end', text="2", values=(rows[0], rows[1], rows[2]))

        tree2.grid(column=1, row=3, padx=5, pady=3)

    R4 = Radiobutton(main_frame, text="View Data", variable=radio, value=4, font=14, command=viewdata)
    R4.grid(column=1, row=14, pady=4, padx=2)

    root.mainloop()


# ------------------------------------------------Update Function-------------------------------------------------------
def update():
    global delupd

    def delupd():
        root.destroy()

    root = Tk()
    root.title("Update Record")

    root.configure(background='light blue')
    root.geometry('400x400')
    main_frame = Frame(root, background='grey', borderwidth=4, border=3, bg='teal')
    window_name_frame = Frame(root, bg='grey', borderwidth=4, border=10, background='teal')
    window_name_frame.grid(column=1, row=1, padx=20, pady=3)
    # window name
    window_name_label = Label(window_name_frame, text='Update Record', width=17, height=2, font='Times 15', bd=2)
    window_name_label.grid(column=1, row=1)

    # window name
    # --------------------- entry widgets ----------------------------------------
    # patient_id set
    patient_id_label = Label(main_frame, text='Enter Patient ID', font='Calibre 12 bold', width=15, height=1,
                             bd=3,
                             borderwidth=3, border=3, bg='white')
    patient_id_label.grid(column=3, row=2, padx=3, pady=5)
    patient_id_entry = Entry(main_frame, width=17, font='Calibre 13 bold')
    patient_id_entry.grid(column=5, row=2, padx=2, pady=5)
    # name set
    name_label = Label(main_frame, text='Enter Patient Name', font='Calibre 12 bold', width=15, height=1,
                       bd=3, borderwidth=3, border=3, bg='white')
    name_label.grid(column=3, row=3, padx=3, pady=5)
    name_entry = Entry(main_frame, width=17, font='Calibre 13 bold')
    name_entry.grid(column=5, row=3, padx=2, pady=5)
    # doctor name
    doctor_label = Label(main_frame, text="Enter Doctor's Name", font='Calibre 12 bold', width=15, height=1,
                         bd=3, borderwidth=3, border=3, bg='white')
    doctor_label.grid(column=3, row=4, padx=3, pady=5)
    doctor_entry = Entry(main_frame, width=17, font='Calibre 13 bold')
    doctor_entry.grid(column=5, row=4, padx=2, pady=5)
    # condition
    condition_label = Label(main_frame, text="Enter Diagnosis", font='Calibre 12 bold', width=15, height=1,
                            bd=3, borderwidth=3, border=3, bg='white')
    condition_label.grid(column=3, row=5, padx=3, pady=5)
    condition_entry = Entry(main_frame, width=17, font='Calibre 13 bold')
    condition_entry.grid(column=5, row=5, padx=2, pady=5)

    # admit_date
    admit_date_label = Label(main_frame, text='Enter Admit Date', font='Calibre 12 bold', width=15, height=1,
                             bd=3, borderwidth=3, border=3, bg='white')
    admit_date_label.grid(column=3, row=6, padx=3, pady=5)
    admit_date_entry = Entry(main_frame, width=17, font='Calibre 13 bold')
    admit_date_entry.grid(column=5, row=6, padx=2, pady=5)
    # discharge
    discharge_label = Label(main_frame, text='Enter Patient discharge', font='Calibre 12 bold', width=15, height=1,
                            bd=3, borderwidth=3, border=3, bg='white')
    discharge_label.grid(column=3, row=7, padx=3, pady=5)
    discharge_entry = Entry(main_frame, width=17, font='Calibre 13 bold')
    discharge_entry.grid(column=5, row=7, padx=2, pady=5)

    def clear():
        patient_id_entry.delete(0, END)
        name_entry.delete(0, END)
        doctor_entry.delete(0, END)
        condition_entry.delete(0, END)
        admit_date_entry.delete(0, END)
        discharge_entry.delete(0, END)

    main_frame.grid(column=1, rows=1, pady=5, padx=5)

    def update_final():
        name = name_entry.get()
        doctorn = doctor_entry.get()
        condition = condition_entry.get()
        admit_date = admit_date_entry.get()
        discharge = discharge_entry.get()
        byidl.clear()
        byid(patient_id_entry.get())
        if name == '':
            name = byidl[0][1]
        if doctorn == '':
            doctorn = byidl[0][2]
        if condition == "":
            condition = byidl[0][3]
        if admit_date == '':
            admit_date = byidl[0][4]
        if discharge == '':
            discharge = byidl[0][5]
        if discharge is None:
            query = f"""update patient_main
                    set name = '{name}',doctor_name = '{doctorn}',conditionn = '{condition}',admit_date = '{admit_date}',discharge_date = null
                    where patient_id = {patient_id_entry.get()}; """
        else:
            query = f"""update patient_main
                    set name = '{name}',doctor_name = '{doctorn}',conditionn = '{condition}',admit_date = '{admit_date}',discharge_date = '{discharge}'
                    where patient_id = {patient_id_entry.get()}; """
        execute_query(connection, query)

        # ----------------submit button -------------

    submit_button = Button(main_frame, command=update_final, width=13, height=2, text='Update Record',
                           font='calibri 12')
    submit_button.grid(column=5, row=8, pady=5, padx=2)
    # ----------------Clear button -------------
    clear_button = Button(main_frame, command=clear, width=13, height=2, font='calibri 12', text='Next Record')
    clear_button.grid(column=5, row=9, pady=5, padx=2)

    root.mainloop()


def closeallwin():  # function to close all sub windows
    try:
        addwindowdes()


    except:
        pass
    try:
        delrotf()
    except:
        pass
    try:
        delevenup()

    except:
        pass
    try:
        delupd()
    except:
        pass

# ----------------------------------------------------------------------------------------------------------------------
