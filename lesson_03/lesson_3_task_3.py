from address import Address
from mailing import Mailing

address_from = Address(index="188800", city="Выборг", street="Ленина пр.", house="1", apartment="10")
address_to = Address(index="101000", city="Москва", street="ул. Тверская", house="24", apartment="5")

my_mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=1350.75,
    track="RU123456789HK"
)


output_format = (
    f"Отправление {my_mailing.track} из "
    f"{my_mailing.from_address.index}, {my_mailing.from_address.city}, {my_mailing.from_address.street}, {my_mailing.from_address.house} - {my_mailing.from_address.apartment} "
    f"в {my_mailing.to_address.index}, {my_mailing.to_address.city}, {my_mailing.to_address.street}, {my_mailing.to_address.house} -{my_mailing.to_address.apartment}. "
    f"Стоимость {my_mailing.cost} рублей."
)

print(output_format)