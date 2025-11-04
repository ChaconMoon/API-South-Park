"""
Module written by Carlos Chacón.

This module configures the Jinja2 template engine for rendering HTML templates path
in the South Park API website. It sets up the template directory and
provides the templates object for use in web routes.
"""

from fastapi.templating import Jinja2Templates

# Initialize Jinja2 template engine with templates directory
templates = Jinja2Templates(directory="templates")
