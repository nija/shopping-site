"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""
    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    # TODO: need to implement this


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customer types.

    Dictionary will be {email: Customer object}
    """
    customers = {}
    # Janet|Jefferson|janet@hotmail.com|seekrit
    for line in open(filepath):
        (first_name,
        last_name,
        email,
        password) = line.strip().split("|")

        customers[email] = Customer(first_name,
                                    last_name,
                                    email,
                                    password)

    return customers