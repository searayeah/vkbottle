# HTTP-Client

По-умолчанию библиотека использует `SingleAiohttpClient` для отправки всех запросов.<br />
(Его особенность в том, что он всегда использует одну и ту же сессию.)

## Работа с клиентами

### request_raw

Делает реквест. Для aiohttp возвращает объект `aiohttp.ClientResponse`.

### request_text

Делает реквест и читает поле `text`. Возвращает строковый тип

### request_json

Делает реквест и десериализует `json` с помощью одной из доступных библиотек, выбираются с помощью `choicelib` в порядке слева направо: `json`, `ujson`, `hyperjson`, `orjson`. Возвращает словарь десериализованный из `json`а

### request_content

Делает реквест и читает вернувшийся `content`, используется для скачивания медиафайлов в аплоадерах. Возвращает байты

### Параметры

* `url` - ссылка по которой будет произведен
* `method` - HTTP метод запроса (например: get)
* `data` - данные которые будут переданы в запросе
* `#!python **kwargs` - передаются в качестве параметров в запросе

#### При инициализации `AiohttpClient` можно указать параметры

* `session` - объект сессии (если не указан, то будет создан новый)
* `json_processing_module` - модуль для десериализации json<br />(если не указан, то будет использован [один из доступных модулей](../modules.md))
* `optimize` - если передан True, то в конструктор сессии будут переданы параметры `#!python raise_for_status=True` и `#!python skip_auto_headers={"User-Agent"}`.
* `#!python **session_params` - `#!python **kwargs`, передаются в конструктор сессии.<br />Можно использовать для передачи `headers` или `cookies`

!!! info "Примечание"
    Подробнее обо всех параметрах можно почитать [здесь](https://docs.aiohttp.org/en/stable/client_reference.html).

### Пример

```python
from vkbottle.http import AiohttpClient

# ...
http_client = AiohttpClient()
await http_client.request_text("https://google.com")
```

## Создание кастомного клиента

Кастомный клиент должен унаследовать `ABCHTTPClient` и имплементировать вышеупомянутые методы
