import json
import os
from datetime import datetime

class FuelType:
    AI92 = "АИ-92"
    AI95 = "АИ-95"
    AI98 = "АИ-98"
    DT = "ДТ"

class Cistern:
    def __init__(self, cistern_id, fuel_type, max_volume, current_volume, min_level):
        self.id = cistern_id
        self.fuel_type = fuel_type
        self.max_volume = max_volume
        self.current_volume = current_volume
        self.min_level = min_level
        self.status = True  # True - включена, False - отключена

    def to_dict(self):
        return {
            'id': self.id,
            'fuel_type': self.fuel_type,
            'max_volume': self.max_volume,
            'current_volume': self.current_volume,
            'min_level': self.min_level,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        cistern = cls(data['id'], data['fuel_type'], data['max_volume'], data['current_volume'], data['min_level'])
        cistern.status = data['status']
        return cistern

class Pump:
    def __init__(self, pump_id, connections):
        self.id = pump_id
        self.connections = connections  # словарь: fuel_type: cistern_id

    def to_dict(self):
        return {
            'id': self.id,
            'connections': self.connections
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['connections'])

class Transaction:
    def __init__(self, operation_type, details, timestamp=None):
        self.operation_type = operation_type
        self.details = details
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            'operation_type': self.operation_type,
            'details': self.details,
            'timestamp': self.timestamp
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['operation_type'], data['details'], data['timestamp'])

class FuelStation:
    def __init__(self, data_file="fuel_station.json"):
        self.data_file = data_file
        self.cisterns = {}
        self.pumps = {}
        self.balance = 0.0
        self.cars_served = 0
        self.fuel_sales = {FuelType.AI92: 0, FuelType.AI95: 0, FuelType.AI98: 0, FuelType.DT: 0}
        self.fuel_income = {FuelType.AI92: 0, FuelType.AI95: 0, FuelType.AI98: 0, FuelType.DT: 0}
        self.history = []
        self.emergency_mode = False
        self.fuel_prices = {
            FuelType.AI92: 55.00,
            FuelType.AI95: 58.30,
            FuelType.AI98: 62.50,
            FuelType.DT: 56.20
        }
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.balance = data.get('balance', 0.0)
                self.cars_served = data.get('cars_served', 0)
                self.fuel_sales = data.get('fuel_sales', {FuelType.AI92: 0, FuelType.AI95: 0, FuelType.AI98: 0, FuelType.DT: 0})
                self.fuel_income = data.get('fuel_income', {FuelType.AI92: 0, FuelType.AI95: 0, FuelType.AI98: 0, FuelType.DT: 0})
                self.emergency_mode = data.get('emergency_mode', False)
                
                # Загрузка цистерн
                for cistern_data in data.get('cisterns', []):
                    cistern = Cistern.from_dict(cistern_data)
                    self.cisterns[cistern.id] = cistern
                
                # Загрузка колонок
                for pump_data in data.get('pumps', []):
                    pump = Pump.from_dict(pump_data)
                    self.pumps[pump.id] = pump
                
                # Загрузка истории
                for history_item in data.get('history', []):
                    transaction = Transaction.from_dict(history_item)
                    self.history.append(transaction)
        else:
            self.initialize_default_data()

    def initialize_default_data(self):
        # Инициализация цистерн
        self.cisterns = {
            "AI-92_1": Cistern("AI-92_1", FuelType.AI92, 20000, 15000, 2000),
            "AI-95_1": Cistern("AI-95_1", FuelType.AI95, 20000, 15000, 2000),
            "AI-95_2": Cistern("AI-95_2", FuelType.AI95, 20000, 15000, 2000),
            "AI-98_1": Cistern("AI-98_1", FuelType.AI98, 15000, 10000, 1500),
            "DT_1": Cistern("DT_1", FuelType.DT, 25000, 20000, 2500)
        }
        
        # Инициализация колонок
        self.pumps = {
            1: Pump(1, {FuelType.AI95: "AI-95_1", FuelType.AI92: "AI-92_1"}),
            2: Pump(2, {FuelType.AI95: "AI-95_1", FuelType.AI92: "AI-92_1"}),
            3: Pump(3, {FuelType.AI95: "AI-95_1", FuelType.AI92: "AI-92_1", FuelType.AI98: "AI-98_1", FuelType.DT: "DT_1"}),
            4: Pump(4, {FuelType.AI95: "AI-95_1", FuelType.AI92: "AI-92_1", FuelType.AI98: "AI-98_1", FuelType.DT: "DT_1"}),
            5: Pump(5, {FuelType.AI95: "AI-95_2", FuelType.AI92: "AI-92_1", FuelType.AI98: "AI-98_1", FuelType.DT: "DT_1"}),
            6: Pump(6, {FuelType.AI95: "AI-95_2", FuelType.AI92: "AI-92_1", FuelType.AI98: "AI-98_1", FuelType.DT: "DT_1"}),
            7: Pump(7, {FuelType.AI95: "AI-95_2", FuelType.DT: "DT_1"}),
            8: Pump(8, {FuelType.AI95: "AI-95_2", FuelType.DT: "DT_1"})
        }

    def save_data(self):
        data = {
            'balance': self.balance,
            'cars_served': self.cars_served,
            'fuel_sales': self.fuel_sales,
            'fuel_income': self.fuel_income,
            'emergency_mode': self.emergency_mode,
            'cisterns': [c.to_dict() for c in self.cisterns.values()],
            'pumps': [p.to_dict() for p in self.pumps.values()],
            'history': [t.to_dict() for t in self.history]
        }
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def check_low_fuel_levels(self):
        """Проверяет уровни топлива и отключает цистерны при необходимости"""
        for cistern in self.cisterns.values():
            if cistern.current_volume < cistern.min_level and cistern.status:
                cistern.status = False
                self.history.append(Transaction("AUTO_DISABLE", f"Цистерна {cistern.id} отключена из-за низкого уровня"))

    def add_transaction(self, operation_type, details):
        transaction = Transaction(operation_type, details)
        self.history.append(transaction)
        # Ограничиваем историю последними 100 записями
        if len(self.history) > 100:
            self.history = self.history[-100:]

    def serve_customer(self):
        if self.emergency_mode:
            print("ОШИБКА: Система находится в аварийном режиме. Обслуживание невозможно.")
            input("Нажмите Enter для возврата в меню...")
            return

        print("\n--- Обслуживание клиента ---")
        print("Доступные колонки:")
        for pump_id in sorted(self.pumps.keys()):
            print(f"{pump_id}) Колонка {pump_id}")

        try:
            pump_choice = int(input("Выберите колонку: "))
            if pump_choice not in self.pumps:
                print("Неверный выбор колонки.")
                input("Нажмите Enter для возврата в меню...")
                return
        except ValueError:
            print("Неверный ввод.")
            input("Нажмите Enter для возврата в меню...")
            return

        pump = self.pumps[pump_choice]
        print(f"\nКолонка {pump_choice}")
        print("Доступные виды топлива:")
        
        available_fuels = []
        for i, (fuel_type, cistern_id) in enumerate(pump.connections.items(), 1):
            cistern = self.cisterns[cistern_id]
            if cistern.status:
                print(f"{i}) {fuel_type} (цистерна {cistern_id})")
                available_fuels.append((i, fuel_type, cistern_id))
            else:
                print(f"{i}) {fuel_type} (цистерна {cistern_id}) - НЕДОСТУПНО")
        
        if not available_fuels:
            print("Нет доступного топлива для этой колонки.")
            input("Нажмите Enter для возврата в меню...")
            return

        try:
            fuel_choice = int(input("Выберите тип топлива: "))
            selected_fuel = None
            selected_cistern_id = None
            for num, fuel_type, cistern_id in available_fuels:
                if num == fuel_choice:
                    selected_fuel = fuel_type
                    selected_cistern_id = cistern_id
                    break
            
            if selected_fuel is None:
                print("Неверный выбор топлива.")
                input("Нажмите Enter для возврата в меню...")
                return
                
            cistern = self.cisterns[selected_cistern_id]
            if not cistern.status:
                print(f"ОШИБКА: Цистерна {selected_cistern_id} отключена.\nОтпуск топлива невозможен.")
                input("Нажмите Enter для возврата в меню...")
                return

        except ValueError:
            print("Неверный ввод.")
            input("Нажмите Enter для возврата в меню...")
            return

        try:
            liters = float(input("Введите количество литров: "))
            if liters <= 0:
                print("Количество литров должно быть положительным.")
                input("Нажмите Enter для возврата в меню...")
                return
        except ValueError:
            print("Неверный ввод количества литров.")
            input("Нажмите Enter для возврата в меню...")
            return

        cistern = self.cisterns[selected_cistern_id]
        if liters > cistern.current_volume:
            print(f"ОШИБКА: Недостаточно топлива в цистерне. Доступно: {cistern.current_volume} л")
            input("Нажмите Enter для возврата в меню...")
            return

        price = liters * self.fuel_prices[selected_fuel]
        print(f"\nСтоимость:\n{liters} л × {self.fuel_prices[selected_fuel]} ₽ = {price:.2f} ₽")

        confirm = input("Подтвердить оплату? (y/n): ").lower()
        if confirm != 'y':
            print("Операция отменена.")
            input("Нажмите Enter для возврата в меню...")
            return

        # Выполняем операцию
        cistern.current_volume -= liters
        self.balance += price
        self.cars_served += 1
        self.fuel_sales[selected_fuel] += liters
        self.fuel_income[selected_fuel] += price
        
        self.check_low_fuel_levels()  # Проверяем уровни после продажи
        
        self.add_transaction("SALE", f"Колонка {pump_choice}, {liters}л {selected_fuel}, {price:.2f}₽")
        
        print("Операция выполнена успешно.")
        print("Спасибо за покупку!")
        input("Нажмите Enter для возврата в меню...")

    def check_cisterns_status(self):
        print("\n--- Состояние цистерн ---")
        print("Доступные цистерны:")
        for cistern_id, cistern in sorted(self.cisterns.items()):
            status = "ВКЛ" if cistern.status else "ВЫКЛ"
            warning = " (ниже порога)" if cistern.current_volume < cistern.min_level else ""
            print(f"{cistern_id} | {cistern.current_volume:.0f} / {cistern.max_volume:.0f} л | {status}{warning}")
        input("\nНажмите Enter для возврата в меню...")

    def refuel_cistern(self):
        if self.emergency_mode:
            print("ОШИБКА: Система находится в аварийном режиме. Пополнение невозможно.")
            input("Нажмите Enter для возврата в меню...")
            return

        print("\n--- Оформить пополнение топлива ---")
        print("Доступные типы топлива:")
        fuel_types = set(cistern.fuel_type for cistern in self.cisterns.values())
        for i, fuel_type in enumerate(sorted(fuel_types), 1):
            print(f"{i}) {fuel_type}")

        try:
            fuel_choice = int(input("Выберите тип топлива: "))
            fuel_types_list = sorted(fuel_types)
            if 1 <= fuel_choice <= len(fuel_types_list):
                selected_fuel = fuel_types_list[fuel_choice - 1]
            else:
                print("Неверный выбор.")
                input("Нажмите Enter для возврата в меню...")
                return
        except ValueError:
            print("Неверный ввод.")
            input("Нажмите Enter для возврата в меню...")
            return

        print(f"\nДоступные цистерны для {selected_fuel}:")
        available_cisterns = []
        for i, (cistern_id, cistern) in enumerate(self.cisterns.items(), 1):
            if cistern.fuel_type == selected_fuel:
                print(f"{i}) {cistern_id} | {cistern.current_volume:.0f}/{cistern.max_volume:.0f} л")
                available_cisterns.append((i, cistern_id, cistern))

        if not available_cisterns:
            print("Нет доступных цистерн для этого типа топлива.")
            input("Нажмите Enter для возврата в меню...")
            return

        try:
            cistern_choice = int(input("Выберите цистерну: "))
            selected_cistern_id = None
            selected_cistern = None
            for num, cistern_id, cistern in available_cisterns:
                if num == cistern_choice:
                    selected_cistern_id = cistern_id
                    selected_cistern = cistern
                    break
            
            if selected_cistern is None:
                print("Неверный выбор цистерны.")
                input("Нажмите Enter для возврата в меню...")
                return

        except ValueError:
            print("Неверный ввод.")
            input("Нажмите Enter для возврата в меню...")
            return

        try:
            liters = float(input("Введите количество литров для пополнения: "))
            if liters <= 0:
                print("Количество литров должно быть положительным.")
                input("Нажмите Enter для возврата в меню...")
                return
        except ValueError:
            print("Неверный ввод количества литров.")
            input("Нажмите Enter для возврата в меню...")
            return

        new_volume = selected_cistern.current_volume + liters
        if new_volume > selected_cistern.max_volume:
            print(f"ОШИБКА: Превышение максимального объема. Доступно: {selected_cistern.max_volume - selected_cistern.current_volume:.0f} л")
            input("Нажмите Enter для возврата в меню...")
            return

        selected_cistern.current_volume = new_volume
        self.add_transaction("REFUEL", f"Цистерна {selected_cistern_id}, +{liters}л")
        
        print(f"Цистерна {selected_cistern_id} успешно пополнена на {liters} литров.")
        input("Нажмите Enter для возврата в меню...")

    def show_balance_statistics(self):
        print("\n--- Баланс и статистика ---")
        print(f"Обслужено автомобилей: {self.cars_served}")
        print(f"Общий доход: {self.balance:.2f} ₽")
        print("\nПродано топлива:")
        for fuel_type in [FuelType.AI92, FuelType.AI95, FuelType.AI98, FuelType.DT]:
            liters = self.fuel_sales[fuel_type]
            income = self.fuel_income[fuel_type]
            print(f"{fuel_type:<6} - {liters:>6.0f} л ({income:>8.2f} ₽)")
        input("\nНажмите Enter для возврата в меню...")

    def show_history(self):
        print("\n--- История операций ---")
        if not self.history:
            print("История операций пуста.")
        else:
            for entry in self.history[-20:]:  # Показываем последние 20 записей
                print(f"[{entry.timestamp}] {entry.operation_type}: {entry.details}")
        input("\nНажмите Enter для возврата в меню...")

    def transfer_fuel(self):
        if self.emergency_mode:
            print("ОШИБКА: Система находится в аварийном режиме. Перекачка невозможна.")
            input("Нажмите Enter для возврата в меню...")
            return

        print("\n--- Перекачка топлива между цистернами ---")
        print("Доступные типы топлива:")
        fuel_types = set(cistern.fuel_type for cistern in self.cisterns.values())
        for i, fuel_type in enumerate(sorted(fuel_types), 1):
            print(f"{i}) {fuel_type}")

        try:
            fuel_choice = int(input("Выберите тип топлива: "))
            fuel_types_list = sorted(fuel_types)
            if 1 <= fuel_choice <= len(fuel_types_list):
                selected_fuel = fuel_types_list[fuel_choice - 1]
            else:
                print("Неверный выбор.")
                input("Нажмите Enter для возврата в меню...")
                return
        except ValueError:
            print("Неверный ввод.")
            input("Нажмите Enter для возврата в меню...")
            return

        print(f"\nДоступные цистерны для {selected_fuel}:")
        available_cisterns = []
        for i, (cistern_id, cistern) in enumerate(self.cisterns.items(), 1):
            if cistern.fuel_type == selected_fuel:
                print(f"{i}) {cistern_id} | {cistern.current_volume:.0f}/{cistern.max_volume:.0f} л")
                available_cisterns.append((i, cistern_id, cistern))

        if len(available_cisterns) < 2:
            print("Недостаточно цистерн для перекачки.")
            input("Нажмите Enter для возврата в меню...")
            return

        try:
            source_choice = int(input("Выберите исходную цистерну: "))
            target_choice = int(input("Выберите целевую цистерну: "))
            
            source_cistern_id = None
            source_cistern = None
            target_cistern_id = None
            target_cistern = None
            
            for num, cistern_id, cistern in available_cisterns:
                if num == source_choice:
                    source_cistern_id = cistern_id
                    source_cistern = cistern
                if num == target_choice:
                    target_cistern_id = cistern_id
                    target_cistern = cistern
            
            if source_cistern is None or target_cistern is None:
                print("Неверный выбор цистерн.")
                input("Нажмите Enter для возврата в меню...")
                return
            if source_cistern_id == target_cistern_id:
                print("Исходная и целевая цистерны не могут быть одинаковыми.")
                input("Нажмите Enter для возврата в меню...")
                return

        except ValueError:
            print("Неверный ввод.")
            input("Нажмите Enter для возврата в меню...")
            return

        try:
            liters = float(input("Введите количество литров для перекачки: "))
            if liters <= 0:
                print("Количество литров должно быть положительным.")
                input("Нажмите Enter для возврата в меню...")
                return
        except ValueError:
            print("Неверный ввод количества литров.")
            input("Нажмите Enter для возврата в меню...")
            return

        if liters > source_cistern.current_volume:
            print(f"ОШИБКА: Недостаточно топлива в исходной цистерне. Доступно: {source_cistern.current_volume:.0f} л")
            input("Нажмите Enter для возврата в меню...")
            return

        new_target_volume = target_cistern.current_volume + liters
        if new_target_volume > target_cistern.max_volume:
            print(f"ОШИБКА: Превышение максимального объема целевой цистерны. Доступно: {target_cistern.max_volume - target_cistern.current_volume:.0f} л")
            input("Нажмите Enter для возврата в меню...")
            return

        source_cistern.current_volume -= liters
        target_cistern.current_volume += liters
        
        self.add_transaction("TRANSFER", f"Из {source_cistern_id} в {target_cistern_id}, {liters}л")
        
        print(f"Перекачка завершена: {liters}л из {source_cistern_id} в {target_cistern_id}")
        input("Нажмите Enter для возврата в меню...")

    def manage_cisterns(self):
        if self.emergency_mode:
            print("ОШИБКА: Система находится в аварийном режиме. Управление невозможно.")
            input("Нажмите Enter для возврата в меню...")
            return

        print("\n--- Управление цистернами ---")
        print("Доступные действия:")
        print("1) Включить цистерну")
        print("2) Отключить цистерну")
        
        try:
            action = int(input("> "))
            if action not in [1, 2]:
                print("Неверный выбор.")
                input("Нажмите Enter для возврата в меню...")
                return
        except ValueError:
            print("Неверный ввод.")
            input("Нажмите Enter для возврата в меню...")
            return

        if action == 1:
            print("\nЦистерны, доступные для включения:")
            available_cisterns = []
            for i, (cistern_id, cistern) in enumerate(self.cisterns.items(), 1):
                if not cistern.status and cistern.current_volume >= cistern.min_level:
                    print(f"{i}) {cistern_id} | {cistern.current_volume:.0f} / {cistern.max_volume:.0f} л")
                    available_cisterns.append((i, cistern_id))
            
            if not available_cisterns:
                print("Нет цистерн, доступных для включения.")
                input("Нажмите Enter для возврата в меню...")
                return

            try:
                choice = int(input("Выберите цистерну: "))
                selected_cistern_id = None
                for num, cistern_id in available_cisterns:
                    if num == choice:
                        selected_cistern_id = cistern_id
                        break
                
                if selected_cistern_id is None:
                    print("Неверный выбор.")
                    input("Нажмите Enter для возврата в меню...")
                    return

                self.cisterns[selected_cistern_id].status = True
                self.add_transaction("ENABLE", f"Цистерна {selected_cistern_id} включена")
                print(f"Цистерна {selected_cistern_id} успешно включена.")
                
            except ValueError:
                print("Неверный ввод.")
        
        else:  # action == 2
            print("\nЦистерны, доступные для отключения:")
            available_cisterns = []
            for i, (cistern_id, cistern) in enumerate(self.cisterns.items(), 1):
                if cistern.status:
                    print(f"{i}) {cistern_id} | {cistern.current_volume:.0f} / {cistern.max_volume:.0f} л")
                    available_cisterns.append((i, cistern_id))
            
            if not available_cisterns:
                print("Нет цистерн, доступных для отключения.")
                input("Нажмите Enter для возврата в меню...")
                return

            try:
                choice = int(input("Выберите цистерну: "))
                selected_cistern_id = None
                for num, cistern_id in available_cisterns:
                    if num == choice:
                        selected_cistern_id = cistern_id
                        break
                
                if selected_cistern_id is None:
                    print("Неверный выбор.")
                    input("Нажмите Enter для возврата в меню...")
                    return

                self.cisterns[selected_cistern_id].status = False
                self.add_transaction("DISABLE", f"Цистерна {selected_cistern_id} отключена")
                print(f"Цистерна {selected_cistern_id} успешно отключена.")
                
            except ValueError:
                print("Неверный ввод.")

        input("Нажмите Enter для возврата в меню...")

    def check_pumps_status(self):
        print("\n--- Состояние колонок ---")
        for pump_id in sorted(self.pumps.keys()):
            print(f"\nКолонка {pump_id}:")
            pump = self.pumps[pump_id]
            for fuel_type, cistern_id in pump.connections.items():
                cistern = self.cisterns[cistern_id]
                status = "РАБОТАЕТ" if cistern.status else "НЕ РАБОТАЕТ (цистерна отключена)"
                print(f"  {fuel_type} -> цистерна {cistern_id} ({status})")
        input("\nНажмите Enter для возврата в меню...")

    def emergency_mode_toggle(self):
        if not self.emergency_mode:
            print("\n--- АВАРИЙНАЯ СИТУАЦИЯ ---")
            confirm = input("Подтвердите активацию аварийного режима (y/n): ").lower()
            if confirm != 'y':
                print("Активация аварийного режима отменена.")
                input("Нажмите Enter для возврата в меню...")
                return
            
            # Отключаем все цистерны
            for cistern in self.cisterns.values():
                if cistern.status:
                    cistern.status = False
            
            self.emergency_mode = True
            self.add_transaction("EMERGENCY", "Аварийный режим активирован")
            print("Аварийный режим активирован. Все цистерны заблокированы.")
            print("Имитация вызова аварийных служб...")
            import time
            time.sleep(1)
            print("Аварийные службы вызваны.")
        else:
            print("\n--- ВЫХОД ИЗ АВАРИЙНОГО РЕЖИМА ---")
            confirm = input("Подтвердите деактивацию аварийного режима (y/n): ").lower()
            if confirm != 'y':
                print("Деактивация аварийного режима отменена.")
                input("Нажмите Enter для возврата в меню...")
                return
            
            self.emergency_mode = False
            self.add_transaction("EMERGENCY_END", "Аварийный режим деактивирован")
            print("Аварийный режим деактивирован.")
            print("ВНИМАНИЕ: Цистерны не разблокированы автоматически. Используйте меню управления цистернами.")

        input("Нажмите Enter для возврата в меню...")

    def show_main_menu(self):
        while True:
            print("\n" + "="*40)
            print("АЗС <<СеверНефть>>")
            print("Система управления заправочной станцией")
            print("="*40)
            
            if self.emergency_mode:
                print("\nВНИМАНИЕ: Система находится в аварийном режиме!")
            
            # Проверяем и показываем отключенные цистерны
            disabled_cisterns = []
            for cistern in self.cisterns.values():
                if not cistern.status:
                    disabled_cisterns.append(f" - {cistern.id}")
            
            if disabled_cisterns:
                print("\nВНИМАНИЕ!")
                print("Обнаружены отключённые цистерны:")
                for cistern_info in disabled_cisterns:
                    print(cistern_info)
            
            print("\n----------------------------------------")
            print("Выберите действие:")
            print("1) Обслужить клиента (касса)")
            print("2) Проверить состояние цистерн")
            print("3) Оформить пополнение топлива")
            print("4) Баланс и статистика")
            print("5) История операций")
            print("6) Перекачка топлива между цистернами")
            print("7) Управление цистернами")
            print("8) Состояние колонок")
            print("9) EMERGENCY - аварийная ситуация")
            print("0) Выход")
            
            try:
                choice = input("> ")
                if choice == '0':
                    print("Сохранение данных...")
                    self.save_data()
                    print("До свидания!")
                    break
                elif choice == '1':
                    self.serve_customer()
                elif choice == '2':
                    self.check_cisterns_status()
                elif choice == '3':
                    self.refuel_cistern()
                elif choice == '4':
                    self.show_balance_statistics()
                elif choice == '5':
                    self.show_history()
                elif choice == '6':
                    self.transfer_fuel()
                elif choice == '7':
                    self.manage_cisterns()
                elif choice == '8':
                    self.check_pumps_status()
                elif choice == '9':
                    self.emergency_mode_toggle()
                else:
                    print("Неверный выбор. Пожалуйста, выберите действие от 0 до 9.")
            except KeyboardInterrupt:
                print("\n\nПрограмма прервана пользователем.")
                self.save_data()
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                input("Нажмите Enter для продолжения...")


def main():
    station = FuelStation()
    station.show_main_menu()


if __name__ == "__main__":
    main()