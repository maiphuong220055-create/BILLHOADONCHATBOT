import streamlit as st
from datetime import datetime

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Bill Trà Sữa",
    page_icon="🧋",
    layout="centered"
)

# =========================================================
# TIÊU ĐỀ
# =========================================================

st.title("🧋 APP TÍNH BILL TRÀ SỮA")
st.write("Nhập thông tin đơn hàng bên dưới để tính hóa đơn.")

st.divider()

# =========================================================
# DANH SÁCH SẢN PHẨM
# =========================================================

menu_tra_sua = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa socola": 32000,
    "Trà sữa matcha": 35000,
    "Trà sữa khoai môn": 35000,
    "Trà sữa dâu": 33000,
    "Trà sữa caramel": 35000,
    "Trà sữa ô long": 32000,
    "Trà sữa thái xanh": 30000,
}

menu_topping = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 6000,
    "Thạch dừa": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese": 10000,
    "Trân châu hoàng kim": 7000,
}

# =========================================================
# THÔNG TIN KHÁCH HÀNG
# =========================================================

st.header("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

# =========================================================
# CHỌN TRÀ SỮA
# =========================================================

st.header("🧋 Chọn trà sữa")

loai_tra_sua = st.selectbox(
    "Loại trà sữa",
    list(menu_tra_sua.keys())
)

gia_tra_sua = menu_tra_sua[loai_tra_sua]

so_luong = st.number_input(
    "Số lượng",
    min_value=1,
    max_value=50,
    value=1,
    step=1
)

# =========================================================
# MỨC ĐƯỜNG
# =========================================================

st.header("🍬 Mức độ đường")

muc_duong = st.radio(
    "Chọn mức đường",
    ["100%", "70%", "0%"],
    horizontal=True
)

# =========================================================
# MỨC ĐÁ
# =========================================================

st.header("🧊 Mức độ đá")

muc_da = st.radio(
    "Chọn mức đá",
    ["100%", "70%", "0%"],
    horizontal=True
)

# =========================================================
# TOPPING
# =========================================================

st.header("🍮 Topping")

topping_chon = []

for topping, gia in menu_topping.items():
    chon = st.checkbox(
        f"{topping} (+{gia:,}đ)",
        key=f"check_{topping}"
    )

    if chon:
        sl_topping = st.number_input(
            f"Số lượng {topping}",
            min_value=1,
            max_value=10,
            value=1,
            step=1,
            key=f"sl_{topping}"
        )

        topping_chon.append({
            "ten": topping,
            "gia": gia,
            "so_luong": sl_topping
        })

# =========================================================
# TÍNH TIỀN
# =========================================================

tien_tra_sua = gia_tra_sua * so_luong

tien_topping = 0

for topping in topping_chon:
    tien_topping += topping["gia"] * topping["so_luong"]

tong_tien = tien_tra_sua + tien_topping

# =========================================================
# HIỂN THỊ ĐƠN HÀNG
# =========================================================

st.divider()

st.header("🧾 THÔNG TIN ĐƠN HÀNG")

if ten_khach.strip() == "":
    ten_hien_thi = "Chưa nhập tên"
else:
    ten_hien_thi = ten_khach

st.write(f"**👤 Khách hàng:** {ten_hien_thi}")

st.write(f"**🧋 Trà sữa:** {loai_tra_sua}")

st.write(f"**💰 Đơn giá:** {gia_tra_sua:,} VNĐ")

st.write(f"**🔢 Số lượng:** {so_luong}")

st.write(f"**🍬 Đường:** {muc_duong}")

st.write(f"**🧊 Đá:** {muc_da}")

# =========================================================
# HIỂN THỊ TOPPING
# =========================================================

st.subheader("🍮 Topping đã chọn")

if len(topping_chon) == 0:
    st.write("Không có topping")
else:
    for topping in topping_chon:
        thanh_tien_topping = topping["gia"] * topping["so_luong"]

        st.write(
            f"- {topping['ten']} "
            f"x {topping['so_luong']} "
            f"= {thanh_tien_topping:,} VNĐ"
        )

# =========================================================
# CHI TIẾT TIỀN
# =========================================================

st.divider()

st.write(
    f"**Tiền trà sữa:** "
    f"{tien_tra_sua:,} VNĐ"
)

st.write(
    f"**Tiền topping:** "
    f"{tien_topping:,} VNĐ"
)

st.subheader(
    f"💵 TỔNG THANH TOÁN: {tong_tien:,} VNĐ"
)

# =========================================================
# NÚT THANH TOÁN
# =========================================================

st.divider()

thanh_toan = st.button(
    "💳 THANH TOÁN",
    use_container_width=True
)

# =========================================================
# TẠO FILE HÓA ĐƠN
# =========================================================

if thanh_toan:

    if ten_khach.strip() == "":
        st.warning("⚠️ Vui lòng nhập tên khách hàng trước khi thanh toán.")

    else:

        # Thời gian lập hóa đơn
        thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Tạo nội dung hóa đơn
        hoa_don = ""

        hoa_don += "========================================\n"
        hoa_don += "          HÓA ĐƠN TRÀ SỮA\n"
        hoa_don += "========================================\n\n"

        hoa_don += f"Khách hàng: {ten_khach}\n"
        hoa_don += f"Thời gian: {thoi_gian}\n\n"

        hoa_don += "----------------------------------------\n"
        hoa_don += "THÔNG TIN ĐỒ UỐNG\n"
        hoa_don += "----------------------------------------\n"

        hoa_don += f"Trà sữa: {loai_tra_sua}\n"
        hoa_don += f"Đơn giá: {gia_tra_sua:,} VNĐ\n"
        hoa_don += f"Số lượng: {so_luong}\n"
        hoa_don += f"Mức đường: {muc_duong}\n"
        hoa_don += f"Mức đá: {muc_da}\n"

        hoa_don += "\n----------------------------------------\n"
        hoa_don += "TOPPING\n"
        hoa_don += "----------------------------------------\n"

        if len(topping_chon) == 0:
            hoa_don += "Không có topping\n"

        else:
            for topping in topping_chon:

                thanh_tien_topping = (
                    topping["gia"] *
                    topping["so_luong"]
                )

                hoa_don += (
                    f"{topping['ten']} x "
                    f"{topping['so_luong']} = "
                    f"{thanh_tien_topping:,} VNĐ\n"
                )

        hoa_don += "\n----------------------------------------\n"
        hoa_don += "THANH TOÁN\n"
        hoa_don += "----------------------------------------\n"

        hoa_don += (
            f"Tiền trà sữa: "
            f"{tien_tra_sua:,} VNĐ\n"
        )

        hoa_don += (
            f"Tiền topping: "
            f"{tien_topping:,} VNĐ\n"
        )

        hoa_don += (
            f"TỔNG THANH TOÁN: "
            f"{tong_tien:,} VNĐ\n"
        )

        hoa_don += "\n========================================\n"
        hoa_don += "       CẢM ƠN QUÝ KHÁCH ĐÃ MUA HÀNG!\n"
        hoa_don += "========================================\n"

        # Hiển thị thông báo
        st.success("✅ Thanh toán thành công!")

        st.subheader("🧾 Hóa đơn")

        st.text(hoa_don)

        # Tạo tên file
        ten_file = (
            "hoa_don_"
            + ten_khach.replace(" ", "_")
            + ".txt"
        )

        # Nút tải hóa đơn
        st.download_button(
            label="📥 TẢI FILE HÓA ĐƠN",
            data=hoa_don,
            file_name=ten_file,
            mime="text/plain",
            use_container_width=True
        )
