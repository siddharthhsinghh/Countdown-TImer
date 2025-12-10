import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.time_left = 0
        self.is_paused = False

        # -------- UI Components -------- #
        tk.Label(root, text="Countdown Timer", font=("Arial", 16)).pack(pady=10)

        frame = tk.Frame(root)
        frame.pack()

        tk.Label(frame, text="Minutes:").grid(row=0, column=0)
        self.min_entry = tk.Entry(frame, width=5)
        self.min_entry.grid(row=0, column=1)

        tk.Label(frame, text="Seconds:").grid(row=1, column=0)
        self.sec_entry = tk.Entry(frame, width=5)
        self.sec_entry.grid(row=1, column=1)

        self.display = tk.Label(root, text="00:00", font=("Arial", 28))
        self.display.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Start", width=7, command=self.start).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Pause", width=7, command=self.pause).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Reset", width=7, command=self.reset).grid(row=0, column=2, padx=5)

    # ---------- FUNCTIONALITY ---------- #

    def start(self):
        """Start the countdown."""
        if self.time_left == 0:
            try:
                mins = int(self.min_entry.get())
                secs = int(self.sec_entry.get())
                self.time_left = mins * 60 + secs
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers!")
                return
        
        self.is_paused = False
        self.countdown()

    def countdown(self):
        """Recursive countdown functionality."""
        if self.time_left > 0 and not self.is_paused:
            mins = self.time_left // 60
            secs = self.time_left % 60
            self.display.config(text=f"{mins:02d}:{secs:02d}")

            self.time_left -= 1
            self.root.after(1000, self.countdown)
        elif self.time_left == 0:
            self.display.config(text="00:00")
            messagebox.showinfo("Time Up", "Countdown finished!")

    def pause(self):
        """Pause the timer."""
        self.is_paused = True

    def reset(self):
        """Reset everything."""
        self.is_paused = True
        self.time_left = 0
        self.display.config(text="00:00")
        self.min_entry.delete(0, tk.END)
        self.sec_entry.delete(0, tk.END)


# ------------ RUN APP ------------ #
if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
