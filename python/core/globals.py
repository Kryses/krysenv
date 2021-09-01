from pathlib import Path
import sys
import os

ROOT = Path(__file__).parents[2]
RESOURCES_PATH = ROOT.joinpath('resources')
QT_UI_PATH = RESOURCES_PATH.joinpath('ui')
DEFAULT_STYLESHEET = RESOURCES_PATH.joinpath('scss', 'dark.css')

class InvalidSystemError(Exception):
    pass

if sys.platform == 'win32':
    LOCAL_CONFIGS_LOCATION = Path(os.environ['APPDATA']).joinpath('kryenv')
else:
    raise InvalidSystemError(F'Invalid system provided: {sys.platform}')
LOCAL_PROJECT_LOCATION = LOCAL_CONFIGS_LOCATION.joinpath('projects')