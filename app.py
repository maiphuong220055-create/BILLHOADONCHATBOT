```python
import streamlit as st
from datetime import datetime
from PIL import Image
import os


# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Bill Trà Sữa",
    page_icon="🧋",
    layout="centered"
)


# =========================================================
# CSS GIAO DIỆN
# =========================================================

st.markdown("""
<style>

    .brand-title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .brand-subtitle {
        text-align: center;
        font-size: 16px;
        margin-bottom: 20px;
    }

    .total-box {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #dddddd;
        margin-top: 15px;
        margin-bottom: 20px;
    }

    .total-label {
        font-size: 18px;
        font-weight: bold;
    }

    .total-price {
        font-size: 30px;
        font-weight: bold;
        margin-top: 5px;
    }

    .order-box {
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #dddddd;
        margin-top: 10px;
        margin-bottom: 10px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOGO / HÌNH ẢNH THƯƠNG HIỆU
# =========================================================

logo_path = "logo.png"

if os.path.exists(logo_path):

    logo = Image.open(logo_path)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            logo,
            use_container_width=True
        )

else:

    st.warning(
        "⚠️ Chưa tìm thấy logo.png. "
        "Hãy đặt logo.png cùng thư mục với app.py."
    )


# =========================================================
# TIÊU ĐỀ
# =========================================================

st.markdown(
    '<div class="brand-title">🧋 APP TÍNH BILL TRÀ SỮA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="brand-subtitle">'
    'Đặt hàng - Tính tiền - Xuất hóa đơn'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# DANH SÁCH TRÀ SỮA
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


# =========================================================
# DANH SÁCH TOPPING
# =========================================================

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
# KHỞI TẠO DANH SÁCH ĐƠN HÀNG
# =========================================================

if "gio_hang" not in st.session_state:
    st.session_state.gio_hang = []


# =========================================================
# THÔNG TIN KHÁCH HÀNG
# =========================================================

st.header("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)


# =========================================================
# TẠO MỘT MÓN TRÀ SỮA
# =========================================================

st.header("🧋 THÊM TRÀ SỮA VÀO ĐƠN")

loai_tra_sua = st.selectbox(
    "Chọn loại trà sữa",
    list(menu_tra_sua.keys())
)

gia_tra_sua = menu_tra_sua[loai_tra_sua]

st.info(
    f"💰 Giá: {gia_tra_sua:,} VNĐ / ly"
)


# =========================================================
# SỐ LƯỢNG
# =========================================================

so_luong = st.number_input(
    "Số lượng",
    min_value=1,
    max_value=50,
    value=1,
    step=1,
    key="so_luong_mon"
)


# =========================================================
# MỨC ĐƯỜNG
# =========================================================

st.subheader("🍬 Mức độ đường")

muc_duong = st.radio(
    "Chọn mức đường",
    ["100%", "70%", "0%"],
    horizontal=True,
    key="muc_duong_mon"
)


# =========================================================
# MỨC ĐÁ
# =========================================================

st.subheader("🧊 Mức độ đá")

muc_da = st.radio(
    "Chọn mức đá",
    ["100%", "70%", "0%"],
    horizontal=True,
    key="muc_da_mon"
)


# =========================================================
# TOPPING CHO MÓN HIỆN TẠI
# =========================================================

st.subheader("🍮 Topping")

topping_mon = []

for topping, gia in menu_topping.items():

    chon = st.checkbox(
        f"{topping} (+{gia:,}đ)",
        key=f"chon_{topping}"
    )

    if chon:

        sl = st.number_input(
            f"Số lượng {topping}",
            min_value=1,
            max_value=10,
            value=1,
            step=1,
            key=f"sl_{topping}"
        )

        topping_mon.append({
            "ten": topping,
            "gia": gia,
            "so_luong": sl
        })


# =========================================================
# NÚT THÊM MÓN
# =========================================================

st.divider()

if st.button(
    "➕ THÊM MÓN VÀO ĐƠN",
    use_container_width=True
):

    tien_mon = gia_tra_sua * so_luong

    tien_topping_mon = 0

    for topping in topping_mon:

        tien_topping_mon += (
            topping["gia"]
            *
            topping["so_luong"]
        )

    thanh_tien_mon = (
        tien_mon
        +
        tien_topping_mon
    )


    # Thêm món vào giỏ hàng

    st.session_state.gio_hang.append({

        "tra_sua": loai_tra_sua,

        "gia": gia_tra_sua,

        "so_luong": so_luong,

        "duong": muc_duong,

        "da": muc_da,

        "topping": topping_mon,

        "tien_topping": tien_topping_mon,

        "thanh_tien": thanh_tien_mon

    })


    st.success(
        f"✅ Đã thêm {so_luong} ly {loai_tra_sua} vào đơn hàng!"
    )


# =========================================================
# HIỂN THỊ GIỎ HÀNG
# =========================================================

st.divider()

st.header("🛒 ĐƠN HÀNG HIỆN TẠI")


if len(st.session_state.gio_hang) == 0:

    st.info(
        "Chưa có món nào trong đơn hàng."
    )

else:

    tong_tien = 0


    for i, mon in enumerate(
        st.session_state.gio_hang
    ):

        tong_tien += mon["thanh_tien"]


        st.markdown(
            f"""
            <div class="order-box">

            <b>🧋 Món {i + 1}: {mon['tra_sua']}</b><br><br>

            💰 Đơn giá: {mon['gia']:,} VNĐ<br>

            🔢 Số lượng: {mon['so_luong']} ly<br>

            🍬 Đường: {mon['duong']}<br>

            🧊 Đá: {mon['da']}<br>

            💵 Thành tiền: {mon['thanh_tien']:,} VNĐ

            </div>
            """,
            unsafe_allow_html=True
        )


        # -------------------------------------------------
        # TOPPING
        # -------------------------------------------------

        if len(mon["topping"]) == 0:

            st.write("🍮 Topping: Không có")

        else:

            st.write("🍮 Topping:")

            for tp in mon["topping"]:

                tien_tp = (
                    tp["gia"]
                    *
                    tp["so_luong"]
                )

                st.write(
                    f"  • {tp['ten']} x "
                    f"{tp['so_luong']} "
                    f"= {tien_tp:,} VNĐ"
                )


        # -------------------------------------------------
        # NÚT XÓA MÓN
        # -------------------------------------------------

        if st.button(
            f"🗑️ Xóa món {i + 1}",
            key=f"xoa_mon_{i}"
        ):

            st.session_state.gio_hang.pop(i)

            st.rerun()


    # =====================================================
    # TỔNG TIỀN
    # =====================================================

    st.markdown(
        f"""
        <div class="total-box">

            <div class="total-label">
                💵 TỔNG THANH TOÁN
            </div>

            <div class="total-price">
                {tong_tien:,} VNĐ
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# XÓA TOÀN BỘ ĐƠN
# =========================================================

if len(st.session_state.gio_hang) > 0:

    if st.button(
        "🗑️ XÓA TOÀN BỘ ĐƠN HÀNG",
        use_container_width=True
    ):

        st.session_state.gio_hang = []

        st.rerun()


# =========================================================
# THANH TOÁN
# =========================================================

st.divider()

st.header("💳 THANH TOÁN")


thanh_toan = st.button(
    "💳 THANH TOÁN VÀ XUẤT HÓA ĐƠN",
    use_container_width=True
)


# =========================================================
# TẠO HÓA ĐƠN
# =========================================================

if thanh_toan:

    if ten_khach.strip() == "":

        st.warning(
            "⚠️ Vui lòng nhập tên khách hàng."
        )

    elif len(st.session_state.gio_hang) == 0:

        st.warning(
            "⚠️ Vui lòng thêm ít nhất một món vào đơn hàng."
        )

    else:

        # -------------------------------------------------
        # THỜI GIAN
        # -------------------------------------------------

        thoi_gian = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )


        # -------------------------------------------------
        # MÃ HÓA ĐƠN
        # -------------------------------------------------

        ma_hoa_don = datetime.now().strftime(
            "%Y%m%d%H%M%S"
        )


        # -------------------------------------------------
        # TÍNH TỔNG
        # -------------------------------------------------

        tong_tien = 0

        for mon in st.session_state.gio_hang:

            tong_tien += mon["thanh_tien"]


        # -------------------------------------------------
        # TẠO NỘI DUNG HÓA ĐƠN
        # -------------------------------------------------

        hoa_don = ""

        hoa_don += "============================================\n"

        hoa_don += "              HÓA ĐƠN TRÀ SỮA\n"

        hoa_don += "============================================\n"

        hoa_don += f"Mã hóa đơn: {ma_hoa_don}\n"

        hoa_don += f"Khách hàng: {ten_khach}\n"

        hoa_don += f"Thời gian: {thoi_gian}\n"

        hoa_don += "\n"


        # -------------------------------------------------
        # DANH SÁCH MÓN
        # -------------------------------------------------

        hoa_don += "--------------------------------------------\n"

        hoa_don += "CHI TIẾT ĐƠN HÀNG\n"

        hoa_don += "--------------------------------------------\n"


        for i, mon in enumerate(
            st.session_state.gio_hang
        ):

            hoa_don += (
                f"\nMÓN {i + 1}: "
                f"{mon['tra_sua']}\n"
            )

            hoa_don += (
                f"Đơn giá: "
                f"{mon['gia']:,} VNĐ\n"
            )

            hoa_don += (
                f"Số lượng: "
                f"{mon['so_luong']} ly\n"
            )

            hoa_don += (
                f"Đường: "
                f"{mon['duong']}\n"
            )

            hoa_don += (
                f"Đá: "
                f"{mon['da']}\n"
            )


            # ---------------------------------------------
            # TOPPING
            # ---------------------------------------------

            if len(mon["topping"]) == 0:

                hoa_don += "Topping: Không có\n"

            else:

                hoa_don += "Topping:\n"

                for tp in mon["topping"]:

                    tien_tp = (
                        tp["gia"]
                        *
                        tp["so_luong"]
                    )

                    hoa_don += (
                        f"  - {tp['ten']} x "
                        f"{tp['so_luong']} = "
                        f"{tien_tp:,} VNĐ\n"
                    )


            hoa_don += (
                f"Thành tiền món: "
                f"{mon['thanh_tien']:,} VNĐ\n"
            )


        # -------------------------------------------------
        # THANH TOÁN
        # -------------------------------------------------

        hoa_don += "\n"

        hoa_don += "--------------------------------------------\n"

        hoa_don += "THANH TOÁN\n"

        hoa_don += "--------------------------------------------\n"

        hoa_don += (
            f"TỔNG THANH TOÁN: "
            f"{tong_tien:,} VNĐ\n"
        )

        hoa_don += "\n"

        hoa_don += "============================================\n"

        hoa_don += (
            "       CẢM ƠN QUÝ KHÁCH ĐÃ MUA HÀNG!\n"
        )

        hoa_don += "============================================\n"


        # -------------------------------------------------
        # THÔNG BÁO
        # -------------------------------------------------

        st.success(
            "✅ Thanh toán thành công!"
        )


        # -------------------------------------------------
        # HIỂN THỊ HÓA ĐƠN
        # -------------------------------------------------

        st.subheader("🧾 HÓA ĐƠN")

        st.code(
            hoa_don,
            language=None
        )


        # -------------------------------------------------
        # TÊN FILE
        # -------------------------------------------------

        ten_file = (
            "hoa_don_"
            +
            ten_khach.replace(" ", "_")
            +
            "_"
            +
            ma_hoa_don
            +
            ".txt"
        )


        # -------------------------------------------------
        # TẢI HÓA ĐƠN
        # -------------------------------------------------

        st.download_button(

            label="📥 TẢI FILE HÓA ĐƠN",

            data=hoa_don,

            file_name=ten_file,

            mime="text/plain",

            use_container_width=True
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🧋 Cảm ơn quý khách đã sử dụng dịch vụ!"
)
```
