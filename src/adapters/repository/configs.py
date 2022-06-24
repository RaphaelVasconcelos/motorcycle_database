from dataclasses import dataclass
import os


@dataclass
class MotorcycleMongoDbRepositoryConfig:
    user: str = os.environ['MONGODB_USER']
    password: str = os.environ['MONGODB_PASSWORD']
    cluster: str = os.environ['MONGODB_CLUSTER']
    database: str = os.environ['MONGODB_DATABASE']
    connection_string: str = f'mongodb+srv://{user}:{password}@{cluster}.y4oha.mongodb.net/?retryWrites=true&w=majority'
