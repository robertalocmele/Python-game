Шаг за шагом объясняется, что нужно сделать, чтобы запустить игры.

Первое это скачать Python - https://www.python.org/downloads/

После этого мы его по шагам запускаем. Install Python.

Потом открываем Терминал на макбуке.

Установить Homebrew 
  
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

После того как там всё скачалось запроси ещё этот код
    
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
    source ~/.zshrc


Установить Python с помощью Homebrew 
    
    brew install python

Потом терминал закрывать можно и заходить в VS code

Слева есть меню где по середине есть Extensions.
Открываем и в поиске ищем Python. И нажимаем Install.

Создай новую папку на рабочем столе. Назовы эту папку "Game". Скачай все файлы игры в эту папку
Теперь у тебя на рабочем столе должна быть папка "Game", содержащая все файлы игры, включая game.py и все фотографии.

Теперь можно открывать папку через VS code. 

Теперь нам нужен Virtual Environment

Создайте новое виртуальное окружение:
      
      python3 -m venv venv

Активируйте новое виртуальное окружение:

      source venv/bin/activate

Установите Pygame:

      pip install pygame

Запускать игры можно либо через скрипт либо нажимая play в правом верхнем углу.

    python game.py
    
