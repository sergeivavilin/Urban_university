class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    # Старый вариант с ошибкой
    # def start(self):
    #     finishers = {}
    #     place = 1
    #     while self.participants:
    #         for participant in self.participants:
    #             participant.run()
    #             if participant.distance >= self.full_distance:
    #                 finishers[place] = participant
    #                 place += 1
    #                 self.participants.remove(participant)
    #
    #     return finishers

    def start(self):
        finishers = {}
        results_list = []

        # Для определения победителя считаем время бега на каждого участника
        for participant in self.participants:
            time_participant = self.full_distance / participant.speed
            results_list.append((time_participant, participant.name))

        # сортируем по времени бега
        results_list.sort(key=lambda x: x[0])

        # Собираем в словарь участников и присваиваем им места согласно времени бега
        for i in range(1, len(results_list) + 1):
            finishers[i] = results_list[i - 1][1]

        return finishers
