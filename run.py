# run.py - вспомогательный скрипт для установки переменных
import os
import subprocess
import sys

# Получаем абсолютный путь к .env файлу
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, 'src', '.env')

print(f"Looking for .env file at: {env_path}")

# Словарь для хранения переменных
env_vars = {}

# Читаем .env файл
try:
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip("'").strip('"')
                    env_vars[key] = value
                    print(f"Set {key}={value}")

    print("Environment variables loaded successfully")
except FileNotFoundError:
    print(f"ERROR: .env file not found at {env_path}")
    exit(1)
except Exception as e:
    print(f"ERROR reading .env file: {e}")
    exit(1)

# Проверяем, что все необходимые переменные есть
required_vars = ['SMTP_SERVER', 'SMTP_PORT', 'SMTP_EMAIL', 'SMTP_EMAIL_PASSWORD']
missing_vars = [var for var in required_vars if var not in env_vars]
if missing_vars:
    print(f"ERROR: Missing required variables: {missing_vars}")
    exit(1)

print("\n=== ENVIRONMENT VARIABLES TO BE PASSED ===")
for key, value in env_vars.items():
    if key == 'SMTP_EMAIL_PASSWORD':
        print(f"{key}=******")
    else:
        print(f"{key}={value}")

# Создаем новое окружение для дочернего процесса
new_env = os.environ.copy()
new_env.update(env_vars)

# Запускаем основную программу с обновленным окружением
print("\n=== RUNNING MAIN PROGRAM ===")
script_path = os.path.join(current_dir, 'src', 'task_7.py')
result = subprocess.run([sys.executable, script_path], env=new_env)
sys.exit(result.returncode)