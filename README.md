# Вычислитель отличий (Python)

[![hexlet-check](https://github.com/mikitasazan/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mikitasazan/python-project-50/actions)

В этом проекте отрабатывается работа с коллекциями. Изучаются способы построения и обхода деревьев. Вы познакомитесь с разными форматами данных (JSON, YAML), научитесь их парсить и формировать. Начнете писать тесты (pytest) и освоите разработку через них. Познакомитесь с непрерывной интеграцией (CI) и элементами экстремального программирования (XP)

Учебный проект Хекслета: https://ru.hexlet.io/programs/python
Как это должно работать: https://asciinema.org/a/Pe6QypnLEmFWssNAjCOJN1iii

## Стек

- Python

## Установка

Требуется Python 3.13+ и [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/mikitasazan/python-project-50.git
cd python-project-50
make install
make build && make package-install   # установить утилиту gendiff в систему
```

## Использование

```bash
gendiff file1.json file2.json                      # формат stylish (по умолчанию)
gendiff --format plain file1.yml file2.yml         # плоский формат
gendiff --format json file1.json file2.json        # машиночитаемый вывод
gendiff --help
```

Утилита сравнивает два файла конфигурации (JSON или YAML), в том числе вложенные,
и печатает отличия: `-` удалено, `+` добавлено, отсутствие знака — не изменилось.

Пример вывода в формате `stylish`:

```
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
    }
}
```

### Разработка

```bash
make lint            # ruff
make test            # pytest
make test-coverage   # pytest с отчётом покрытия (порог 80%)
make check           # линтер и тесты вместе
```

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.
