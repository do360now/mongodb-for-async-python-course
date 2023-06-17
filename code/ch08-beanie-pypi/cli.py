import asyncio

from infrastructure import mongo_setup
from services import package_service, user_service


async def main():
    print_header()

    await mongo_setup.init_connection('pypi')
    print()
    await summary()

    while True:
        print("[s] Show summary statistics")
        print("[f] Search the database for packages")
        print("[p] Most recently updated packages")
        print("[u] Create a new user")
        print("[r] Create a release")
        print("[x] Exit program")
        resp = input("Enter the character for your command: ").strip().lower()
        print('-' * 40)

        match resp:
            case 's':
                await summary()
            case 'f':
                await search_for_package()
            case 'p':
                await recently_updated()
            case 'u':
                await create_user()
            case 'r':
                await create_release()
            case 'x':
                break
            case _:
                print("Sorry, we don't understand that command.")


def print_header():
    pad = 30
    print('/' + "-" * pad + '\\')
    print('|' + ' ' * pad + '|')
    print('|        PyPI CLI v1.0 ' + ' ' * (pad - 22) + '|')
    print('|' + ' ' * pad + '|')
    print('\\' + "-" * pad + '/')
    print()


async def summary():
    package_count = await package_service.package_count()
    release_count = await package_service.release_count()
    user_count = await user_service.user_count()

    print('PyPI Package Stats')
    print(f'Packages: {package_count:,}')
    print(f'Releases: {release_count:,}')
    print(f'Users: {user_count:,}')
    print()


async def search_for_package():
    print("searching")


async def recently_updated():
    packages = await package_service.recently_updated()
    for n, p in enumerate(packages, start=1):
        print(f'{n}. {p.id} ({p.last_updated.date().isoformat()}) - {p.summary[:80]}')
    print()


async def create_user():
    print("create_user")


async def create_release():
    print("create_release")


if __name__ == '__main__':
    asyncio.run(main())