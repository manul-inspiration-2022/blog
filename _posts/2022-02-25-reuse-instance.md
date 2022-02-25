---
title: "Reusing instance in python"
date: 2022-02-24T17:00:00+07:00
categories:
  - blog
tags:
  - python
  - quick note
---
Description

```python
from __future__ import annotations

class Simple():
    _instances = {}

    def __new__(cls, key: str):
        if key not in cls._instances:
            cls._instances[key] = super().__new__(cls)

        return cls._instances[key]

```
