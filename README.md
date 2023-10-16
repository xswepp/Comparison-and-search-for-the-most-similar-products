# Решение задачи сопоставления и поиска наиболее похожих товаров

**Дано:** два множества объектов: A и B. Каждый объект в множестве описывается безымянными признаками.

**Цель:** для каждого объекта из множества A найти один или несколько объектов из B, которые близки к нему по заданной метрике.

**Задача:**
- разработать алгоритм, который для всех товаров измножества A предложит несколько вариантов наиболее похожих товаров из множества B;
- оценить качество алгоритма по метрике accuracy@5;
- деплой: разработать REST API сервис, который по предложенным данным будем предлагать несколько похожих товаров.

**Минимальные требования к памяти** 0,9 Gb.

## Выводы

- Данные в основном представлены непрерывными числовыми значениями, основная их доля очевидно имеет нормальное распределение. Те данные, которые явно не характеризуются нормальным распределением, будут вносить лишний шум в результаты метчинга ('6','21','25','33','44','59','65'). Пропусков не обнаружено, сильных корреляций и зависимостей так же не выявлено. Найдена пара признаков, отличия которых не значимы на уровне 0,001, из них отфильтрован признак '3', который характеризуются распределением, в наибольшей степени отличающимся от нормального.
- Для исследования задачи, выбрана библиотека HNSW (Hierarchical Navigable Small World), алгорит, дающий очень высокую скорость поиска индексов и высокое качество поиска, при этом имеет высокие требования к оперативной памяти. Поскольку для данной задачи проблематика использования оперативной памяти была определена как незначительная, был выбрана именно эта библиотека.
- Оптимизация предсказаний выбранной модели осуществленно с использованием бинарной классификации CatBoostClassifier, которая выполняет задачу определения вероятности положительного исхода в первых пяти вариантах прогноза HNSW модели. Подобрав модель бинарной классификации, мы смогли хорошо разделить данные которые отметчились, согласна целевой метрики, доля которых составляет 71,36%.
- Модель HNSW показывает отличные результаты, высокую скорость работы как на тестовой так и на тренировочной выборках, и практически идентичную целевую метрику (71,76% и 71.16%), результаты применения ML для улучшения показателей метчинга показали неоднозначные результаты, большое различие в значениях целевых метрик (74,18% и 68,49%) может свидетельствовать о переобучености модели, вероятно увеличение количества фолдов на кросвалидации до 10 и увеличение времени на оптимизацию поможет значительно улучшить целевую метрику.

## Установка

1. Клонируйте репозиторий на ваш локальный компьютер:
   ```
   https://github.com/xswepp/Comparison-and-search-for-the-most-similar-products.git
   ```

2. Загрузите в директорию проекта и разорхивируй следующие файлы:
   ```
   idx_hnsw.bin - https://drive.google.com/file/d/1mtKk796sTr3kccFP2NrJeEXluo0Ijqkn/view?usp=sharing
   mcbc_model.cbm - https://drive.google.com/file/d/114V0WDH2v-UEtdTx73sHfMy6-j2riDa9/view?usp=sharing
   mcbr_model.cbm - https://drive.google.com/file/d/1YUMEG0otYbQFxwkGwkbdRv3a5AHK_pYX/view?usp=sharing
   ```

## Инструкция к запуску Docker

1. Выполни инструкции раздела "Установка".

2. Используя командную стоку, перейдите в директорию своего проекта.

3. Создайте образ с помощью команды docker build (требуется установить Docker): 
   ```
   docker build -t default-service:v01 .
   ```

4. Запустите докеризованное приложение, используя следующую команду:
   ```
   docker run -it --rm -p 8989:8989 default-service:v01
   ```

5. Используя пример из тетрадки test.ipynb, выполните запрос.

6. Остановка докеризованного приложение осуществляется следующей командой:
   ```
   docker stop $(docker ps -a -q)
   ```

---
Автор: Евтухов Павел
E-mail: xswepp@tut.by