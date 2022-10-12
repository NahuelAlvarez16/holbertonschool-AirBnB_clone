#!/usr/bin/python3
import datetime
from uuid import uuid4
import uuid


class BaseModel:
    number_of_instances = 0

    def __init__(self):
        self.id = uuid.uuid4() + self.number_of_instances
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.number_of_instances += 1

    def __str__(self):
        print(f"[{type(self)}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        return self.__dict__