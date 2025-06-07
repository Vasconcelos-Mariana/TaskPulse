
def center_window(width: int, height: int) -> str:
    screen_width = 800  # Default fallback
    screen_height = 600

    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Oculta a janela temporária
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.destroy()
    except:
        pass

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    return f"{width}x{height}+{x}+{y}"
