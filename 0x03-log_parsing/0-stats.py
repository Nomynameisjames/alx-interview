#!/usr/bin/python3
''' import files'''
import sys
import re

'''
    basic summary of the log_parser algorithm
    1. read input from stdin
    2. split line into array using split
    3. get file size and status code
    based on this format [IP Address] - [user] [date] "GET /projects/260
                            HTTP/1.1" [status code] [file size]
    4. check if status code is in dictionary
    5. if true, increment the value by 1
    6. check if the file size is a number
    7. if true, add to total size
    8. if count is 10, print the stats
    9. if user presses CTRL + C, print stats
'''


def print_stats():
    '''
        reading input from stdin. using while loop and break when it
        encounters an end-of-file character
    '''
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                    '404': 0, '405': 0, '500': 0}
    file_size = 0
    count = 0
    try:
        for line in sys.stdin:
            # split line into array using split
            line = line.split()
            if len(line) > 2:
                file_size = line[-1]
                status = line[-2]
                # check if status code is in dictionary
                if status in status_codes:
                    status_codes[status] += 1
                # check if the file size is a number
                if re.search(r'\d', file_size):
                    total_size += int(file_size)
                count += 1
                # if count is 10, print the stats
                if count % 10 == 0:
                    print(f"File size: {total_size}")
                    for key, value in sorted(status_codes.items()):
                        if value != 0:
                            print(f"{key} : {value}")

    except KeyboardInterrupt:
        # if user lresses CTRL + C, print stats
        print(f"File size: {total_size}")
        for key, value in sorted(status_codes.items()):
            if value != 0:
                print(f"{key}: {value}")
        raise


if __name__ == "__main__":
    print_stats()
