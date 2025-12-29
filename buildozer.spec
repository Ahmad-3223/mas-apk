[app]
# Название твоего приложения
title = MAS Translator
# Имя пакета (без пробелов, только латиница)
package.name = mastranslator
# Домен (можно оставить так)
package.domain = org.test
# Папка с кодом (точка означает текущую папку)
source.dir = .
# Расширения файлов, которые нужно включить в APK
source.include_exts = py,png,jpg,kv,atlas
# Версия
version = 0.1

# ВАЖНО: Список библиотек. Мы используем чистый Kivy для стабильности
requirements = python3,kivy==2.3.0

# Ориентация экрана
orientation = portrait

# Разрешения (нужны для доступа в интернет, если будешь расширять)
android.permissions = INTERNET

# Архитектура (для большинства современных телефонов)
android.archs = arm64-v8a

# Настройки системы (лучше не менять)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1