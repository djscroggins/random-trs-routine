import os
import random
import subprocess

from requests import Session
from bs4 import BeautifulSoup
from dotenv import load_dotenv


class RoutineManager:
    def __init__(self, email: str, password: str, minutes: int):
        self._email = email
        self._password = password
        self._minutes = minutes
        self._login_url = 'https://members.thereadystate.com/wp-login.php'
        self._daily_maintenance_url = 'https://members.thereadystate.com/daily-maintenance/'
        self._html = self._get_raw_html()
        self._routine_map = self._generate_routine_map()

    @property
    def routine(self):
        routines = self._routine_map.get(self._minutes)
        return random.choice(routines)

    def _get_raw_html(self):
        with Session() as session:
            post = session.post(self._login_url, data={'log': self._email, 'pwd': self._password})
            r = session.get(self._daily_maintenance_url)
        return r.text

    def _generate_routine_map(self):
        soup = BeautifulSoup(self._html, 'html.parser')
        sections = soup.find_all('section', {'class': 'has-parallax'})[1:]
        _routine_map = {}

        for i, section in enumerate(sections):
            routine_length = (i + 1) * 10
            _routine_map[routine_length] = []
            a_tags = section.find_all('a', {'style': 'color:#000'})
            for a_tag in a_tags:
                _routine_map.get(routine_length).append(a_tag.text)

        return _routine_map

    def open_daily_maintenance_page(self):
        subprocess.run(['open', f'{self._daily_maintenance_url}'])


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
