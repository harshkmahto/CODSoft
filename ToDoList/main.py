import os
import tkinter as tk
from tkinter import ttk, messagebox
import json

class ModernTodo:
    def __init__(self, master):
          self.master = master
          self.master.title("Modern To-Do List")
          self.master.geometry("400x500")
          self.master.configure(bg="#f0f0f0")
          
          