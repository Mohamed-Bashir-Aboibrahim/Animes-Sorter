import os
import tkinter as tk
import re
from tkinter import filedialog , messagebox

from test import browse_btn, rename_btn


def sorting(folder):
    extensions=['.mp4', '.mkv', '.avi']
    files=[]
    for filename in os.listdir(folder):
        fullpath=os.path.join(folder, filename)
        if os.path.isfile(fullpath) and os.path.splitext(filename)[1].lower() in extensions:
            files.append((fullpath , os.path.getctime(fullpath)))
    files.sort(key=lambda x:x[1])
    return [f[0] for f in files]
def browsing():
    selected_folder=filedialog.askdirectory()
    if selected_folder:
        folder_var.set(selected_folder)
def renamer():
    folder=folder_var.get()
    the_name=name_var.get().strip()
    the_name=re.sub(r'[<>:"/\\|?*]', '', the_name)
    if not folder or not the_name:
        messagebox.showerror("Error", "Please choose folder and name.")
        return
    try:
        files = sorting(folder)
        if not files:
            status_var.set("No videos were found.")
            return
        if not messagebox.askyesno("Are you sure that you want to", f"Rename {len(files)} files?"):
            return
        for i, file in enumerate(files, start=1):
            ch=os.path.split(file)[-1]
            rename=f"{the_name} {i:02}{ch}"
            renamed_path=os.path.join(folder, rename)
            os.rename(file, renamed_path)
        status_var.set("All Videos were renamed successfully.")
    except Exception as e:
        messagebox.showerror("Something went wrong", str(e))
        status_var.set("an error occurred")
root=tk.Tk()
root.title("Anime renamer App")
root.geometry("600*300")
root.configure(bg="#fff8e1")
header_font = ("Segoe UI", 32, "bold")
text_font=("Segoe UI", 20, "bold")
folder_var=tk.StringVar()
name_var=tk.StringVar()
status_var=tk.StringVar()
tk.Label(root , text="Anime folder:",  font=text_font , bg="#fff8e1").place(x=40, y=40)
tk.Entry(root, textvariable=folder_var, font=text_font, width=45).place(x=150, y=40)
browse_btn = tk.Button(root, text="Browse", command=browse_btn, font = text_font, bg = "#b3e5fc", activebackground = "#81d4fa", relief = "flat")
browse_btn.place(x=480, y=36)
tk.Label(root, text="Enter anime name:", font=text_font, bg="#fff8e1").place(x=40, y=90)
tk.Entry(root, textvariable=name_var, font=text_font, width=40).place(x=150, y=90)
rename_btn = tk.Button(root, text="Rename Files", command=renamer, font=header_font, bg="#d1c4e9", activebackground="#b39ddb", relief="flat", fg="black")
rename_btn.place(relx=0.5, y=160, anchor="center")
tk.Label(root, textvariable=status_var, font=text_font, bg="#fff8e1", fg="#444").place(relx=0.5, y=210, anchor="center")
def on_enter(e): e.widget.config(bg="#b39ddb")
def on_leave(e): e.widget.config(bg="#d1c4e9")
rename_btn.bind("<Enter>", on_enter)
rename_btn.bind("<Leave>", on_leave)
root.mainloop()




