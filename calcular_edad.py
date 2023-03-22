from datetime import datetime


def calculate_age(date_birth):
    current_date = datetime.now().date()
    date_birth = datetime.strptime(date_birth, '%d/%m/%Y').date()

    # Calculando edad en años
    years = current_date.year - date_birth.year
    if current_date.month <= date_birth.month:
        if current_date.month < date_birth.month:
            years -= 1
        elif current_date.month == date_birth.month and current_date.day < date_birth.day:
            years -= 1

    # Calculando edad en meses
    months = years * 12
    if current_date.month <= date_birth.month:
        months += 12 - date_birth.month + current_date.month
        if current_date.day < date_birth.day:
            months -= 1
    else:
        months += current_date.month - date_birth.month
        if current_date.day < date_birth.day:
            months -= 1

    # Calcular dias
    days = current_date - date_birth
    print(f'Edad en años: {years}')
    print(f'Edad en meses: {months}')
    print(f'Edad en dias: {days.days}')


date = input("Ingrese la fecha de nacimiento,en el siguiente orden dd/mm/aaaa: ")
calculate_age(date)
