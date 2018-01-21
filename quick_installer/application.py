from abc import ABC, abstractmethod


class Application(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass

    @abstractmethod
    def is_installed(self) -> bool:
        pass

    def __str__(self):
        return f"Application(name={self.name})"
