[app]

# Application details
title = Calculator
package.name = calculator
package.domain = org.kivy
source.dir = .
source.include_exts = py,kv,png,jpg,kv
version = 1.0
requirements = kivy

# Orientation and features
orientation = portrait
fullscreen = 0

# Presplash and icon (optional)
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

# Supported screens
android.archs = armeabi-v7a, arm64-v8a

# NDK, API, and build tools
android.ndk = 23b
android.api = 33
android.build_tools = 33.0.2

# Entry point
entrypoint = main.py

# Logging and packaging
log_level = 2
android.logcat_filters = *:S python:D

# Permissions (add if needed)
# android.permissions = INTERNET

# Include .kv files
include_exts = py, kv

# Other options
copy_libs = 1

# Don't include unnecessary files
exclude_dirs = tests, bin, venv

# Keep original .py files in APK
android.keep_build_dir = 0

# Avoid stripping binaries (optional for debugging)
# android.strip = false

# Don't use AndroidX unless needed
# android.enable_androidx = 0

# Optional: specify custom Java version
# android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
