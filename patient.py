# patient.py - 환자 관리 모듈
# 환자 등록, 환자 목록 조회 기능 포함

patients = []  # 환자 정보를 저장하는 리스트

def register_patient(name, age, phone):
    """환자를 등록하는 함수"""
    patient = {"name": name, "age": age, "phone": phone}
    patients.append(patient)  # 환자 정보 추가
    print(f"[등록 완료] {name}")

def show_patients():
    """등록된 환자 목록 출력"""
    print("=== 환자 목록 ===")
    if not patients:
        print("등록된 환자가 없습니다.")
    for p in patients:
        print(f"{p['name']} (나이: {p['age']}, 전화: {p['phone']})")
