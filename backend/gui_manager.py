from components.sortable_column import SortableColumn
from nicegui.elements.column import Column
from nicegui.elements.card import Card
from nicegui.elements.row import Row
from nicegui.element import Element
from nicegui import ui

from typing import Optional
from backend import paths
import re

def extract_css_variables(css_content):
    variables = {}
    
    for match in re.finditer(r'(--[a-zA-Z0-9-_]+):\s*(#[0-9a-fA-F]+);', css_content):
        variables[match.group(1)] = match.group(2)
    
    for match in re.finditer(r'(--[a-zA-Z0-9-_]+):\s*var\((--[a-zA-Z0-9-_]+)\);', css_content):
        if match.group(2) in variables:
            variables[match.group(1)] = variables[match.group(2)]
    
    return variables

def apply_theme_from_css(css_theme):
    try:
        with open(css_theme, 'r', encoding='utf-8') as file:
            css_content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{css_theme}' was not found.")
        return
    
    variables = extract_css_variables(css_content)
    
    color_map = {
        'primary': '--c-primary',
        'secondary': '--c-sky',
        'accent': '--c-mauve',
        'dark': '--c-base',
        'dark_page': '--c-mantle',
        'positive': '--c-green',
        'negative': '--c-red',
        'info': '--c-blue',
        'warning': '--c-yellow'
    }
    
    resolved_colors = {key: variables.get(value) for key, value in color_map.items() if value in variables}
    ui.colors(**resolved_colors)
    

class UIManager:
    def __init__(self) -> None:
        apply_theme_from_css(paths.local_theme_css)
        
        # self.example1: Optional[Card] = None
        # self.example2: SortableColumn[Element] = None
        # self.example3: Optional[Element] = None
        
gui = UIManager()
