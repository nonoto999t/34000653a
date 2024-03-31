import requests
import json
import time

# กำหนด URL ของ API สำหรับเข้าห้อง
enter_room_url = "https://api.escapemaster.net/escape_game/enter_room"

# กำหนด URL ของ API สำหรับการวางเดิมพัน
bet_url = "https://api.escapemaster.net/escape_game/bet"

# กำหนด headers สำหรับการเข้าห้อง
enter_room_headers = {
    "User-ID": "1100057955",
    "Content-Type": "application/json",
    "User-Login": "login_v2",
    "User-Secret-Key":
    "aa77d40b42ca0357d2f48d9f5b6941e20f1ac2218fd72562c327d0c3a36184c5",
    "Accept-Language": "th-TH,th;q=0.9",
    "Origin": "https://escapemaster.net",
    "Referer": "https://escapemaster.net/",
}

# กำหนด headers สำหรับการวางเดิมพัน
bet_headers = {
    "User-ID": "1100057955",
    "Content-Type": "application/json",
    "User-Login": "login_v2",
    "User-Secret-Key":
    "aa77d40b42ca0357d2f48d9f5b6941e20f1ac2218fd72562c327d0c3a36184c5",
    "Accept-Language": "th-TH,th;q=0.9",
    "Origin": "https://escapemaster.net",
    "Referer": "https://escapemaster.net/",
}

# กำหนดแพ็กเกจสำหรับการเข้าห้อง
enter_room_payload = {
    "asset_type": "BUILD",
    "user_id": 1100057955,
    "room_id": 1,
}

# กำหนดแพ็กเกจสำหรับการวางเดิมพัน
bet_payload = {
    "asset_type": "BUILD",
    "user_id": 1100057955,
    "room_id": 1,
    "bet_amount": 1.25,
}


def switch_rooms():
  room_ids = [1, 2, 3, 4, 5, 6, 7, 8]
  delay = 1  # กำหนดเวลาประบดีเลย์เริ่มต้นเป็น 1 วินาที
  for _ in range(30000000000000000000000):  # วนลูป 30 รอบ
    for room_id in room_ids:
      enter_room_payload['room_id'] = room_id
      bet_payload[
          'room_id'] = room_id  # กำหนดห้องในแพ็กเกจการวางเดิมพันเพื่อสลับห้อง

      try:

        # วางเดิมพัน
        bet_response = requests.post(bet_url,
                                     headers=bet_headers,
                                     json=bet_payload,
                                     verify=False)
        if bet_response.status_code == 200:
          print('{"code":0,"data":null,"msg":"bet1"}')
        else:
          print(
              f'เกิดข้อผิดพลาดในการวางเดิมพัน {room_id}: {bet_response.status_code}'
          )

      except Exception as e:
        print(f'เกิดข้อผิดพลาด: {e}')

      time.sleep(delay)  # รอจนกว่าจะถึงเวลาประบดีเลย์

      # เพิ่มเวลาประบดีเลย์เพื่อสลับห้องต่อไป
      delay += 0.1


# เรียกใช้งานฟังก์ชันสลับห้อง
switch_rooms()
time.sleep(0)
