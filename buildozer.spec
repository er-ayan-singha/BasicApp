[app]
# (str) Title of your application
title = My Application

# (str) Package name (use lowercase, no spaces or special characters)
package.name = myapp

# (str) Package domain (reverse domain name style)
package.domain = org.example

# (str) Source code directory (default is '.')
source.dir = .

# (list) List of inclusions by extension
source.include_exts = py,png,jpg,kv,atlas,ttf,otf,wav,mp3,ini,txt,json,pdf

# (str) Application versioning
version = 1.0.0

# (str) Automatically extract version from main.py
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (str) Application entry point
entrypoint = main.py

# (list) Supported orientation (portrait, landscape, sensor, all)
orientation = portrait

# (bool) Fullscreen mode (1 = Yes, 0 = No)
fullscreen = 0

# (list) Application icon(s)
icon.filename = %(source.dir)s/icon.png

# (list) Presplash image
presplash.filename = %(source.dir)s/presplash.png

# (str) Supported languages
osx.kivy_language = en

# (list) Requirements: comma-separated Python modules
requirements = python3, kivy, pillow, reportlab

# (str) Custom source folders to include (separate by comma)
#source.include_patterns = assets/*,images/*

# (list) Permissions for Android app
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Android API level (you must have it installed)
android.api = 31

# (int) Minimum supported Android API
android.minapi = 21

# (int) Targeted Android API (set same as android.api for best results)
android.target = 31

# (str) NDK version to use
android.ndk = 23b

# (int) Android NDK API level
android.ndk_api = 21

# (bool) Enable Android X support
android.enable_androidx = True

# (list) Add any Java .jar files to include
#android.add_jars = path/to/yourlib.jar

# (list) Android AAR libraries
#android.add_aars = path/to/yourlib.aar

# (bool) Hide status bar
android.hide_statusbar = False

# (list) Screens to support
android.supported_screens = small,normal,large,xlarge

# (str) Entry point for service (optional)
#android.service = myservice.py

# (bool) Launch app with service (e.g., background task)
#android.start_service = False

# (bool) Package as android App Bundle (Google Play Store format)
android.build_type = release

# (bool) Auto accept SDK licenses
android.accept_sdk_license = True

# (str) Architecture (armeabi-v7a, arm64-v8a, x86, x86_64)
android.arch = armeabi-v7a

# (bool) Enable logcat on device when launching
log_level = 2

# (str) Path to keystore for signing release APK
#android.keystore = mykeystore.keystore
#android.keyalias = mykey
#android.keyalias_password = password
#android.keystore_password = password

# (str) iOS deployment target version (iOS only)
ios.min_version = 12.0

# (str) iOS archs (iOS only)
ios.archs = arm64

# (list) iOS frameworks to include (iOS only)
#ios.frameworks = Metal, UIKit

# (bool) Code obfuscation (Python files only)
#android.obfuscate = True

# (bool) Include *.pyo files (Python optimized bytecode)
#android.include_pyo = False

# (bool) Compress app (speeds up installation)
#android.compress = True

# (str) Custom build directory
#build_dir = ./build

[buildozer]
# (str) Log level (0 = error, 1 = warning, 2 = info, 3 = debug, 4 = trace)
log_level = 2

# (bool) Whether to warn about running as root
warn_on_root = 1

# (str) Buildozer global cache directory
#build_cache_dir = ~/.buildozer_cache
