from tkinter import *
from tkinter import ttk



def get_query(*args):
    try:
        errmsg.set("")
        value = float(event_list.get())
        sql_nc_bss_query.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        errmsg.set("Error Message : "+event_env.get())
        pass

root = Tk()
root.title("Catch UP QA helper")

mainframe = ttk.Frame(root ,padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


event_env = StringVar()
event_env_select = ttk.Combobox(mainframe, textvariable=event_env)
event_env_select.state(["readonly"])
event_env_select.set("MRE")
event_env_select['values'] = ('MRE', 'PRD', 'UAT')
event_env_select.grid(column=2, row=1, sticky=(N, W, E, S))

event_list = StringVar()
event_list_entry = ttk.Entry(mainframe, width=40,textvariable=event_list)
event_list_entry.grid(column=2, row=2, sticky=(N, W, E, S))

sql_nc_bss_query = StringVar()
sql_nc_bss_sql = ttk.Entry(mainframe, width=40, textvariable=sql_nc_bss_query)
sql_nc_bss_sql.grid(column=2, row=3, sticky=(N, W, E, S))

sql_nc_bss_out = StringVar()
sql_nc_bss_output = ttk.Entry(mainframe, width=40, textvariable=sql_nc_bss_out)
sql_nc_bss_output.grid(column=2, row=4, sticky=(N, W, E, S))

sql_nc_qsm = StringVar()
sql_nc_qsm_output = ttk.Entry(mainframe, width=40, textvariable=sql_nc_qsm)
sql_nc_qsm_output.grid(column=2, row=5, sticky=(N, W, E, S))

sql_nc_link = StringVar()
sql_nc_bss_link = ttk.Entry(mainframe, width=40, textvariable=sql_nc_link)
#sql_nc_link.set("sql_nc_link")
sql_nc_bss_link.grid(column=2, row=6, sticky=(N, W, E, S))

ttk.Label(mainframe, text="Set Environment").grid(column=1, row=1, sticky=(N, W, E, S))
ttk.Label(mainframe, text="Copy&Past Event").grid(column=1, row=2, sticky=(N, W, E, S))
ttk.Button(mainframe, text="Generate SQL NC.BSS", command=get_query).grid(column=1, row=3, sticky=(N, W, E, S))
ttk.Label(mainframe, text="Copy&Past SQL output").grid(column=1, row=4, sticky=(N, W, E, S))
ttk.Button(mainframe, text="Generate SQL QSM & Link", command=get_query).grid(column=1, row=5, sticky=(N, W, E, S))

errmsg = StringVar()
msg = ttk.Label(mainframe, font='TkSmallCaptionFont', foreground='red', textvariable=errmsg)
msg.grid(column=1, row=6, padx=5, pady=5, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

event_env_select.focus()
root.bind("<Return>", get_query)

root.mainloop()



