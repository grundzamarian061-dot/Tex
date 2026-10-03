[app]
title = T.Ex Detective
package.name = texdetective
package.domain = org.tex
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf,txt
version = 7.7.30

# Pure-python balíčky jdou přes pip, ffpyplayer/kivy/pillow mají recepty
requirements = python3,kivy==2.3.0,pyjnius,android,plyer,requests,urllib3,idna,certifi,charset-normalizer,pillow,ffpyplayer,pypdf,yt-dlp

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE,CAMERA,RECORD_AUDIO,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO,VIBRATE,WAKE_LOCK,QUERY_ALL_PACKAGES

android.api = 33
android.minapi = 24
android.archs = arm64-v8a
android.accept_sdk_license = True
android.enable_androidx = True
android.release_artifact = apk

# ikonka (volitelné): nahraj icon.png vedle main.py a odkomentuj
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 0
