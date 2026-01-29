import json
import os
from datetime import datetime

DATA_FILE = "data.json"

PRICES = {
    "АИ-92": 50.0,
    "АИ-95": 58.3,
    "АИ-98": 65.0,
    "ДТ": 55.0
}


# ====================== КЛАССЫ ======================
#Класс колонка, содержит номер колонки, тип топлива, вместимость, объём и флаги для блокировки и включения
class Tank:
    def __init__(self, id, fuel_type, max_volume, current_volume, min_level, enabled=True, blocked=False):
        self.id = id
        self.fuel_type = fuel_type
        self.max_volume = max_volume
        self.current_volume = current_volume
        self.min_level = min_level
        self.enabled = enabled
        self.blocked = blocked

    #Функция проверки того, что топлива достаточно для работы
    def check_min_level(self):
        if self.current_volume < self.min_level:
            self.enabled = False
    #Функция "налива" топлива
    def dispense(self, liters):
        if self.current_volume >= liters:
            self.current_volume -= liters
            self.check_min_level()
            return True
        return False
    #Функция пополнения колонки
    def refill(self, liters):
        if self.current_volume + liters <= self.max_volume:
            self.current_volume += liters
            return True
        return False
    #Функция перелива топлива с одной колонки на другую
    def transfer_to(self, other, liters):
        if self.fuel_type != other.fuel_type:
            return False
        if self.current_volume < liters:
            return False
        if other.current_volume + liters > other.max_volume:
            return False

        self.current_volume -= liters
        other.current_volume += liters
        self.check_min_level()
        return True
    #Преобразование класса в словарь
    def to_dict(self):
        return self.__dict__


class Dispenser:
    def __init__(self, id, connections):
        self.id = id
        self.connections = connections  # fuel_type -> tank_id

    def to_dict(self):
        return self.__dict__

#Основной класс заправочной станции
class GasStation:
    def __init__(self):
        self.tanks = {}
        self.dispensers = {}
        self.stats = {
            "income": 0,
            "cars": 0,
            "liters": {},
            "fuel_income": {}
        }
        self.history = []
        self.emergency_mode = False
        self.load()

    # =================== ЗАГРУЗКА / СОХРАНЕНИЕ ===================

    def load(self):
        if not os.path.exists(DATA_FILE):
            self.create_default()
            self.save()
            return

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Загрузка танков с проверкой ключей
        for t in data["tanks"]:
            # Нормализуем ключи
            tank_data = {}
            if "tank_id" in t:
                tank_data["id"] = t["tank_id"]
            else:
                tank_data["id"] = t["id"]
            
            # Копируем остальные поля
            for key in ["fuel_type", "max_volume", "current_volume", "min_level", "enabled", "blocked"]:
                if key in t:
                    tank_data[key] = t[key]
            
            # Создаем объект
            tank = Tank(**tank_data)
            self.tanks[tank.id] = tank

        # Загрузка диспенсеров с проверкой ключей
        for d in data["dispensers"]:
            dispenser_data = {}
            if "dispenser_id" in d:
                dispenser_data["id"] = d["dispenser_id"]
            else:
                dispenser_data["id"] = d["id"]
            
            dispenser_data["connections"] = d["connections"]
            
            dispenser = Dispenser(**dispenser_data)
            self.dispensers[dispenser.id] = dispenser

        self.stats = data["stats"]
        self.history = data["history"]
        self.emergency_mode = data.get("emergency_mode", False)

    def save(self):
        data = {
            "tanks": [t.to_dict() for t in self.tanks.values()],
            "dispensers": [d.to_dict() for d in self.dispensers.values()],
            "stats": self.stats,
            "history": self.history,
            "emergency_mode": self.emergency_mode
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    #Стартовый шаблон для начала игры.
    def create_default(self):
        self.tanks = {
            "T1": Tank("T1", "АИ-92", 20000, 15000, 1000),
            "T2": Tank("T2", "АИ-95", 20000, 12000, 1000),
            "T3": Tank("T3", "АИ-95", 20000, 800, 1000, enabled=False),
            "T4": Tank("T4", "АИ-98", 15000, 10000, 1000),
            "T5": Tank("T5", "ДТ", 25000, 20000, 1000),
        }

        for fuel in PRICES:
            self.stats["liters"][fuel] = 0
            self.stats["fuel_income"][fuel] = 0

        # Создание 8 колонок
        for i in range(1, 9):
            connections = {}
            if i <= 6:
                connections["АИ-92"] = "T1"
            if i <= 4:
                connections["АИ-95"] = "T2"
            else:
                connections["АИ-95"] = "T3"
            if 3 <= i <= 6:
                connections["АИ-98"] = "T4"
            if i >= 3:
                connections["ДТ"] = "T5"

            self.dispensers[i] = Dispenser(i, connections)

    # =================== ФУНКЦИИ ===================
    #Функция обслуживания клиента. В ней мы выбираем колонку, тип топлива, проверяем работает ли колонка и продаём
    def serve_client(self):
        if self.emergency_mode:
            print("АЗС в аварийном режиме!")
            return

        try:
            col = int(input("Выберите колонку (1-8): "))
            dispenser = self.dispensers[col]
        except:
            print("Ошибка!")
            return

        fuels = list(dispenser.connections.keys())
        for i, f in enumerate(fuels, 1):
            print(f"{i}) {f}")

        try:
            choice = int(input("Выберите топливо: "))
            fuel = fuels[choice - 1]
        except:
            print("Ошибка!")
            return

        tank = self.tanks[dispenser.connections[fuel]]

        if not tank.enabled or tank.blocked:
            print("Цистерна недоступна!")
            return

        try:
            liters = float(input("Введите литры: "))
        except:
            print("Ошибка!")
            return

        if liters <= 0:
            print("Некорректное количество!")
            return

        if not tank.dispense(liters):
            print("Недостаточно топлива!")
            return

        cost = liters * PRICES[fuel]
        print(f"К оплате: {cost:.2f} ₽")
        confirm = input("Подтвердить? (y/n): ")

        if confirm.lower() != "y":
            tank.current_volume += liters
            return

        self.stats["income"] += cost
        self.stats["cars"] += 1
        self.stats["liters"][fuel] += liters
        self.stats["fuel_income"][fuel] += cost

        self.history.append(f"{datetime.now()} - Продажа {fuel} {liters} л")
        self.save()
        print("Успешно!")
    #Функция просмотра информации о цистернах
    def show_tanks(self):
        for t in self.tanks.values():
            status = "ВКЛ" if t.enabled else "ВЫКЛ"
            print(f"{t.id} | {t.fuel_type} | {t.current_volume}/{t.max_volume} | {status}")
    #Функция пополнения цистерн топливом
    def refill(self):
        for t in self.tanks.values():
            print(f"{t.id} - {t.fuel_type}")

        tank_id = input("Выберите цистерну: ")
        if tank_id not in self.tanks:
            return

        try:
            liters = float(input("Введите литры: "))
        except:
            return

        if self.tanks[tank_id].refill(liters):
            self.history.append(f"{datetime.now()} - Пополнение {tank_id} {liters} л")
            self.save()
            print("Пополнение выполнено.")
        else:
            print("Переполнение!")
    #Функция перекачки топлива между цистернами
    def transfer(self):
        print("Перекачка топлива")
        from_id = input("Из цистерны: ")
        to_id = input("В цистерну: ")

        if from_id not in self.tanks or to_id not in self.tanks:
            return

        try:
            liters = float(input("Литры: "))
        except:
            return

        if self.tanks[from_id].transfer_to(self.tanks[to_id], liters):
            self.history.append(f"{datetime.now()} - Перекачка {liters} л {from_id}->{to_id}")
            self.save()
            print("Успешно.")
        else:
            print("Ошибка перекачки.")
    #Функция управления работой цистерн
    def manage_tanks(self):
        tank_id = input("Введите ID цистерны: ")
        if tank_id not in self.tanks:
            return

        action = input("1-Включить 2-Отключить: ")
        tank = self.tanks[tank_id]

        if action == "1":
            if tank.current_volume >= tank.min_level:
                tank.enabled = True
                print("Включена.")
            else:
                print("Недостаточный уровень.")
        elif action == "2":
            tank.enabled = False
            print("Отключена.")

        self.save()
    #Функция просмотра статистики заправки
    def show_stats(self):
        print(f"Доход: {self.stats['income']:.2f} ₽")
        print(f"Машин: {self.stats['cars']}")
        for fuel in PRICES:
            print(f"{fuel}: {self.stats['liters'][fuel]} л | {self.stats['fuel_income'][fuel]:.2f} ₽")
    #Функция просмотра недавних действий
    def show_history(self):
        for h in self.history[-10:]:
            print(h)
    #Функция включения аварийного режима
    def emergency(self):
        confirm = input("Подтвердить аварийный режим? (y/n): ")
        if confirm.lower() == "y":
            self.emergency_mode = True
            for t in self.tanks.values():
                t.blocked = True
                t.enabled = False
            self.history.append(f"{datetime.now()} - АВАРИЯ")
            self.save()
            print("АЗС остановлена!")
    #Функция выключения аварийного режима
    def exit_emergency(self):
        self.emergency_mode = False
        print("Аварийный режим снят. Цистерны остаются отключенными.")
        self.save()


# ====================== ЗАПУСК ======================

station = GasStation() #Создаём экземпляр класса заправки
#Игровой цикл
while True:
    print("\n=== СИСТЕМА УПРАВЛЕНИЯ АЗС ===")
    print("1) Обслужить клиента")
    print("2) Состояние цистерн")
    print("3) Пополнение")
    print("4) Статистика")
    print("5) История")
    print("6) Перекачка")
    print("7) Управление цистернами")
    print("8) EMERGENCY")
    print("9) Снять аварийный режим")
    print("0) Выход")

    choice = input("> ")

    if choice == "1":
        station.serve_client()
    elif choice == "2":
        station.show_tanks()
    elif choice == "3":
        station.refill()
    elif choice == "4":
        station.show_stats()
    elif choice == "5":
        station.show_history()
    elif choice == "6":
        station.transfer()
    elif choice == "7":
        station.manage_tanks()
    elif choice == "8":
        station.emergency()
    elif choice == "9":
        station.exit_emergency()
    elif choice == "0":
        break