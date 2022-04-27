import os

PROJECT_DIRECTORY = os.getcwd()


if __name__ == '__main__':

    # post-gen Configuration
    os.system('bash --rcfile post-gen.sh')