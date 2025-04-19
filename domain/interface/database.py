#Abstrakcja repozytorium
from abc import ABC, abstractmethod
from typing import Protocol
from core.domain import User  # Załóżmy, że mamy model User


class DatabasePort(Protocol):
    @abstractmethod
    def connect(self, connection_string: str) -> None:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def save_user(self, user: User) -> None:
        pass