from models.basemodel import Config

Config.Base.metadata.create_all(Config.engine)