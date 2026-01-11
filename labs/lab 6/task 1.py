def time_converter(value: float, from_unit: str, to_unit: str) -> float:
   
    #Конвертирует время из одной единицы измерения в другую
    
    #Поддерживаемые единицы измерения:
    #- s (секунды)
    #- m (минуты)
    #- h (часы)
    
    #Args:
        #value: значение времени
        #from_unit: исходная единица измерения
        #to_unit: целевая единица измерения
        
    #Returns:
        #Конвертированное значение
    
    # Преобразуем все единицы к секундам (базовой единице)
    if from_unit == "h":
        value_in_seconds = value * 3600
    elif from_unit == "m":
        value_in_seconds = value * 60
    elif from_unit == "s":
        value_in_seconds = value
    else:
        raise ValueError("Неверная исходная единица измерения")
    
    # Преобразуем из секунд в целевую единицу
    if to_unit == "h":
        return value_in_seconds / 3600
    elif to_unit == "m":
        return value_in_seconds / 60
    elif to_unit == "s":
        return value_in_seconds
    else:
        raise ValueError("Неверная целевая единица измерения")


# Пример использования
if __name__ == "__main__":
    # Примеры из задания
    print(f"4h -> m: {time_converter(4, 'h', 'm')}m")
    print(f"30m -> h: {time_converter(30, 'm', 'h')}h")
    print(f"12s -> h: {time_converter(12, 's', 'h')}h")