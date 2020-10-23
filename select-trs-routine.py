import random
import subprocess


class RoutineManager:
    def __init__(self, minutes: int):
        self._minutes = minutes
        self._daily_maintenance_url = 'https://members.thereadystate.com/daily-maintenance/'
        self._routine_map = {
            10: ['Elbow Grease', 'Thompson', 'Hawk', 'Gorbachev', 'Zoom', 'Cerberus', 'Kevin Hart', 'Madden', 'Irving',
                 'Low Back Bake Out', 'Margaret', 'Consistent vs. Heroic'],
            20: ['Trifecta', 'Ruth', 'Emerson', 'Chadwick', 'GZA', 'Good Trouble', 'Rusty Hinges', 'Desk Jockey',
                 'Atreides',
                 'Derek Jeter', 'Amelia', 'Kardashian'],
            30: ['EVH', 'Dick Dale', 'Rusch Hour', 'San Dimas', 'Orlando', 'Mamba', 'Talent', 'Lombardi', 'Jerry Rice',
                 'Hebe',
                 'Text Neck Be Gone', 'The Rock']
        }

    @property
    def routine(self):
        routines = self._routine_map.get(self._minutes)
        return random.choice(routines)

    def open_daily_maintenance_page(self):
        subprocess.run(['open', f'{self._daily_maintenance_url}'])


if __name__ == '__main__':
    prompt = 'Enter length of routine in minutes: 10, 20, 30: '
    accepted_lengths = {10, 20, 30}
    while True:
        try:
            user_minutes = int(input(prompt))
            if user_minutes not in accepted_lengths:
                raise ValueError
            rm = RoutineManager(user_minutes)
            print(f'\nRoutine: {rm.routine}\nOpening TRS Daily Maintenance ...\n')
            rm.open_daily_maintenance_page()
            break
        except ValueError:
            prompt = 'Make sure you enter your length as a number and one of these three values: 10, 20 or 30: '
