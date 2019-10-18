# TecMundo Scraper

>This project aims to collect news from the [Tecmundo](https://www.tecmundo.com.br/) site using the Scrapy framework.

>The purpose of this project is for study purposes only, so all data collected by this project will not be shared as it is the right of Tecmundo website.

## Workspace
* `$ git clone https://github.com/CarlosQuixada/Tecmundo-Scraper.git`
* `$ cd Tecmundo-Scraper`
* `$ pip install -r requirements.txt`

## Execution
* `scrapy runspider tecmundo_scraper/spiders/Tecmundo.py`

## Workspace Docker
* `docker build -t tecmundo .`
* `docker run -it tecmundo /bin/bash`
* `scrapy runspider tecmundo_scraper/spiders/Tecmundo.py`

* open new tab on terminal and insert:
    ```
    root@id_container:/app# docker cp id_container:/app/tecmundo.csv /home/user_name/tecmundo.csv
    ```

*Built by Carlos Quixadá*

## Technology
* ![alt text](images/scrapy+python.png?raw=true "Scrapy+Python")

* ![alt text](images/docker.jpeg?raw=true "Docker")
