from datetime import datetime

hour = datetime.now().hour

if hour <= 12:
    print("오전입니다.")
else:
    print("오후입니다.")

