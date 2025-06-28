#!/bin/bash
python main.py
printf "\n === Task 3. Log analysing functionality === \n\n"
printf "print all logs \n\n"
python log_analyse.py app.log
printf "print all logs and mark specified log level \n\n"
python log_analyse.py app.log error
printf "\n === Task 4. console assistant functionality === \n\n"
python assistant.py