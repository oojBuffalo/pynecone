"""Base file for constants that don't fit any other categories."""

from __future__ import annotations

import os
import platform
from enum import Enum
from importlib import metadata
from types import SimpleNamespace

from platformdirs import PlatformDirs

IS_WINDOWS = platform.system() == "Windows"


class Dirs(SimpleNamespace):
    """Various directories/paths used by Reflex."""

    # The frontend directories in a project.
    # The web folder where the NextJS app is compiled to.
    WEB = ".web"
    # The name of the assets directory.
    APP_ASSETS = "assets"
    # The name of the assets directory for external ressource (a subfolder of APP_ASSETS).
    EXTERNAL_APP_ASSETS = "external"
    # The name of the utils file.
    UTILS = "utils"
    # The name of the output static directory.
    STATIC = "_static"
    # The name of the public html directory served at "/"
    PUBLIC = "public"
    # The name of the state file.
    STATE_PATH = "/".join([UTILS, "state"])
    # The name of the components file.
    COMPONENTS_PATH = "/".join([UTILS, "components"])
    # The name of the contexts file.
    CONTEXTS_PATH = "/".join([UTILS, "context"])
    # The directory where the app pages are compiled to.
    WEB_PAGES = os.path.join(WEB, "pages")
    # The directory where the static build is located.
    WEB_STATIC = os.path.join(WEB, STATIC)
    # The directory where the utils file is located.
    WEB_UTILS = os.path.join(WEB, UTILS)
    # The directory where the assets are located.
    WEB_ASSETS = os.path.join(WEB, PUBLIC)
    # The env json file.
    ENV_JSON = os.path.join(WEB, "env.json")
    # The reflex json file.
    REFLEX_JSON = os.path.join(WEB, "reflex.json")
    # The path to postcss.config.js
    POSTCSS_JS = os.path.join(WEB, "postcss.config.js")


class Reflex(SimpleNamespace):
    """Base constants concerning Reflex."""

    # App names and versions.
    # The name of the Reflex package.
    MODULE_NAME = "reflex"
    # The current version of Reflex.
    VERSION = metadata.version(MODULE_NAME)

    # The reflex json file.
    JSON = os.path.join(Dirs.WEB, "reflex.json")

    # Files and directories used to init a new project.
    # The directory to store reflex dependencies.
    # Get directory value from enviroment variables if it exists.
    _dir = os.environ.get("REFLEX_DIR", "")

    DIR = _dir or (
        # on windows, we use C:/Users/<username>/AppData/Local/reflex.
        # on macOS, we use ~/Library/Application Support/reflex.
        # on linux, we use ~/.local/share/reflex.
        # If user sets REFLEX_DIR envroment variable use that instead.
        PlatformDirs(MODULE_NAME, False).user_data_dir
    )
    # The root directory of the reflex library.

    ROOT_DIR = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )


class ReflexHostingCLI(SimpleNamespace):
    """Base constants concerning Reflex Hosting CLI."""

    # The name of the Reflex Hosting CLI package.
    MODULE_NAME = "reflex-hosting-cli"


class Templates(SimpleNamespace):
    """Constants related to Templates."""

    # The route on Reflex backend to query which templates are available and their URLs.
    APP_TEMPLATES_ROUTE = "/app-templates"

    # The default template
    DEFAULT = "blank"

    class Dirs(SimpleNamespace):
        """Folders used by the template system of Reflex."""

        # The template directory used during reflex init.
        BASE = os.path.join(Reflex.ROOT_DIR, Reflex.MODULE_NAME, ".templates")
        # The web subdirectory of the template directory.
        WEB_TEMPLATE = os.path.join(BASE, "web")
        # The jinja template directory.
        JINJA_TEMPLATE = os.path.join(BASE, "jinja")
        # Where the code for the templates is stored.
        CODE = "code"


class Next(SimpleNamespace):
    """Constants related to NextJS."""

    # The NextJS config file
    CONFIG_FILE = "next.config.js"
    # The sitemap config file.
    SITEMAP_CONFIG_FILE = os.path.join(Dirs.WEB, "next-sitemap.config.js")
    # The node modules directory.
    NODE_MODULES = "node_modules"
    # The package lock file.
    PACKAGE_LOCK = "package-lock.json"
    # Regex to check for message displayed when frontend comes up
    FRONTEND_LISTENING_REGEX = "Local:[\\s]+(.*)"


# Color mode variables
class ColorMode(SimpleNamespace):
    """Constants related to ColorMode."""

    NAME = "colorMode"
    USE = "useColorMode"
    TOGGLE = "toggleColorMode"


# Env modes
class Env(str, Enum):
    """The environment modes."""

    DEV = "dev"
    PROD = "prod"


# Log levels
class LogLevel(str, Enum):
    """The log levels."""

    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

    def __le__(self, other: LogLevel) -> bool:
        """Compare log levels.

        Args:
            other: The other log level.

        Returns:
            True if the log level is less than or equal to the other log level.
        """
        levels = list(LogLevel)
        return levels.index(self) <= levels.index(other)


# Server socket configuration variables
POLLING_MAX_HTTP_BUFFER_SIZE = 1000 * 1000


class Ping(SimpleNamespace):
    """PING constants."""

    # The 'ping' interval
    INTERVAL = 25
    # The 'ping' timeout
    TIMEOUT = 120


# Keys in the client_side_storage dict
COOKIES = "cookies"
LOCAL_STORAGE = "local_storage"

# If this env var is set to "yes", App.compile will be a no-op
SKIP_COMPILE_ENV_VAR = "__REFLEX_SKIP_COMPILE"

# This env var stores the execution mode of the app
ENV_MODE_ENV_VAR = "REFLEX_ENV_MODE"

# Testing variables.
# Testing os env set by pytest when running a test case.
PYTEST_CURRENT_TEST = "PYTEST_CURRENT_TEST"
RELOAD_CONFIG = "__REFLEX_RELOAD_CONFIG"

REFLEX_VAR_OPENING_TAG = "<reflex.Var>"
REFLEX_VAR_CLOSING_TAG = "</reflex.Var>"
