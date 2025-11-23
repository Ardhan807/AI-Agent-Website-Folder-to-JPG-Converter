from colorama import Fore, Style
from agent import ask_ai
from tools import convert_html_folder_to_jpg
import os

print(Fore.CYAN + "AI Agent — Website Folder to JPG Converter" + Style.RESET_ALL)

history = []

if not os.getenv("OPENROUTER_API_KEY"):
    print(Fore.RED + "[ERROR] OPENROUTER_API_KEY tidak ditemukan di .env!" + Style.RESET_ALL)

def log_terminal(thinking_msg=None, tool_msg=None, final_msg=None):
    if thinking_msg:
        print(Fore.YELLOW + f"• [AI Thinking]: {thinking_msg}" + Style.RESET_ALL)
    if tool_msg:
        print(Fore.YELLOW + f"• [Tool Output]: {tool_msg}" + Style.RESET_ALL)
    if final_msg:
        print(Fore.CYAN + f"• [AI Final Answer]: {final_msg}" + Style.RESET_ALL)

while True:
    user_input = input(Fore.GREEN + "You: " + Style.RESET_ALL)

    if user_input.strip().lower() in ["exit", "quit", "keluar"]:
        print(Fore.YELLOW + "Program dihentikan." + Style.RESET_ALL)
        break

    lower_text = user_input.lower()

    # deteksi perintah folder → JPG
    if "folder" in lower_text and ("html" in lower_text or "jpg" in lower_text or "image" in lower_text):
        log_terminal(thinking_msg="User meminta konversi folder ke JPG. Memanggil convert_html_folder_to_jpg.")

        folder_name = input("Masukkan nama folder HTML (di dalam folder input/): ").strip()
        folder_path = f"input/{folder_name}"
        output_path = "output"

        result = convert_html_folder_to_jpg(folder_path, output_path)

        if result["status"] == "success":
            log_terminal(
                tool_msg=f"Berhasil mengonversi {len(result['files'])} file HTML menjadi JPG.",
                final_msg="Tugas konversi HTML → JPG selesai!"
            )
            for f in result["files"]:
                print(Fore.CYAN + "• " + f + Style.RESET_ALL)
        else:
            log_terminal(
                tool_msg="Proses gagal.",
                final_msg=result["message"]
            )
        continue

    # Jika bukan perintah konversi → tanyakan ke AI
    history.append({"role": "user", "content": user_input})
    log_terminal(thinking_msg="Mengirim pertanyaan ke AI melalui OpenRouter...")
    ai_reply = ask_ai(history)
    history.append({"role": "assistant", "content": ai_reply})
    log_terminal(final_msg=ai_reply)