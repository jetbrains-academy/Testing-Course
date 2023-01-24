## Установка драйвера для браузера: Linux
Давайте установим и настроим ChromeDriver с помощью команд в терминале.
Укажем нужную нам версию ChromeDriver для загрузки.
Для получения ссылки перейдите в браузере на нужную вам версию драйвера по ссылке 
на https://sites.google.com/chromium.org/driver/. 
На открывшейся странице нажмите на файле для Linux правой кнопкой и 
скопируйте путь к файлу. 
Замените в примере ниже путь к файлу для команды wget вашей ссылкой:

``` 
wget https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```
Переместите разархивированный файл с СhromeDriver в папку `/usr/local/bin/` и разрешите 
запускать chromedriver как исполняемый файл:
```
sudo mv chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```
Проверьте, что chromedriver доступен, выполнив команду chromedriver в терминале, вы должны получить сообщение о том, что процесс успешно запущен:

![img.png](img.png)

