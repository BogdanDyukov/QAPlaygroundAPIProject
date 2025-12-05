from faker import Faker


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def email(self, domain: str | None = None) -> str:
        return self.faker.email(domain=domain)

    def password(self) -> str:
        return self.faker.password()

    def name(self) -> str:
        return self.faker.name()

    def nickname(self) -> str:
        return self.faker.user_name()


fake = Fake(faker=Faker())
