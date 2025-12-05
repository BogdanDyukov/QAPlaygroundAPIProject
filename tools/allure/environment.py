import platform
import sys
from config.settings import settings


def create_allure_environment_file():
    settings_dict = settings.model_dump(exclude={"bearer_token"})
    items = [f'{key}={value}' for key, value in settings_dict.items()]

    items.append(f'os_info={platform.system()}, {platform.release()}')
    items.append(f'python_version={sys.version}')
    
    # Собираем все элементы в единую строку с переносами
    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
