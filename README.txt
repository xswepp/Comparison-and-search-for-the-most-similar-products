# Решение задачи сопоставления и поиска наиболее похожих товаров

**Дано:** два множества объектов: A и B. Каждый объект в множестве описывается безымянными признаками.

**Цель:** для каждого объекта из множества A найти один или несколько объектов из B, которые близки к нему по заданной метрике.

**Задача:**
- разработать алгоритм, который для всех товаров измножества A предложит несколько вариантов наиболее похожих товаров из множества B;
- оценить качество алгоритма по метрике accuracy@5;
- деплой: разработать REST API сервис, который по предложенным данным будем предлагать несколько похожих товаров.

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

3. Установите окружение:
   ```
   requirements_2.txt
   ```

---
Автор: Евтухов Павел
E-mail: xswepp@tut.by