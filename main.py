import tkinter as tk
import pyautogui # Added import

# Define the typing function
def start_typing_action(text_widget, status_var):
    text_to_type = text_widget.get()
    if text_to_type:
        status_var.set("Focus the target window... Typing in 3 seconds...")
        window.update_idletasks() # Ensure label updates immediately
        pyautogui.sleep(3) 
        
        status_var.set("Typing...")
        window.update_idletasks() # Ensure label updates immediately
        pyautogui.typewrite(text_to_type, interval=0.05)
        status_var.set("Done!")
    else:
        status_var.set("Please enter text to type.")

# Declare window globally so it can be accessed by start_typing_action for update_idletasks
window = None 

def main():
    global window # Declare that we are using the global window variable
    # Create the main window
    window = tk.Tk()
    window.title("AutoTyper")

    # Create the text input area
    text_input = tk.Entry(window, width=50)
    text_input.pack(pady=10)

    # Create the "Start Typing" button
    # status_var will be created below, need to ensure it's passed to the lambda
    status_var = tk.StringVar()
    status_var.set("Ready") # Initial status message
    
    start_button = tk.Button(window, text="Start Typing", command=lambda: start_typing_action(text_input, status_var))
    start_button.pack(pady=5)

    # Create the status label
    status_label = tk.Label(window, textvariable=status_var)
    status_label.pack(pady=5)

    # Start the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main()
