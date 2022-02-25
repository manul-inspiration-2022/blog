---
title: "Extending built-ins class in python"
date: 2022-02-24T17:00:00+07:00
categories:
  - blog
tags:
  - python
  - quick note
---

Type: List, Dict, Set

```python
from __future__ import annotations
from typing import List

class ContactList(List['Contact']):
    def show_all(self):
        for contact in self:
            print(contact)


class Contact():
    all_contacts = ContactList()

    def __init__(self, name: str, address=''):
        self.name = name
        self.address = address

        Contact.all_contacts.append(self)
    
    def __repr__(self) -> str:

        return f'{self.name} {self.address}'

```