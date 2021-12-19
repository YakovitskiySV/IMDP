from tkinter import Tk

def create_window():
    """creates window object"""
    root = Tk()
    root.title =("Модель складской базы")
    root.geometry("400x400")
    root.resizable(width=True, height=True)

    return root

