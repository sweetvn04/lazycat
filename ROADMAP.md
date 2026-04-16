# 🐱 Lazycat — Roadmap

> "Just a hobby, won't be big and professional" — Linus Torvalds, 1991

---

## Giai đoạn 1 — CLI (Tuần 1–2)

Mục tiêu: làm cho nó **chạy được**. Không cần đẹp.

### Ngày 1–2 ✅
- [x] Setup project, venv, gitignore
- [x] Kết nối Docker API
- [x] List tất cả container đang chạy

### Ngày 3–4
- [ ] Hiển thị thêm thông tin: image, ports, compose stack
- [ ] Group container theo compose stack (wordpress, ollama...)
- [x] Format output đẹp hơn bằng `rich` library

### Ngày 5–7
- [ ] `lazycat ps` — list containers
- [ ] `lazycat up <stack>` — start một stack
- [ ] `lazycat down <stack>` — stop một stack
- [ ] `lazycat restart <service>` — restart một service

### Ngày 8–10
- [ ] `lazycat logs <service>` — xem log của service
- [ ] Streaming log realtime (không phải chỉ đọc một lần)
- [ ] `lazycat logs <service> --follow` — follow log liên tục

### Checkpoint giai đoạn 1
Dùng được lazycat thay thế hoàn toàn các lệnh `docker compose` hàng ngày.

---

## Giai đoạn 2 — TUI (Tuần 3–4)

Mục tiêu: làm cho nó **dùng được** hàng ngày.

### Tuần 3
- [ ] Tìm hiểu Textual — làm tutorial chính thức
- [ ] Layout cơ bản: panel trái (danh sách stack) + panel phải (services)
- [ ] Navigate bằng bàn phím giữa các stack và service

### Tuần 4
- [ ] Panel log ở dưới — hiển thị log realtime khi chọn service
- [ ] Keyboard shortcuts: `s` start, `d` down, `r` restart, `l` logs
- [ ] Status indicator: running 🟢 / stopped 🔴 / restarting 🟡

### Checkpoint giai đoạn 2
Mở lazycat lên, nhìn thấy toàn bộ homelab, không cần gõ thêm lệnh nào.

---

## Giai đoạn 3 — Edit & Polish (Sau thực tập)

Mục tiêu: làm cho nó **đáng tin** — từ toy thành tool.

- [ ] `e` — mở file compose trong `$EDITOR` (vim/nvim)
- [ ] Sau khi save, tự động hỏi "Reload stack? [y/n]"
- [ ] Parse và validate YAML trước khi reload
- [ ] Hiển thị error rõ ràng nếu compose file sai
- [ ] README đầy đủ — install, usage, screenshots
- [ ] Viết `CONTRIBUTING.md` — open source đúng nghĩa

### Stretch goals (nếu còn thời gian)
- [ ] Rewrite bằng Go + Bubble Tea
- [ ] Multi-host support — quản lý Docker trên nhiều server
- [ ] Publish lên PyPI — `pip install lazycat`

---

## Tài liệu cần đọc

| Giai đoạn | Tài liệu | Link |
|-----------|----------|------|
| 1 | Docker SDK for Python | https://docker-py.readthedocs.io |
| 1 | Docker Engine API | https://docs.docker.com/engine/api |
| 2 | Textual | https://textual.textualize.io |
| 2 | Rich | https://rich.readthedocs.io |
| 3 | PyYAML | https://pyyaml.org/wiki/PyYAMLDocumentation |
| Tham khảo | Lazydocker source | https://github.com/jesseduffield/lazydocker |

---

## Nguyên tắc

- Commit nhỏ, commit thường xuyên
- Chạy được > đẹp > hoàn hảo
- Stuck thì đọc doc trước, hỏi sau
- Mỗi tuần phải có thứ gì đó **chạy được** mới, không chỉ học lý thuyết

---

*"Talk is cheap, show me the code." — Linus Torvalds* 🐧
