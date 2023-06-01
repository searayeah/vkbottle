import asyncio
import os

from vkbottle.api import API
from vkbottle.exception_factory import VKAPIError

# Load token from system environment variable
# https://12factor.net/config
api = API(os.environ["TOKEN"])


async def main():
    try:
        await api.users.get(user_ids=["123456789"])
    except VKAPIError[5]:
        print("Ой, неверный ключ доступа.")
    except VKAPIError[30]:
        print("Ой, у пользователя закрытый профиль.")
    except VKAPIError as e:
        print(f"Произошла ошибка {e.code}.")


asyncio.run(main())
