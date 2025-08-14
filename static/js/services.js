const navTabs = document.getElementById('nav-tabs');
const mainContent = document.getElementById('main-content');


function getGoodCard(good) {
    const goodDiv = document.createElement('div');
    goodDiv.id = `good-div${good.id}`;

    const cardDiv = document.createElement('div');
    cardDiv.className = 'card h-100';
    cardDiv.style = 'min-width: 250px; max-width: 250px;'; // Фиксируем размер карточки

    const cardImage = document.createElement('img');
    cardImage.className = 'card-img-top';

    if (good.image == null) {
        cardImage.src = "static/imgs/wo-image.bmp";
    } else {
        cardImage.src = good.image;
    };
    cardDiv.appendChild(cardImage);

    const cardBody = document.createElement('div');
    cardBody.className = "card-body";
    cardDiv.appendChild(cardBody);

    const cardTitle = document.createElement('h5');
    cardTitle.className = 'card-title';
    cardTitle.innerText = good.name;
    cardBody.appendChild(cardTitle);

    const cardSubTitle = document.createElement('h6');
    cardSubTitle.className = 'card-subtitle mb-2 text-body-secondary';
    cardSubTitle.innerText = `${good.price} ₽`;
    cardBody.appendChild(cardSubTitle);

    const cardText = document.createElement('p');
    cardText.className = 'card-text';
    cardText.innerText = good.description;
    cardBody.appendChild(cardText);

    goodDiv.appendChild(cardDiv)
    return goodDiv
        ;
}


async function changeContent(categoryId) {

    try {
        const response = await fetch(`http://localhost:8000/api/categories/${categoryId}/`);
        const categories = await response.json();

        mainContent.innerHTML = '';
        categories.subcategories.forEach(subcategory => {
            const subcategoryDiv = document.createElement('div');
            const goods = subcategory.goods;

            // Заголовок подкатегории
            const p = document.createElement('p');
            p.className = 'text-black-50 text-center fw-bold';
            p.innerText = subcategory.name;
            subcategoryDiv.appendChild(p);

            // Контейнер для горизонтального скролла
            const scrollContainer = document.createElement('div');
            scrollContainer.className = 'scroll-container'; // Добавляем класс для стилей

            goods.forEach(good => {
                scrollContainer.appendChild(getGoodCard(good));
            });

            subcategoryDiv.appendChild(scrollContainer);
            subcategoryDiv.appendChild(document.createElement("hr"));
            mainContent.appendChild(subcategoryDiv);
        });
    }
    catch (error) {
        console.error('Ошибка при получении списка подкатегорий: ', error);
    };
};

async function addNavTabs() {
    try {
        const response = await fetch("http://localhost:8000/api/categories/");
        const categories = await response.json();
        const scrollContainer = document.createElement('div');
        scrollContainer.className = 'scroll-container'; // Добавляем класс для стилей

        categories.forEach(element => {
            const li = document.createElement("li");
            const button = document.createElement("button");
            const h3 = document.createElement("h3");
            li.className = 'nav-item';
            li.id = `nav-category-${element.id}`;
            button.className = 'nav-link';
            button.type = 'button';
            button.onclick = function () { changeContent(element.id); };
            h3.innerHTML = element.name;

            button.appendChild(h3);
            li.appendChild(button);
            scrollContainer.appendChild(li);
            navTabs.appendChild(scrollContainer);
        });
    }
    catch (error) {
        console.error("Ошибка при загрузке Нивигационных категорий:", error);
    };
};
