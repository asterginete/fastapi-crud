# This is a mockup and should be replaced with actual payment gateway integration.
from typing import Optional

class PaymentGateway:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def process_payment(self, amount: float, payment_method: str) -> Optional[str]:
        """
        Process a payment and return a transaction ID if successful.
        """
        # Logic to process payment using a payment gateway.
        # For the sake of this example, we'll assume the payment is always successful and return a mock transaction ID.
        return "mock_transaction_id_12345"

    def refund_payment(self, transaction_id: str) -> bool:
        """
        Refund a payment based on a transaction ID.
        """
        # Logic to refund a payment using a payment gateway.
        # For the sake of this example, we'll assume the refund is always successful.
        return True

# In a real-world scenario, you'd initialize the PaymentGateway with actual API keys and other necessary configurations.
payment_service = PaymentGateway(api_key="your_payment_gateway_api_key")
