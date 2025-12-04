import streamlit as st
import requests
# (1) هذا الرابط سيعمل فقط للاختبار المحلي.
API_URL = "https://abdullah-res-agent-xyz.a.run.app/run"
st.set_page_config(page_title="🤖 مطعم ADK", layout="wide")
st.title("مطعم ADK الذكي 🍔")
st.caption("يتصل هذا التطبيق بوكيل (Agent) يعمل على خادم منفصل.")
# ⚠️ ملاحظة: يجب أن يحتوي ملف requirements.txt على مكتبة 'requests' أيضًا.
user_input = st.text_input("أدخل طلبك هنا، مثال: أريد طلب برجر وبيتزا", key="user_input")
if st.button("أرسل الطلب"):
    if user_input:
        st.info(f"إرسال الطلب: {user_input}")
        try:
            # إرسال طلب HTTP إلى الوكيل الذي يعمل في الخلفية (على Cloud Run لاحقاً)
            response = requests.post(
                API_URL,
                json={"input": user_input}
            )
            # عرض الاستجابة
            if response.status_code == 200:
                result = response.json()
                st.success("✅ استجابة الوكيل:")
                # افتراض أن الاستجابة تحتوي على مفتاح 'output'
                st.markdown(f"**{result.get('output', 'لا توجد استجابة')}**") 
            else:
                st.error(f"❌ خطأ في الاتصال بالوكيل: {response.status_code}")
                st.write(response.text)
        except requests.exceptions.ConnectionError:
            st.error("❌ فشل الاتصال بالخادم. تأكد من أن الوكيل يعمل على Cloud Run.")