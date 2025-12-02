from google.adk.agents.llm_agent import Agent 
# -----------------------------------------------
# 1. تعريف أداة معالجة الطلب (Tool/Function)
# -----------------------------------------------

def process_food_order(item: str, quantity: int) -> str:
    """
    Processes a food order, checks availability, and confirms the price in SAR.
    
    Args:
        item: The name of the food item (e.g., 'Pizza', 'Burger').
        quantity: The number of items to order.
        
    Returns:
        A confirmation message with the calculated total price in SAR.
    """
    
    menu = {
        "pizza": {"price": 45, "time": "30 minutes"},
        "burger": {"price": 30, "time": "20 minutes"},
        "كابسة": {"price": 60, "time": "45 minutes"}
    }
    
    item_lower = item.lower().strip()
    found_item = next((k for k in menu if k in item_lower or item_lower in k.lower()), None)
    
    if found_item:
        unit_price = menu[found_item]["price"]
        estimated_time = menu[found_item]["time"]
        total_price = unit_price * quantity
        
        return (
            f"Restaurant Agent: Order for {quantity} x {found_item} confirmed. "
            f"Total Price: {total_price} SAR. "
            f"Estimated preparation time: {estimated_time}."
        )
    else:
        return f"Restaurant Agent: عذراً، '{item}' غير متوفرة. قائمة طعامنا تشمل البيتزا، البرجر، والكابسة."

# -----------------------------------------------
# 2. تعريف وكيل المطعم (Restaurant Agent)
# -----------------------------------------------

restaurant_agent = Agent(
    model='gemini-2.5-flash',
    name='RestaurantAgent',
    description='Handles food order processing and menu inquiries for Abdullah_res in Riyadh.',
    instruction=(
        "You are the professional order processor for Abdullah_res in Riyadh. "
        "Your responses must be in Arabic, polite, and clearly state the prices in SAR. "
        "Use the 'process_food_order' tool whenever the client requests an item and quantity."
    ),
    tools=[process_food_order], 
)