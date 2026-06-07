raw_logs = []
processed_logs = []


def clean_logs(log_text):
    table = str.maketrans('', '', '!@#$')

    log_text = log_text.translate(table)

    logs = []

    for log in log_text.split(';'):
        log = log.strip()

        if log != "":
            logs.append(log)

    return logs

def filter_logs():
    global processed_logs

    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    processed_logs = []

    for log in raw_logs:
        lower_log = log.lower()

        if "error" in lower_log:
            processed_logs.append(log)

        elif "critical" in lower_log:
            processed_logs.append(log)

    print("--- LỌC CẢNH BÁO ---")

    if len(processed_logs) == 0:
        print("Không tìm thấy cảnh báo nguy hiểm")
        return

    print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")

    for log in processed_logs:
        print(f"- {log}")

def mask_ip():
    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return []

    masked_logs = [log for log in processed_logs]

    for i in range(len(masked_logs)):
        words = masked_logs[i].split()

        for j in range(len(words)):

            if "." not in words[j]:
                continue

            ip_parts = words[j].split(".")

            if len(ip_parts) != 4:
                continue

            ip_parts[2] = "*"
            ip_parts[3] = "*"

            words[j] = ".".join(ip_parts)

        masked_logs[i] = " ".join(words)

    return masked_logs

while True:
    print("============= SECURITY LOG ANALYZER =============")
    print("1. Nhập và làm sạch dữ liệu Log thô")
    print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
    print("3. Mã hóa địa chỉ IP (Masking)")
    print("4. Đóng hệ thống")
    print("=================================================")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        print("--- NẠP DỮ LIỆU LOG ---")
        log_text = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")
        raw_logs = clean_logs(log_text)
        print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")

    elif choice == "2":
        filter_logs()
    elif choice == "3":
        if len(raw_logs) == 0:
            print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
            continue
        masked_logs = mask_ip()
        print("--- MÃ HÓA IP ---")
        if len(masked_logs) == 0:
            print("Không có log nguy hiểm để mã hóa")
            continue
        print("Báo cáo log an toàn:")
        for index, log in enumerate(masked_logs, start=1):
            print(f"{index}. {log}")

    elif choice == "4":
        print("Đóng hệ thống thành công!")
        break

    else:
        print("Lựa chọn không hợp lệ")