document.addEventListener("DOMContentLoaded", function () {
    const btnNotes = document.getElementById("btn-notes");
    const btnTodos = document.getElementById("btn-todos");
    const notesSection = document.getElementById("notes-section");
    const todosSection = document.getElementById("todos-section");

    function switchTab(showNotes) {
        const current = showNotes ? todosSection : notesSection;
        const target = showNotes ? notesSection : todosSection;

        // مرحله 1: انیمیشن مخفی‌سازی (fade + slide)
        current.classList.remove("fade-in");
        current.classList.add(showNotes ? "fade-out-right" : "fade-out-left");

        // بعد از انیمیشن مخفی‌سازی
        setTimeout(() => {
            current.classList.add("d-none");
            current.classList.remove("fade-out-left", "fade-out-right");

            // مرحله 2: نمایش بخش جدید
            target.classList.remove("d-none");
            target.classList.add("fade-in");

        }, 400); // باید برابر با زمان transition در CSS باشه

        // دکمه فعال/غیرفعال
        btnNotes.classList.toggle("active", showNotes);
        btnTodos.classList.toggle("active", !showNotes);
    }

    btnNotes.addEventListener("click", () => switchTab(true));
    btnTodos.addEventListener("click", () => switchTab(false));
});