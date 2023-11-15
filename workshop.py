import os

def End(text):
    print(text)
    print("**************************************")
    exit #--"จบโปรแกรม"
    #inputChoice()

def Creation():
    try:
        name = input("ป้อนชื่อไฟล์วิชาเพื่อเก็บข้อมูลคะแนน(xxxxx.txt): ")
        if not name.endswith(".txt") or name.startswith("."):
            print("-------------------------------------")
            print("ชื่อ-นามสกุลไฟล์ไม่ถูกต้องกรุณาป้อนใหม่")
            print("-------------------------------------")
            Creation()
            return
        print("**************************************")
        stName = input("ป้อนชื่อ-สกุลนักเรียน: ")
        def getGrades():
            try:
                stMid = float(input("ป้อนคะแนนกลางภาค: "))
                stFinal = float(input("ป้อนคะแนนปลายภาค: "))
                stAll = float(input("ป้อนคะแนนเก็บ: "))
                return stMid, stFinal, stAll
            except ValueError:
                print("ป้อนตัวเลขเท่านั้น")
                getGrades()
            except:
                print("Exception found...")
                inputChoice()
        stMid, stFinal, stAll = getGrades()
        file = open(f"{name}.txt", "w", encoding="utf-8")
        file.writelines([
            f"ชื่อ-สกุล: {stName}\n"
            f"คะแนนกลางภาค: {stMid}\n"
            f"คะแนนปลายภาค: {stFinal}\n"
            f"ป้อนคะแนนเก็บ: {stAll}\n"
            ]
        )
        ##file.write(f"ชื่อ-สกุล: {stName}")
        ##file.write(f"คะแนนกลางภาค: {stMid}")
        ##file.write(f"คะแนนปลายภาค: {stFinal}")
        ##file.write(f"ป้อนคะแนนเก็บ: {stAll}")
        file.close()
        print("""
            **************************************
            สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว
            **************************************""")
        inputChoice()
    except:
        print("Exception found...")
        inputChoice()

def DeleteFile():
    print("""
        **************************************
                    เลือกวิชาและลบไฟล์
        **************************************""")
    try:
        theFiles = os.listdir()
        theFiles.remove("workshop.py")
        if not theFiles == []:
            for i in theFiles:
                if i.endswith(".txt"):
                    print(i)
            theFile = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ")
            if os.path.exists(theFile):
                os.remove(theFile)
                print("""
        **************************************
                    ลบไฟล์ข้อมูลเรียบร้อย
        **************************************""")
                inputChoice()
            else:
                End("คุณพิมพ์ชื่อไฟล์ผิด")
        else:
            End("ไม่มีไฟล์วิชาใดๆอยู่เลย")
    except FileNotFoundError:
        print("ระบบค้นหาไฟล์ไม่เจอ โปรดลองอีกครั้ง")
        inputChoice()
    except:
        print("Exception found...")
        inputChoice()

def AppendFile():
    print("""
        **************************************
               เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ 
        **************************************""")
    try:
        theFiles = os.listdir()
        theFiles.remove("workshop.py")
        if not theFiles == []:
            for i in theFiles:
                if i.endswith(".txt"):
                    print(i)
            theFile = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ")
            if os.path.exists(theFile):
                thisFile = open(f"{theFile}", "a", encoding="utf-8")
                stName = input("ป้อนชื่อ-สกุลนักเรียน: ")
                def getGrades():
                    try:
                        stMid = float(input("ป้อนคะแนนกลางภาค: "))
                        stFinal = float(input("ป้อนคะแนนปลายภาค: "))
                        stAll = float(input("ป้อนคะแนนเก็บ: "))
                        return stMid, stFinal, stAll
                    except ValueError:
                        print("ป้อนตัวเลขเท่านั้น")
                        getGrades()
                    except:
                        print("Exception found...")
                        inputChoice()
                stMid, stFinal, stAll = getGrades()
                stSum = stMid + stFinal + stAll
                grading = "ผ่าน"
                if stSum < 50:
                    grading = "ไม่ผ่าน"
                thisFile.writelines([
                f"ชื่อ-สกุล: {stName}\n"
                f"คะแนนกลางภาค: {stMid}\n"
                f"คะแนนปลายภาค: {stFinal}\n"
                f"ป้อนคะแนนเก็บ: {stAll}\n"
                f"คะแนนรวมที่คํานวณได้: {stSum}\n"
                f"ผลคะแนน: {grading}\n"
                ])
                thisFile.close()
                print("""
        **************************************
               เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว
        **************************************""")
                inputChoice()
            else:
                End("คุณพิมพ์ชื่อไฟล์ผิด")
        else:
            End("ไม่มีไฟล์วิชาใดๆอยู่เลย")
    except FileNotFoundError:
        print("ระบบค้นหาไฟล์ไม่เจอ โปรดลองอีกครั้ง")
        inputChoice()
    except:
        print("Exception found...")
        inputChoice()

def ReadFile():
    print("""
        **************************************
            เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล
        **************************************""")
    try:
        theFiles = os.listdir()
        theFiles.remove("workshop.py")
        if not theFiles == []:
            for i in theFiles:
                if i.endswith(".txt"):
                    print(i)
            theFile = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ")
            if os.path.exists(theFile):
                thisFile = open(f"{theFile}", "r", encoding="utf-8")
                readd = thisFile.readlines()
                for data_by_line in readd:
                    print(data_by_line, end='')
                thisFile.close()
                print("""
        **************************************
                  อ่านข้อมูลในไฟล์เรียบร้อย
        **************************************""")
                inputChoice()
            else:
                End("คุณพิมพ์ชื่อไฟล์ผิด")
        else:
            End("ไม่มีไฟล์วิชาใดๆอยู่เลย")
    except FileNotFoundError:
        print("ระบบค้นหาไฟล์ไม่เจอ โปรดลองอีกครั้ง")
        inputChoice()
    except:
        print("Exception found...")
        inputChoice()

def inputChoice():
    print("""
    1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล
    2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ 
    3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล
    4. เลือกวิชาและลบไฟล์ 
    0. จบการทํางาน
    """)
    iChoice = input("เลือกเมนู: ")
    if iChoice == "0":
        print("ปิดการทำงาน...")
        exit
    elif iChoice == "1":
        Creation()
    elif iChoice == "2":
        AppendFile()
    elif iChoice == "3":
        ReadFile()
    elif iChoice == "4":
        DeleteFile()
    else:
        print("-------------------------------------")
        print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")
        print("-------------------------------------")
        inputChoice()

print("""
    *************************************************
                        SCHOOL    
    *************************************************""")
inputChoice()