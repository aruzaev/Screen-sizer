# Screen-sizer

This repository now includes a small web page for viewing your screen size in the browser, along with the original Python script.

## Website Usage

Open `index.html` directly in your browser or serve it with a simple HTTP server:

```bash
python3 -m http.server
```

Navigate to `http://localhost:8000` and the page will display your current window size and screen resolution. Resize the browser window to see the values update.

## Python Script

You can still run the command-line script if you prefer:

```bash
python3 screen_size.py
```

The script prints the terminal size and, if Tkinter can access your display, the screen resolution.
