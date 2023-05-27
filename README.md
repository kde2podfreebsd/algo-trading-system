# 🤖💰 TA-BackTesting-TradingBot
#### Этот проект представляет собой систему для бэктестинга торговых стратегий, основанных на техническом анализе. Проект позволяет анализировать и тестировать стратегии, построенные с использованием различных технических индикаторов, а также автоматизировать торговлю на выбранной бирже или через брокерскую платформу.
## [👨‍🔬 GitHub Wiki](https://github.com/kde2podfreebsd/TA-BackTesting-TradingBot/wiki)
### 💸
* BTC: ```bc1qplx5mjrh6jt24hged09a64zq5ctg6v4lffjzhx  ```
* ETH: ```0xdE6C5b5eCaa6afC014C6CBb04cA7298ED214B899 ```
* SOL: ```2U6GWuoRriSufiwiYreFrPUF2N7Ht3DhgULbK7vDgN6d ```
* USDT: ``` 0xdE6C5b5eCaa6afC014C6CBb04cA7298ED214B899 ```

# ❗️ Отказ от ответственности за финансовые сделки
Данный проект представляет собой инструмент, разработанный в основном для исследования рынка и проверки торговых стратегий. Хотя мы прикладываем все усилия для обеспечения надежности и точности проекта, мы хотели бы ясно указать, что использование модуля трейдинг ботов несет финансовые риски, и мы не несем ответственности за любые финансовые убытки, возникшие в результате его использования.
<br/><br/>
# 🗂 Основные модули проекта
* ## 🤔 Набор кастомных торговых стратегий
В проекте предусмотрен набор кастомных торговых стратегий, которые вы можете использовать для:
1) Бэк-тестинга и подбора оптимальных конфигов тех индикаторов
2) Real-time тестирования на виртуальном счете
3) Запуска торговой стратегии на своем брокероском или биржевом счете.

Вы можете выбрать стратегию, которая наилучшим образом соответствует вашим инвестиционным целям и стилю торговли.

* ## 🔬 Бэктестинг стратегий
Проект предоставляет возможность бэктест-анализа торговых стратегий на основе исторических данных. Вы можете создавать, оптимизировать и анализировать стратегии, используя различные технические индикаторы, предоставленные библиотекой Ta-Lib.
* ## 📊 Интеграция Ta-Lib
Мы используем библиотеку Ta-Lib для построения технических индикаторов. Ta-Lib предоставляет широкий набор функций для анализа финансовых данных, таких как скользящие средние, стохастические осцилляторы, MACD и многое другое. Это позволяет вам создавать сложные торговые стратегии, основанные на различных индикаторах.
* ## 📈 Работа с котировками через pandas
Мы используем библиотеку pandas для удобной работы с котировками и временными рядами. Вы можете загружать и обрабатывать исторические данные, создавать свечные графики, выполнять ресемплинг данных и многое другое.
* ## 🌐 Веб-фронтенд
Веб-фронтенд проекта позволяет вам легко взаимодействовать с функциональностью проекта, включая вывод всех технических индикаторов и технических маркеров, а также отображение всей информации о вашем профиле, сделках и открытых позициях. Вы сможете легко отслеживать текущее состояние своих торговых активов и принимать соответствующие решения.
* ## 🤝  Бэкенд API и SDK для брокеров и бирж
Репозиторий предоставляет бэкенд API (async FastAPI + async PostgreSQL + Redis + Async WebSockets) и SDK для интеграции с брокерскими платформами и биржами. С помощью нашего API и SDK вы можете взаимодействовать с платформами и получать реальные котировки, размещать и управлять ордерами, а также получать информацию о своем счете и позициях. Это позволит вам использовать наш проект для написания своих торговых систем и торговых стратегий.
* ## 🤖 Трейдинг боты
Мы предоставляем возможность автоматизировать торговлю на основе выбранной стратегии. Вы можете настроить трейдинг бота, который будет следить за сигналами вашей стратегии и автоматически размещать соответствующие ордера на вашем выделенном счете. Для этого требуются API-ключи от брокеров, с которыми вы планируете работать.

## Доступные биржи и брокеры 
| Брокер / Биржа | Статус | Что реализовано 
|----------|----------|----------|
| Binance|✅❌| Spot✅: Market <-> Spot❌: Margin, Fiat, Wallet, Pay, Trade
| Binance-Futures|❌| 
| Тинькофф Инвестиции|❌| 
| ByBit|❌| 
| OKX|❌| 

# 🛠 Установка и настройка проекта
1. Клонируйте репозиторий на свой локальный компьютер.
```.sh
git clone <https://.git>
```
2. Создайте ``` config.ini ``` и добавьте ключи своих брокеров
```
[Redis]
host = 192.168.128.2
port = 6379

[POSTGRESQL]
host = 192.168.48.2
port = 5432
database = postgres
user = postgres
password = postgres


[HTTPS_SERVER_HOST]
protocol = http
server_host = 127.0.0.1
server_port = 5000

[Binance]
#inactive keys!
apiKey = <BinanceApiKey>
apiSecret = <BinanceApiSecret>

```
3. Установите необходимые зависимости, запустив команду:
```.sh
pip install -r requirements.txt
or
poetry install
```
4. Отдельно установить ta-lib
* ## Для Linux:
```.sh
chmod +x talib.sh
./talib.sh
```
* ## Для Windows:
1. Скачать и установить библиотеку  ta-lib  ZIP-файлом по ссылке: https://sourceforge.net/projects/ta-lib/files/ta-lib/0.4.0/ta-lib-0.4.0-msvc.zip/download?use_mirror=deac-fra
2. Разархивировать архив в диск С: по пути: ``` C:\ta-lib ```
3. Скачать и установить Visual Studio Community (2015 и позже)- при установке VSC обязательно поставить галочку рядом с  "Разработка на С++" и "Мобильная разработка на С++" 
4. Запустить из панели "Пуск" Native Tools Command Prompt for VS...
5. Прописать путь:``` C:\ta-lib\c\make\cdr\win32\msvc ```
6. Прописать команду ``` nmake ```
7. В терминале PyCharm прописать команду ``` pip install ta-lib ``` (для проверки)

# Запуск стратеги DualSMA:
```.sh
cd Strategy/CustomStrategy/
python DualSMA
```

### Настройка pre-committer
```.sh
$ pre-commit migrate-config
Configuration has been migrated.
$ pre-commit run flake8 --all-files
flake8...................................................................Passed
```
