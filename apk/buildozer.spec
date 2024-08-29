[app]
# (str) Title of your application
title = Audio Client

# (str) Package name
package.name = audioclient

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Application versioning (must be a string)
version = 0.1

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO

# (list) Application requirements
# Comma-separated list of requirements. 
# For example: requirements = python3,kivy
requirements = python3, kivy, jnius

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png
