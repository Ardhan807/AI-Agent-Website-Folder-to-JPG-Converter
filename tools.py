import os
from playwright.sync_api import sync_playwright

def convert_html_folder_to_jpg(folder_path: str, output_folder: str):
    if not os.path.exists(folder_path):
        return {"status": "error", "message": f"Folder '{folder_path}' tidak ditemukan"}

    os.makedirs(output_folder, exist_ok=True)
    converted_files = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1080})

        for file in os.listdir(folder_path):
            if not file.lower().endswith(".html"):
                continue

            html_path = os.path.abspath(os.path.join(folder_path, file))
            url = f"file:///{html_path}".replace("\\", "/")

            try:
                page.goto(url, wait_until="networkidle")
                page.wait_for_timeout(2000)  # beri waktu JS selesai

                jpg_name = os.path.splitext(file)[0] + ".jpg"
                jpg_output_path = os.path.join(output_folder, jpg_name)

                page.screenshot(
                    path=jpg_output_path,
                    full_page=True,
                    type="jpeg",
                    quality=90   # 100 = maksimal
                )

                converted_files.append(jpg_output_path)

            except Exception as e:
                browser.close()
                return {"status": "error", "message": f"Gagal konversi {file}: {e}"}

        browser.close()

    if not converted_files:
        return {"status": "error", "message": "Tidak ada file HTML dalam folder"}

    return {
        "status": "success",
        "message": f"{len(converted_files)} JPG berhasil dibuat",
        "files": converted_files
    }