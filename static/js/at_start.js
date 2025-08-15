async function addNavTabs() {
    try {
        const response = await fetch("http://localhost:8000/api/categories/");
        const categories = await response.json();
        const scrollContainer = document.createElement('div');
        scrollContainer.className = 'scroll-container'; // Добавляем класс для стилей

        categories.forEach(category => {
            const li = document.createElement("li");
            const button = document.createElement("button");
            const h3 = document.createElement("h3");
            li.className = 'nav-item';
            li.id = `nav-category-${category.id}`;
            button.className = 'nav-link';
            button.type = 'button';
            button.onclick = function () { changeContent(category.id); };
            h3.innerHTML = category.name;

            button.appendChild(h3);
            li.appendChild(button);
            scrollContainer.appendChild(li);
            navTabs.appendChild(scrollContainer);
        });
        
        const firstCategoryId = categories[0].id

        changeContent(firstCategoryId); // Добавляем на главный экран контент первой категории
    }
    catch (error) {
        console.error("Ошибка при загрузке Нивигационных категорий:", error);
    };
};

document.addEventListener("DOMContentLoaded", () => {
    addNavTabs();
});