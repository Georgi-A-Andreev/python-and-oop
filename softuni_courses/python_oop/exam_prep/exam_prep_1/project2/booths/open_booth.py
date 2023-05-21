from project2.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.5

    def reserve(self, number_of_people):
        price_for_reservation = OpenBooth.PRICE_PER_PERSON * number_of_people
        self.price_for_reservation = price_for_reservation
        self.is_reserved = True
