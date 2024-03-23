import csv
import re
from pprint import pprint

with open('phonebook_raw.csv', 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)


def format_all_in_last_name(contact):
    s_occur = contact[0].count(" ")
    # print(s_occur)
    if s_occur == 2:
        contact[0], contact[1], contact[2] = contact[0].split()
    elif s_occur == 1:
        contact[0], contact[1] = contact[0].split()
    return

def format_all_in_first_name(contact):
    s_occur = contact[1].count(" ")
    # print(s_occur)
    if s_occur == 1:
        contact[1], contact[2] = contact[1].split()
    return

def format_phone(phone):
    def print_phone(phone):
        return f'+7({phone[:3]}){phone[3:6]}-{phone[6:8]}-{phone[8:10]}'
    if not phone:
        return
    phone = re.sub(r'[^0-9]', '', phone)[1:]
    if len(phone) > 10:
        additional = phone[10:]
        phone = phone[:10]
        return f'{print_phone(phone)} доб. {additional}'
    elif len(phone) == 10:
        return print_phone(phone)

def merge_fio(contact_list, contact, n):
    list_len = len(contact)
    for i in range(3, list_len):
        if contact[i]: contact_list[n][i] = contact[i]

def delete_contact(contacts_list, n):
    del contacts_list[n]


fio_list = []
contacts_to_delete = []

for contact in contacts_list:
    if not contact[1]:
        format_all_in_last_name(contact)
    elif not contact[2]:
        format_all_in_first_name(contact)
    if contact[5]:
        contact[5] = format_phone(contact[5])
    fio = ' '.join(contact[:3])
    fi = ' '.join(contact[:2])
    # print(fio + '|' )
    # print(fi + '|')
    # print(fio_list)
    for n, fio2 in enumerate(fio_list):
        if fi in fio2:
            # print(f'match {fio} with {fio2} n = {n}')
            merge_fio(contacts_list, contact, n)
            contacts_to_delete.append(len(fio_list))
            fio_list.append('')
            break
    else: fio_list.append(fio)

for n in sorted(contacts_to_delete, reverse=True):
    # print(n)
    delete_contact(contacts_list, n)

# pprint(fio_list)
pprint(contacts_list)

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)