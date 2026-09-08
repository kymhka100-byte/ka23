[app]

# (str) Title of your application
title = 가위바위보 게임

# (str) Package name
package.name = rpsgame

# (str) Package domain (needed for android/ios packaging)
package.domain = com.game

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,wav,ttf,otf,ttc

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# code 내 파이썬 모듈 및 Kivy 빌드에 필요한 최소 단위 지정
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# 오디오 재생 및 외부 파일 저장을 위한 권한
permissions = INTERNET, RECORD_AUDIO

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.accept_sdk_license = True

# (str) Android entry point, default is ok
# main.py가 진입점입니다.
android.entrypoint = org.kivy.android.PythonActivity

# (list) List of Java .jar files to add to the libs
# android.add_jars = foo.jar

# (list) List of Java files to add to the project (e.g. com/android/GcmIntentService.java)
# android.add_src =

# (list) Android AAR archives to add
# android.add_aars =

# (list) Gradle dependencies to add
# android.gradle_dependencies =

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) Architectures to build for
# 최신 안드로이드 휴대폰 대부분(arm64-v8a)과 가상머신/구형기기(armeabi-v7a) 대응
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow code signing
# android.skip_update = False

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab)
# bin_dir = ./bin

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v3
      with:
        name: app-release
        path: bin/*.apk

