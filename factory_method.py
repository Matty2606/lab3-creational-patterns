from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"Console logger: {message}")


class FileLogger(Logger):
    def log(self, message: str):
        print(f"File logger: {message}")


class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

    def log_message(self, message: str):
        logger = self.create_logger()
        logger.log(message)


class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()


class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()


if __name__ == "__main__":
    factory = ConsoleLoggerFactory()
    factory.log_message("Hello Factory Method")
