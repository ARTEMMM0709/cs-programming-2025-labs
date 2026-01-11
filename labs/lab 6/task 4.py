def add_matrices():
   
    #Складывает две квадратные матрицы
    
    #Ввод:
    #1. Размер матрицы n
    #2. Элементы первой матрицы
    #3. Элементы второй матрицы
    
    #Вывод:
    #Результирующая матрица или сообщение об ошибке
   
    try:
        # Чтение размера матрицы
        n = int(input("Введите размер матрицы n: "))
        
        # Проверка размера
        if n <= 2:
            return "Error!"
        
        # Чтение первой матрицы
        print("Введите элементы первой матрицы (по строкам):")
        matrix1 = []
        for i in range(n):
            row = list(map(float, input().split()))
            if len(row) != n:
                return "Error!"
            matrix1.append(row)
        
        # Чтение второй матрицы
        print("Введите элементы второй матрицы (по строкам):")
        matrix2 = []
        for i in range(n):
            row = list(map(float, input().split()))
            if len(row) != n:
                return "Error!"
            matrix2.append(row)
        
        # Сложение матриц
        result = []
        for i in range(n):
            result_row = []
            for j in range(n):
                result_row.append(matrix1[i][j] + matrix2[i][j])
            result.append(result_row)
        
        # Форматирование вывода
        output = []
        for row in result:
            output.append(" ".join(f"{x:g}" for x in row))
        return "\n".join(output)
        
    except (ValueError, IndexError):
        return "Error!"


# Пример использования
if __name__ == "__main__":
    print(add_matrices())