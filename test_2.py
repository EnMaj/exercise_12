class AirTicket:
    passenger_name = None
    _from = None
    to = None
    date_time = None
    flight = None
    seat = None
    _class = None
    gate = None

    def __repr__(self):
        str = (self.passenger_name + self._from + self.to + self.date_time
               + self.flight + self.seat + self._class + self.gate)
        return str

class Load:
    data = []

    @staticmethod
    def write(file):
        with open(file, 'r') as text_file:
            for line in text_file:
                array_ticket = list(line.split(';'))
                current_ticket = AirTicket()
                current_ticket.passenger_name = '|' + array_ticket[0] + ' '*(16 - len(array_ticket[0]))
                current_ticket._from = '|' + array_ticket[1] + ' '
                current_ticket.to = '|' + array_ticket[2]
                current_ticket.date_time ='|' + array_ticket[3]
                current_ticket.flight = '|' + array_ticket[4] + ' '*(20 - len(array_ticket[4]))
                current_ticket.seat ='|' + array_ticket[5] + ' '*(4-len(array_ticket[5]))
                current_ticket._class ='|' + array_ticket[6] + ' '*2
                current_ticket.gate = '|' +array_ticket[7] + ' '*2 + '|'
                Load.data.append(current_ticket)
        Load.data.pop(0)
        return Load.data

tickets = Load.write('tickets.txt')
print('-' * 79)
print('|     NAME       |FROM|TO |   DATE/TIME    |       FLIGHT       |SEAT|CLS|GATE|')
print('=' * 79)
for item in Load.data:
    print(item)
print('-' * 79)




