import os
import json

# กำหนดพาธของโฟลเดอร์ CHATBOT_LEARNING
chatbot_learning_dir = "CHATBOT_LEARNING"

# ตรวจสอบว่าโฟลเดอร์ CHATBOT_LEARNING มีอยู่หรือไม่ และสร้างถ้ายังไม่มี
if not os.path.exists(chatbot_learning_dir):
    os.makedirs(chatbot_learning_dir)

# ใช้ os.path.join() เพื่อสร้างพาธของไฟล์ OuOBot_Data.json ในโฟลเดอร์ CHATBOT_LEARNING
data_file_path = os.path.join(chatbot_learning_dir, "OuOBot_Data.json")

# ตรวจสอบว่าไฟล์ OuOBot_Data.json มีอยู่หรือไม่ และสร้างถ้ายังไม่มี
if not os.path.exists(data_file_path):
    # สร้างไฟล์ OuOBot_Data.json ถ้ายังไม่มี
    with open(data_file_path, "w") as data_file:
        json.dump({}, data_file)

def load_memory():
    # อ่านข้อมูลจาก OuOBot_Memory หากมี
    try:
        with open("OuOBot_Memory.json", "r") as memory_file:
            memory = json.load(memory_file)
    except FileNotFoundError:
        memory = {}
    return memory

def save_memory(memory):
    # บันทึกข้อมูลลงใน OuOBot_Memory
    with open("OuOBot_Memory.json", "w") as memory_file:
        json.dump(memory, memory_file, indent=4)

def get_response(question, memory):
    # ตรวจสอบว่ามีคำตอบใน OuOBot_Memory หรือไม่
    if question in memory:
        return memory[question]
    else:
        return "เอ่อออ หนูไม่รู้อะบอกหน่อยสิ"

def main():
    # โหลดข้อมูลจาก OuOBot_Memory
    memory = load_memory()

    # เริ่มคำสนทนาด้วย "Hi How are you?" หรือ "Hi How are you today?"
    print("OuOBot: Hi How are you today?")

    while True:
        user_input = input("คุณ: ").lower()  # แปลงข้อความเป็นตัวพิมพ์เล็ก
        if user_input == "Bye":
            print("แล้วเจอกันค่ะ")
            break

        # หาคำตอบจาก OuOBot_Memory หรือใช้คำว่า "เอ่อออ หนูไม่รู้อะบอกหน่อยสิ" หากไม่พบคำตอบ
        response = get_response(user_input, memory)
        print("OuOBot: ", response)

        # ถ้าไม่มีคำตอบใน OuOBot_Memory ให้บันทึกคำถามและคำตอบลงใน OuOBot_Memory
        if response == "เอ่อออ หนูไม่รู้อะบอกหน่อยสิ":
            new_response = input("คำตอบที่ถูกต้องคืออะไรคือะไรหรอ? : ")
            memory[user_input] = new_response
            save_memory(memory)

if __name__ == "__main__":
    main()
