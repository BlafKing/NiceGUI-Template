import os, shutil

project_name = "PLACEHOLDER"

main_dir = os.path.dirname(os.path.dirname(__file__))
components_dir = os.path.join(main_dir, "components")
gui_dir = os.path.join(main_dir, "gui")
icons_dir = os.path.join(main_dir, "icons")
static_dir = os.path.join(main_dir, "static")


font_dir = os.path.join(static_dir, "font")
font_metropolis = os.path.join(font_dir, "Metropolis")
static_theme_css = os.path.join(static_dir, "theme.css")

exe_dir = os.path.dirname(main_dir)

# ---------------------------------------------------------- #

user_local = os.getenv("LOCALAPPDATA")
app_data_dir = os.path.join(user_local, project_name)

theme_dir = os.path.join(app_data_dir, "theme")
local_theme_css = os.path.join(theme_dir, "theme.css")


# ---------------------------------------------------------- #

if not os.path.exists(app_data_dir):
    os.makedirs(app_data_dir)
    
if not os.path.exists(theme_dir):
    os.makedirs(theme_dir)

if not os.path.exists(local_theme_css):
    shutil.copy(static_theme_css, local_theme_css)
