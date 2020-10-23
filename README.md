# Random TRS Routine

During the pandemic I've been working out at home a lot and have really gotten into mobility training, specifically using
the excellent resources provided by [The Ready State](https://thereadystate.com).

I was pretty bored the other night, and who knows, maybe boredom is actually the mother of invention.
Sat down and made a simple program to randomly select which mobility exercise I want to complete.

The program prompts you for your desired routine time interval, creates a Requests session, logs in, parses the [Daily Maintenance](https://members.thereadystate.com/daily-maintenance/) page
to construct a list of available maintenance routines, randomly selects one for you, then opens the website.

# Prerequisites

- A Python interpreter (I used 3.8 but should play nicely with most recent versions)
- Login info for your Ready State account
- Subprocess for opening website is OSX specific for now

# Installation and Setup

```bash
python -m venv .env-test \
    && source $_/bin/activate \
    && pip install -U pip \
    && pip install -r requirements.txt
```

Create .env file in root with following content:
```bash
USER_EMAIL=your-email
USER_PASSWORD=your-password
```

# Usage
```bash
python select-trs-routine.py

# Sample Output

Enter length of routine in minutes: 10, 20, 30: 10

Routine: Consistent vs. Heroic
Opening TRS Daily Maintenance ...

```
