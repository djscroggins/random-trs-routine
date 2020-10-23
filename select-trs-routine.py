import os

from dotenv import load_dotenv

from routine_manager import RoutineManager

if __name__ == '__main__':
    prompt = 'Enter length of routine in minutes: 10, 20, 30: '
    accepted_lengths = {10, 20, 30}
    load_dotenv()
    _email = os.getenv('USER_EMAIL')
    _password = os.getenv('USER_PASSWORD')
    while True:
        try:
            user_minutes = int(input(prompt))
            if user_minutes not in accepted_lengths:
                raise ValueError
            rm = RoutineManager(email=_email, password=_password, minutes=user_minutes)
            print(f'\nRoutine: {rm.routine}\nOpening TRS Daily Maintenance ...\n')
            rm.open_daily_maintenance_page()
            break
        except ValueError:
            prompt = 'Make sure you enter your length as a number and one of these three values: 10, 20 or 30: '
