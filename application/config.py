from environs import Env

env = Env()

env.read_env()

with env.prefixed("APP_"):
    with env.prefixed("DB_"):
        DB_CONFIG = dict(
            database=env.str("NAME"),
            user=env.str("USER"),
            password=env.str("PASSWORD"),
            host=env.str("HOST"),
            port=env.int("PORT"),
        )
