import sys
from colorama import Fore

def count_logs_by_level(logs: list) -> dict:
    log_counts = {}

    for log in logs:
        # get log level
        log_lvl = log['log_level']

        update_count = lambda level: log_counts.update({level: log_counts.get(level, 0) + 1})
        update_count(log_lvl)
    
    return log_counts
            

def display_log_counts(counts: dict):
    counts_table = "Рівень логування | Кількість\n"
    counts_table += "-----------------|-----------\n"

    for key, value in counts.items():
        if is_filtered and logging_level:
            if key.lower() == logging_level:
                key = Fore.MAGENTA + key.ljust(17, " ") + Fore.RESET
        counts_table += key.ljust(17, " ") + "| " + str(value) + "\n"

    return counts_table

def filter_logs_by_level(logs: list, level: str) -> list:
    logs_by_level = list()

    for log in logs:
        if log['log_level'].lower() == level:
            logs_by_level.append(log)
    print(f"\nДеталі логів для рівня '{level.upper()}'")

    for log in logs_by_level:
        print(log['log_date'], log['log_time'], f"- {log['log_msg']}")

def load_logs(file_path: str) -> list:
    logs_list = list()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                logs_list.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Error: file {file_path} not found!")
    except Exception as e:
        print(f"An error occured: {e}")
    
    return logs_list

def parse_log_line(line: str) -> dict:
    splited_log_line = line.strip().split()

    log_data = dict({
        "log_date": splited_log_line[0],
        "log_time": splited_log_line[1],
        "log_level": splited_log_line[2],
        "log_msg": ' '. join(splited_log_line[3:])
    })

    return log_data

def main():
    global is_filtered, logging_level
    sys_args = sys.argv
    
    if len(sys_args) < 2:
        print("Enter a first argument as file path and optional second argument as log level")
        return

    file_path = sys_args[1]

    logs = load_logs(file_path)

    if len(sys_args) == 3:
        log_level = sys_args[2]
        is_filtered = True
        logging_level = log_level
    else:
        log_level = False
        is_filtered = False
        logging_level = False

    print(display_log_counts(count_logs_by_level(logs)))

    if log_level:
        filter_logs_by_level(logs, log_level)

if __name__ == "__main__":
    main()