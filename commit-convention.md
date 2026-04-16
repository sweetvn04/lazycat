# 📝 Quy tắc viết Commit Message

> Dựa theo chuẩn [Conventional Commits](https://www.conventionalcommits.org/)

---

## Cấu trúc cơ bản

```
<type>(<scope>): <mô tả ngắn>
```

- **type** — loại thay đổi (bắt buộc)
- **scope** — phạm vi thay đổi (tuỳ chọn)
- **mô tả ngắn** — viết thường, không dấu chấm cuối, dưới 72 ký tự

---

## Các type phổ biến

| Type | Ý nghĩa | Ví dụ |
|------|---------|-------|
| `feat` | Thêm tính năng mới | `feat: add table display for containers` |
| `fix` | Sửa bug | `fix: handle empty image tags` |
| `refactor` | Refactor code, không thêm feature hay fix bug | `refactor: extract get_stack_name function` |
| `chore` | Việc lặt vặt — update deps, config | `chore: add rich to requirements.txt` |
| `docs` | Cập nhật tài liệu | `docs: update README with usage examples` |
| `style` | Format code, không ảnh hưởng logic | `style: reorder imports` |
| `test` | Thêm hoặc sửa test | `test: add test for container grouping` |

---

## Ví dụ thực tế cho lazycat

```bash
# Ngày 1-2
feat: connect to Docker API and list running containers

# Ngày 3-4 hôm nay
feat: add rich table display with name, status, image columns
chore: add rich to project dependencies
```

---

## Quy tắc viết

- Dùng **tiếng Anh** — chuẩn quốc tế, đẹp hơn trên GitHub
- Động từ ở dạng **nguyên thể** — `add`, `fix`, `update` (không phải `added`, `fixed`)
- Mô tả **cái gì** thay đổi, không phải **tại sao** — cái đó để trong body nếu cần
- Mỗi commit = **một việc** — không gộp nhiều thứ vào một commit

---

## Commit có body (khi cần giải thích thêm)

```
feat(containers): group containers by compose stack

Containers without compose labels are grouped under "standalone".
This makes it easier to manage multi-service stacks at a glance.
```

Cách nhau một dòng trống giữa subject và body.

---

## ❌ Những kiểu commit nên tránh

```bash
git commit -m "fix"
git commit -m "update code"
git commit -m "asdfgh"
git commit -m "done"
git commit -m "wip"          # nếu push lên main
```

---

## Tip cho lazycat

Vì đây là solo project, không cần quá strict — nhưng giữ **type + mô tả ngắn** là đủ. Sau này nhìn lại `git log` sẽ biết ngay từng bước mình đã làm gì.
