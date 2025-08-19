const cartMainContent = document.getElementById('cart-modal-content')



async function fillCartContent() {

    // очищаем контент
    cartMainContent.innerHTML = '';

    const userTgId = 1

    try {
        const response = await fetch(`http://localhost:8000/api/users/${userTgId}`);
        const cartData = await response.json();
        const cartGoods = cartData.cart.goods;
        cartGoods.forEach(good => {
            console.log(good);
        });

    }

    // загружаем контент конзины при ошибке
    catch (error) {
        console.error(error);

        const cartErrorElem = document.createElement('p');
        cartErrorElem.innerText = "Ошибка при загрузке конзины";

        cartMainContent.appendChild(cartErrorElem);
    };

}