import re, os, sys
from nicegui import ui, app
from backend import paths

#                          SETUP                        #
# ----------------------------------------------------- #

def get_css_color(variable: str) -> str:
    with open(paths.local_theme_css, "r", encoding="utf-8") as file:
        css_content = file.read()
    
    variables = dict(re.findall(r"(--[a-zA-Z0-9-]+):\s*([^;]+);", css_content))
    def resolve_variable(value):
        match = re.match(r"var\((--[a-zA-Z0-9-]+)\)", value.strip())
        if match:
            ref_var = match.group(1)
            return resolve_variable(variables.get(ref_var, "#000000"))
        return value.strip()
    
    return resolve_variable(variables.get(variable, "#000000"))

background_color = get_css_color("--c-mantle")
main_color = get_css_color("--c-lavender")

def load_svg(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

loading_html = f"""
    <style>
        body {{ height: 100%; width: 100%; position: fixed; display: flex; justify-content: center; align-items: center;
                flex-direction: column; background-color: {background_color}; color: {main_color}; margin: 0px; gap: 3em; }}
        .loader {{ width: 50px; height: 50px; border: 5px solid {main_color}; border-top: 5px solid transparent;
                border-radius: 50%; animation: spin 1.5s linear infinite; }}
        .logo {{ height: 200px; }}
        @keyframes spin {{ 100% {{ transform: rotate(360deg); }} }}
    </style>
    <body>
        {load_svg(os.path.join(paths.icons_dir, "app-icon.svg"))}
        <div class="loader"></div>
    </body>
"""


app.native.window_args = {
    'background_color': background_color,
    'html': loading_html
}

if not getattr(sys, 'frozen', False):
    app.native.start_args['debug'] = True
    app.native.start_args['private_mode'] = False
    app.native.start_args['storage_path'] = False
    app.native.settings['OPEN_DEVTOOLS_IN_DEBUG'] = False

app.add_static_files(f'/static', paths.static_dir)
app.add_static_files(f'/theme', paths.theme_dir)

for root, _, files in os.walk(paths.static_dir):
    for file in files:
        rel_path = os.path.relpath(os.path.join(root, file), paths.static_dir).replace("\\", "/")
        if file.endswith(".js"):
            ui.add_head_html(f'<script src="/static/{rel_path}"></script>', shared=True)
        elif file.endswith(".css") and file != "theme.css":
            ui.add_head_html(f'<link rel="stylesheet" type="text/css" href="/static/{rel_path}">', shared=True)

ui.add_head_html(f'<link rel="stylesheet" type="text/css" href="/theme/theme.css">', shared=True)

run_args = {
    'title': paths.project_name,
    'dark': True,
    'reload': False,
    'native': True
}

# ----------------------------------------------------- #


#                      UI CREATION                      #
# ----------------------------------------------------- #

with ui.column().classes("h-full w-full"):
    ui.label("Example")
        

ui.run(**run_args)
