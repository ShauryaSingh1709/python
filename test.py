import google.generativeai as genai

genai.configure(api_key="AIzaSyDGgdOuFui2yhHiYSYYXYHXWu35EGJEdyY")

try:
    models = list(genai.list_models())
    for m in models:
        print(m.name)
except Exception as e:
    print("Error:", e)
