const cartMainContent = document.getElementById('cart-modal-content')

function getThNames() {
    return [
        'Название',
        'Цена',
        'Шт.',
    ]
};


async function fillCartContent() {

    // очищаем контент модального окна
    cartMainContent.innerHTML = '';

    const userTgId = 1

    try {
        const response = await fetch(`http://localhost:8000/api/users/${userTgId}`);
        const cartData = await response.json();

        // table div
        const tableDiv = document.createElement("div");
        // table
        const table = document.createElement("table");
        table.className = 'table';
        table.id = 'cart-table';
        // thead
        const thead = document.createElement("thead");
        // tr
        const tr = document.createElement('tr')
        // tbody
        const tbody = document.createElement('tbody')


        // список названий столбцов
        const thNamesList = getThNames();

        // соединяем названия столбцов с таблицей
        thNamesList.forEach(element => {
            const th = document.createElement('th')
            th.scope = 'col'
            th.innerText = element
            tr.appendChild(th)
        });

        // соединяем названия столбцов в таблицу
        thead.appendChild(tr);
        table.appendChild(thead);
        table.appendChild(tbody);
        tableDiv.appendChild(table);
        cartMainContent.appendChild(tableDiv);

        // данные элемента таблицы по id
        const goodsTable = document.getElementById('cart-table').getElementsByTagName('tbody')[0];

        // получаем корзинные товары
        const cartGoods = cartData.cart.goods;
        cartGoods.forEach(good => {
            const row = goodsTable.insertRow();
            row.id = `row-${good.id}`
            row.insertCell(0).textContent = good.good.name;
            row.insertCell(1).textContent = `${good.good.price}₽`;
            row.insertCell(2).textContent = good.quantity;
        });

    }

    // загружаем контент конзины при ошибке
    catch (error) {
        console.error(error);

        const cartErrorElem = document.createElement('p');
        cartErrorElem.innerText = "Ошибка при загрузке корзины";
        cartErrorElem.className = "";

        cartMainContent.appendChild(cartErrorElem);
    };

};




