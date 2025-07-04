import os
import webbrowser

try:
    from tkinter import Tk
except Exception:
    Tk = None


def get_terminal_size():
    try:
        return os.get_terminal_size()
    except OSError:
        return None


def get_screen_size():
    if Tk is None:
        return None
    try:
        root = Tk()
        root.withdraw()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.destroy()
        return width, height
    except Exception:
        return None


def main():
    term = get_terminal_size()
    screen = get_screen_size()

    if term:
        print(f"Terminal size: {term.columns}x{term.lines}")
    else:
        print("Terminal size: unavailable")

    if screen:
        width, height = screen
        print(f"Screen resolution: {width}x{height}")
    else:
        print("Screen resolution: unavailable")

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
    webbrowser.open("file://" + path)
    print("Launching web interface...")


if __name__ == "__main__":
    main()
