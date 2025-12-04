import streamlit as st
import os
from google import genai
from agents.client_agent import ClientAgent

# --- إعداد صفحة Streamlit ---
st.set_page_config(page_title="مطعم عبدالله_res", layout="wide")
st.title("نظام المطعم الذكي 🍽️")
st.caption("🎛️ Gemini + ADK + Streamlit Example")

# --- التحقق من وجود مفتاح API ---
if "GEMINI_API_KEY" not in os.environ:
    st.error("⚠️ يرجى إضافة GEMINI_API_KEY في Secrets داخل Streamlit Cloud")
    st.stop()

# --- إنشاء عميل Gemini ---
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
agent_client = ClientAgent(client)

# --- إدخال المستخدم ---
user_input = st.text_input("اكتب طلبك هنا 👇", key="user_input")

# --- زر التنفيذ ---
if st.button("إرسال الطلب 🚀"):
    if not user_input:
        st.warning("أدخل طلبًا أولاً.")
    else:
        st.info(f"🔎 طلب العميل: {user_input}")

        try:
            response = agent_client.run(user_input)
            st.success("🎉 استجابة الوكيل:")
            st.markdown(f"**{response}**")

        except Exception as e:
            st.error(f"❌ حدث خطأ: {e}")
