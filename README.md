# Screen-sizer

This repository provides a simple tool to report the size of your terminal or browser window. Originally it included only a Python script, but you can now view the information directly in your browser using the included web page.

## Usage

Run the script using Python:

```bash
python3 screen_size.py
```

The script will output the terminal size and, if Tkinter can access your display, the screen resolution.

## Website

Open `index.html` in any modern web browser. The page will display the current
window size and your screen's resolution. Resizing the browser window updates
the values automatically.
