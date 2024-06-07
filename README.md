Шаг за шагом объясняется, что нужно сделать, чтобы запустить игры.

Первое это скачать Python - https://www.python.org/downloads/

После этого мы его по шагам запускаем. Install Python.

Потом открываем Терминал на макбуке.

Установить Homebrew
КОД: 
  
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

После того как там всё скачалось запроси ещё этот код
КОД: 
    
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
    source ~/.zshrc


Установить Python с помощью Homebrew
КОД: 
    
    brew install python

Потом терминал закрывать можно и заходить в VS code

Слева есть меню где по середине есть Extensions.
Открываем и в поиске ищем Python. И нажимаем Install.

Теперь можно открывать папки через VS code. 
Должен открыться файл game.py и все фотки.

Теперь нам нужен Virtual Environment

Создайте новое виртуальное окружение:
КОД: 
      
      python3 -m venv venv

Активируйте новое виртуальное окружение:
КОД: 

      source venv/bin/activate

Установите Pygame:
КОД: 

      pip install pygame

Запускать игры можно либо через скрипт либо нажимая play в правом верхнем углу.
КОД: 

    python game.py
    
