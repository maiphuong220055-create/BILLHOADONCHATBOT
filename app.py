import streamlit as st
from datetime import datetime
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
# CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    font-size: 17px;
    margin-bottom: 20px;
}

.total-box {
    border: 2px solid #dddddd;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
}

.total-title {
    font-size: 18px;
    font-weight: bold;
}

.total-money {
    font-size: 30px;
    font-weight: bold;
    margin-top: 10px;
}

.order-box {
    border: 1px solid #dddddd;
    border-radius: 12px;
    padding: 15px;
    margin-top: 10px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOGO THƯƠNG HIỆU
# =========================================================

logo_path = "logo.png"

if os.path.exists(logo_path):
    st.image(logo_path, use_container_width=True)
else:
    st.info(
        "ℹ️ Chưa có logo.png. "
        "Nếu muốn hiển thị logo, hãy đặt ảnh logo.png "
        "cùng thư mục với app.py."
    )


# =========================================================
# TIÊU ĐỀ
# =========================================================

st.markdown(
    '<div class="main-title">🧋 APP TÍNH BILL TRÀ SỮA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'Đặt hàng - Tính tiền - Xuất hóa đơn'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# MENU TRÀ SỮA
# =========================================================

menu_tra_sua = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa socola": 32000,
    "Trà sữa matcha": 35000,
    "Trà sữa khoai môn": 35000,
    "Trà sữa dâu": 33000,
    "Trà sữa caramel": 35000,
    "Trà sữa ô long": 32000,
    "Trà sữa thái xanh": 30000
}


# =========================================================
# MENU TOPPING
# =========================================================

menu_topping = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 6000,
    "Thạch dừa": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese": 10000,
    "Trân châu hoàng kim": 7000
}


# =========================================================
# KHỞI TẠO GIỎ HÀNG
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
# THÊM MÓN MỚI
# =========================================================

st.header("🧋 Thêm món vào đơn hàng")


# ---------------------------------------------------------
# Chọn trà sữa
# ---------------------------------------------------------

loai_tra_sua = st.selectbox(
    "Loại trà sữa",
    list(menu_tra_sua.keys())
)

gia_tra_sua = menu_tra_sua[loai_tra_sua]

st.write(
    f"💰 **Giá:** {gia_tra_sua:,} VNĐ / ly"
)


# ---------------------------------------------------------
# Số lượng
# ---------------------------------------------------------

so_luong = st.number_input(
    "Số lượng",
    min_value=1,
    max_value=50,
    value=1,
    step=1
)


# ---------------------------------------------------------
# Đường
# ---------------------------------------------------------

st.subheader("🍬 Mức độ đường")

muc_duong = st.radio(
    "Chọn mức đường",
    ["100%", "70%", "0%"],
    horizontal=True
)


# ---------------------------------------------------------
# Đá
# ---------------------------------------------------------

st.subheader("🧊 Mức độ đá")

muc_da = st.radio(
    "Chọn mức đá",
    ["100%", "70%", "0%"],
    horizontal=True
)


# ---------------------------------------------------------
# TOPPING
# ---------------------------------------------------------

st.subheader("🍮 Topping")

topping_mon = []


for i, (topping, gia) in enumerate(menu_topping.items()):

    chon_topping = st.checkbox(
        f"{topping} (+{gia:,} VNĐ)",
        key=f"topping_{i}"
    )

    if chon_topping:

        so_luong_topping = st.number_input(
            f"Số lượng {topping}",
            min_value=1,
            max_value=10,
            value=1,
            step=1,
            key=f"topping_sl_{i}"
        )

        topping_mon.append({
            "ten": topping,
            "gia": gia,
            "so_luong": so_luong_topping
        })


# =========================================================
# TÍNH TIỀN MÓN HIỆN TẠI
# =========================================================

tien_tra_sua = gia_tra_sua * so_luong

tien_topping = 0

for topping in topping_mon:

    tien_topping += (
        topping["gia"] *
        topping["so_luong"]
    )

thanh_tien = tien_tra_sua + tien_topping


st.write(
    f"💵 **Thành tiền món này: {thanh_tien:,} VNĐ**"
)


# =========================================================
# NÚT THÊM MÓN
# =========================================================

if st.button(
    "➕ THÊM MÓN VÀO ĐƠN",
    use_container_width=True
):

    mon_moi = {
        "ten": loai_tra_sua,
        "gia": gia_tra_sua,
        "so_luong": so_luong,
        "duong": muc_duong,
        "da": muc_da,
        "topping": topping_mon.copy(),
        "tien_topping": tien_topping,
        "thanh_tien": thanh_tien
    }

    st.session_state.gio_hang.append(mon_moi)

    st.success(
        f"✅ Đã thêm {loai_tra_sua} vào đơn hàng!"
    )


# =========================================================
# GIỎ HÀNG
# =========================================================

st.divider()

st.header("🛒 Đơn hàng hiện tại")


if len(st.session_state.gio_hang) == 0:

    st.info(
        "Chưa có món nào. "
        "Hãy chọn trà sữa và bấm 'THÊM MÓN VÀO ĐƠN'."
    )

else:

    tong_tien = 0

    # Dùng danh sách tạm để tránh lỗi khi xóa
    for i, mon in enumerate(st.session_state.gio_hang):

        tong_tien += mon["thanh_tien"]

        st.markdown(
            f"""
            <div class="order-box">

            <b>🧋 MÓN {i + 1}: {mon['ten']}</b>
            <br><br>

            💰 Đơn giá: {mon['gia']:,} VNĐ
            <br>

            🔢 Số lượng: {mon['so_luong']} ly
            <br>

            🍬 Đường: {mon['duong']}
            <br>

            🧊 Đá: {mon['da']}
            <br>

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
                    tp["gia"] *
                    tp["so_luong"]
                )

                st.write(
                    f"- {tp['ten']} x "
                    f"{tp['so_luong']} = "
                    f"{tien_tp:,} VNĐ"
                )


        # -------------------------------------------------
        # NÚT XÓA MÓN
        # -------------------------------------------------

        if st.button(
            f"🗑️ Xóa món {i + 1}",
            key=f"xoa_{i}",
            use_container_width=True
        ):

            del st.session_state.gio_hang[i]

            st.rerun()


    # =====================================================
    # TỔNG TIỀN
    # =====================================================

    st.markdown(
        f"""
        <div class="total-box">

        <div class="total-title">
        💵 TỔNG SỐ TIỀN CẦN THANH TOÁN
        </div>

        <div class="total-money">
        {tong_tien:,} VNĐ
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # XÓA TOÀN BỘ
    # =====================================================

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

st.header("💳 Thanh toán")


if st.button(
    "💳 THANH TOÁN VÀ XUẤT HÓA ĐƠN",
    use_container_width=True
):

    # -----------------------------------------------------
    # Kiểm tra tên
    # -----------------------------------------------------

    if ten_khach.strip() == "":

        st.warning(
            "⚠️ Vui lòng nhập tên khách hàng."
        )

    # -----------------------------------------------------
    # Kiểm tra giỏ hàng
    # -----------------------------------------------------

    elif len(st.session_state.gio_hang) == 0:

        st.warning(
            "⚠️ Đơn hàng chưa có sản phẩm."
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
        # TẠO HÓA ĐƠN
        # -------------------------------------------------

        hoa_don = ""

        hoa_don += "============================================\n"
        hoa_don += "              HÓA ĐƠN TRÀ SỮA\n"
        hoa_don += "============================================\n"

        hoa_don += f"Mã hóa đơn: {ma_hoa_don}\n"
        hoa_don += f"Khách hàng: {ten_khach}\n"
        hoa_don += f"Thời gian: {thoi_gian}\n"

        hoa_don += "\n"
        hoa_don += "--------------------------------------------\n"
        hoa_don += "CHI TIẾT ĐƠN HÀNG\n"
        hoa_don += "--------------------------------------------\n"


        # -------------------------------------------------
        # TỪNG MÓN
        # -------------------------------------------------

        for i, mon in enumerate(st.session_state.gio_hang):

            hoa_don += "\n"

            hoa_don += (
                f"MÓN {i + 1}: "
                f"{mon['ten']}\n"
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
                f"Mức đường: "
                f"{mon['duong']}\n"
            )

            hoa_don += (
                f"Mức đá: "
                f"{mon['da']}\n"
            )


            # ---------------------------------------------
            # TOPPING
            # ---------------------------------------------

            if len(mon["topping"]) == 0:

                hoa_don += (
                    "Topping: Không có\n"
                )

            else:

                hoa_don += "Topping:\n"

                for tp in mon["topping"]:

                    tien_tp = (
                        tp["gia"] *
                        tp["so_luong"]
                    )

                    hoa_don += (
                        f"  - {tp['ten']} x "
                        f"{tp['so_luong']} = "
                        f"{tien_tp:,} VNĐ\n"
                    )


            hoa_don += (
                f"Thành tiền: "
                f"{mon['thanh_tien']:,} VNĐ\n"
            )


        # -------------------------------------------------
        # TỔNG THANH TOÁN
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
        hoa_don += "       CẢM ƠN QUÝ KHÁCH ĐÃ MUA HÀNG!\n"
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
            + ten_khach.replace(" ", "_")
            + "_"
            + ma_hoa_don
            + ".txt"
        )


        # -------------------------------------------------
        # DOWNLOAD
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
