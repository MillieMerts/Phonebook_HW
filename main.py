import re
from pprint import pprint

import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

phone_pattern = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
new_pattern = r"+7 (\2)\3-\4-\5 \6\7"



def fix_list(contact_list):
    new_list = []
    for data in contact_list:
        fullname = ' '.join(data[:3]).split(' ')
        result = [fullname[0], fullname[1], fullname[2], data[3], data[4],
                  re.sub(phone_pattern, new_pattern, data[5]),
                  data[6]]
        new_list.append(result)
        phone_book = {}
        for contact in new_list:
            if contact[0] in phone_book:
                contact_value = phone_book[contact[0]]
                for i in range(len(contact_value)):
                    if contact[i]:
                        contact_value[i] = contact[i]
            else:
                phone_book[contact[0]] = contact
    return list(phone_book.values())


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(fix_list(contacts_list))
