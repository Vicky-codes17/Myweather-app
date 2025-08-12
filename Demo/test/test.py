import sys
import os
from pathlib import Path

def get_asset_path(filename):
    """Get the correct path for assets whether running as script or executable"""
    if getattr(sys, 'frozen', False):
        # Running as PyInstaller executable
        base_path = Path(sys.executable).parent
    else:
        # Running as script
        base_path = Path(__file__).parent.parent
    
    # Try different locations
    for folder in ['assets', 'build']:
        asset_path = base_path / folder / filename
        if asset_path.exists():
            return str(asset_path)
    
    # Fallback to original path
    return filename

# Use in your code like:
# image_path = get_asset_path("background.png")
# photo = PhotoImage(file=image_path)