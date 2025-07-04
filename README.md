# Screen-sizer

A minimal web application for checking your window and display dimensions.

## Webapp

Open `index.html` directly in a browser, or run the Python helper script to
launch it automatically:

```bash
python3 screen_size.py
```

The page shows your current window size, screen resolution and an approximate
physical display size based on a 96 DPI assumption. Values update as you resize
the browser.

## Python script

When run, `screen_size.py` prints the terminal size and screen resolution (if
available) before opening the web interface.
