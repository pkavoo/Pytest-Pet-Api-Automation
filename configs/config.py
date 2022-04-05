from environs import Env

env = Env()
env.read_env()

environments = {
    "local": {
        "host_url": "https://petstore.swagger.io/v2/",
    }

}


def get_environment():
    """Retrieve environment variables"""
    app_env = environments.get(env("app_env", "local"))
    print(f"""Tests will be run against {app_env} environment""")
    return app_env
