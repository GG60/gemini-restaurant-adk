from agents.restaurant_agent import RestaurantAgent

class ClientAgent:
    def __init__(self, client):
        self.agent = RestaurantAgent(
            model="gemini-2.5-flash",
            name="ClientAgent",
            description="Client requesting food orders.",
            instruction=(
                "أنت عميل تطلب طعاماً من وكيل المطعم. "
                "اكتب الطلب بشكل واضح وبالعربية."
            ),
            client=client
        )

    def run(self, message):
        if not message.strip():
            return "❌ لا يمكن إرسال رسالة فارغة."
        return self.agent.run(message).output
