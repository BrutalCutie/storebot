const navTabs = document.getElementById('nav-tabs');
const mainContent = document.getElementById('main-content');

const userTgId = 2
const userCartId = 2



// Фция для сбора карточки
function getGoodCard(good) {
    const goodDiv = document.createElement('div');
    goodDiv.id = `good-div${good.id}`;

    // Пустой дух карточки
    const cardDiv = document.createElement('div');
    cardDiv.className = 'card h-100 mx-1';
    cardDiv.style = 'min-width: 18rem; max-width: 18rem;'; // Фиксируем размер карточки

    // Изображение карточки
    const cardImage = document.createElement('img');
    cardImage.className = 'card-img-top';
    if (good.image == null) {
        cardImage.src = "static/imgs/wo-image.bmp";
    } else {
        cardImage.src = good.image;
    };
    cardDiv.appendChild(cardImage);

    // Содержимое ниже картинки
    const cardBody = document.createElement('div');
    cardBody.className = "card-body";
    cardDiv.appendChild(cardBody);

    // Название
    const cardTitle = document.createElement('h5');
    cardTitle.className = 'card-title';
    cardTitle.innerText = good.name;
    cardBody.appendChild(cardTitle);

    // Цена
    const cardSubTitle = document.createElement('h6');
    cardSubTitle.className = 'card-subtitle mb-2 text-body-secondary';
    cardSubTitle.innerText = `${good.price} ₽`;
    cardBody.appendChild(cardSubTitle);

    // Описание
    const cardText = document.createElement('p');
    cardText.className = 'card-text';
    cardText.innerText = good.description;
    cardBody.appendChild(cardText);

    // Подвал карточки
    const cardFooterDiv = document.createElement('div');
    cardFooterDiv.className = 'card-footer p-0';
    cardDiv.appendChild(cardFooterDiv);

    // Кнопка добавления в корзину
    const addToCardButton = document.createElement('button');
    addToCardButton.type = 'button';
    addToCardButton.className = 'btn w-100'
    addToCardButton.style = "border-radius: 0px;background-color: #00f7ffb2;";
    addToCardButton.onclick = function () { putInCart(good.id) }

    const buttonText = document.createElement('h6')
    buttonText.innerText = 'В корзину'
    addToCardButton.appendChild(buttonText)
    // addToCardButton.innerText = 'В корзину';

    cardFooterDiv.append(addToCardButton);

    goodDiv.appendChild(cardDiv);
    return goodDiv;
};


async function putInCart(goodId) {
    const cartItemData = {
        good: goodId,  // ID товара
        cart: userCartId,     // ID корзины
        quantity: 1  // Количество
    };

    // Отправка POST-запроса
    fetch('/api/cartgoods/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Если используете CSRF защиту
        },
        body: JSON.stringify(cartItemData)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка сети');
            }
            return response.json();
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });

    // Функция для получения CSRF токена (если нужно)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}


// Фция Изменения блока контента
async function changeContent(categoryId) {
    try {
        const response = await fetch(`/api/categories/${categoryId}/`);
        const categories = await response.json();

        mainContent.innerHTML = '';
        categories.subcategories.forEach(subcategory => { // Цикл по подкатегориям
            // Пустой дух подкатегорий
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

            goods.forEach(good => { // Цикл по товарам в подкатегориях
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


