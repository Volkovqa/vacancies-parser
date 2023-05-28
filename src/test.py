from src.api_classes import HHru, SuperJob

sj_engine = SuperJob("python")

txt = sj_engine.get_request()
print(txt.json())
