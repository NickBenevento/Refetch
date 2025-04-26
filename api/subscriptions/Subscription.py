from api.subscriptions.Product import Product


class Subscription:

    def __init__(self, name: str, products: list[Product] = []) -> None:
        self._subscription_name = name
        self._products = products
        self._notification_queue: list[Product] = []

    def fetch(self) -> None:
        """Check each of the products to see if they are in stock"""
        for product in self._products:
            old_status = product.get_status()
            # if the product is in stock
            new_status = product.check_status()
            # If there was a status change
            if old_status != new_status:
                # add to notification queue
                self._notification_queue.append(product)

    def notify(self) -> None:
        email_body = ""

        for notification in self._notification_queue:
            # add to email
            email_body += notification.__repr__ + "\n"

        # send email
        self.send_email(email_body)

    def send_email(contents: str) -> None:
        print(f"Email contents: {contents}")
        pass
