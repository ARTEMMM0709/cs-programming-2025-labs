# Создание списка словарей с отчетами сотрудников
# Каждый словарь содержит автора и текст отчета
reports = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org    "},
    {"author": "Supervisor Kane", "text": "No anomalies detected during inspection."},
    {"author": "Researcher Bloom", "text": "Extended observations uploaded to http://research-notes.lab"},
    {"author": "Agent Novak", "text": "Perimeter secured. No external interference observed."},
    {"author": "Dr. Hargreeve", "text": "Full containment log stored at https://internal-db.scp    "},
    {"author": "Technician Moore", "text": "Routine maintenance completed successfully."},
    {"author": "Dr. Alvarez", "text": "Cross-reference materials: http://crosslink.foundation"},
    {"author": "Security Officer Tan", "text": "Shift completed without incidents."},
    {"author": "Analyst Wright", "text": "Statistical model published at https://analysis-hub.org    "},
    {"author": "Dr. Kowalski", "text": "Behavioral deviations documented internally."},
    {"author": "Agent Fischer", "text": "Additional footage archived: http://video-storage.sec"},
    {"author": "Senior Researcher Hall", "text": "All test results verified and approved."},
    {"author": "Operations Lead Grant", "text": "Emergency protocol draft shared via https://ops-share.scp    "}
]

# Сложное преобразование в одну строку:
# 1. Сначала filter() отбирает только отчеты, содержащие http:// или https:// в тексте
# 2. Затем map() обрабатывает каждый отфильтрованный отчет
# 3. Внутри map() создается новый словарь с автором и обработанным текстом
# 4. Обработка текста: разбиваем на слова, заменяем URL на "[ДАННЫЕ УДАЛЕНЫ]"
filtered_reports_sanitized = list(map(
    lambda r: {  # Для каждого отчета r создаем новый словарь
        "author": r["author"],  # Сохраняем автора без изменений
        "text": (lambda t: " ".join(  # Вложенная lambda для обработки текста
            "[ДАННЫЕ УДАЛЕНЫ]" if w.startswith(("http://", "https://")) else w  # Заменяем URL
            for w in t.split()  # Разбиваем текст на слова для проверки
        ))(r["text"])  # Передаем текст отчета во внутреннюю lambda
    },
    filter(  # Фильтруем исходные отчеты
        lambda r: "http://" in r["text"] or "https://" in r["text"],  # Условие: есть URL в тексте
        reports  # Применяем фильтр ко всем отчетам
    )
))

# Результат: список отчетов, содержащих URL, где все URL заменены на "[ДАННЫЕ УДАЛЕНЫ]"