from .restaurant_agent import RestaurantAgent

# -----------------------------------------------
# تعريف وكيل العميل (Client Agent)
# -----------------------------------------------

client_agent = RestaurantAgent(
    model='gemini-2.5-flash',
    name='ClientAgent',
    description='Represents a customer placing a food order.',
    instruction=(
        "You are a hungry customer looking to order food from the restaurant agent. "
        "Your goal is to clearly request an item and the quantity. You must speak Arabic."
    )
)