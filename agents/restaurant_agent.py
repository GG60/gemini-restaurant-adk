from google import genai

# ---------------------------------------------------
# 1. أداة معالجة الطلب (Tool)
# ---------------------------------------------------
def process_food_order(item: str, quantity: int) -> str:
    """
    Process a food order and provide total price and time.
    """
    
    menu = {
        "pizza": {"price": 45, "time": "30 دقيقة"},
        "burger": {"price": 30, "time": "20 دقيقة"},
        "كبسة": {"price": 60, "time": "45 دقيقة"},
    }

    item_clean = item.strip().lower()
    found_item = next(
        (name for name in menu if name.lower() in item_clean or item_clean in name.lower()),
        None
    )

    if found_item:
        unit_price = menu[found_item]["price"]
        total = unit_price * quantity
        time = menu[found_item]["time"]

        return (
            f"تم تأكيد طلب {quantity} × {found_item}. "
            f"السعر الإجمالي: {total} ريال سعودي. "
            f"وقت التحضير المتوقع: {time}."
        )
    else:
        return f"عذراً، '{item}' غير متوفر حالياً في القائمة."


# ---------------------------------------------------
# 2. تعريف وكيل المطعم RestaurantAgent (Class)
# ---------------------------------------------------
class RestaurantAgent:
    def __init__(self, model, name, description, instruction, client):
        self.model = model
        self.name = name
        self.description = description
        self.instruction = instruction
        self.client = client

    def run(self, message):
        """
        يشغل وكيل المطعم باستخدام Gemini
        """
        response = self.client.models.generate_content(
            model=self.model,
            contents=f"{self.instruction}\n\nرسالة العميل: {message}",
            tools=[process_food_order]
        )
        return response.text
