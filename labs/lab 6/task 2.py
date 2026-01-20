def calculate_profit(amount: float, years: int) -> float:
    
    #Рассчитывает прибыль по вкладу со сложным процентом
    
    #Args:
        #amount: сумма вклада
        #years: срок вклада в годах
        
    #Returns:
        #Сумма прибыли (без учета первоначального вклада)
   
    # Проверка минимального вклада
    if amount < 30000:
        raise ValueError("Минимальный вклад - 30 000 рублей")
    
    # Расчет ставки в зависимости от суммы
    base_rate = min(0.003 * (amount // 10000), 0.05)
    
    # Расчет ставки в зависимости от срока
    if years <= 3:
        term_rate = 0.03
    elif 4 <= years <= 6:
        term_rate = 0.05
    else:
        term_rate = 0.02
    
    # Итоговая ставка
    total_rate = base_rate + term_rate
    
    # Расчет сложного процента
    total_amount = amount * ((1 + total_rate) ** years)
    
    # Прибыль (без учета первоначального вклада)
    profit = total_amount - amount
    
    return round(profit, 2)


# Пример использования
if __name__ == "__main__":
    # Примеры из задания
    print(f"Вклад 30000 на 3 года: {calculate_profit(30000, 3)}")
    print(f"Вклад 100000 на 5 лет: {calculate_profit(100000, 5)}")
    print(f"Вклад 200000 на 8 лет: {calculate_profit(200000, 8)}")